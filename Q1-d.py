import matplotlib.pyplot as plt
import numpy as np
import math
import random
"""
Start on day 1, continue for 3 months, assume 30 days in each month, so day ranges in [1,90]
On day 1, everyone have probability p of being infected.
Every person needs a test after 7 days.
Every person not being to work (due to test limitation or was sick) results in a lose of $172 dollars per day.
Goal: Minimize social/economic impact
"""
class person_class:
    def __init__(self, is_infected: bool, infected_date, last_test_date, test_good: bool):
        self.is_infected = is_infected
        self.infected_date = infected_date
        self.last_test_date = last_test_date
        self.test_good = test_good
population = 10000
max_test = 500
p_lst = np.arange(0.002, 0.0201, 0.002)

#########################################################################
# Individual Code
# 1. All tests should be used in a day
# 2. Test individual when they need a new test to go to work
# Representation: A size 10000 people list, a size 10000 day list
# each index is a person
# for each day, first update the people list to simulate people getting sick
# do tests for 500 people
##########################################################################
total_cost = []
for p_i in p_lst:
    p = p_i
    people_lst = []
    daily_cost = []
    print("p =", p)
    # initialize day 0
    for i in range(population):
        people_lst.append(person_class(False, -30, -30, True))
    # simulate other days
    for day in range(1, 91, 1):
        temp_count = 0
        # calculating cost
        for person in people_lst:
            if(person.last_test_date < day - 7 or not person.test_good):
                temp_count = temp_count + 1
        daily_cost.append(temp_count)
        # each day:
        available_test = max_test
        # simulate sick now
        for person in people_lst:
            if (not person.is_infected):
                rand_num = random.random()
                if(rand_num < p):
                    person.is_infected = True
                    person.infected_date = day
        # do tests
        for person in people_lst:
            # they need a test right now
            # 1) People who were healthy
            #   -> test_result good AND last_test_date diff 7
            # 2) People who were sick, waited 21 days
            #   -> test_result bad AND infection_date diff 21
            if person.test_good and person.last_test_date <= day - 7:
                available_test = available_test - 1
                person.last_test_date = day
                person.test_good = not person.is_infected
                if available_test == 0:
                    break

            elif not person.test_good and person.infected_date <= day - 21:
                available_test = available_test - 1
                person.last_test_date = day
                person.is_infected = False
                person.test_good = True
                if available_test == 0:
                    break
    sum_cost = 0
    for k in daily_cost:
        sum_cost = k + sum_cost
    total_cost.append(sum_cost)
print(total_cost)
plt.xlabel("p")
plt.ylabel("total economic cost in 3 months (unit: $172)")
plt.title("p vs total cost with individual testing")
plt.xlim([0.002, 0.02])
plt.ylim([40000, 650000])
plt.plot(p_lst, total_cost, color='c')
plt.savefig('images/1.d-1.png')


#####################################################################
# Dorfman Code
# 1. Almost all tests should be used in a day
# 2. Test the n_star group (depending on p) in the population with the Dorfman method.
# 3. If the remaining available test in a day is less then n_star + 1 to promise over
# the whole group via Dorfman method, switch to individual test for such remaining tests
# 4. Prioritize and give test to people that need test tomorrow first.
# 5. If more tests are left, give test to people that need test in two days.
# 6. If still have more test left, give test to people that need test in four days.
#####################################################################
total_cost_10 = [0 for i in range(10)]
for run in range(10):
    total_cost_lst = []
    n = np.arange(0, 25)
    n_star_lst = []
    for diff_p in p_lst:
        max = 0
        max_n = 0
        for i in n:
            num = i / (i + (1-i) * math.pow(1-diff_p, i))
            if(num > max):
                max = num
                max_n = i
        n_star_lst.append(max_n)
    for p_i in range(len(p_lst)):
        p = p_lst[p_i]
        daily_cost = []
        n_star = n_star_lst[p_i]
        people_lst = []
        print("p =", p)
        # initialize day 0
        for i in range(population):
            people_lst.append(person_class(False, -30, -30, True))
        # simulate other days
        for day in range(1, 91, 1):
            good_to_work = 0
            index = 0
            for person in people_lst:
                index = index + 1
                if person.test_good and person.last_test_date >= day - 7:
                    good_to_work = good_to_work + 1
            # calculating cost
            temp_count = 0
            for person in people_lst:
                if(person.last_test_date < day - 7 or not person.test_good):
                    temp_count = temp_count + 1
            daily_cost.append(temp_count)
            # each day:
            available_test = max_test
            # simulate sick now
            for person in people_lst:
                if (not person.is_infected):
                    rand_num = random.random()
                    if(rand_num < p):
                        person.is_infected = True
                        person.infected_date = day
            find_next_n = 0
            # do tests
            # they need a test right now
            # 1) People who were healthy
            #   -> test_result good AND last_test_date diff 7
            # 2) People who were sick, waited 21 days
            #   -> test_result bad AND infection_date diff 21
            clear = 0
            for i in range(0, 10000, n_star):
                break_i_loop = False
                if available_test == 0:
                    break
                # if not enough test, use individual testing, if at the end of the list, just end the day
                if(available_test <= n_star):
                    for j in range(i, i+available_test, 1):
                        if j >= 10000:
                            break
                        person = people_lst[j]
                        # 1) healthy people need regular test 2) sick people need proof test 3) healthy person testing early with extra test
                        if person.test_good and person.last_test_date <= day - 7:
                            available_test = available_test - 1
                            person.last_test_date = day
                            person.test_good = not person.is_infected
                        elif not person.test_good and person.infected_date <= day - 21:
                            available_test = available_test - 1
                            person.last_test_date = day
                            person.is_infected = False
                            person.test_good = True
                # test n_star people together
                else:
                    all_clear = True
                    skip = 0
                    j = i
                    while (j < i+n_star+skip):
                        if j >= 10000:
                            break_i_loop = True
                            break
                        person = people_lst[j]
                        if person.test_good and person.last_test_date <= day - 7:
                            person.last_test_date = day
                            person.test_good = not person.is_infected
                            if person.is_infected:
                                all_clear = False
                        elif not person.test_good and person.infected_date <= day - 21:
                            person.last_test_date = day
                            person.is_infected = False
                            person.test_good = True
                        else:
                            skip = skip + 1
                        j = j + 1
                    if all_clear:
                        available_test = available_test - 1
                        clear = clear + 1
                    else:
                        available_test = available_test - 1 - n_star
                if available_test == 0 or break_i_loop:
                    break

            if available_test > 0:
                for i in range(0, 10000, n_star):
                    break_i_loop = False
                    if available_test == 0:
                        break
                    if(available_test <= n_star):
                        for j in range(i, i+available_test, 1):
                            if j >= 10000:
                                break
                            person = people_lst[j]
                            if person.test_good and person.last_test_date <= day - 5:
                                available_test = available_test - 1
                                person.last_test_date = day
                                person.test_good = not person.is_infected
                    else:
                        all_clear = True
                        skip = 0
                        j = i
                        while (j < i+n_star+skip):
                            if j >= 10000:
                                break_i_loop = True
                                break
                            person = people_lst[j]
                            if person.test_good and person.last_test_date <= day - 5:
                                person.last_test_date = day
                                person.test_good = not person.is_infected
                                if person.is_infected:
                                    all_clear = False
                            else:
                                skip = skip + 1
                            j = j + 1
                        if all_clear:
                            available_test = available_test - 1
                            clear = clear + 1
                        else:
                            available_test = available_test - 1 - n_star
                    if available_test == 0 or break_i_loop:
                        break
            if available_test > 0:
                for i in range(0, 10000, n_star):
                    break_i_loop = False
                    if available_test == 0:
                        break
                    if(available_test <= n_star):
                        for j in range(i, i+available_test, 1):
                            if j >= 10000:
                                break
                            person = people_lst[j]
                            if person.test_good and person.last_test_date <= day - 3:
                                available_test = available_test - 1
                                person.last_test_date = day
                                person.test_good = not person.is_infected
                    else:
                        all_clear = True
                        skip = 0
                        j = i
                        while (j < i+n_star+skip):
                            if j >= 10000:
                                break_i_loop = True
                                break
                            person = people_lst[j]
                            if person.test_good and person.last_test_date <= day - 3:
                                person.last_test_date = day
                                person.test_good = not person.is_infected
                                if person.is_infected:
                                    all_clear = False
                            else:
                                skip = skip + 1
                            j = j + 1
                        if all_clear:
                            available_test = available_test - 1
                            clear = clear + 1
                        else:
                            available_test = available_test - 1 - n_star
                    if available_test == 0 or break_i_loop:
                        break
        sum_cost = 0
        for k in daily_cost:
            sum_cost = k + sum_cost
        total_cost_lst.append(sum_cost)
    print(total_cost_lst)
    for p_i in range(len(total_cost_lst)):
        total_cost_10[p_i] = total_cost_10[p_i] + total_cost_lst[p_i]
    total_cost_lst = []
for p_i in range(len(total_cost_10)):
    total_cost_10[p_i] = total_cost_10[p_i] / 10
print(total_cost_10)


plt.clf()
plt.xlabel("p")
plt.ylabel("total economic cost for 3 months with Dorfman testing (unit: $172)")
plt.title("p vs total cost with Dorfman testing")
plt.xlim([0.002, 0.02])
plt.ylim([40000, 650000])
plt.plot(p_lst, total_cost_10, color='c')
plt.savefig('images/1.d-2.png')
