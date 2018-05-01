Feature: Keep track of inventory

  Scenario: add items to inventory
    Given we have have a banana stand with inventory
        | items   | qty |
        | bananas | 10  |
        | nuts    | 10  |
        | choc    | 10  |
      Then the inventory will match
        | items   | qty |
        | bananas | 10  |
        | nuts    | 10  |
        | choc    | 10  |
