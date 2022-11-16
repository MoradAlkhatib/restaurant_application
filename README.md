# LAB-02: GUI - tkinter

This Lab will make you practice building GUI using tkinter library and testing by write some functions and import them to another file to test them because as you learned today python when combined with Tkinter provides a fast and easy way to create GUI applications.

## Steps
- Please follow the below steps as an example.
 
1. Create a local git repo with root folder named `restaurant_application-gui` in the windows system.
2. Create a new repo on Github called `restaurant_application-gui`.
3. Link your local and remote repositories
4. Create python environment using windows powerShell

        ```bash
        python -m venv .venv

        .venv\Scripts\activate

        pip install package-name

        ```
5. then set it up based on the following structure.

```    
├── .venv
├── module_name
    ├── __init__.py
│   ├── name.py
├── test
    ├── __init__.py
│   ├── test_module_name.py
├── .gitignore
├── README.md

Please make sure don't use the names as its here its just an example.
```
5. create a new branch and called it `gui`.
6. Work on a `gui` branch.
7. After completing the lab, create a PR from your `gui` branch to `main` then merge your code.


## Lab Requirements

Build Restaurant Menu application using tkinter library by following these steps:

- Create a form that allow the user to enter
    - `pizza quantity` and `pizza size` using dropdown list which allow the user to select one of these options [ `Small` ,`Medium` , `Large`]
    - `burger quantity` and `burger size` using dropdown list which allow the user to select one of these options [ `Classic` ,`Big`] 
    - `Soft drinks quantity`
    - user should select order type if it is `Takeaway` or `Dine in` using radio buttons
    - user can decide if he want `Extra Cheese` or `Extra Ketchup` using checkboxes
    - `Order Summary` button which will display a `message box` after clicking on it
- `message box` should display the summary of the order
- Describe the purpose of each entry using `labels`
- Use the tkinter `grid` to place the form entries in a pretty way

### stretch goal

- Compute the total price for the order and display it in the message box

| Category      | Siza   |  Price |
|---------------|:------:|-------:|
| Pizza         | Small  | 5$     |
| Pizza         | Medium | 7$     |
| Pizza         | Large  | 10$    |
| Burger        | Classic| 5$     |
| Burger        | Big    | 7$     |
| Soft Drink    |        | 2$     |
| Extra Cheese  |        | 1$     |
| Extra Ketchup |        | 1$     |


## Submission Instructions
- Submit your pull request.
- Tell us if you faced any issue.
- Tell us the time you used to solved the lab. 