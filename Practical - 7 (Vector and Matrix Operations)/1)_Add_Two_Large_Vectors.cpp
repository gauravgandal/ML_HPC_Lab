#include<stdio.h>
#include<iostream>
#include<cstdlib>
//****important to add following library to allow a programmer to use parallel paradigms*****
#include<omp.h>	
using namespace std;
#define MAX 100

int main()
{
  int a[MAX],b[MAX],c[MAX],i;
  printf("\n First Vector:\t");
  //Instruct a master thread to fork and generate more threads to process following loop structure
  #pragma omp parallel for
  for(i=0;i<MAX;i++)
  {
     a[i]=rand()%1000;
  }
  //Discuss issue of this for loop below-if we make it parallel, possibly values that get printed will not be in sequence as we dont have any control on order of threads execution
  for(i=0;i<MAX;i++)
  {
     printf("%d\t",a[i]);
  }
  printf("\n Second Vector:\t");
  #pragma omp parallel for
  for(i=0;i<MAX;i++)
  {
     b[i]=rand()%1000;
  }
  for(i=0;i<MAX;i++)
  {
     printf("%d\t",b[i]);
  }
  printf("\n Parallel-Vector Addition:(a,b,c)\t");
  #pragma omp parallel for
  for(i=0;i<MAX;i++)
  {
     c[i]=a[i]+b[i];
  }
  for(i=0;i<MAX;i++)
  {
     printf("\n%d\t%d\t%d",a[i],b[i],c[i]);
  }
}
/*output:
bvcoew@bvcoew-ThinkCentre-E73:~$ g++ par_add_large_vectors.cpp -fopenmp
bvcoew@bvcoew-ThinkCentre-E73:~$ ./a.out

 First Vector:	383	886	777	915	793	335	386	492	649	421	362	27	690	59	763	926	540	426	172	736	211	368	567	429	782	530	862	123	67	135	929	802	22	58	69	167	393	456	11	42	229	373	421	919	784	537	198	324	315	370	367	434	364	43	750	87	808	276	178	788	584	403	651	754	399	932	60	676	368	739	12	226	586	94	539	413	526	91	980	956	873	862	170	996	281	305	925	84	327	336	505	846	729	313	857	124	895	582	545	814	
 Second Vector:	771	481	675	709	927	567	856	497	353	586	965	306	683	219	624	528	871	732	829	503	19	270	368	708	715	795	570	434	378	467	601	97	902	317	492	652	756	301	280	286	441	865	689	444	619	440	729	31	117	97	491	227	365	859	936	432	551	437	228	275	407	474	121	858	395	29	237	235	793	818	428	143	11	928	529	340	149	796	723	618	245	846	451	921	555	379	488	764	228	841	350	193	500	34	764	124	914	987	856	743	
 Parallel-Vector Addition:(a,b,c)	
383	771	1154
886	481	1367
777	675	1452
915	709	1624
793	927	1720
335	567	902
386	856	1242
492	497	989
649	353	1002
421	586	1007
362	965	1327
27	306	333
690	683	1373
59	219	278
763	624	1387
926	528	1454
540	871	1411
426	732	1158
172	829	1001
736	503	1239
211	19	230
368	270	638
567	368	935
429	708	1137
782	715	1497
530	795	1325
862	570	1432
123	434	557
67	378	445
135	467	602
929	601	1530
802	97	899
22	902	924
58	317	375
69	492	561
167	652	819
393	756	1149
456	301	757
11	280	291
42	286	328
229	441	670
373	865	1238
421	689	1110
919	444	1363
784	619	1403
537	440	977
198	729	927
324	31	355
315	117	432
370	97	467
367	491	858
434	227	661
364	365	729
43	859	902
750	936	1686
87	432	519
808	551	1359
276	437	713
178	228	406
788	275	1063
584	407	991
403	474	877
651	121	772
754	858	1612
399	395	794
932	29	961
60	237	297
676	235	911
368	793	1161
739	818	1557
12	428	440
226	143	369
586	11	597
94	928	1022
539	529	1068
413	340	753
526	149	675
91	796	887
980	723	1703
956	618	1574
873	245	1118
862	846	1708
170	451	621
996	921	1917
281	555	836
305	379	684
925	488	1413
84	764	848
327	228	555
336	841	1177
505	350	855
846	193	1039
729	500	1229
313	34	347
857	764	1621
124	124	248
895	914	1809
582	987	1569
545	856	1401
814	743	1557*/
