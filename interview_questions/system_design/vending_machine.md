# Vending Machine

## Description

Design a vending machine

## Requirements

#### Actors
* User
* Machine

#### Actions
* Machine must keep track of inventory
* Person must insert payment into machine and select an item
* Machine confirms payment and the price of the item
* Machine displays any errors (insufficient payment, unavailable item)
* Person receives their selected item


## States

### Machine
* Ready
* Cash Collected
* Dispense Change
* Dispense Item
* Transaction Cancelled


