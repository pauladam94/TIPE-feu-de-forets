#include <string>
#include <iostream>
#include <cmath>
#include <fstream>
#include <random>
#include <string.h>
#include "math.h"
using namespace std;

// DEFINITIONS VARIABLES

//const int h(466),l(300);

// .. siginifie le retour en arrière de fichier
string favant("../../experience/video_feu/videos_selec/20/foretavant.txt");
string fbrulee("../../experience/video_feu/videos_selec/20/foretbrulee.txt");

int terre[h][l];
int nvterre[h][l];
int foretavant[h][l];
int foretbrulee[h][l];

//double const regl(0.5); double rule[5] = {regl, regl, regl, regl, regl, regl};
//double rule[5] = {0.5, 0.5, 0.5, 0.5, 0.5};
//int const l_rule  = 24;
//double rule[l_rule];
//double rule[l_rule] = {0.705790 , 0.413583 , 0.698237 , 0.299002 , 0.768593};

int main()
{
/// creation rule aléatoirement
//rule_al(rule, l_rule);
//for(int i = 0; i<l_rule; i++){rule[i] = 0.05;}

/// CREATION des deux listes par lecture des fichiers textes
creat_list(favant,foretavant,h,l); // h=i=329 , l=j=300
creat_list(fbrulee,foretbrulee,h,l);
cout << "done compilating data" << endl;

/// BATTERIE TESTS
//cout << foretavant[4][20] << endl; // doit renvoyer 3
//cout << foretavant[1][1] << endl; // doit renvoyer 1
//cout << foretavant << endl;

/*
for (int j=50; j>=0; j--){
for (int i=0; i<50; i++){
cout<<foretavant[i][j] ;
}cout<<";"<<endl;}

const int k(50);
for (int i=300; i<466; i++){
for (int j=k; j<k+209; j++){
cout << foretbrulee[i][j] ;}
cout << ";" << endl ;}
*/



/// affichage de la norme de départ
//cout << "SANS CALCUL difference euclidienne = " << dif_eucl(foretavant,foretbrulee,h,l) << endl;

/// DEMARRAGE DU FEU :
//foretavant[109][150] = 7; foretavant[110][150] = 7; foretavant[111][150] = 7;
//foretavant[112][150] = 7; foretavant[113][150] = 7; foretavant[111][148] = 7;
//foretavant[111][149] = 7; foretavant[111][151] = 7; foretavant[111][152] = 7;

/// terre = foretavant et nvterre = foretavant
egalite(terre, foretavant, h, l);
egalite(nvterre, foretavant, h, l);
//cout << "done 1er mise a egalite" << endl;



/// Test de moyenne
//int iter (50);
//cout << "moyenne pour " << iter << " iterations = " ;
//double moy( moyenne(terre, nvterre, foretbrulee, foretavant, h, l, rule, iter) );
//cout << moy << " et " << sqrt(moy)<<endl;


/// Calcul écart type pour savoir le nb efficace
/// de nombre d'itération choisir
//EC_V(terre, nvterre, foretbrulee, foretavant, h, l, rule, 20);

/// TEST Calcul de norme  0.484 s
//cout << norme(terre, nvterre, foretbrulee, h, l, rule) << endl;

/// AFFICHAGE QUELQUES NORMES
//for(int k=0; k<100; k++){cout << norme(terre, nvterre, foretbrulee, h, l, rule) << endl;}

/*
/// 1 Pas descente de gradient
string write;
int nb_iter (20); // entre 30-50
double eps = 0.05; // 0.05 / 0.03 / 0.01
double alpha = 1; //  pow(10,-2)pow(10,-3)pow(10,-4)
double newrule[l_rule];
int nb_pas = 300;

/// INITIALISATION :
/// DEBUT
wf("\n\nDEBUT DG\n");


/// DG 5 REGLES
for (int i = 0; i<nb_pas; i++)
{
    /// RULE
    cout << "   rule   : ";
    for (int k = 0; k<l_rule; k++)
    { if (k==0) {cout << rule[k] ; } else {cout << " , " << rule[k] ;}   }
    cout << "" << endl;

    wf("   rule   : ");
    for (int k = 0; k<l_rule; k++)
    { if (k==0) {wf( to_string(rule[k]));} else {wf(" , " + to_string(rule[k]));} }
    wf("\n");

    /// NORME
    cout << "   Norme  = " ;
    write = to_string( moyenne(terre, nvterre, foretbrulee, foretavant, h, l, rule, nb_iter) );
    cout << write << endl;
    wf("   Norme  = " + write + "\n");

    // on fait un pas la descente de gradient
    /// Affichage derivee inclu dans pas_dg
    pas_dg(terre, nvterre, foretbrulee, foretavant, h, l, rule,l_rule, nb_iter, eps, alpha, newrule);

    /// rule = newrule
    for (int k = 0; k<l_rule; k++) { rule[k] = newrule[k];}
}*/

/*
/// DG 24 REGLES
for (int i = 0; i<nb_pas; i++)
{
    /// RULE
    cout << "   rule   : "<<endl;
    for (int k = 0; k<l_rule; k++)
    {
        cout << rule[k] << " , " ;
        if (k==11){cout <<"           ";}
        if (k==4 || k==9 || k==13 || k==18 || k == 23){cout<<""<<endl;}
    }
    cout << "" << endl;

    wf("   rule   : ");if (l_rule==24){wf("\n");}
    for (int k = 0; k<l_rule; k++)
    {
        wf( to_string(rule[k]) + " , " );
        if (k==11){wf("           ");}
        if (k==4 || k==9 || k==13 || k==18 || k == 23){wf("\n");}
    }

    /// NORME
    cout << "   Norme  = " ;
    write = to_string( moyenne(terre, nvterre, foretbrulee, foretavant, h, l, rule, nb_iter) );
    cout << write << endl;
    wf("   Norme  = " + write + "\n");

    /// DERIVEE
    // Affichage derivee inclu dans pas_dg
    pas_dg(terre, nvterre, foretbrulee, foretavant, h, l, rule,l_rule, nb_iter, eps, alpha, newrule);

    /// rule = newrule
    for (int k = 0; k<l_rule; k++) { rule[k] = newrule[k];}
*/

// alea();

/// DEMARRAGE DU FEU :
foretavant[463][145] = 7; foretavant[462][145] = 7;
foretavant[463][144] = 7; foretavant[462][144] = 7;
foretavant[463][143] = 7; foretavant[462][143] = 7;
foretavant[463][142] = 7; foretavant[462][142] = 7;


/*
for (int p = 0; p<5 ; p++)
{

const int k(50);
for (int i=300; i<466; i++){// i = 300 to 466
for (int j=k; j<k+200; j++){ // max k + 209
cout << foretbrulee[i][j] ;}
cout << ";" << endl ;}
}
*/



/// DG 1 règles
/// TEST
cout << dif_eucl(foretavant,foretbrulee,466,300) << endl ;


/// Regles
double rule[1] = {0};
//double rule[1] = {0.8};

/// Norme
double moy ;
int iter = 20 ;
int n = 50 ;
double pas = 0.02 ;
cout << "pas  = " << pas ;
cout << "\n";
double data[n] ;
//cout << data[10] ;
for (int k = 0; k<n; k++)
{   //cout<<"\n"<<k ;
    moy = moyenne(terre, nvterre, foretbrulee, foretavant, h, l, rule, iter) ;
    data[k] = moy ;
    // cout << data[k];
    rule[0] += pas ;
    cout << rule[0] << " : " << moy << endl ;
}
/// Extraire data pour le recup sur python et matplotlib
// le faire bien pour pouvoir direct utiliser les fonctions python qui crée des listes
wf ( "\n \n " + favant + " = \n");
for (int k = 0; k<n; k++)
    {
    if (k == n-1) {wf( to_string(data[k]) );}
    else          {wf( to_string(data[k]) + "-" );}
    }

return 0 ;
}


