import random as rand
import matplotlib.pyplot as plt

def Fred_indeedSick(prevalence, specificity, sensitivity):
    prob_list = []
    # iterate 1000 times
    for n in range(1000):
        # record number of incidence where Fred is tested sick
        count_testSick = 0
        # record number of incidence where Fred is indeed sick
        count_testSick_sick = 0
        # iterate 1000 times to get one statistic
        for i in range(1000):
            # randomly select a person, with 'prevalence' chance of being infected
            health_status = rand.choices(['sick', 'healthy'], weights=[prevalence, 1-prevalence], k=1)[0]
            # if health_status is sick, use sensitivity to predict his testing result
            test_result = ''
            if health_status == 'sick':
                test_result = rand.choices(['sick', 'healthy'], weights=[specificity, 1-specificity], k=1)[0]
            # otherwise, health_status is healthy, use specificity to predict his testing result
            else:
                test_result = rand.choices(['healthy', 'sick'], weights=[sensitivity, 1-sensitivity], k=1)[0]

            # increment if test result is 'sick'
            if test_result == 'sick':
                count_testSick += 1
            # increment if test result and health status are both 'sick'
            if test_result == 'sick' and health_status == 'sick':
                count_testSick_sick += 1

        # calculate probability of being sick when tested sick
        prob = count_testSick_sick / count_testSick
        # record it in the list
        prob_list.append(prob)
    return prob_list




def main():

    prevalence = 0.50  # real-number value between 0.001% to 50%
    specificity = 0.99  # takes values 99%, 99.9%,99.99%, and 99.999%
    sensitivity = 0.99  # fix at 0.99

    prob_list = Fred_indeedSick(prevalence, specificity, sensitivity)

    avg=sum(prob_list)/len(prob_list)
    # visualize the distribution of probabilities via a histogram
    n = plt.hist(prob_list, bins=50)
    plt.title("Task 2: Prevalence = 0.50, Specificity=0.99")
    plt.vlines(x=avg, ymin=0, ymax=max(n[0]+2), colors='r', label='average {:1.2f} %'.format(avg*100))
    plt.xlabel("Probability of Fred is actually infected")
    plt.ylabel("Count of Occurance across 1000 simulations")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
