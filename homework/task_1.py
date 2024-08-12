# Task: Visualize the result of Euler's Method in Python to analyze error and stability.

# 1. Import matplotlib.pyplot with its corresponding alias and the math library.




# 2. Copy and paste the Euler's Method function from class (called eulers_method).



# 3. Define a function called plot_newtons_method that outputs the result of applying Newton's Method
# to an ODE initial value problem with specified step sizes.
#    - Parameters:
#      - f: The function representing the ODE.
#      - t0: Initial time.
#      - y0: Initial value of y.
#      - t_end: End time.
#      - step_sizes: List of step sizes to compare.
#      - true_y: The true solution to the ODE.



    fig, ax = plt.subplots(figsize=(12, 8))

    # 3. Loop through each step size.



        # 4. Save the outputs of eulers_method with the corresponding
        # step size to t_values and y_values.



        # 5. Plot the results of Euler's Method using the label Step Size = #
        # where # is replaced with the actual step size.



    # 6. Create a list called y_values that evaluates true_y for each t in t_values.



    # 7. Plot true_y in the color black with the label True Solution.



    ax.set_xlabel("t")
    ax.set_ylabel("y")
    ax.set_title("Euler's Method for Different Step Sizes")
    ax.legend()
    ax.grid(True)
    return fig


# 8. Define a function f representing the ODE dy/dt = -2ty.



# 9. Define a function true_y representing the solution to the ODE dy/dt = -2ty with y(0)=1.
# You will need to use the math library here.



# 10. Apply the plot_eulers_method function to the ODE dy/dt = -2ty with an initial value
# y(0) = 1, end time of 2, and step_sizes 0.2, 0.1, 0.05, 0.01, and 0.001.


