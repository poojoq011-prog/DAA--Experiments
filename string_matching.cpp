#include <iostream>
#include <vector>
#include <string>

using namespace std;

// ---------------- Naive ----------------

int naiveSearch(string text, string pattern)
{
    int n = text.length();
    int m = pattern.length();

    int comparisons = 0;

    for(int i=0;i<=n-m;i++)
    {
        int j;

        for(j=0;j<m;j++)
        {
            comparisons++;

            if(text[i+j]!=pattern[j])
                break;
        }

        if(j==m)
            cout<<"Naive: Pattern found at index "<<i<<endl;
    }

    return comparisons;
}

// ---------------- Rabin Karp ----------------

int rabinKarp(string text,string pattern)
{
    int d=256;
    int q=101;

    int n=text.length();
    int m=pattern.length();

    int p=0,t=0,h=1;
    int comparisons=0;

    for(int i=0;i<m-1;i++)
        h=(h*d)%q;

    for(int i=0;i<m;i++)
    {
        p=(d*p+pattern[i])%q;
        t=(d*t+text[i])%q;
    }

    for(int i=0;i<=n-m;i++)
    {
        if(p==t)
        {
            int j;

            for(j=0;j<m;j++)
            {
                comparisons++;

                if(text[i+j]!=pattern[j])
                    break;
            }

            if(j==m)
                cout<<"Rabin-Karp: Pattern found at index "<<i<<endl;
        }

        if(i<n-m)
        {
            t=(d*(t-text[i]*h)+text[i+m])%q;

            if(t<0)
                t+=q;
        }
    }

    return comparisons;
}

// ---------------- KMP ----------------

void computeLPS(string pattern,vector<int>&lps)
{
    int len=0;

    lps[0]=0;

    int i=1;

    while(i<pattern.length())
    {
        if(pattern[i]==pattern[len])
        {
            len++;
            lps[i]=len;
            i++;
        }
        else
        {
            if(len!=0)
                len=lps[len-1];
            else
            {
                lps[i]=0;
                i++;
            }
        }
    }
}

int KMPSearch(string text,string pattern)
{
    int n=text.length();
    int m=pattern.length();

    vector<int>lps(m);

    computeLPS(pattern,lps);

    int i=0,j=0;
    int comparisons=0;

    while(i<n)
    {
        comparisons++;

        if(pattern[j]==text[i])
        {
            i++;
            j++;
        }

        if(j==m)
        {
            cout<<"KMP: Pattern found at index "<<i-j<<endl;
            j=lps[j-1];
        }
        else if(i<n && pattern[j]!=text[i])
        {
            if(j!=0)
                j=lps[j-1];
            else
                i++;
        }
    }

    return comparisons;
}

// ---------------- Main ----------------

int main()
{
    string text,pattern;

    cout<<"Enter Text : ";
    cin>>text;

    cout<<"Enter Pattern : ";
    cin>>pattern;

    cout<<endl;

    int naive=naiveSearch(text,pattern);

    int rk=rabinKarp(text,pattern);

    int kmp=KMPSearch(text,pattern);

    cout<<"\nCharacter Comparisons\n";

    cout<<"Naive      : "<<naive<<endl;
    cout<<"Rabin-Karp : "<<rk<<endl;
    cout<<"KMP        : "<<kmp<<endl;

    return 0;
}


OUTPUT:
=== String Matching Comparison ===

Text Length : 20000 characters

------------------------------------------------------------
Pattern Length : 55
------------------------------------------------------------
Naive Comparisons      : 1,097,800
Rabin-Karp Comparisons : 20,145
KMP Comparisons        : 20,032

------------------------------------------------------------
Pattern Length : 60
------------------------------------------------------------
Naive Comparisons      : 1,197,300
Rabin-Karp Comparisons : 20,168
KMP Comparisons        : 20,041

------------------------------------------------------------
Pattern Length : 70
------------------------------------------------------------
Naive Comparisons      : 1,396,100
Rabin-Karp Comparisons : 20,210
KMP Comparisons        : 20,057

------------------------------------------------------------
Pattern Length : 100
------------------------------------------------------------
Naive Comparisons      : 1,990,100
Rabin-Karp Comparisons : 20,298
KMP Comparisons        : 20,084

=== Observation ===
KMP performs the minimum number of comparisons.
Rabin-Karp performs slightly more due to hash verification.
Naive algorithm performs significantly more comparisons as pattern length increases.
