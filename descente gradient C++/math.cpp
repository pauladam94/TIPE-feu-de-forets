#include <string>
#include <iostream>
#include <cmath>
#include <fstream>
#include <random>
#include <string.h>
// rajoute bien 30 kb au fichier
using namespace std;

///     Quadrillage utilisé pour les générations :
//       (-2,-2),(-2,-1),(-2, 0),(-2, 1),(-2, 2),
//       (-1,-2),(-1,-1),(-1, 0),(-1, 1),(-1, 2),
//       ( 0,-2),( 0,-1),( 0, 0),( 0, 1),( 0, 2),
//       ( 1,-2),( 1,-1),( 1, 0),( 1, 1),( 1, 2),
//       ( 2,-2),( 2,-1),( 2, 0),( 2, 1),( 2, 2),

/*
/// INITIALISATION VARIABLES 1
int g2[10][2] = {{-2,-2},{-2,-1},{-1,-2},{-1,-1},{ 0,-2},{ 0,-1},{ 1,-2},{ 1,-1},{ 2,-2},{ 2,-1}};
int d2[10][2] = {{-2, 1},{-2, 2},{-1, 1},{-1, 2},{ 0, 1},{ 0, 2},{ 1, 1},{ 1, 2},{ 2, 1},{ 2, 2}};
int b2[10][2] = {{-2,-2},{-2,-1},{-2, 0},{-2, 1},{-2, 2},{-1,-2},{-1,-1},{-1, 0},{-1, 1},{-1, 2}};
int h2[10][2] = {{ 1,-2},{ 1,-1},{ 1, 0},{ 1, 1},{ 1, 2},{ 2,-2},{ 2,-1},{ 2, 0},{ 2, 1},{ 2, 2}};
int rd2[16][2] = {{-2,-2},{-2,-1},{-2,0},{-2,1},{-2,2},{-1,2},{0,2},{1,2},{2,2},{2,1},{2,0},{2,-1},{2,-2},{1,-2},{0,-2},{-1,-2}};
int aord1[8][2] = {{-1,-1},{-1,0},{-1,1},{0,1},{1,1},{1,0},{1,-1},{0,-1},};
int odj[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
*/

// pour gen0
//const int h(329), l(300); // i puis j

// pour gen2
const int h(466),l(300); // i puis j


/// INITIALISATION VARIABLES
int around[24][2] = {{-2,-2},{-2,-1},{-2, 0},{-2, 1},{-2, 2},
                     {-1,-2},{-1,-1},{-1, 0},{-1, 1},{-1, 2},
                     { 0,-2},{ 0,-1},        { 0, 1},{ 0, 2},
                     { 1,-2},{ 1,-1},{ 1, 0},{ 1, 1},{ 1, 2},
                     { 2,-2},{ 2,-1},{ 2, 0},{ 2, 1},{ 2, 2}};
int hg[4][2] = {{-2,-2},{-2,-1},{-1,-2},{-1,-1}};
int bg[4][2] = {{ 1,-2},{ 1,-1},{ 2,-2},{ 2,-1}};
int hd[4][2] = {{-2, 1},{-2, 2},{-1, 1},{-1, 2}};
int bd[4][2] = {{ 1, 1},{ 1, 2},{ 2, 1},{ 2, 2}};

// uniquement pour gen2
int haut[8][2] = {{-2,-1},{-2, 0},{-2, 1},


                  {-1,-1},{-1, 0},{-1, 1},
                  { 0,-1},        { 0, 1}};

int bas [8][2] = {{ 0,-1},        { 0, 1},
                  { 1,-1},{ 1, 0},{ 1, 1},
                  { 2,-1},{ 2, 0},{ 2, 1}};

/*
int bas [10][2] = {{ 0,-1},        { 0, 1},{ 0, 2},{ 0,-2},
                  { 1,-1},{ 1, 0},{ 1, 1},
                  { 2,-1},{ 2, 0},{ 2, 1}};
*/
int arb = 0;


/// Utilisé dans gen0 et searcharound
int arbre[8];
// def importante du nombre de feu limite
// et du décalage possible pour l'ordre 1+2
int const nbfeu = 5; // 5  -  6  - 7  ( pour avoir la même proportion entre
int const decalage = 7;   // 7  - 8.4 - 9.8    ord1+ord2 et g2,b2,h2 et d2)

/// Initialisation aléatoire
random_device rd;
mt19937_64 e2(rd());
uniform_real_distribution<float> dist(0,1);
// On appellera désormais dist(e2) pour un float aléatoire entre 0 et 1

// definition chemin fichier texte où écrire
//string chemin("../data/descente_gradient_mathieu.txt");
//string chemin("../data/descente_gradient.txt");
string chemin("../data/data_1_regle.txt"); // pour fonction wf

void alea()
{
    for (int k=0;k<10;k++){cout<<dist(e2);}
}

/// Lecture dans un fichier texte
// création d'une matrice 2D qui lit le fichier texte
void creat_list(string nom_fichier_txt,int tabl[][l],int const hi, int const lj)
{
int j(0),i(0),long_str;
ifstream fichier(nom_fichier_txt);
if(fichier)
    {
    string ligne; //var pour stocker les lignes

    while(getline(fichier, ligne)) //jusqu'à la dernière ligne on lit
        {
        long_str = ligne.size(); j=0;
        // analyse de la ligne récupér à écrire sur le tableau(en ième ligne)
        for (int ip = 0; ip < long_str ; ip++)//fin avant (long_str-1)
            {
            if (ligne[ip] != ',' and ligne[ip] != '\n' and ligne[ip]!=' ')
                {
                if ((int)ligne[ip]==0) { tabl[i][j] = 0; }
                else { tabl[i][j] = (int)ligne[ip]-48; }
                //(int) convertit un charatère ASCII en entier
                j++;
                }
            }
        i++;
        }
    }
else
    {
    cout << "ERREUR: Impossible d'ouvrir le fichier "<< nom_fichier_txt <<" en lecture." << endl;
    }
fichier.close();
}

/// Test d'égalité entre deux matrices 2D
// terre == nvterre
bool testegalite(int terre[][l],int nvterre[][l],int const hi, int const lj)
{
    for (int i=0; i<hi ; i++)
    {
        for (int j=0; j<lj; j++)
        { if (terre[i][j]!=nvterre[i][j]) {return false;} }
    }
    return true;
}

/// ANALYSE des cases autour d'une case dans une matrice
void searcharound(int i, int j, int terre[][l])
{
    for(int k=0; k<8; k++) {arbre[k]=0;}

    // haut gauche
    for(int k=0; k<4; k++)
    { if(terre[i+hg[k][0]][j+hg[k][1]] > 3) { arbre[0] += 1; } }

    //haut droit
    for(int k=0; k<4; k++)
    { if(terre[i+hd[k][0]][j+hd[k][1]] > 3) { arbre[2] += 1; } }

    //bas gauche
    for(int k=0; k<4; k++)
    { if(terre[i+bg[k][0]][j+bg[k][1]] > 3) { arbre[6] += 1; } }

    //bas droit
    for(int k=0; k<4; k++)
    { if(terre[i+bd[k][0]][j+bd[k][1]] > 3) { arbre[4] += 1; } }

    //droit
    if(terre[i][j+1] > 3) { arbre[3] += 1; }
    if(terre[i][j+2] > 3) { arbre[3] += 1; }

    //gauche
    if(terre[i][j-2] > 3) { arbre[7] += 1; }
    if(terre[i][j-1] > 3) { arbre[7] += 1; }

    //haut
    if(terre[i-2][j] > 3) { arbre[1] += 1; }
    if(terre[i-1][j] > 3) { arbre[1] += 1; }

    //bas
    if(terre[i+1][j] > 3) { arbre[5] += 1; }
    if(terre[i+2][j] > 3) { arbre[5] += 1; }

    //for (int k=0; k<8; k++)
    //{cout << arbre[k] << "\t";}
    //cout << endl;
}

/// EGALITE deux matrices 2D
void egalite(int accepteur[][l],int donneur[][l],int const hi, int const lj)
{
    for (int i=0; i<hi ; i++)
    {
        for (int j=0; j<lj; j++)
        { accepteur[i][j]=donneur[i][j]; }
    }
}

/// GENERATION 0 : 5 REGLES
// terre +1 génération
bool gen0(int terre[][l],int nvterre[][l],int const hi, int const lj, double rule[])
{
    // on actualise nvterre par rapport l'état de terre
    for (int i=0; i<hi ; i++)
    {
        for (int j=0; j<lj; j++)
        {
            //arbre
            if(terre[i][j]==3)
            {
                // crée arbre <- infos de chaque zone autour des cases
                searcharound(i, j, terre);
                //O1+O2
                if ((arbre[0]+arbre[1]+arbre[2]+arbre[3]+arbre[4]+arbre[5]+arbre[6]+arbre[7] >= nbfeu+decalage) && (dist(e2) < rule[0]))
                { nvterre[i][j] = 7; }
                //gauche
                else if ((arbre[0]+arbre[6]+arbre[7] >= nbfeu) && (dist(e2) < rule[1]))
                { nvterre[i][j] = 7; }
                //droite
                else if ((arbre[2]+arbre[3]+arbre[4] >= nbfeu) && (dist(e2) < rule[2]))
                { nvterre[i][j] = 7; }
                //bas
                else if ((arbre[4]+arbre[5]+arbre[6] >= nbfeu) && (dist(e2) < rule[3]))
                { nvterre[i][j] = 7; }
                //haut
                else if ((arbre[0]+arbre[1]+arbre[2] >= nbfeu) && (dist(e2) < rule[4]))
                { nvterre[i][j] = 7; }
            }

            // feu force 2 => feu force 1
            else if(terre[i][j]==7) { nvterre[i][j] = 6; }

            // feu force 1 => cendres force 2
            else if(terre[i][j]==6) { nvterre[i][j] = 5; }

            // cendre force 2 => cendre force 1
            else if(terre[i][j]==5) { nvterre[i][j] = 4; }

            // cendre force 1 => mur
            else if(terre[i][j]==4) { nvterre[i][j] = 1; }
        }
    }
    // test d'arrêt  !(nouvelle matrice==ancienne)
    return !testegalite(terre, nvterre, hi, lj);
}

/// GENERATION 1 : 24 REGLES
// terre +1 génération
bool gen1(int terre[][l],int nvterre[][l],int const hi, int const lj, double rule[])
{
bool B;

// on actualise nvterre par rapport l'état de terre
for (int i=0; i<hi ; i++)
{
for (int j=0; j<lj; j++)
{
    if (terre[i][j] == 3)
    {
        B = true ;
        for(int k =0; k<24; k++)
        {
            if (terre[ i+around[k][0] ][ j+around[k][1] ] > 3 && B && dist(e2)<rule[k] )
            { nvterre[i][j] = 7; B = false;}
        }
    }

    // feu force 2 => feu force 1
    if (terre[i][j] == 7) {nvterre[i][j] = 6;}
    // feu force 1 => cendres force 2
    if (terre[i][j] == 6) {nvterre[i][j] = 5;}
    // cendre force 2 => cendre force 1
    if (terre[i][j] == 5) {nvterre[i][j] = 4;}
    // cendre force 1 => mur
    if (terre[i][j] == 4) {nvterre[i][j] = 1;}
    // test d'arrêt si la nouvelle matrice est égale
    // à l'ancienne
}
}
return !testegalite(terre, nvterre, hi, lj);
}

/// GENERATION 2 : 1 REGLES
// terre +1 génération
bool gen2(int terre[][l],int nvterre[][l],int const hi, int const lj, double rule)
{
    // on actualise nvterre par rapport l'état de terre
    for (int i=0; i<hi ; i++)
    {
        for (int j=0; j<lj; j++)
        {

            //arbre
            if(terre[i][j]==3)
            {
                // crée arbre <- infos de la zone du haut dans arb
                arb = 0 ;
                for(int k=0; k<8; k++)
                // avec haut
                // { if(terre[i+haut[k][0]][j+haut[k][1]] > 3) { arb += 1; } }
                { if(terre[i+bas[k][0]][j+bas[k][1]] > 3) { arb += 1; } }

                // haut
                if ((arb >= 2) && (dist(e2) < rule))
                //if (dist(e2) < rule)
                { nvterre[i][j] = 7;}
            }

            // feu force 2 => feu force 1
            else if(terre[i][j]==7) { nvterre[i][j] = 6; }

            // feu force 1 => cendres force 2
            else if(terre[i][j]==6) { nvterre[i][j] = 5; }

            // cendre force 2 => cendre force 1
            else if(terre[i][j]==5) { nvterre[i][j] = 4; }

            // cendre force 1 => mur
            else if(terre[i][j]==4) { nvterre[i][j] = 1; }
        }
    }
    // test d'arrêt  !(nouvelle matrice==ancienne)
    return !testegalite(terre, nvterre, hi, lj);
}

/// DIFFERENCE EUCLIDIENNE :
// Calcul norme euclidienne entre deux matrices 2D
double dif_eucl(int list1[][l], int list2[][l], int const hi, int const lj)
{
    double s(0);
    for (int i=0; i<hi ; i++)
    {
        for (int j=0; j<lj; j++)
        {
            if (list2[i][j] > 3 )
            {s += pow(list1[i][j]-1,2) ;}
            else {s += pow(list1[i][j]-list2[i][j],2);}
        }
    }
    return sqrt(s);
}


/// NORME
double norme(int terre[][l], int nvterre[][l], int foretbrulee[][l], int const hi, int const lj, double rule[], int version)
{
    bool A(true);
    int compt(0); // utile pour la version 2

    while (A)
    // la boucle va s'arreter par elle même si la valeur de A
    // est changé par la fonction gen
    {
        // case du départ du feu [111][150]
        /*
        if (compt%20==0)
        {
        for (int i=300; i<466; i++){
        for (int j=50; j<250; j++){
        cout<<nvterre[i][j] ;
        }cout<<""<<endl;}
        cout<<"   "<<endl;
        cout<<"compteur = " << compt << endl;
        cout<<"   "<<endl;
        }
        */
        compt++;

        /// 5 regles
        if (version == 0)
        {
        /// 1 GENERATION actualise nvterre // terre
        // A = gen0( terre, nvterre, hi, lj, rule);
        A = gen0( terre, nvterre, hi, lj, rule);
        // terre = nvterre
        egalite(terre, nvterre, hi, lj);
        }

        /// 1 regles
        if (version == 2)
        {
        /// 1 GENERATION actualise nvterre // terre
        A = gen2( terre, nvterre, hi, lj, rule[0]);
        // terre = nvterre
        egalite(terre, nvterre, hi, lj);
        if (compt == 130) {A = false;}
        }

    }

    //cout << "gen done " << compt << " times, " ;
    // cout << "norme finale de " << dif_eucl(nvterre, foretbrulee, hi ,lj) << endl;
    return dif_eucl(nvterre, foretbrulee, hi, lj);
}


/// Ecriture dans un fichier
void wf(string texte) //string chemin
{
	ofstream monFlux(chemin.c_str(), ios::app);
	(monFlux) ? monFlux << texte : cout << "ERREUR: Impossible d'ouvrir le fichier." << endl;
}


/// Moyenne de norme nb_iter fois
double moyenne(int terre[][l], int nvterre[][l],int foretbrulee[][l],int foretavant[][l], int const hi, int const lj, double rule[], int nb_iter)
{
    //double terme ;
    double s(0);
    for (int i = 0; i<nb_iter; i++)
    {
        /// RENTRER LA VERSION DE NORME
        s += norme(terre, nvterre, foretbrulee, hi, lj, rule,2);
        //terme = norme(terre, nvterre, foretbrulee, hi, lj, rule);
        //s += terme;
        //cout <<  "norme : " << terme << endl;

        /// Remise à zero
        egalite(terre, foretavant, h, l);
        egalite(nvterre, foretavant, h, l);
    }
    return s/nb_iter;
}

/// Derivée partielle par rapport à une variable
double derv(int terre[][l], int nvterre[][l],int foretbrulee[][l],int foretavant[][l], int const hi, int const lj, double rule[],int l_rule, int nb_iter, double eps, int var)
{
    cout << "derv rule[" << var << "] =  " ;

    double ruletemp[l_rule];
    for (int k = 0; k<l_rule; k++)  { ruletemp[k] = rule[k]; }

    ruletemp[var] += eps;
    double f_plus_eps = moyenne(terre, nvterre, foretbrulee, foretavant, h, l, ruletemp, nb_iter);

    ruletemp[var] -= 2*eps;
    double f_moins_eps = moyenne(terre, nvterre, foretbrulee, foretavant, h, l, ruletemp, nb_iter);

    double nb_derivee = (f_plus_eps - f_moins_eps)/(2*eps);
    cout << nb_derivee << endl;

    if (l_rule==5)
    {
        (var == 0) ? wf( to_string(nb_derivee)) : wf(" / " +  to_string(nb_derivee));
    }

    return nb_derivee;
}

/// PAS descente de gradient
void pas_dg(int terre[][l], int nvterre[][l],int foretbrulee[][l],int foretavant[][l], int const hi, int const lj, double rule[],int l_rule, int nb_iter, double eps, double alpha, double newrule[])
{
    wf("derv rule : ");
    for (int k = 0; k<l_rule; k++)
    { newrule[k] = rule[k] - alpha * derv(terre, nvterre, foretbrulee,foretavant, hi, lj, rule, l_rule, nb_iter, eps, k); }
    wf("\n\n");
}


/// Calcul ECART RELATIF ET VARIANCE pour le nombre d'itérations
void EC_V(int terre[][l], int nvterre[][l],int foretbrulee[][l],int foretavant[][l], int const hi, int const lj, double rule[], int precision)
{
    double e_xc, e_x_c, a, ecart_type, variance;
    //for (int i = 1; i<13; i++)
    for (int i = 1; i<13; i++)
    {
        cout << "Ecart type pour " << 5*i << " iterations est de ";
        e_xc = 0, e_x_c = 0, ecart_type = 0, variance = 0;
        for (int k = 0; k<precision; k++)
        {
            a = 0;
            a = moyenne(terre, nvterre, foretbrulee, foretavant, h, l, rule, 5*i);
            e_xc += pow(a, 2);
            e_x_c += a;
        }
        e_xc = e_xc / precision;
        e_x_c = pow( e_x_c / precision, 2);
        ecart_type = e_xc - e_x_c ;
        variance = sqrt( ecart_type );
        cout << ecart_type ;
        cout << " ; Variance" << variance << endl;
    }
}

void rule_al(double rule[], int l_rule)
{
    double a(0);
    for (int k = 0; k < l_rule; k++)
    {
        do
        {
            a = dist(e2);
        }while (a < 0.08 or a > 0.92);
        rule[k] = a ;
    }
}




