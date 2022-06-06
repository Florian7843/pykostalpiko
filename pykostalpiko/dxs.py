from aenum import MultiValueEnum


class Entries(MultiValueEnum):
    AnalaogInput1 = 167772417, "Analog Input 1"
    AnalaogInput2 = 167772673, "Analog Input 2"
    AnalaogInput3 = 167772929, "Analog Input 3"
    AnalaogInput4 = 167773185, "Analog Input 4"

    BatteryVoltage = 33556226, "Battery Voltage"
    BatteryCharge = 33556229, "Battery Charge"
    BatteryCurrent = 33556238, "Battery Current"
    BatteryCurrentDirection = 33556230, "Battery Current Direction"
    BatteryChargeCycles = 33556228, "Battery Charge Cycles"
    BatteryTemperature = 33556227, "Battery Temperature"

    GridOutputPower = 67109120, "Grid Output Power"
    GridFrequency = 67110400, "Grid Frequency"
    GridCosPhi = 67110656, "Grid Cos Phi"
    GridLimitation = 67110144, "Grid Limitation"
    GridVoltageL1 = 67109378, "Grid Voltage L1"
    GridCurrentL1 = 67109377, "Grid Current L1"
    GridPowerL1 = 67109379, "Grid Power L1"
    GridVoltageL2 = 67109634, "Grid Voltage L2"
    GridCurrentL2 = 67109633, "Grid Current L2"
    GridPowerL2 = 67109635, "Grid Power L2"
    GridVoltageL3 = 67109890, "Grid Voltage L3"
    GridCurrentL3 = 67109889, "Grid Current L3"
    GridPowerL3 = 67109891, "Grid Power L3"

    HomeConsumptionSolar = 83886336, "Home Consumption Solar"
    HomeConsumptionBattery = 83886592, "Home Consumption Battery"
    HomeConsumptionGrid = 83886848, "Home Consumption Grid"
    HomeConsumptionL1 = 83887106, "Home Consumption L1"
    HomeConsumptionL2 = 83887362, "Home Consumption L2"
    HomeConsumptionL3 = 83887618, "Home Consumption L3"

    GeneratorDc1Voltage = 33555202, "Generator DC1 Voltage"
    GeneratorDc1Current = 33555201, "Generator DC1 Current"
    GeneratorDc1Power = 33555203, "Generator DC1 Power"
    GeneratorDc2Voltage = 33555458, "Generator DC2 Voltage"
    GeneratorDc2Current = 33555457, "Generator DC2 Current"
    GeneratorDc2Power = 33555459, "Generator DC2 Power"
    GeneratorDc3Voltage = 33555714, "Generator DC3 Voltage"
    GeneratorDc3Current = 33555713, "Generator DC3 Current"
    GeneratorDc3Power = 33555715, "Generator DC3 Power"

    S0InPulseCnt = 184549632, "S0 In Pulse Count"
    S0InLoginterval = 150995968, "S0 In Loginterval"

    HomeDcPowerPV = 33556736, "Home DC Power PV"
    HomeOwnConsumption = 83888128, "Home Own Consumption"
    HomeOperatingStatus = 16780032, "Home Operating Status"

    InverterName = 16777984, "Inverter Name"
    InverterMake = 16780544, "Inverter Make"

    VersionUI = 16779267, "Version UI"
    VersionFW = 16779265, "Version FW"
    VersionHW = 16779266, "Version HW"
    VersionPAR = 16779268, "Version PAR"
    SerialNumber = 16777728, "Serial Number"
    ArticleNumber = 16777472, "Article Number"
    CountrySettingsName = 16779522, "Country Settings Name"
    CountrySettingsVersion = 16779521, "Country Settings Version"

    StatisticsDayYield = 251658754, "Statistics Day Yield"
    StatisticsDayHomeConsumption = 251659010, "Statistics Day Home Consumption"
    StatisticsDayOwnConsumption = 251659266, "Statistics Day Own Consumption"
    StatisticsDayOwnConsumptionRate = 251659278, "Statistics Day Own Consumption Rate"
    StatisticsDayAutonomyDegree = 251659279, "Statistics Day Autonomy Degree"

    StatisticsYearYield = 251658753, "Statistics Year Yield"
    StatisticsYearOperatingTime = 251658496, "Statistics Year Operating Time"
    StatisticsYearHomeConsumption = 251659009, "Statistics Year Home Consumption"
    StatisticsYearOwnConsumption = 251659265, "Statistics Year Own Consumption"
    StatisticsYearOwnConsRate = 251659280, "Statistics Year Own Consumption Rate"
    StatisticsYearAutonomyDegree = 251659281, "Statistics Year Autonomy Degree"
