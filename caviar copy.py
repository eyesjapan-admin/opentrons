from opentrons import containers, instruments



#Automatic Caviar

# Solution
trough = containers.load('trough-12row', 'D3')

# 1. Container
plate = containers.load('96-PCR-flat', 'B1')

# 2. Container
plate2 = containers.load('96-PCR-flat', 'C1')

# 3. Container
plate3 = containers.load('96-PCR-flat', 'D1')

# Pipettes
p1000rack = containers.load('tiprack-200ul', 'B3')


# Fill 1. Container
green_wells = [
    well.bottom() for well in plate.wells(
        'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
        'A9', 'A10', 'A11', 'A12')
    ]
    
# Fill 2. Container
green_wells2 = [
    well.bottom() for well in plate2.wells(
        'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
        'A9', 'A10', 'A11', 'A12')
    ]
    
# Fill 3. Container
green_wells3 = [
    well.bottom() for well in plate3.wells(
        'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
        'A9', 'A10', 'A11', 'A12')
    ]


# Solution location
green = trough.wells('A1')


p1000 = instruments.Pipette(
        axis='a',
        min_volume=10,
        max_volume=200,
        tip_racks=[p1000rack],
        channels=8
    )


    # Macro commands like .distribute() make writing long sequences easier:
    # Distribute solution to the containers
p1000.distribute(16.2, green, green_wells,disposal_vol=0, blow_out=True)

p1000.distribute(16.2, green, green_wells2, disposal_vol=0, blow_out=True)

p1000.distribute(16.2, green, green_wells3, disposal_vol=0, blow_out=True)