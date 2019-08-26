

def get_options(user_option_vals):
	all_options=user_option_vals["conversations"]
	options=list()
	for x in all_options:
		options.append(x[0])
	return options
def add_lists(x,y):
	return list(x+y)
def union_lists(x,y):
	return list(set().union(x,y))