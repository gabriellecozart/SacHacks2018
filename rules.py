from vehicle import Vehicle

# vehicleTest = Vehicle(12455, "Tesla", "S3", 2018, 50000, (38.665266, -121.391185), None)

def manipulateTeslaAirFilter(vehicleInstance, airQuality):
  updatedInstance = vehicleInstance
  filterStatus = updatedInstance.getTeslaAirFilterLifespan()
  updatedInstance.setTeslaAirFilterLifespan(filterStatus - airQuality * 0.03)
  return updatedInstance

def manipulateBrakePad(vehicleInstance):
  updatedInstance = vehicleInstance
  brakeStatus = updatedInstance.getBrakePadLifespan()
  updatedInstance.setBrakePadLifespan(brakeStatus - 42)
  return updatedInstance

def manipulateBattery(vehicleInstance):
  updatedInstance = vehicleInstance
  batteryStatus = updatedInstance.getBatteryLifespan()
  updatedInstance.setBatteryLifespan(batteryStatus - 19)
  return updatedInstance

def manipulateWindshieldWiper(vehicleInstance):
  updatedInstance = vehicleInstance
  wiperStatus = updatedInstance.getWindshieldWiperLifespan()
  updatedInstance.setWindshieldWiperLifespan(wiperStatus - 18)
  return updatedInstance

def executeRules(vehicleInstance, airQuality, tempurature, climate):
  updatedInstance = vehicleInstance

  if len(updatedInstance.odometer) > 1:
    milesDrivenSinceLast = updatedInstance.odometer[-1] - updatedInstance.odometer[-2]
  else:
    milesDrivenSinceLast = 0

  updatedInstance.decreaseWindshieldWiperLifespan(milesDrivenSinceLast)
  if climate == "Drizzle" or climate == "Rain" or climate == "Snow":
    updatedInstance = manipulateWindshieldWiper(updatedInstance)

  if updatedInstance.make == "TESLA":
    updatedInstance.decreaseTeslaAirFilterLifespan(milesDrivenSinceLast) 
    if airQuality > 100:
      updatedInstance = manipulateTeslaAirFilter(updatedInstance, airQuality)
  else:
    updatedInstance.decreaseBatteryLifespan(milesDrivenSinceLast)
    updatedInstance.decreasebrakePadLifespan(milesDrivenSinceLast)
    if tempurature <= 32:
      updatedInstance = manipulateBattery(updatedInstance)
      updatedInstance = manipulateBrakePad(updatedInstance)
  return updatedInstance