# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright (c) 2025 Tecnalia Research & Innovation

import json
import shutil
import sys
import pandas as pd

from building_stock_energy_model import constants
from building_stock_energy_model import model
from building_stock_energy_model import validator
from datetime import datetime
from pathlib import Path


# Function: Format the Hourly results
def formatHourlyResults(dictHourlyResults: dict,
                        archetypes: list,
                        archetipesNotFound: list) -> dict:
    """Function to format the Hourly results.

    Args:
        dictHourlyResults (dict): The dictionary resulting from the Hourly results calculation. Example::

            "{
                "Apartment Block": DataFrame,
                "Single family- Terraced houses": DataFrame,
                "Hotels and Restaurants": DataFrame,
                "Health": DataFrame,
                "Education": DataFrame,
                "Offices": DataFrame,
                "Trade": DataFrame,
                "Other non-residential buildings": DataFrame,
                "Sport": DataFrame
            }"
        archetypes (list): The list of building uses. Example::

            "[
                "Apartment Block",
                "Single family- Terraced houses",
                "Hotels and Restaurants",
                "Health,
                "Education",
                "Offices",
                "Trade",
                "Other non-residential buildings",
                "Sport"
            ]"
        archetipesNotFound (list): The list of archetipes with no data found.
    
    Returns:
        dict

    """

    formattedOutput = {}
    for arch in archetypes:
        if not arch in archetipesNotFound:
            formattedOutput[arch] = []
            df = dictHourlyResults[arch]
            for index, row in df.iterrows():
                datetimeConverted = datetime.strptime(row['Datetime'],
                                                    '%d/%m/%Y %H:%M')
                dictConverted = {
                    'Datetime': datetimeConverted.strftime('%Y-%m-%d %H:%M'),
                    'Solids|Coal': row['Solids|Coal'],
                    'Liquids|Gas': row['Liquids|Gas'],
                    'Liquids|Oil': row['Liquids|Oil'],
                    'Gases|Gas': row['Gases|Gas'],
                    'Solids|Biomass': row['Solids|Biomass'],
                    'Electricity': row['Electricity'],
                    'Heat': row['Heat'],
                    'Liquids|Biomass': row['Liquids|Biomass'],
                    'Gases|Biomass': row['Gases|Biomass'],
                    'Hydrogen': row['Hydrogen'],
                    'Heat|Solar': row['Heat|Solar'],
                    'Variable cost [€]': row['Variable cost [€]'],
                    'Emissions [KgCO2]': row['Emissions [kgCO2]']
                }
                formattedOutput[arch].append(dictConverted)
    return formattedOutput


# Function: Execute the Model
def executeModel(currentNutsId: str, modelPayload: dict) -> dict:
    """Function to execute the Buildings Stock Energy Model.

    Args:
        currentNutsId (str): The current NUTSID.
        modelPayload (dict): The dictionary with the Model input payload::

            Example: see "input.json" file in the root directory.
    
    Returns:
        dict

    """

    # Obtain all the nutsId's defined in the input data file
    print(f'Main/>  Executing the Buildings Stock Energy Model for [{currentNutsId}] (please wait)...')
    print('')
    dfCsv, dfSolar = model.s01LoadPreviousResult(currentNutsId)
    print('')
    tempsPath = model.s02RetrieveTemperatures(currentNutsId,
                                              modelPayload['year'])
    print('')
    radPath = model.s03RetrieveRadiationValues(currentNutsId,
                                               modelPayload['year'])
    print('')
    if tempsPath is None or radPath is None:
        raise ValueError(
            'Main/>  There is no data on radiation and/or temperatures!')
    dfDHW, dfYears, dfSectors, dfSeasons, \
        dfTemperatures, dfSchedule, dfResHHTes, \
        dfSerHHTes, dfUvalues, dfRetroUvalues, \
        dfACH, dfBaseTemperatures, dfCalendar, \
        dfBesCapex, dfBesOpex, dfRes, dfBesCapacity, \
        dfRetroCost, dfSolarOffice, dfSolarNoffice, \
        dfDwellings, dfRTHHEff, dictDBBuildings = model.s04LoadDatabase(currentNutsId,
                                                                        modelPayload['scenario']['hdd_reduction'],
                                                                        modelPayload['scenario']['cdd_reduction'])
    print('')
    dfSolarResults = model.s05RetrieveSolarData(currentNutsId,
                                                modelPayload['year'],
                                                modelPayload['scenario']['solar'],
                                                dictDBBuildings,
                                                dfTemperatures)
    print('')
    dfInput = model.s06AddColumnsToMainDataFrame(dfCsv)
    print('')
    dfInput = model.s07AddInputDataToMainDataframe(dfInput,
                                                   dfDHW,
                                                   dfYears,
                                                   dfSectors,
                                                   dfDwellings,
                                                   currentNutsId,
                                                   modelPayload['scenario']['increase_residential_built_area'],
                                                   modelPayload['scenario']['increase_service_built_area'])
    del dfYears, dfSectors, dfDwellings
    print('')
    dfInput = model.s08AddActiveMeasures(dfInput,
                                         dfResHHTes,
                                         dfSerHHTes,
                                         dfRTHHEff,
                                         currentNutsId,
                                         modelPayload['scenario']['active_measures'],
                                         modelPayload['scenario']['active_measures_baseline'],
                                         constants.BUILDING_USES)
    del dfResHHTes, dfSerHHTes, dfRTHHEff
    print('')
    dfInput = model.s09AddPassiveMeasures(dfInput,
                                          modelPayload['scenario']['passive_measures'])
    print('')
    dfInput = model.s10WriteUValuesAndInternalGains(dfInput,
                                                    dfDHW,
                                                    dfUvalues,
                                                    dfRetroUvalues,
                                                    dfACH,
                                                    currentNutsId)
    del dfDHW, dfUvalues, dfRetroUvalues, dfACH
    print('')
    dfInput = model.s11AddCapexDataFrame(dfInput,
                                         dfBesCapex)
    del dfBesCapex
    print('')
    dfInput = model.s12AddOpexDataFrame(dfInput,
                                        dfBesOpex)
    del dfBesOpex
    print('')
    dfInput = model.s13AddRetrofittingCostDataFrame(dfInput,
                                                    dfRetroCost)
    del dfRetroCost
    print('')
    dfInput = model.s14AddRenewableEnergySystemsDataFrame(dfInput,
                                                          dfRes)
    del dfRes
    print('')
    dfInput = model.s15AddCapacityDataFrame(dfInput,
                                            dfBesCapacity,
                                            constants.BUILDING_USES)
    del dfBesCapacity
    print('')
    dfInput = model.s16AddEquivalentPowerDataFrame(dfInput)
    print('')
    dfInput = model.s17CalculateCosts(dfInput)
    print('')
    dictSchedule, archetypesNotFound = model.s18CalculateGeneralSchedule(dfInput,
                                                                         dfSchedule,
                                                                         dfTemperatures,
                                                                         dfBaseTemperatures,
                                                                         dfSolarOffice,
                                                                         dfSolarNoffice,
                                                                         currentNutsId)
    del dfTemperatures, dfBaseTemperatures, dfSolarOffice, dfSolarNoffice
    print('')
    dictSchedule = model.s19CalculateScenario(dfInput,
                                              dictSchedule)
    print('')
    dfAnualResults = model.s20CalculateAnualResults(dfInput,
                                                    dictSchedule)
    print('')
    dictConsolidated = {}
    for arch in constants.BUILDING_USES:
        dictConsolidated[arch] = model.s21CalculateConsolidate(dictSchedule,
                                                               arch)
    print('')
    dictHourlyResults = {}
    for arch in constants.BUILDING_USES:
        dictHourlyResults[arch] = model.s22CalculateHourlyResults(dfInput,
                                                                  dfSolarResults,
                                                                  dictSchedule,
                                                                  arch)
    del dictSchedule
    print('')
            
     # Format the output and save
    output = formatHourlyResults(dictHourlyResults,
                                 constants.BUILDING_USES,
                                 archetypesNotFound)
    result = pd.DataFrame(output)
    result.to_json("usecases/results/" + currentNutsId + ".json")

    # Return the output
    return output


# Function: Execute the Building Energy Simulation process
def executeBuildingEnergySimulationProcess(processPayload: dict,
                                           startTime: str,
                                           endTime: str,
                                           buildingUse: str) -> dict:
    """Function to execute the Building Energy Simulation process.

    Args:
        processPayload (dict): The dictionary with the process input payload::

            Example: see "input.json" file in the root directory.

        startTime (str): The start datetime, e.g., "2019-03-01T13:00:00".
        endTime (str): The end datetime, e.g., "2019-03-02T13:00:00".
        buildingUse (str): The archetype (building use). For example: "Offices".
    
    Returns:
        dict

    """

    try:
        # Execute the Model
        print(
            'Main/>  *** Building Energy Simulation process [version ' + constants.VERSION + '] ***')
        
        nutsidList = processPayload['nutsid'].split(',')
        if nutsidList:
            processResult = {}
            for nutsid in nutsidList:
                # Print the starting date at time
                now = datetime.now()
                print('')
                print('Main/>  Starting date and time for [' + nutsid.strip() + ']: ' + now.strftime("%Y-%m-%d %H:%M:%S"))
                print('')

                # Execute the model
                output = executeModel(nutsid.strip(), processPayload)
                processResult[nutsid] = output

                # Move the resulting Excel file to the proper directory (if allowed)
                if constants.SAVE_RESULT_TO_EXCEL_ALLOWED:
                    shutil.move('temporary/result.xlsx', 'usecases/results/' +
                                processPayload['nutsid'] + '.xlsx')
        
                # Return the first result (filtered), only for the sampling function
                output = next(iter(processResult.values()))
                result = pd.DataFrame(output[buildingUse])
                result['Datetime'] = pd.to_datetime(result['Datetime'])
                start = pd.to_datetime(datetime.strptime(startTime,
                                                        '%Y-%m-%dT%H:%M:%S'))
                end = pd.to_datetime(datetime.strptime(endTime,
                                                       '%Y-%m-%dT%H:%M:%S'))
                resultFiltered = result[(result['Datetime'] >= start) & (
                    result['Datetime'] <= end)]
                negativeValues = validator.validateProcessOutput(resultFiltered)
                print('Main/>  Validating the output...')
                if negativeValues:
                    raise Exception('Main/>  The output contains negative values!')
                print('Main/>  The output has no negative values.')
                print('')

                # Write the filtered result to a JSON file (if allowed)
                if constants.SAVE_RESULT_TO_SAMPLING_FILE_ALLOWED:
                    with open(f"usecases/results/{nutsid}_sampling_result.json", "w", encoding="utf-8") as sampling:
                        json.dump(resultFiltered.to_dict(),
                                  ensure_ascii=False,
                                  indent=4,
                                  default=str)
                        
                # Print the ending date at time
                now = datetime.now()
                print('Main/>  Ending date and time for [' + nutsid.strip() + ']: ' + now.strftime("%Y-%m-%d %H:%M:%S"))
                print('')
                        
                # Return the filtered result, only for the sampling function
                if len(nutsidList) < 2:
                    return resultFiltered.to_dict(orient='list')
        else:
            raise Exception(
                'Main/>  The process did NOT execute correctly!')
    except Exception as error:
        print('Main/>  An error occurred executing the Building Energy Simulation process!')
        print(error)
    finally:
        # Remove the temporary directory
        print('Main/>  Removing the temporary directory...')
        directory = Path(__file__).parent / 'temporary'
        if directory.exists() and directory.is_dir():
            shutil.rmtree(directory)
        print('Main/>  [OK]')

# Function: Main
def main():
    """Main function.

    Args:
        sys.argv[0] (str): The current file name, e.g., "building_energy_process.py".
        sys.argv[1] (str): The process input data file path, e.g., "input.json".
        sys.argv[2] (str): The start datetime, e.g., "2019-03-01T13:00:00". Optional.
        sys.argv[3] (str): The end datetime, e.g., "2019-03-02T13:00:00". Optional.
        sys.argv[4] (str): The archetype (building use), e.g., "Offices". Optional.
    
    Returns:
        None

    """

    try:
        # Validate the command line parameters
        validator.validateCommandLineParameters(sys.argv)

        # Load the process payload
        print('Main/>  Loading the process payload...')
        with open(sys.argv[1].strip(), 'r') as payloadFile:
            processPayload = json.load(payloadFile)

        # Validate the process payload
        processPayload = validator.validateProcessPayload(processPayload)
        print('Main/>  Input data validation OK!...')

        # Validate the integrity of the database
        print('Main/>  Validating the integrity of the database...')
        validator.validateDatabaseIntegrity()

        # Configure the final input to the process
        if len(sys.argv) == 2:
            sys.argv.append(constants.DEFAULT_START_DATETIME)
            sys.argv.append(constants.DEFAULT_END_DATETIME)
            sys.argv.append(constants.DEFAULT_BUILDING_USE)

        # Execute the process
        print('Main/>  Loading the Model...')
        executeBuildingEnergySimulationProcess(processPayload,
                                               sys.argv[2],
                                               sys.argv[3],
                                               sys.argv[4])
    except Exception as exception:
        print(f'{exception}')


if __name__ == "__main__":
    main()
