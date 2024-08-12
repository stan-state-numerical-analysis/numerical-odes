
# Task: Visualize the result of the 4th-Order Runge-Kutta Method in Python to analyze accuracy.

# 1. Import matplotlib.pyplot with its corresponding alias.



# 2. Create a function called runge_kutta_4 that approximates the ODE solution using the 4th-Order Runge-Kutta method.
#    - Parameters:
#      - f: The function representing the ODE.
#      - t0: Initial time.
#      - y0: Initial value of y.
#      - t_end: End time.
#      - step_size: Size of each time step.



    # 3. Initialize the lists t_values and y_values using the initial condition.



    # 4. Use a while-loop which breaks once the next step exceeds the end time.



        # 5. Initialize the variables k1, k2, k3, k4 from the 4th-Order Runge-Kutta method.

        

        # 6. Append to y_values the approximate value for the next time step.

        

        # 7. Append the new time step to the t_values list.

        

    # 8. Return the t_values and y_values lists.

    


# 9. Define a function called plot_runge_kutta_4 that outputs the result of applying the 4th-Order
# Runge Kutta Method to an ODE initial value problem with specified step sizes. Copy and paste the code
# from task_1 or task_2 and make the necessary adjustments.



# 11. Import f and true_y from task_1.py.



# 12. Apply the plot_runge_kutta_2 function to the ODE dy/dt = -2ty with an initial value
# y(0) = 1, end time of 2, and step_sizes 0.2, 0.1, 0.05, 0.01, and 0.001.


