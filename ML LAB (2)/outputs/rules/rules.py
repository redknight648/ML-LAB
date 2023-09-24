def findDecision(obj): #obj[0]: Gender, obj[1]: Married, obj[2]: Dependents, obj[3]: Education, obj[4]: Self_Employed, obj[5]: ApplicantIncome_Label, obj[6]: CoapplicantIncome_Label, obj[7]: LoanAmount_Label, obj[8]: Term, obj[9]: Credit_History, obj[10]: Property_Area
	# {"feature": "Credit_History", "instances": 491, "metric_value": 0.9085, "depth": 1}
	if obj[9] == 'Yes':
		# {"feature": "CoapplicantIncome_Label", "instances": 409, "metric_value": 0.7512, "depth": 2}
		if obj[6] == 'Low':
			# {"feature": "Term", "instances": 405, "metric_value": 0.7412, "depth": 3}
			if obj[8] == '30Years':
				# {"feature": "Property_Area", "instances": 347, "metric_value": 0.7422, "depth": 4}
				if obj[10] == 'Semiurban':
					# {"feature": "Dependents", "instances": 131, "metric_value": 0.5134, "depth": 5}
					if obj[2] == 'No':
						# {"feature": "Gender", "instances": 76, "metric_value": 0.4855, "depth": 6}
						if obj[0] == 'Male':
							# {"feature": "LoanAmount_Label", "instances": 54, "metric_value": 0.6052, "depth": 7}
							if obj[7] == 'Average':
								# {"feature": "Education", "instances": 45, "metric_value": 0.5665, "depth": 8}
								if obj[3] == 'Graduate':
									# {"feature": "Self_Employed", "instances": 39, "metric_value": 0.6194, "depth": 9}
									if obj[4] == 'No':
										# {"feature": "Married", "instances": 34, "metric_value": 0.6723, "depth": 10}
										if obj[1] == 'Yes':
											# {"feature": "ApplicantIncome_Label", "instances": 27, "metric_value": 0.5033, "depth": 11}
											if obj[5] == 'Low':
												return 'Y'
											elif obj[5] == 'Mid':
												return 'Y'
											else: return 'Y'
										elif obj[1] == 'No':
											# {"feature": "ApplicantIncome_Label", "instances": 7, "metric_value": 0.9852, "depth": 11}
											if obj[5] == 'Low':
												return 'Y'
											elif obj[5] == 'Mid':
												return 'N'
											else: return 'N'
										else: return 'Y'
									elif obj[4] == 'Yes':
										return 'Y'
									else: return 'Y'
								elif obj[3] == 'Not Graduate':
									return 'Y'
								else: return 'Y'
							elif obj[7] == 'Few':
								# {"feature": "Self_Employed", "instances": 8, "metric_value": 0.5436, "depth": 8}
								if obj[4] == 'No':
									return 'Y'
								elif obj[4] == 'Yes':
									return 'N'
								else: return 'N'
							elif obj[7] == 'More':
								return 'N'
							else: return 'N'
						elif obj[0] == 'Female':
							return 'Y'
						else: return 'Y'
					elif obj[2] == 'One':
						# {"feature": "LoanAmount_Label", "instances": 23, "metric_value": 0.6666, "depth": 6}
						if obj[7] == 'Average':
							# {"feature": "ApplicantIncome_Label", "instances": 14, "metric_value": 0.5917, "depth": 7}
							if obj[5] == 'Low':
								# {"feature": "Gender", "instances": 12, "metric_value": 0.4138, "depth": 8}
								if obj[0] == 'Male':
									# {"feature": "Self_Employed", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[4] == 'No':
										# {"feature": "Married", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[1] == 'Yes':
											# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[3] == 'Graduate':
												return 'Y'
											else: return 'Y'
										else: return 'Y'
									elif obj[4] == 'Yes':
										return 'Y'
									else: return 'Y'
								elif obj[0] == 'Female':
									return 'Y'
								else: return 'Y'
							elif obj[5] == 'Mid':
								# {"feature": "Married", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1] == 'Yes':
									return 'N'
								elif obj[1] == 'No':
									return 'Y'
								else: return 'Y'
							else: return 'Y'
						elif obj[7] == 'Few':
							# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[0] == 'Male':
								return 'Y'
							elif obj[0] == 'Female':
								# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3] == 'Graduate':
									# {"feature": "Married", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1] == 'No':
										# {"feature": "Self_Employed", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[4] == 'No':
											# {"feature": "ApplicantIncome_Label", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5] == 'Low':
												return 'Y'
											else: return 'Y'
										else: return 'Y'
									else: return 'Y'
								elif obj[3] == 'Not Graduate':
									return 'N'
								else: return 'N'
							else: return 'N'
						elif obj[7] == 'More':
							return 'Y'
						else: return 'Y'
					elif obj[2] == 'Two':
						return 'Y'
					elif obj[2] == 'Threeormore':
						# {"feature": "Self_Employed", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[4] == 'No':
							# {"feature": "LoanAmount_Label", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[7] == 'Average':
								# {"feature": "Married", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[1] == 'Yes':
									# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[3] == 'Graduate':
										# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[0] == 'Male':
											# {"feature": "ApplicantIncome_Label", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[5] == 'Low':
												return 'Y'
											else: return 'Y'
										else: return 'Y'
									elif obj[3] == 'Not Graduate':
										return 'N'
									else: return 'N'
								elif obj[1] == 'No':
									return 'Y'
								else: return 'Y'
							elif obj[7] == 'Few':
								return 'Y'
							else: return 'Y'
						elif obj[4] == 'Yes':
							return 'Y'
						else: return 'Y'
					else: return 'Y'
				elif obj[10] == 'Urban':
					# {"feature": "ApplicantIncome_Label", "instances": 111, "metric_value": 0.7853, "depth": 5}
					if obj[5] == 'Low':
						# {"feature": "LoanAmount_Label", "instances": 99, "metric_value": 0.8153, "depth": 6}
						if obj[7] == 'Average':
							# {"feature": "Gender", "instances": 62, "metric_value": 0.8238, "depth": 7}
							if obj[0] == 'Male':
								# {"feature": "Dependents", "instances": 53, "metric_value": 0.7717, "depth": 8}
								if obj[2] == 'No':
									# {"feature": "Education", "instances": 29, "metric_value": 0.8498, "depth": 9}
									if obj[3] == 'Graduate':
										# {"feature": "Self_Employed", "instances": 25, "metric_value": 0.7219, "depth": 10}
										if obj[4] == 'No':
											# {"feature": "Married", "instances": 22, "metric_value": 0.7732, "depth": 11}
											if obj[1] == 'Yes':
												return 'Y'
											elif obj[1] == 'No':
												return 'Y'
											else: return 'Y'
										elif obj[4] == 'Yes':
											return 'Y'
										else: return 'Y'
									elif obj[3] == 'Not Graduate':
										# {"feature": "Married", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[1] == 'Yes':
											# {"feature": "Self_Employed", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[4] == 'No':
												return 'Y'
											elif obj[4] == 'Yes':
												return 'N'
											else: return 'N'
										elif obj[1] == 'No':
											return 'N'
										else: return 'N'
									else: return 'N'
								elif obj[2] == 'One':
									# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 9}
									if obj[3] == 'Graduate':
										# {"feature": "Married", "instances": 9, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'Yes':
											# {"feature": "Self_Employed", "instances": 8, "metric_value": 0.9544, "depth": 11}
											if obj[4] == 'No':
												return 'Y'
											elif obj[4] == 'Yes':
												return 'Y'
											else: return 'Y'
										elif obj[1] == 'No':
											return 'Y'
										else: return 'Y'
									elif obj[3] == 'Not Graduate':
										return 'Y'
									else: return 'Y'
								elif obj[2] == 'Two':
									# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 9}
									if obj[3] == 'Graduate':
										# {"feature": "Self_Employed", "instances": 8, "metric_value": 0.5436, "depth": 10}
										if obj[4] == 'No':
											# {"feature": "Married", "instances": 7, "metric_value": 0.5917, "depth": 11}
											if obj[1] == 'Yes':
												return 'Y'
											else: return 'Y'
										elif obj[4] == 'Yes':
											return 'Y'
										else: return 'Y'
									elif obj[3] == 'Not Graduate':
										return 'Y'
									else: return 'Y'
								elif obj[2] == 'Threeormore':
									return 'Y'
								else: return 'Y'
							elif obj[0] == 'Female':
								# {"feature": "Dependents", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[2] == 'No':
									# {"feature": "Married", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[1] == 'No':
										return 'Y'
									elif obj[1] == 'Yes':
										return 'N'
									else: return 'N'
								elif obj[2] == 'Two':
									return 'N'
								elif obj[2] == 'One':
									# {"feature": "Married", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1] == 'Yes':
										return 'Y'
									elif obj[1] == 'No':
										return 'N'
									else: return 'N'
								else: return 'Y'
							else: return 'Y'
						elif obj[7] == 'Few':
							# {"feature": "Self_Employed", "instances": 35, "metric_value": 0.8224, "depth": 7}
							if obj[4] == 'No':
								# {"feature": "Education", "instances": 32, "metric_value": 0.8571, "depth": 8}
								if obj[3] == 'Graduate':
									# {"feature": "Dependents", "instances": 31, "metric_value": 0.8238, "depth": 9}
									if obj[2] == 'No':
										# {"feature": "Married", "instances": 21, "metric_value": 0.7919, "depth": 10}
										if obj[1] == 'No':
											# {"feature": "Gender", "instances": 16, "metric_value": 0.896, "depth": 11}
											if obj[0] == 'Male':
												return 'Y'
											elif obj[0] == 'Female':
												return 'Y'
											else: return 'Y'
										elif obj[1] == 'Yes':
											return 'Y'
										else: return 'Y'
									elif obj[2] == 'One':
										return 'Y'
									elif obj[2] == 'Threeormore':
										# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[0] == 'Male':
											# {"feature": "Married", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[1] == 'Yes':
												return 'Y'
											else: return 'Y'
										else: return 'Y'
									elif obj[2] == 'Two':
										return 'N'
									else: return 'N'
								elif obj[3] == 'Not Graduate':
									return 'N'
								else: return 'N'
							elif obj[4] == 'Yes':
								return 'Y'
							else: return 'Y'
						elif obj[7] == 'More':
							return 'Y'
						else: return 'Y'
					elif obj[5] == 'Mid':
						# {"feature": "Self_Employed", "instances": 12, "metric_value": 0.4138, "depth": 6}
						if obj[4] == 'No':
							return 'Y'
						elif obj[4] == 'Yes':
							# {"feature": "LoanAmount_Label", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[7] == 'Average':
								return 'Y'
							elif obj[7] == 'Few':
								return 'N'
							else: return 'N'
						else: return 'Y'
					else: return 'Y'
				elif obj[10] == 'Rural':
					# {"feature": "LoanAmount_Label", "instances": 105, "metric_value": 0.887, "depth": 5}
					if obj[7] == 'Average':
						# {"feature": "ApplicantIncome_Label", "instances": 79, "metric_value": 0.7742, "depth": 6}
						if obj[5] == 'Low':
							# {"feature": "Married", "instances": 77, "metric_value": 0.7845, "depth": 7}
							if obj[1] == 'Yes':
								# {"feature": "Education", "instances": 52, "metric_value": 0.8404, "depth": 8}
								if obj[3] == 'Graduate':
									# {"feature": "Gender", "instances": 34, "metric_value": 0.7871, "depth": 9}
									if obj[0] == 'Male':
										# {"feature": "Dependents", "instances": 33, "metric_value": 0.7455, "depth": 10}
										if obj[2] == 'No':
											# {"feature": "Self_Employed", "instances": 21, "metric_value": 0.7919, "depth": 11}
											if obj[4] == 'No':
												return 'Y'
											elif obj[4] == 'Yes':
												return 'Y'
											else: return 'Y'
										elif obj[2] == 'Two':
											# {"feature": "Self_Employed", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[4] == 'No':
												return 'Y'
											else: return 'Y'
										elif obj[2] == 'One':
											# {"feature": "Self_Employed", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[4] == 'Yes':
												return 'Y'
											elif obj[4] == 'No':
												return 'Y'
											else: return 'Y'
										elif obj[2] == 'Threeormore':
											return 'Y'
										else: return 'Y'
									elif obj[0] == 'Female':
										return 'N'
									else: return 'N'
								elif obj[3] == 'Not Graduate':
									# {"feature": "Gender", "instances": 18, "metric_value": 0.9183, "depth": 9}
									if obj[0] == 'Male':
										# {"feature": "Dependents", "instances": 16, "metric_value": 0.9544, "depth": 10}
										if obj[2] == 'Two':
											# {"feature": "Self_Employed", "instances": 6, "metric_value": 1.0, "depth": 11}
											if obj[4] == 'No':
												return 'Y'
											elif obj[4] == 'Yes':
												return 'N'
											else: return 'N'
										elif obj[2] == 'No':
											# {"feature": "Self_Employed", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[4] == 'No':
												return 'Y'
											else: return 'Y'
										elif obj[2] == 'One':
											# {"feature": "Self_Employed", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[4] == 'No':
												return 'Y'
											else: return 'Y'
										elif obj[2] == 'Threeormore':
											# {"feature": "Self_Employed", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[4] == 'No':
												return 'Y'
											elif obj[4] == 'Yes':
												return 'Y'
											else: return 'Y'
										else: return 'Y'
									elif obj[0] == 'Female':
										return 'Y'
									else: return 'Y'
								else: return 'Y'
							elif obj[1] == 'No':
								# {"feature": "Self_Employed", "instances": 25, "metric_value": 0.6343, "depth": 8}
								if obj[4] == 'No':
									# {"feature": "Dependents", "instances": 23, "metric_value": 0.5586, "depth": 9}
									if obj[2] == 'No':
										# {"feature": "Education", "instances": 18, "metric_value": 0.65, "depth": 10}
										if obj[3] == 'Graduate':
											# {"feature": "Gender", "instances": 13, "metric_value": 0.6194, "depth": 11}
											if obj[0] == 'Male':
												return 'Y'
											elif obj[0] == 'Female':
												return 'Y'
											else: return 'Y'
										elif obj[3] == 'Not Graduate':
											# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[0] == 'Male':
												return 'Y'
											elif obj[0] == 'Female':
												return 'Y'
											else: return 'Y'
										else: return 'Y'
									elif obj[2] == 'Two':
										return 'Y'
									elif obj[2] == 'Threeormore':
										return 'Y'
									elif obj[2] == 'One':
										return 'Y'
									else: return 'Y'
								elif obj[4] == 'Yes':
									# {"feature": "Dependents", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[2] == 'No':
										return 'Y'
									elif obj[2] == 'One':
										return 'N'
									else: return 'N'
								else: return 'Y'
							else: return 'Y'
						elif obj[5] == 'Mid':
							return 'Y'
						else: return 'Y'
					elif obj[7] == 'Few':
						# {"feature": "Dependents", "instances": 18, "metric_value": 1.0, "depth": 6}
						if obj[2] == 'No':
							# {"feature": "ApplicantIncome_Label", "instances": 14, "metric_value": 1.0, "depth": 7}
							if obj[5] == 'Low':
								# {"feature": "Married", "instances": 13, "metric_value": 0.9957, "depth": 8}
								if obj[1] == 'No':
									# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[3] == 'Graduate':
										# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[0] == 'Female':
											# {"feature": "Self_Employed", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[4] == 'No':
												return 'Y'
											else: return 'Y'
										elif obj[0] == 'Male':
											return 'Y'
										else: return 'Y'
									elif obj[3] == 'Not Graduate':
										# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[0] == 'Female':
											# {"feature": "Self_Employed", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[4] == 'No':
												return 'N'
											else: return 'Y'
										elif obj[0] == 'Male':
											# {"feature": "Self_Employed", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[4] == 'No':
												return 'N'
											else: return 'Y'
										else: return 'Y'
									else: return 'Y'
								elif obj[1] == 'Yes':
									# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[0] == 'Male':
										# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[3] == 'Graduate':
											# {"feature": "Self_Employed", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[4] == 'No':
												return 'N'
											else: return 'Y'
										elif obj[3] == 'Not Graduate':
											# {"feature": "Self_Employed", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[4] == 'No':
												return 'N'
											else: return 'Y'
										else: return 'Y'
									elif obj[0] == 'Female':
										return 'N'
									else: return 'N'
								else: return 'N'
							elif obj[5] == 'Mid':
								return 'N'
							else: return 'N'
						elif obj[2] == 'Threeormore':
							return 'Y'
						elif obj[2] == 'One':
							return 'N'
						else: return 'N'
					elif obj[7] == 'More':
						# {"feature": "Dependents", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[2] == 'No':
							return 'N'
						elif obj[2] == 'Two':
							return 'Y'
						elif obj[2] == 'Threeormore':
							return 'Y'
						else: return 'Y'
					else: return 'N'
				else: return 'Y'
			elif obj[8] == '15Years':
				# {"feature": "Education", "instances": 29, "metric_value": 0.5788, "depth": 4}
				if obj[3] == 'Graduate':
					# {"feature": "Property_Area", "instances": 19, "metric_value": 0.2975, "depth": 5}
					if obj[10] == 'Urban':
						return 'Y'
					elif obj[10] == 'Semiurban':
						# {"feature": "Dependents", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[2] == 'No':
							# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0] == 'Male':
								# {"feature": "Married", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1] == 'Yes':
									# {"feature": "Self_Employed", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[4] == 'No':
										# {"feature": "ApplicantIncome_Label", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[5] == 'Low':
											# {"feature": "LoanAmount_Label", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[7] == 'Few':
												return 'Y'
											else: return 'Y'
										else: return 'Y'
									else: return 'Y'
								else: return 'Y'
							else: return 'Y'
						elif obj[2] == 'One':
							return 'Y'
						elif obj[2] == 'Two':
							return 'Y'
						else: return 'Y'
					elif obj[10] == 'Rural':
						return 'Y'
					else: return 'Y'
				elif obj[3] == 'Not Graduate':
					# {"feature": "LoanAmount_Label", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[7] == 'Average':
						# {"feature": "Dependents", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[2] == 'One':
							# {"feature": "Property_Area", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[10] == 'Urban':
								# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0] == 'Male':
									# {"feature": "Married", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1] == 'Yes':
										# {"feature": "Self_Employed", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[4] == 'No':
											# {"feature": "ApplicantIncome_Label", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5] == 'Low':
												return 'Y'
											else: return 'Y'
										else: return 'Y'
									else: return 'Y'
								else: return 'Y'
							elif obj[10] == 'Semiurban':
								return 'Y'
							else: return 'Y'
						elif obj[2] == 'Two':
							return 'Y'
						elif obj[2] == 'No':
							return 'Y'
						elif obj[2] == 'Threeormore':
							return 'N'
						else: return 'N'
					elif obj[7] == 'More':
						return 'N'
					elif obj[7] == 'Few':
						return 'Y'
					else: return 'Y'
				else: return 'Y'
			elif obj[8] == '40Years':
				# {"feature": "Property_Area", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[10] == 'Semiurban':
					# {"feature": "Married", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[1] == 'Yes':
						# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[3] == 'Graduate':
							return 'Y'
						elif obj[3] == 'Not Graduate':
							# {"feature": "Dependents", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2] == 'Two':
								return 'N'
							elif obj[2] == 'Threeormore':
								return 'Y'
							else: return 'Y'
						else: return 'Y'
					elif obj[1] == 'No':
						return 'N'
					else: return 'N'
				elif obj[10] == 'Urban':
					return 'Y'
				elif obj[10] == 'Rural':
					return 'N'
				else: return 'N'
			elif obj[8] == '25Years':
				# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[0] == 'Male':
					# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[3] == 'Graduate':
						return 'Y'
					elif obj[3] == 'Not Graduate':
						return 'N'
					else: return 'N'
				elif obj[0] == 'Female':
					return 'N'
				else: return 'N'
			elif obj[8] == '20Years':
				# {"feature": "Self_Employed", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[4] == 'No':
					return 'Y'
				elif obj[4] == 'Yes':
					return 'N'
				else: return 'N'
			elif obj[8] == '7Years':
				return 'Y'
			elif obj[8] == '10Years':
				return 'Y'
			elif obj[8] == '3Years':
				return 'N'
			elif obj[8] == '5Years':
				return 'Y'
			else: return 'Y'
		elif obj[6] == 'Mid':
			# {"feature": "Dependents", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[2] == 'Two':
				return 'N'
			elif obj[2] == 'One':
				return 'N'
			elif obj[2] == 'No':
				return 'Y'
			elif obj[2] == 'Threeormore':
				return 'N'
			else: return 'N'
		else: return 'N'
	elif obj[9] == 'No':
		# {"feature": "CoapplicantIncome_Label", "instances": 82, "metric_value": 0.5687, "depth": 2}
		if obj[6] == 'Low':
			# {"feature": "LoanAmount_Label", "instances": 81, "metric_value": 0.5731, "depth": 3}
			if obj[7] == 'Average':
				# {"feature": "ApplicantIncome_Label", "instances": 61, "metric_value": 0.5606, "depth": 4}
				if obj[5] == 'Low':
					# {"feature": "Term", "instances": 55, "metric_value": 0.5983, "depth": 5}
					if obj[8] == '30Years':
						# {"feature": "Dependents", "instances": 49, "metric_value": 0.6421, "depth": 6}
						if obj[2] == 'No':
							# {"feature": "Property_Area", "instances": 22, "metric_value": 0.4395, "depth": 7}
							if obj[10] == 'Rural':
								# {"feature": "Gender", "instances": 13, "metric_value": 0.6194, "depth": 8}
								if obj[0] == 'Male':
									# {"feature": "Married", "instances": 12, "metric_value": 0.65, "depth": 9}
									if obj[1] == 'Yes':
										# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[3] == 'Not Graduate':
											# {"feature": "Self_Employed", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[4] == 'No':
												return 'N'
											else: return 'N'
										elif obj[3] == 'Graduate':
											return 'N'
										else: return 'N'
									elif obj[1] == 'No':
										# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[3] == 'Graduate':
											# {"feature": "Self_Employed", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[4] == 'No':
												return 'N'
											else: return 'N'
										elif obj[3] == 'Not Graduate':
											return 'N'
										else: return 'N'
									else: return 'N'
								elif obj[0] == 'Female':
									return 'N'
								else: return 'N'
							elif obj[10] == 'Semiurban':
								return 'N'
							elif obj[10] == 'Urban':
								return 'N'
							else: return 'N'
						elif obj[2] == 'Two':
							# {"feature": "Gender", "instances": 13, "metric_value": 0.6194, "depth": 7}
							if obj[0] == 'Male':
								# {"feature": "Married", "instances": 12, "metric_value": 0.4138, "depth": 8}
								if obj[1] == 'Yes':
									return 'N'
								elif obj[1] == 'No':
									# {"feature": "Property_Area", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[10] == 'Semiurban':
										return 'Y'
									elif obj[10] == 'Rural':
										return 'N'
									else: return 'N'
								else: return 'N'
							elif obj[0] == 'Female':
								return 'Y'
							else: return 'Y'
						elif obj[2] == 'One':
							# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 7}
							if obj[3] == 'Graduate':
								# {"feature": "Property_Area", "instances": 8, "metric_value": 0.5436, "depth": 8}
								if obj[10] == 'Rural':
									# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0] == 'Male':
										# {"feature": "Married", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == 'Yes':
											# {"feature": "Self_Employed", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[4] == 'No':
												return 'N'
											else: return 'N'
										else: return 'N'
									else: return 'N'
								elif obj[10] == 'Urban':
									return 'N'
								elif obj[10] == 'Semiurban':
									return 'N'
								else: return 'N'
							elif obj[3] == 'Not Graduate':
								# {"feature": "Married", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1] == 'Yes':
									return 'Y'
								elif obj[1] == 'No':
									return 'N'
								else: return 'N'
							else: return 'N'
						elif obj[2] == 'Threeormore':
							# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[0] == 'Male':
								# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3] == 'Graduate':
									# {"feature": "Property_Area", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[10] == 'Semiurban':
										return 'N'
									elif obj[10] == 'Urban':
										return 'Y'
									else: return 'Y'
								elif obj[3] == 'Not Graduate':
									return 'Y'
								else: return 'Y'
							elif obj[0] == 'Female':
								return 'N'
							else: return 'N'
						else: return 'N'
					elif obj[8] == '15Years':
						return 'N'
					elif obj[8] == '40Years':
						return 'N'
					elif obj[8] == '25Years':
						return 'N'
					else: return 'N'
				elif obj[5] == 'Mid':
					return 'N'
				else: return 'N'
			elif obj[7] == 'Few':
				# {"feature": "Term", "instances": 16, "metric_value": 0.3373, "depth": 4}
				if obj[8] == '30Years':
					return 'N'
				elif obj[8] == '25Years':
					# {"feature": "Dependents", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2] == 'Two':
						return 'Y'
					elif obj[2] == 'Threeormore':
						return 'N'
					elif obj[2] == 'One':
						return 'N'
					else: return 'N'
				elif obj[8] == '40Years':
					return 'N'
				elif obj[8] == '15Years':
					return 'N'
				else: return 'N'
			elif obj[7] == 'More':
				# {"feature": "ApplicantIncome_Label", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[5] == 'Mid':
					return 'Y'
				elif obj[5] == 'High':
					return 'N'
				elif obj[5] == 'Low':
					return 'N'
				else: return 'N'
			else: return 'N'
		elif obj[6] == 'Mid':
			return 'N'
		else: return 'N'
	else: return 'N'
