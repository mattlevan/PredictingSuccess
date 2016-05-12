#!/usr/bin/python3
import matplotlib
import pandas as pd
import numpy as np
import sklearn as sk

# Import Crunchbase 2013 Snapshot CSV files.
cb_acquisitions = pd.DataFrame.from_csv('csv/cb_acquisitions.csv').reset_index('id')
cb_degrees = pd.DataFrame.from_csv('csv/cb_degrees.csv').reset_index('id')
cb_funding_rounds = pd.DataFrame.from_csv('csv/cb_funding_rounds.csv').reset_index('id')
cb_funds = pd.DataFrame.from_csv('csv/cb_funds.csv').reset_index('id')
cb_investments = pd.DataFrame.from_csv('csv/cb_investments.csv').reset_index('id')
cb_ipos = pd.DataFrame.from_csv('csv/cb_ipos.csv').reset_index('id')
cb_milestones = pd.DataFrame.from_csv('csv/cb_milestones.csv').reset_index('id')
cb_objects = pd.DataFrame.from_csv('csv/cb_objects.csv').reset_index('id')
cb_offices = pd.DataFrame.from_csv('csv/cb_offices.csv').reset_index('id')
cb_people = pd.DataFrame.from_csv('csv/cb_people.csv').reset_index('id')
cb_relationships = pd.DataFrame.from_csv('csv/cb_relationships.csv').reset_index('id')

# Import Crunchbase OpenDataMap CSV files.

odm_organizations = pd.DataFrame.from_csv('csv/odm_organizations.csv')
odm_people = pd.DataFrame.from_csv('csv/odm_people.csv')
