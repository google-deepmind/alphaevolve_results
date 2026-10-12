# Results in the notebook that have since been superseded

The notebook records the values AlphaEvolve obtained in 2025. Better values for the 14 problems below have since appeared, most of them in 2026. The notebook's values are unchanged, and this table only points to the newer records. Each better value was checked against the source listed: the paper or canonical table was opened and the number read there, or a public construction file was downloaded and checked offline (marked *construction checked*). Sources were checked on 2026-10-12. "Before pin" means the source predates the notebook's last commit (2026-01-05).

| problem (notebook section) | direction | notebook value | better value | source | date |
|---|---|---|---|---|---|
| Rank decomposition of ⟨3,4,8⟩ over Z | min rank | 74 | 73 (over Z) | Perminov, arXiv:2603.02398, Table 3 ("Rediscovered schemes with integer coefficients (Z)") — https://arxiv.org/abs/2603.02398 | 2026-03-02 |
| Rank decomposition of ⟨3,5,7⟩ over Z | min rank | 80 | 79 (over Z; also over {-1,0,1}) | Perminov, arXiv:2603.02398, Table 3; arXiv:2606.02480, Table 3 — https://arxiv.org/abs/2603.02398 (*construction checked*: 11025 tensor entries, 0 mismatches) | 2026-03-02 |
| Rank decomposition of ⟨4,4,8⟩ over 0.5*C | min rank | 96 | 95 (over Q) | Perminov, FastMatrixMultiplication repository, `schemes/results/Q/4x4x8_m95_Q.json` — https://github.com/dronperminov/FastMatrixMultiplication; listed in the Lille catalogue (fmm.univ-lille.fr) (*construction checked*: 16384 tensor entries, 0 mismatches) | 2026-09-28 |
| B.1 First autocorrelation inequality (upper bound on C₁) | min | 1.5053 | 1.50286 | arXiv:2601.16175 — https://arxiv.org/abs/2601.16175 (AlphaEvolve's own v2 report, arXiv:2511.02864, already had 1.5032) | 2026-01-22 |
| B.2 Second autocorrelation inequality (lower bound on C₂) | max | 0.8962 | 0.94136 (2025); 0.962694 (2026) | Jaech & Joseph, arXiv:2508.02803 — https://arxiv.org/abs/2508.02803 (before pin); arXiv:2604.19341 | 2025-08-04; 2026-04-21 |
| B.4 Uncertainty inequality, formulation 1 (upper bound on C₄) | min | 0.3521 | 0.3482 | arXiv:2602.16805, Sec. 4.1 / App. I (same Hermite × Gaussian family with more coefficients) — https://arxiv.org/abs/2602.16805 | 2026-02-18 |
| B.5 Erdős minimum overlap (upper bound) | min | 0.380924 | 0.380868 | arXiv:2604.19341, Table 1 — https://arxiv.org/abs/2604.19341 (earlier 0.380876, arXiv:2601.16175) | 2026-04-21 |
| B.6 Sums and differences of finite sets (lower bound on C₆) | max | 1.1584 | 1.173077 | Zheng, arXiv:2506.01896 — https://arxiv.org/abs/2506.01896 (before pin; earlier 1.173050, Gerbicz, arXiv:2505.16105) | 2025-06-02 |
| B.7 Packing 11 unit hexagons in a regular hexagon (side) | min | 3.931 | 2+10/(3√3) = 3.92450… | Friedman's Packing Center, hexagons in hexagons — https://erich-friedman.github.io/packing/hexinhex/ (Schellhorn; before pin) | 2025-07 |
| B.8 Min/max distance ratio, 16 points in 2D (ratio²) | min | 12.889266112 | 12.889230201 | arXiv:2510.26144, §5.3.3 — https://arxiv.org/abs/2510.26144 (before pin) | 2025-10-30 |
| B.8 Min/max distance ratio, 14 points in 3D (ratio²) | min | 4.165849767 | 4.16578 | Berthold, Kamp, Mexi, Pokutta, Pólik, arXiv:2601.05943 — https://arxiv.org/abs/2601.05943 | 2026-01-09 |
| B.11 Kissing number in dimension 11 | max | 593 | 604 | Bianchi, Kwon, Pappu, Zou, arXiv:2606.10402; Cohn's kissing-number table — https://arxiv.org/abs/2606.10402 | 2026-06-09 |
| B.12 Circle packing, 26 circles in a unit square (sum of radii) | max | 2.635 | 2.63598 | Friedman's Packing Center, circles in squares (max sum of radii) — https://erich-friedman.github.io/packing/cirRsqu/ | 2026-07 |
| B.12 Circle packing, 32 circles in a unit square (sum of radii) | max | 2.937 | 2.93957 | Berthold, Kamp, Mexi, Pokutta, Polik, arXiv:2605.04850, Table 1 — https://arxiv.org/abs/2605.04850 | 2026-05-06 |
