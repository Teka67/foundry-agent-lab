targetScope = 'resourceGroup'

param location string = resourceGroup().location

resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: 'stfoundrydemo1234'
  location: location

  sku: {
    name: 'Standard_LRS'
  }

  kind: 'StorageV2'
}
