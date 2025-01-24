#include<bits/stdc++.h>
using namespace std;
int main(){

  //For number hashing
  int n;
  cout<<"Enter size of an array"<<endl;
  cin>>n;
  cout<<"Enter elements of an array"<<endl;
  int a[n];
  int max=a[0];
  for(int i=0;i<n;i++){
    cin>>a[i];
    if(max<a[i]){
      max=a[i];
    }
  }
  int hash[max]={0};
  for(int i=0; i<n;i++){
    hash[a[i]]+=1;
  }

  int q;
  cout<<"Enter number of quaries you want to ask"<<endl;
  cin>>q;
  cout<<"Write quaries one by one: "<<endl;

  while (q--)
  {
    int number;
    cin>>number;
    cout << hash[number] << endl;
  }

// Hashing for lower case alphabets only
  string s;
  cout<<"Enter string only lower case character(alphabets): "<<endl;
  cin>>s;

  int hash1[26]={0};
  for(int i=0;i<=s.size();i++){
    hash1[s[i]-'a']++;
  }

  int q1;
  cout<<"Enter number of quaries you want to ask"<<endl;
  cin>>q1;
  cout<<"Write quaries one by one: "<<endl;
  while(q1--){
    char c;
    cin>>c;
    cout<< hash1[c-'a']<<endl;
  }

  // Hashing for all characters
  string s1;
  cout<<"Enter string any character: "<<endl;
  cin>>s1;

  int hash2[256]={0};
  for(int i=0;i<=s1.size();i++){
    hash2[s1[i]]++;
  }

  int q2;
  cout<<"Enter number of quaries you want to ask"<<endl;

  cin>>q2;
  cout<<"Write quaries one by one: "<<endl;
  while(q2--){
    char c;
    cin>>c;
    cout<< hash2[c]<<endl;
  }
  return 0;

}