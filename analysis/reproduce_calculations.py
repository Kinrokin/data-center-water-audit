"""Reproduce only the article's explicit calculations; no deployment is simulated."""
from math import isclose
L_PER_US_GAL = 3.785411784
indirect = 176 * 4.52 / L_PER_US_GAL
direct = 66 / L_PER_US_GAL
total = direct + indirect
daily_mgal = total * 1000 / 365
ratio = daily_mgal / 75698
checks = {
 'national_liters': isclose(176 * 4.52 + 66, 861.52),
 'gallon_reconstruction': isclose(total, 861.52 / L_PER_US_GAL),
 'national_rounded_billions': round(total) == 228,
 'continuous_500mw_twh': isclose(500 * 24 * 365 / 1e6, 4.38),
 'clinical_minutes': isclose(.36 * 60, 21.6),
 'clinical_20_day_extrapolation': isclose(.36 * 20, 7.2),
 'workflow_3_percent_overhead': isclose(.8 + .2/2 + .03, .93),
 'workflow_12_percent_overhead': isclose(.8 + .2/2 + .12, 1.02),
 'intensity_times_scale': isclose(.5 * 3, 1.5),
 'illustrative_phased_load': 50 + 150 == 200,
}
if __name__ == '__main__':
 for name,ok in checks.items():
  if not ok: raise AssertionError(name)
 print(f'{len(checks)} arithmetic checks passed')
 print(f'Direct / indirect / total, billion US gal: {direct:.9f} / {indirect:.9f} / {total:.9f}')
 print(f'Daily million US gal: {daily_mgal:.9f}; irrigation benchmark percent: {ratio*100:.9f}')
 print('The assumptions remain assumptions. These checks establish arithmetic only.')
