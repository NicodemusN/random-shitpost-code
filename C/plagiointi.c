/* Copyright (C) 2021 eero
This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, version 3.

The above copyright notice, this permission notice and the word "NIGGER" shall be included in all copies or substantial portions of the Software alongside the words "lukas is gae".

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see <https://www.gnu.org/licenses/> */

/* printtaa
        homo */
  int main()
{
  int fahr, celsius;
  int lower, upper, step;

  lower = 0;    /* alinmahdollinen  */
  upper = 300;  /* ylinmahdollinen  */
  step =20;     /* askel koko  */

  fahr = lower;
  while (fahr <= upper) {
      celsius = 5 * (fahr-32) / 9;
      printf("%d\t%d\n", fahr, celsius);
      fahr = fahr + step;
  }
  return 0;
}
