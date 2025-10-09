# iDesignRES: Building Stock Energy Model

## Use Case full example: Basque Country (NUTS2 ES21)

As mentioned in [Implemented features](../README.md#implemented-features) section, it is necessary to clarify that at the current stage of development, only the *ES21* region is available for processing.

First, a **geoprocessing workflow** is executed to obtain the required geometric and building stock data for the BSEM module. This process is fully automated and generates the input CSV file containing all relevant information described above.

Once the data is generated, the results of the geoprocessing are validated against real-world data:

- On the one hand, **total residential floor areas and the number of dwellings** are compared with official statistical data.

- On the other hand, results for the **city of Bilbao** are compared against cadastral data.

Both comparisons show only minimal deviations. It is not possible to perform a more detailed validation, since building stock data at the required level of disaggregation is not available at the regional scale.

1. In addition to the geometric information, the model requires a set of input parameters related to energy systems and fuels. These parameters are defined in the *input.json* file.

For each building use or sector, the following are defined:

- The **fuel mix** (share of fuels used for each final energy use).

- The **percentage of buildings** equipped with each system.

For the Basque Country case study, these values were derived mainly from regional statistical sources. Where specific data was not available, the tool relies on an **internal
database of default values** defined at the national.

With these inputs, the **baseline year scenario** can be simulated for the case study.

To model the **2050 scenario**, the same process is followed but with additional  parameters describing the target year. These parameters are informed by existing regional strategies, such as the **2030 Energy Transition and Climate Change Strategy for the Basque Country**, as well as the **2050 Roadmap and decarbonisation scenarios**. From these narratives, the required input values are extracted.

As in the baseline, fuel mixes and system shares are defined for each building use or sector.

![buildings_es21_example_01.png](../assets/buildings_es21_example_01.png)

In addition, further parameters are introduced, such as:

- The evolution of **Heating Degree Days (HDD)** and **Cooling Degree Days  CDD)**.

- The projected growth of **residential and non-residential floor area**.

- The **renovation rate of the existing building stock**, differentiated by use and construction period.

![buildings_es21_example_02.png](../assets/buildings_es21_example_02.png)

![buildings_es21_example_03.png](../assets/buildings_es21_example_03.png)

It should be noted that these parameters also exist for the base year in input.json, but their values will be set to 0.

Once all parameters are defined, the model can simulate the **target-year scenario** and compare the results against those of the baseline year.

---

#### Execution

---

The Building Stock Energy Model uses two main types of input data:

1. **Parameters defined in the *input.json* file**.

2. **Building data obtained from a prior geoprocessing step**, stored in a CSV file named according to the NUTS2 region code (*ES21.csv*).

The CSV file contains aggregated information on buildings, classified by archetypes and grouped into **seven construction periods**, resulting in a total of **98 archetypes**:

- **28 archetypes for residential apartment buildings**: 4 archetypes for each of the 7 construction periods.

- **21 archetypes for single-family houses**: 3 archetypes for each construction period.

- **49 archetypes for non-residential buildings**: covering 7 building uses, with 1 archetype per construction period.

Each archetype includes aggregated geometric characteristics such as:

- Built floor area. [m2]

- Number of floors and average height. [-]

- Building volume. [m3]

- Total built area. [m2]

- Total exterior façade area. [m2]

This dataset represents the **building stock of the selected region**. Based on this representation, the model performs the **energy characterization of buildings**, estimating both the energy demand and the expected energy consumption.

The combination of the structured archetype approach and the detailed geometric parameters enables the model to provide a scalable and region-specific assessment of building energy performance.

Regarding the information contained in the *input.json* file, it defines the execution scenario as follows:

```
{
    "nutsid": "ES21",
    "year": 2019,
    "scenario": {
        "increase_residential_built_area": 0.13,
        "increase_service_built_area": 0,
        "hdd_reduction": 0.16,
        "cdd_reduction": 0,
        "active_measures": [
            {
                "building_use": "Apartment Block",
                "user_defined_data": true,
                "space_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "diesel_oil": 0,
                    "gas_heat_pumps": 0,
                    "natural_gas": 0,
                    "biomass": 0.5363,
                    "geothermal": 0.1016,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.3621,
                    "conventional_electric_heating": 0,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "electricity_in_circulation": 0
                },
                "space_cooling": {
                    "pct_build_equipped": 0.02,
                    "gas_heat_pumps": 0,
                    "electric_space_cooling": 1
                },
                "water_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "diesel_oil": 0,
                    "natural_gas": 0,
                    "biomass": 0.4914,
                    "geothermal": 0.0885,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.3096,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "solar": 0.1105,
                    "electricity": 0
                },
                "cooking": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "natural_gas": 0,
                    "biomass": 0,
                    "electricity": 1
                },
                "lighting": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                },
                "appliances": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                }
            },
            {
                "building_use": "Single family- Terraced houses",
                "user_defined_data": true,
                "space_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "diesel_oil": 0,
                    "gas_heat_pumps": 0,
                    "natural_gas": 0,
                    "biomass": 0.5363,
                    "geothermal": 0.1016,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.3621,
                    "conventional_electric_heating": 0,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "electricity_in_circulation": 0
                },
                "space_cooling": {
                    "pct_build_equipped": 0.005,
                    "gas_heat_pumps": 0,
                    "electric_space_cooling": 1
                },
                "water_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "diesel_oil": 0,
                    "natural_gas": 0,
                    "biomass": 0.4914,
                    "geothermal": 0.0885,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.3096,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "solar": 0.1105,
                    "electricity": 0
                },
                "cooking": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "natural_gas": 0,
                    "biomass": 0,
                    "electricity": 1
                },
                "lighting": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                },
                "appliances": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                }
            },
            {
                "building_use": "Offices",
                "user_defined_data": true,
                "space_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "diesel_oil": 0,
                    "gas_heat_pumps": 0,
                    "natural_gas": 0,
                    "biomass": 0.5363,
                    "geothermal": 0.1016,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.3621,
                    "conventional_electric_heating": 0,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "electricity_in_circulation": 0
                },
                "space_cooling": {
                    "pct_build_equipped": 1,
                    "gas_heat_pumps": 0,
                    "electric_space_cooling": 1
                },
                "water_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "diesel_oil": 0,
                    "natural_gas": 0,
                    "biomass": 0.4914,
                    "geothermal": 0.0885,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.3096,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "solar": 0.1105,
                    "electricity": 0
                },
                "cooking": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0563,
                    "natural_gas": 0.5222,
                    "biomass": 0,
                    "electricity": 0.4215
                },
                "lighting": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                },
                "appliances": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                }
            },
            {
                "building_use": "Education",
                "user_defined_data": true,
                "space_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "diesel_oil": 0,
                    "gas_heat_pumps": 0,
                    "natural_gas": 0,
                    "biomass": 0.5363,
                    "geothermal": 0.1016,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.3621,
                    "conventional_electric_heating": 0,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "electricity_in_circulation": 0
                },
                "space_cooling": {
                    "pct_build_equipped": 0,
                    "gas_heat_pumps": 0,
                    "electric_space_cooling": 1
                },
                "water_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "diesel_oil": 0,
                    "natural_gas": 0,
                    "biomass": 0.4914,
                    "geothermal": 0.0885,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.3096,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "solar": 0.1105,
                    "electricity": 0
                },
                "cooking": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0563,
                    "natural_gas": 0.5222,
                    "biomass": 0,
                    "electricity": 0.4215
                },
                "lighting": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                },
                "appliances": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                }
            },
            {
                "building_use": "Health",
                "user_defined_data": true,
                "space_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "diesel_oil": 0,
                    "gas_heat_pumps": 0,
                    "natural_gas": 0,
                    "biomass": 0.5363,
                    "geothermal": 0.1016,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.3621,
                    "conventional_electric_heating": 0,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "electricity_in_circulation": 0
                },
                "space_cooling": {
                    "pct_build_equipped": 0.6,
                    "gas_heat_pumps": 0,
                    "electric_space_cooling": 1
                },
                "water_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "diesel_oil": 0,
                    "natural_gas": 0,
                    "biomass": 0.4914,
                    "geothermal": 0.0885,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.3096,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "solar": 0.1105,
                    "electricity": 0
                },
                "cooking": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0563,
                    "natural_gas": 0.5222,
                    "biomass": 0,
                    "electricity": 0.4215
                },
                "lighting": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                },
                "appliances": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                }
            },
            {
                "building_use": "Trade",
                "user_defined_data": true,
                "space_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "diesel_oil": 0,
                    "gas_heat_pumps": 0,
                    "natural_gas": 0,
                    "biomass": 0.5363,
                    "geothermal": 0.1016,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.3621,
                    "conventional_electric_heating": 0,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "electricity_in_circulation": 0
                },
                "space_cooling": {
                    "pct_build_equipped": 1,
                    "gas_heat_pumps": 0,
                    "electric_space_cooling": 1
                },
                "water_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "diesel_oil": 0,
                    "natural_gas": 0,
                    "biomass": 0.4914,
                    "geothermal": 0.0885,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.3096,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "solar": 0.1105,
                    "electricity": 0
                },
                "cooking": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0563,
                    "natural_gas": 0.5222,
                    "biomass": 0,
                    "electricity": 0.4215
                },
                "lighting": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                },
                "appliances": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                }
            },
            {
                "building_use": "Hotels and Restaurants",
                "user_defined_data": true,
                "space_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "diesel_oil": 0,
                    "gas_heat_pumps": 0,
                    "natural_gas": 0,
                    "biomass": 0.5363,
                    "geothermal": 0.1016,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.3621,
                    "conventional_electric_heating": 0,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "electricity_in_circulation": 0
                },
                "space_cooling": {
                    "pct_build_equipped": 1,
                    "gas_heat_pumps": 0,
                    "electric_space_cooling": 1
                },
                "water_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "diesel_oil": 0,
                    "natural_gas": 0,
                    "biomass": 0.4914,
                    "geothermal": 0.0885,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.3096,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "solar": 0.1105,
                    "electricity": 0
                },
                "cooking": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0563,
                    "natural_gas": 0.5222,
                    "biomass": 0,
                    "electricity": 0.4215
                },
                "lighting": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                },
                "appliances": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                }
            },
            {
                "building_use": "Other non-residential buildings",
                "user_defined_data": true,
                "space_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "diesel_oil": 0,
                    "gas_heat_pumps": 0,
                    "natural_gas": 0,
                    "biomass": 0.5363,
                    "geothermal": 0.1016,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.3621,
                    "conventional_electric_heating": 0,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "electricity_in_circulation": 0
                },
                "space_cooling": {
                    "pct_build_equipped": 0.75,
                    "gas_heat_pumps": 0,
                    "electric_space_cooling": 1
                },
                "water_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "diesel_oil": 0,
                    "natural_gas": 0,
                    "biomass": 0.4914,
                    "geothermal": 0.0885,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.3096,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "solar": 0.1105,
                    "electricity": 0
                },
                "cooking": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0563,
                    "natural_gas": 0.5222,
                    "biomass": 0,
                    "electricity": 0.4215
                },
                "lighting": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                },
                "appliances": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                }
            },
            {
                "building_use": "Sport",
                "user_defined_data": true,
                "space_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "diesel_oil": 0,
                    "gas_heat_pumps": 0,
                    "natural_gas": 0,
                    "biomass": 0.5363,
                    "geothermal": 0.1016,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.3621,
                    "conventional_electric_heating": 0,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "electricity_in_circulation": 0
                },
                "space_cooling": {
                    "pct_build_equipped": 0.5,
                    "gas_heat_pumps": 0,
                    "electric_space_cooling": 1
                },
                "water_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "diesel_oil": 0,
                    "natural_gas": 0,
                    "biomass": 0.4914,
                    "geothermal": 0.0885,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.3096,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "solar": 0.1105,
                    "electricity": 0
                },
                "cooking": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0563,
                    "natural_gas": 0.5222,
                    "biomass": 0,
                    "electricity": 0.4215
                },
                "lighting": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                },
                "appliances": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                }
            }
        ],
        "active_measures_baseline": [
            {
                "building_use": "Apartment Block",
                "user_defined_data": true,
                "space_heating": {
                    "pct_build_equipped": 0.783,
                    "solids": 0,
                    "lpg": 0.0645,
                    "diesel_oil": 0.1342,
                    "gas_heat_pumps": 0,
                    "natural_gas": 0.6342,
                    "biomass": 0.1059,
                    "geothermal": 0.001,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.0036,
                    "conventional_electric_heating": 0.0566,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "electricity_in_circulation": 0
                },
                "space_cooling": {
                    "pct_build_equipped": 0.02,
                    "gas_heat_pumps": 0,
                    "electric_space_cooling": 1
                },
                "water_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.124,
                    "diesel_oil": 0.1093,
                    "natural_gas": 0.5399,
                    "biomass": 0.0614,
                    "geothermal": 0.0014,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.004,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "solar": 0.0308,
                    "electricity": 0.1292
                },
                "cooking": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "natural_gas":0,
                    "biomass":0,
                    "electricity": 1
                },
                "lighting": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                },
                "appliances": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                }
            },
            {
                "building_use": "Single family- Terraced houses",
                "user_defined_data": true,
                "space_heating": {
                    "pct_build_equipped": 0.786,
                    "solids": 0,
                    "lpg": 0.0645,
                    "diesel_oil": 0.1342,
                    "gas_heat_pumps": 0,
                    "natural_gas": 0.6342,
                    "biomass": 0.1059,
                    "geothermal": 0.001,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.0036,
                    "conventional_electric_heating": 0.0566,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "electricity_in_circulation": 0
                },
                "space_cooling": {
                    "pct_build_equipped": 0.005,
                    "gas_heat_pumps": 0,
                    "electric_space_cooling": 1
                },
                "water_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.124,
                    "diesel_oil": 0.1093,
                    "natural_gas": 0.5399,
                    "biomass": 0.0614,
                    "geothermal": 0.0014,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.004,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "solar": 0.0308,
                    "electricity": 0.1292
                },
                "cooking": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0,
                    "natural_gas":0,
                    "biomass":0,
                    "electricity": 1
                },
                "lighting": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                },
                "appliances": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                }
            },
            {
                "building_use": "Offices",
                "user_defined_data": true,
                "space_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0645,
                    "diesel_oil": 0.1342,
                    "gas_heat_pumps": 0,
                    "natural_gas": 0.6342,
                    "biomass": 0.1059,
                    "geothermal": 0.001,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.0036,
                    "conventional_electric_heating": 0.0566,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "electricity_in_circulation": 0
                },
                "space_cooling": {
                    "pct_build_equipped": 1,
                    "gas_heat_pumps": 0,
                    "electric_space_cooling": 1
                },
                "water_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.124,
                    "diesel_oil": 0.1093,
                    "natural_gas": 0.5399,
                    "biomass": 0.0614,
                    "geothermal": 0.0014,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.004,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "solar": 0.0308,
                    "electricity": 0.1292
                },
                "cooking": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0563,
                    "natural_gas": 0.5222,
                    "biomass": 0,
                    "electricity": 0.4215
                },
                "lighting": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                },
                "appliances": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                }
            },
            {
                "building_use": "Education",
                "user_defined_data": true,
                "space_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0645,
                    "diesel_oil": 0.1342,
                    "gas_heat_pumps": 0,
                    "natural_gas": 0.6342,
                    "biomass": 0.1059,
                    "geothermal": 0.001,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.0036,
                    "conventional_electric_heating": 0.0566,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "electricity_in_circulation": 0
                },
                "space_cooling": {
                    "pct_build_equipped": 0,
                    "gas_heat_pumps": 0,
                    "electric_space_cooling": 1
                },
                "water_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.124,
                    "diesel_oil": 0.1093,
                    "natural_gas": 0.5399,
                    "biomass": 0.0614,
                    "geothermal": 0.0014,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.004,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "solar": 0.0308,
                    "electricity": 0.1292
                },
                "cooking": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0563,
                    "natural_gas": 0.5222,
                    "biomass": 0,
                    "electricity": 0.4215
                },
                "lighting": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                },
                "appliances": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                }
            },
            {
                "building_use": "Health",
                "user_defined_data": true,
                "space_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0645,
                    "diesel_oil": 0.1342,
                    "gas_heat_pumps": 0,
                    "natural_gas": 0.6342,
                    "biomass": 0.1059,
                    "geothermal": 0.001,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.0036,
                    "conventional_electric_heating": 0.0566,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "electricity_in_circulation": 0
                },
                "space_cooling": {
                    "pct_build_equipped": 0.6,
                    "gas_heat_pumps": 0,
                    "electric_space_cooling": 1
                },
                "water_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.124,
                    "diesel_oil": 0.1093,
                    "natural_gas": 0.5399,
                    "biomass": 0.0614,
                    "geothermal": 0.0014,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.004,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "solar": 0.0308,
                    "electricity": 0.1292
                },
                "cooking": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0563,
                    "natural_gas": 0.5222,
                    "biomass": 0,
                    "electricity": 0.4215
                },
                "lighting": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                },
                "appliances": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                }
            },
            {
                "building_use": "Trade",
                "user_defined_data": true,
                "space_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0645,
                    "diesel_oil": 0.1342,
                    "gas_heat_pumps": 0,
                    "natural_gas": 0.6342,
                    "biomass": 0.1059,
                    "geothermal": 0.001,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.0036,
                    "conventional_electric_heating": 0.0566,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "electricity_in_circulation": 0
                },
                "space_cooling": {
                    "pct_build_equipped": 1,
                    "gas_heat_pumps": 0,
                    "electric_space_cooling": 1
                },
                "water_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.124,
                    "diesel_oil": 0.1093,
                    "natural_gas": 0.5399,
                    "biomass": 0.0614,
                    "geothermal": 0.0014,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.004,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "solar": 0.0308,
                    "electricity": 0.1292
                },
                "cooking": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0563,
                    "natural_gas": 0.5222,
                    "biomass": 0,
                    "electricity": 0.4215
                },
                "lighting": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                },
                "appliances": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                }
            },
            {
                "building_use": "Hotels and Restaurants",
                "user_defined_data": true,
                "space_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0645,
                    "diesel_oil": 0.1342,
                    "gas_heat_pumps": 0,
                    "natural_gas": 0.6342,
                    "biomass": 0.1059,
                    "geothermal": 0.001,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.0036,
                    "conventional_electric_heating": 0.0566,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "electricity_in_circulation": 0
                },
                "space_cooling": {
                    "pct_build_equipped": 1,
                    "gas_heat_pumps": 0,
                    "electric_space_cooling": 1
                },
                "water_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.124,
                    "diesel_oil": 0.1093,
                    "natural_gas": 0.5399,
                    "biomass": 0.0614,
                    "geothermal": 0.0014,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.004,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "solar": 0.0308,
                    "electricity": 0.1292
                },
                "cooking": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0563,
                    "natural_gas": 0.5222,
                    "biomass": 0,
                    "electricity": 0.4215
                },
                "lighting": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                },
                "appliances": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                }
            },
            {
                "building_use": "Other non-residential buildings",
                "user_defined_data": true,
                "space_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0645,
                    "diesel_oil": 0.1342,
                    "gas_heat_pumps": 0,
                    "natural_gas": 0.6342,
                    "biomass": 0.1059,
                    "geothermal": 0.001,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.0036,
                    "conventional_electric_heating": 0.0566,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "electricity_in_circulation": 0
                },
                "space_cooling": {
                    "pct_build_equipped": 0.75,
                    "gas_heat_pumps": 0,
                    "electric_space_cooling": 1
                },
                "water_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.124,
                    "diesel_oil": 0.1093,
                    "natural_gas": 0.5399,
                    "biomass": 0.0614,
                    "geothermal": 0.0014,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.004,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "solar": 0.0308,
                    "electricity": 0.1292
                },
                "cooking": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0563,
                    "natural_gas": 0.5222,
                    "biomass": 0,
                    "electricity": 0.4215
                },
                "lighting": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                },
                "appliances": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                }
            },
            {
                "building_use": "Sport",
                "user_defined_data": true,
                "space_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0645,
                    "diesel_oil": 0.1342,
                    "gas_heat_pumps": 0,
                    "natural_gas": 0.6342,
                    "biomass": 0.1059,
                    "geothermal": 0.001,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.0036,
                    "conventional_electric_heating": 0.0566,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "electricity_in_circulation": 0
                },
                "space_cooling": {
                    "pct_build_equipped": 0.5,
                    "gas_heat_pumps": 0,
                    "electric_space_cooling": 1
                },
                "water_heating": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.124,
                    "diesel_oil": 0.1093,
                    "natural_gas": 0.5399,
                    "biomass": 0.0614,
                    "geothermal": 0.0014,
                    "distributed_heat": 0,
                    "advanced_electric_heating": 0.004,
                    "bio_oil": 0,
                    "bio_gas": 0,
                    "hydrogen": 0,
                    "solar": 0.0308,
                    "electricity": 0.1292
                },
                "cooking": {
                    "pct_build_equipped": 1,
                    "solids": 0,
                    "lpg": 0.0563,
                    "natural_gas": 0.5222,
                    "biomass": 0,
                    "electricity": 0.4215
                },
                "lighting": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                },
                "appliances": {
                    "pct_build_equipped": 1,
                    "electricity": 1
                }
            }
        ],
        "passive_measures": [
            {
                "building_use": "Apartment Block",
                "ref_level": "High",
                "percentages_by_periods":  {
                    "Pre-1945": 1,
                    "1945-1969": 1,
                    "1970-1979": 1,
                    "1980-1989": 1,
                    "1990-1999": 0.13,
                    "2000-2010": 0,
                    "Post-2010": 0
                }
            },
            {
                "building_use": "Single family- Terraced houses",
                "ref_level": "High",
                "percentages_by_periods":  {
                    "Pre-1945": 1,
                    "1945-1969": 1,
                    "1970-1979": 1,
                    "1980-1989": 1,
                    "1990-1999": 0.13,
                    "2000-2010": 0,
                    "Post-2010": 0
                }
            },
            {
                "building_use": "Offices",
                "ref_level": "Medium",
                "percentages_by_periods":  {
                    "Pre-1945": 0,
                    "1945-1969": 0,
                    "1970-1979": 0,
                    "1980-1989": 0,
                    "1990-1999": 0,
                    "2000-2010": 0,
                    "Post-2010": 0
                }
            },
            {
                "building_use": "Education",
                "ref_level": "Medium",
                "percentages_by_periods":  {
                    "Pre-1945": 0,
                    "1945-1969": 0,
                    "1970-1979": 0,
                    "1980-1989": 0,
                    "1990-1999": 0,
                    "2000-2010": 0,
                    "Post-2010": 0
                }
            },
            {
                "building_use": "Health",
                "ref_level": "Low",
                "percentages_by_periods":  {
                    "Pre-1945": 0,
                    "1945-1969": 0,
                    "1970-1979": 0,
                    "1980-1989": 0,
                    "1990-1999": 0,
                    "2000-2010": 0,
                    "Post-2010": 0
                }
            },
            {
                "building_use": "Trade",
                "ref_level": "Low",
                "percentages_by_periods":  {
                    "Pre-1945": 0,
                    "1945-1969": 0,
                    "1970-1979": 0,
                    "1980-1989": 0,
                    "1990-1999": 0,
                    "2000-2010": 0,
                    "Post-2010": 0
                }
            },
            {
                "building_use": "Hotels and Restaurants",
                "ref_level": "Medium",
                "percentages_by_periods":  {
                    "Pre-1945": 0,
                    "1945-1969": 0,
                    "1970-1979": 0,
                    "1980-1989": 0,
                    "1990-1999": 0,
                    "2000-2010": 0,
                    "Post-2010": 0
                }
            },
            {
                "building_use": "Other non-residential buildings",
                "ref_level": "Medium",
                "percentages_by_periods":  {
                    "Pre-1945": 0,
                    "1945-1969": 0,
                    "1970-1979": 0,
                    "1980-1989": 0,
                    "1990-1999": 0,
                    "2000-2010": 0,
                    "Post-2010": 0
                }
            },
            {
                "building_use": "Sport",
                "ref_level": "Medium",
                "percentages_by_periods":  {
                    "Pre-1945": 0,
                    "1945-1969": 0,
                    "1970-1979": 0,
                    "1980-1989": 0,
                    "1990-1999": 0,
                    "2000-2010": 0,
                    "Post-2010": 0
                }
            }
        ]
    }
}
```

The file can be edited to apply a custom configuration of the scenario to be executed. To facilitate the adjustment of scenario values, the set of editable properties and their possible values ​​are described below as a data dictionary:

```
- nutsid: text -> Region over which the model will be generated.
- year: integer between 1900 and 2050 -> Year of the modeled scenario.
- increase_residential_built_area: decimal number as percentage, between 0 and 1 -> % increase in residential built area compared to the base year. It represents the construction of new residential buildings.
- increase_service_built_area: decimal number as percentage, between 0 and 1 -> % increase in tertiary built area compared to the base year. It represents the construction of new tertiary buildings.
- hdd_reduction: decimal number as percentage, between -1 and 1 -> Reduction in heating degree days for future scenario.
- cdd_reduction: decimal number as percentage, between -1 and 1 -> Reduction in cooling degree days for future scenarios. The value represents the reduction. If the value is negative, it will imply an increase.
- building_use: text -> Input values are defined for each of the building uses.
- user_defined_data: boolean -> Indicates whether the values used are user defined or those from the database are taken.
- pct_build_equipped: decimal number as percentage, between 0 and 1 -> Represents the % of buildings equipped with the technology.

% of buildings supplied by each type of fuel:

- solids: decimal number as percentage, between 0 and 1.
- lpg: decimal number as percentage, between 0 and 1.
- diesel_oil: decimal number as percentage, between 0 and 1.
- gas_heat_pumps: decimal number as percentage, between 0 and 1.
- natural_gas: decimal number as percentage, between 0 and 1.
- biomass: decimal number as percentage, between 0 and 1.
- geothermal: decimal number as percentage, between 0 and 1.
- distributed_heat: decimal number as percentage, between 0 and 1.
- advanced_electric_heating: decimal number as percentage, between 0 and 1.
- conventional_electric_heating: decimal number as percentage, between 0 and 1.
- bio_oil: decimal number as percentage, between 0 and 1.
- bio_gas: decimal number as percentage, between 0 and 1.
- hydrogen: decimal number as percentage, between 0 and 1.
- electricity_in_circulation: decimal number as percentage, between 0 and 1.
- electric_space_cooling: decimal number as percentage, between 0 and 1.
- solar: decimal number as percentage, between 0 and 1.
- electricity: decimal number as percentage, between 0 and 1.

- ref_level: text -> Type of renovation implemented: Low, Medium, or High level.
- Pre-1945: decimal number as percentage, between 0 and 1 -> % of buildings from the construction period that are renovated.
- 1945-1969: decimal number as percentage, between 0 and 1 -> % of buildings from the construction period that are renovated.
- 1970-1979: decimal number as percentage, between 0 and 1 -> % of buildings from the construction period that are renovated.
- 1980-1989: decimal number as percentage, between 0 and 1 -> % of buildings from the construction period that are renovated.
- 1990-1999: decimal number as percentage, between 0 and 1 -> % of buildings from the construction period that are renovated.
- 2000-2010: decimal number as percentage, between 0 and 1 -> % of buildings from the construction period that are renovated.
- Post-2010: decimal number as percentage, between 0 and 1 -> % of buildings from the construction period that are renovated.

Clarifications:
1) As mentioned before, the fields "building_use" can only have the values:
   - Apartment Block
   - Single family- Terraced houses
   - Offices
   - Education
   - Health
   - Trade
   - Hotels and Restaurants
   - Other non-residential buildings
   - Sport
2) The fields "ref_level" can only have the values:
   - "Low"
   - "Medium"
   - "High"
3) The sum of all the Energy Systems in each section must add up to 1.
```

Once all the input data is configured, the next step is to proceed with execution. Assuming that the model is already installed with Poetry, execute the command:

```
poetry run python building_energy_process.py <input_payload> <start_time> <end_time> <building_use>
```

Let's suppose that the information to be obtained corresponds to the period between 1:00 p.m. on March 1, 2019, and 1:00 p.m. on March 2, 2019. The *<start_time>* and *<end_time>* parameters will have the values:

> 2019-03-01T13:00:00    :    start_time
> 
> 2019-03-02T13:00:00    :    end_time

This model has *<building_use>* as an additional parameter, and it can take one of the following values:

> - Apartment Block.
> - Single family- Terraced houses.
> - Hotels and Restaurants.
> - Health.
> - Education.
> - Offices.
> - Trade.
> - Other non-residential buildings.
> - Sport.

For this example, *Apartment Block* will be used, so the final execution command will be as follows:

```
poetry run python building_energy_process.py input.json 2019-03-01T13:00:00 2019-03-02T13:00:00 "Apartment Block"
```

This command automatically runs the simulation, taking the necessary input data from the *[usecases](../usecases)* folder and the *[input.json](../input.json)* file.

When execution is launched, a full input validation is performed. And when the execution finishes, a result similar to the following is obtained:

```
{
    'Datetime': [
        Timestamp('2019-03-0113: 00: 00'),
        Timestamp('2019-03-0114: 00: 00'),
        Timestamp('2019-03-0115: 00: 00'),
        Timestamp('2019-03-0116: 00: 00'),
        Timestamp('2019-03-0117: 00: 00'),
        Timestamp('2019-03-0118: 00: 00'),
        Timestamp('2019-03-0119: 00: 00'),
        Timestamp('2019-03-0120: 00: 00'),
        Timestamp('2019-03-0121: 00: 00'),
        Timestamp('2019-03-0122: 00: 00'),
        Timestamp('2019-03-0123: 00: 00'),
        Timestamp('2019-03-0200: 00: 00'),
        Timestamp('2019-03-0201: 00: 00'),
        Timestamp('2019-03-0202: 00: 00'),
        Timestamp('2019-03-0203: 00: 00'),
        Timestamp('2019-03-0204: 00: 00'),
        Timestamp('2019-03-0205: 00: 00'),
        Timestamp('2019-03-0206: 00: 00'),
        Timestamp('2019-03-0207: 00: 00'),
        Timestamp('2019-03-0208: 00: 00'),
        Timestamp('2019-03-0209: 00: 00'),
        Timestamp('2019-03-0210: 00: 00'),
        Timestamp('2019-03-0211: 00: 00'),
        Timestamp('2019-03-0212: 00: 00'),
        Timestamp('2019-03-0213: 00: 00')
    ],
    'Solids|Coal': [
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00
    ],
    'Liquids|Gas': [
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00
    ],
    'Liquids|Oil': [
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00
    ],
    'Gases|Gas': [
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00
    ],
    'Solids|Biomass': [
        3.20e+04,
        3.20e+04,
        6.41e+04,
        6.41e+04,
        6.41e+04,
        6.41e+04,
        1.48e+05,
        1.95e+05,
        1.78e+05,
        1.52e+05,
        1.94e+05,
        3.20e+04,
        2.13e+04,
        2.14e+04,
        1.77e+04,
        2.16e+04,
        1.90e+04,
        1.88e+05,
        1.48e+05,
        7.19e+04,
        3.20e+04,
        3.20e+04,
        3.20e+04,
        3.20e+04,
        3.20e+04
    ],
    'Electricity': [
        1.61e+05,
        1.60e+05,
        1.65e+05,
        1.66e+05,
        2.11e+05,
        2.81e+05,
        3.09e+05,
        3.14e+05,
        2.96e+05,
        2.80e+05,
        2.47e+05,
        7.43e+04,
        6.04e+04,
        5.48e+04,
        6.10e+04,
        1.14e+05,
        1.83e+05,
        2.93e+05,
        2.84e+05,
        2.06e+05,
        2.00e+05,
        2.07e+05,
        1.54e+05,
        1.71e+05,
        1.61e+05
    ],
    'Heat': [
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00
    ],
    'Liquids|Biomass': [
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00
    ],
    'Gases|Biomass': [
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00
    ],
    'Hydrogen': [
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00,
        0.00e+00
    ],
    'Heat|Solar': [
        6.13e+03,
        6.13e+03,
        1.23e+04,
        1.23e+04,
        1.23e+04,
        1.23e+04,
        1.23e+04,
        1.23e+04,
        1.23e+04,
        1.23e+04,
        2.45e+04,
        6.13e+03,
        2.45e+03,
        2.45e+03,
        2.45e+03,
        2.45e+03,
        2.45e+03,
        2.45e+04,
        1.23e+04,
        6.13e+03,
        6.13e+03,
        6.13e+03,
        6.13e+03,
        6.13e+03,
        6.13e+03
    ],
    'Variablecost[
        €/KWh
    ]': [
        3.88e+04,
        3.86e+04,
        4.17e+04,
        4.19e+04,
        5.22e+04,
        6.83e+04,
        7.95e+04,
        8.34e+04,
        7.82e+04,
        7.30e+04,
        6.78e+04,
        1.89e+04,
        1.51e+04,
        1.38e+04,
        1.50e+04,
        2.74e+04,
        4.31e+04,
        7.82e+04,
        7.39e+04,
        5.15e+04,
        4.79e+04,
        4.95e+04,
        3.74e+04,
        4.11e+04,
        3.88e+04
    ],
    'Emissions[
        KgCO2/KWh
    ]': [
        6.47e+04,
        6.44e+04,
        6.72e+04,
        6.75e+04,
        8.53e+04,
        1.13e+05,
        1.26e+05,
        1.29e+05,
        1.21e+05,
        1.14e+05,
        1.02e+05,
        3.02e+04,
        2.45e+04,
        2.23e+04,
        2.46e+04,
        4.58e+04,
        7.33e+04,
        1.20e+05,
        1.16e+05,
        8.36e+04,
        8.05e+04,
        8.32e+04,
        6.22e+04,
        6.87e+04,
        6.47e+04
    ]
}
```