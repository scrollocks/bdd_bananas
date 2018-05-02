Feature: Keep track of quantity of bananas sold

  Scenario: sell some bananas
    Given we have have a banana stand with inventory
        | items   | qty |
        | bananas | 10  |
        | nuts    | 10  |
        | choc    | 10  |
      When we sell 5 frozen bananas at 4.50 each 
      Then we will have total quantity sold of 5

  Scenario: sell some bananas without enough stock
    Given we have have a banana stand with inventory
        | items   | qty |
        | bananas | 1  |
        | nuts    | 1  |
        | choc    | 1  |
      When we sell 5 frozen bananas at 4.50 each 
      Then we will have total quantity sold of 1
