import random

from constants import UNDER_0_DEGREE, OVER_30_DEGREE, UNDER_4_DEGREE, SAMPLE_COUNT, UNDER_8_DEGREE, UNDER_11_DEGREE, \
    UNDER_16_DEGREE, UNDER_19_DEGREE, UNDER_22_DEGREE, UNDER_27_DEGREE, UNDER_30_DEGREE


def choose_clothes(temperature):
    result = []
    if temperature <= 0:
        return UNDER_0_DEGREE
    if temperature > 30:
        return OVER_30_DEGREE

    if temperature <= 4:
        result = random.sample(UNDER_4_DEGREE, SAMPLE_COUNT)
    elif temperature <= 8:
        result = random.sample(UNDER_8_DEGREE, SAMPLE_COUNT)
    elif temperature <= 11:
        result = random.sample(UNDER_11_DEGREE, SAMPLE_COUNT)
    elif temperature <= 16:
        result = random.sample(UNDER_16_DEGREE, SAMPLE_COUNT)
    elif temperature <= 19:
        result = random.sample(UNDER_19_DEGREE, SAMPLE_COUNT)
    elif temperature <= 22:
        result = random.sample(UNDER_22_DEGREE, SAMPLE_COUNT)
    elif temperature <= 27:
        result = random.sample(UNDER_27_DEGREE, SAMPLE_COUNT)
    elif temperature <= 30:
        result = random.sample(UNDER_30_DEGREE, SAMPLE_COUNT)

    return ', '.join(result)