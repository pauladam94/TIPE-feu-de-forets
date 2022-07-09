#ifndef MATH_H_INCLUDED
#define MATH_H_INCLUDED
#include <string.h>

const int h(466),l(300);

void alea();

void creat_list   (std::string nom, int tabl[][l], int const hi, int const lj);

bool testegalite  (int terre[][l],int nvterre[][l],int const hi, int const lj);

void searcharound (int i, int j, int terre[][l]);

bool gen0         (int terre[][l],int nvterre[][l],int const hi, int const lj, double rule[]);

bool gen1         (int terre[][l],int nvterre[][l],int const hi, int const lj, double rule[]);

bool gen2         (int terre[][l],int nvterre[][l],int const hi, int const lj, double rule);

double dif_eucl   (int list1[][l], int list2[][l], int const hi, int const lj);

void egalite      (int accepteur[][l],int donneur[][l],int const hi, int const lj);

double norme      (int terre[][l], int nvterre[][l], int foretbrulee[][l], int const hi, int const lj, double rule[], int version);

void wf           (std::string texte);

double moyenne    (int terre[][l], int nvterre[][l], int foretbrulee[][l], int foretavant[][l],int const hi, int const lj, double rule[], int nb_iter);

double derv       (int terre[][l], int nvterre[][l], int foretbrulee[][l], int foretavant[][l], int const hi, int const lj, double rule[], int l_rule, int nb_iter, double eps, int var);

void pas_dg       (int terre[][l], int nvterre[][l], int foretbrulee[][l], int foretavant[][l], int const hi, int const lj, double rule[], int l_rule, int nb_iter, double eps, double alpha, double newrule[]);

void EC_V         (int terre[][l], int nvterre[][l], int foretbrulee[][l], int foretavant[][l],int const hi, int const lj, double rule[], int precision);

void rule_al      (double rule[], int l_rule);

#endif // MATH_H_INCLUDED
