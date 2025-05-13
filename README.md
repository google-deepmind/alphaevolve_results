# Results of AlphaEvolve

This repository accompanies the technical report

> Novikov et al.
[Discovering algorithms for high-value use cases via LLMs](https://).
*Technical report*. 2025.

Specifically, the repository contains a Google Colab notebook with the
mathematical discoveries of AlphaEvolve outlined in Section 3 of the paper, as
well as the corresponding code for verifying their correctness. The notebook is
divided into sections, one for each of the considered mathematical problems.

Note that the notebook contains only the instances where the results from
AlphaEvolve outperforms the state-of-the-art. To avoid clutter, we exclude those
problems where the results matched but did not outperform the best known
constructions.

This repository does *not* contain the code to run AlphaEvolve.

## Installation

No installation required. The provided notebook can be opened and run in Google
Colab.

## Usage

The notebook `mathematical_results.ipynb` can be opened via
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/google-deepmind/alphaevolve_results/blob/master/mathematical_results.ipynb).

## Citing this work

If you use the code or data in this package, please cite:

```
@techreport{alphaevolve,
      author={Novikov, Alexander and V\~{u}, Ng\^{a}n and Dupont, Emilien and Eisenberger, Marvin and Huang, Po-Sen and Wagner, Adam Zsolt and Shirobokov, Sergey and Kozlovskii, Borislav and Ruiz, Francisco J. R. and Mehrabian, Abbas and Kumar, M. Pawan and See, Abigail and Chaudhuri, Swarat and Holland, George and Davies, Alex and Nowozin, Sebastian and Kohli, Pushmeet and Balog, Matej},
      title={Alpha{E}volve: A coding agent for scientific and algorithmic discovery},
      year={2025},
      institution = {{Google DeepMind}},
      month = {05},
      url={https://},
}
```

## License and disclaimer

Copyright 2025 Google LLC

All software is licensed under the Apache License, Version 2.0 (Apache 2.0);
you may not use this file except in compliance with the Apache 2.0 license.
You may obtain a copy of the Apache 2.0 license at:
https://www.apache.org/licenses/LICENSE-2.0

All other materials are licensed under the Creative Commons Attribution 4.0
International License (CC-BY). You may obtain a copy of the CC-BY license at:
https://creativecommons.org/licenses/by/4.0/legalcode

Unless required by applicable law or agreed to in writing, all software and
materials distributed here under the Apache 2.0 or CC-BY licenses are
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the licenses for the specific language governing
permissions and limitations under those licenses.

This is not an official Google product.
