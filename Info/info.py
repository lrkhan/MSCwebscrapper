import pandas as pd

actgrp = ['Abrasives','Clamping,Workholding&Positioning','Holemaking','IndexableCuttingTools','Lubricants,Coolants&Fluids','Machinery','Measuring&Inspecting','Milling','Threading','ToolHolding','Turning&Boring','MISC']
actsbgrp = ['Files','Batteries','SteelRules','CutoffWheels','DeburringWheels','DiscBrushes','QuickChangeDiscs','Swivel&ScraperBlades','TubeBrush','UnmountedBuffingWheels','WheelBrushes','FingerClamps','ManualEdgeClamps','Jaws','Collet','Chuk','AircraftExtensionDrillBits','ChamferMills','ChuckingReamers','CombinationDrill&Countersinks','Countersinks','ExtraLengthDrillBits','JobberLengthDrillBits','MicroDrillBits','PortingTools','ScrewMachineLengthDrillBits','SpottingDrills','Straight-Flute&DieDrillBits','TaperLengthDrillBits','BoringInserts','Caps&PlugsForIndexables','Cut-OffInserts','DrillBodies','GroovingInserts','IndexableBoringBars','IndexableCut-OffBlades','IndexableCut-OffToolholders','IndexableDrillInserts','IndexableGroovingToolholders','IndexableInsertDrills','IndexableThreadingToolholders','IndexableTurningToolholders','LaydownThreadingInserts','MillingInserts','MillingTipInserts','ModularGroovingCuttingUnitHeads','ModularThreadingCuttingUnitHeads','ModularTurning&ProfilingCuttingUnitHeads','ReplaceableDrillTips','Replaceable-TipDrills','ScrewsForIndexables','ShimsForIndexables','SpadeDrillInserts','ThreadingInserts','ThreadMillInserts','TurningInserts','CoolantHoseNozzles','MillingMachineCleaningTools','CMMStyli&Probes','NoGoGages','ScrewThreadMicrometers','SteelRule','Calipers','DepthMicrometers','PinGuageKit','BallEndMills','CornerRadius&CornerChamferEndMills','CornerRoundingEndMills','Double-AngleCutters','DovetailCutters','DrillMills','EngravingCutters','KeyseatCutters','Roughing&FinishingEndMills','RoughingEndMills','Slitting&SlottingSaws','SpiralRouterBits','SquareEndMills','TaperedEndMills','T-SlotCutters','CombinationDrill&Taps','ExtensionTaps','HandSTITaps','HelicalFluteThreadMills','SingleProfileThreadMills','SpiralFlutePipeTaps','SpiralFluteSTITaps','SpiralFluteTaps','SpiralPointTaps','StandardPipeTaps','StraightFluteTaps','StraightFluteThreadMills','ThreadFormingTaps','BoringBarHolders&Adapters','ColletChucks','MachineToolArbors&ArborAdapters','ModularToolHoldingSystemAdapters','RetentionKnobs','RotaryToolHolderHardware','Shrink-FitAccessories','Shrink-FitToolHolders&Adapters','BoringBars','GroovingTools','KnurlWheels','Tooling','Blades','Broach','Cleaning','Automate','FlexHone','Screws']

data = pd.read_csv('./info/gsheet.csv')

#print(data)

group=[]
subgroup=[]

for i in range(len(data.index)-1):
    if str(data.iloc[i,3]) not in group:
        group.append(str(data.iloc[i,3]))
        print("Added " + str(data.iloc[i,3]) + " to group")
    
    if str(data.iloc[i,4]) not in subgroup:
        subgroup.append(str(data.iloc[i,4]))
        #print("Added " + str(data.iloc[i,4]) + " to subgroup")

'''print("The possible Groups are:")
print()
for i in group:
    print(i)

print("----------")
print("The possible subgroups are:")
print()

for i in subgroup:
    print(i)'''

#checking for discrepencies

print('checking for discrepencies in group')
for i in group:
    if i not in actgrp:
        print("Error: " + i + " not in grp lst")
print('')
print('checking for discrepencies in subgroup')
for i in subgroup:
    if i not in actsbgrp:
        print("Error: " + i + " not in sbgrp lst")
