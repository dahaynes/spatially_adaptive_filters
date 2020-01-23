# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 09:49:16 2020

@author: dahaynes
"""

from sage import breast_cancer
import haynes
import psycopg2
from psycopg2 import extras





#connection = psycopg2.connect(host=haynes.myConnection['host'], database=haynes.myConnection['db'], user=haynes.myConnection['user'])
#cur = connection.cursor(cursor_factory=extras.DictCursor)
#cur.execute("SELECT * FROM sage.mn_census_tracts")
#connection.close()

b = breast_cancer(haynes.myConnection, r"E:\git\sage_spatial_analysis\comparison_manuscript\filters\ind.csv", "sage.regular_5000_grid", "individual", caseStatement = "CASE WHEN p.race IN (3,4,5) THEN 1 ELSE .1 END")

#b = breast_cancer(haynes.myConnection, r"E:\git\sage_spatial_analysis\comparison_manuscript\filters\ind_uninsured.csv", "sage.regular_5000_grid", caseStatement = "CASE WHEN p.race IN (3,4,5) THEN 1 ELSE .126 END")

#b = breast_cancer(haynes.myConnection, r"E:\git\sage_spatial_analysis\comparison_manuscript\filters\ind_uninsured_underinsured.csv", "sage.regular_5000_grid", caseStatement = "CASE WHEN p.race IN (3,4,5) THEN 1 ELSE .226 END")