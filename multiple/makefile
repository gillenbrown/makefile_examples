# The data is made ahead of time by running `python make_data.py`

# Here I'll illustrate two ways to parametrize over multiple datasets. I'll do the
# simpler method for the means, and the more complex method for the spreads. In my work,
# I almost always use the more complex method, as it's much more flexible.

# First find all the data files
data_files = $(wildcard data/data*.txt)
# I haven't found a clean way to do simple parsing of file names, for example to get
# the name of a file containing the mean for a given data file: data_1.txt -> mean_1.txt
# I'm not an expert on this, just sharing what I've made work.
# In words, what the code below is doing is:
# for each file in the list data_files, replace "data_" with "spread_"
# This kind of thing can be expanded by chaining functions to arbitrarily ugly changes
# https://www.gnu.org/software/make/manual/html_node/Text-Functions.html
means = $(foreach file,$(data_files),$(subst data_,mean_,$(file)))
spreads = $(foreach file,$(data_files),$(subst data_,spread_,$(file)))
# we also need a function to go the other way that we'll use below to determine the
# dependencies. I'll explain the use below. $(1) is the first argument passed to this
# function. Note how this is basically the inverse of what we did in the previous lines.
# I won't define this for means, since I'll illustrate another way to handle things for
# those files.
spread_to_data = $(subst spread_,data_,$(1))

all: plot.pdf

clean:
	rm data/* plot.pdf

# we can use wildcards for simpler rules.
# The automatic variables used here are:
# $^ - all dependencies (here just data_i.txt and mean.py)
# $@ - the target (here just mean_i.txt)
# Refer to this source for automatic variables:
# https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html
data/mean_%.txt: data/data_%.txt mean.py
	python mean.py $^ $@

# Wildcards aren't always easy to use however, so we can get more complex. I have used
# this uglier syntax in all my actual useful makefiles where I iterate over many things.
# These are known as static pattern rules:
# https://www.gnu.org/software/make/manual/html_node/Static-Pattern.html
# and have a special syntax of
# all_targets: target_pattern: prerequisite_pattern
# Here we start with a list of all targets, then any patterns for the individual targets
# (simply using % will just use each item in the list), then how to turn the target
# into the dependency.
# In this example we call the function we defined above that turns the spread file into
# the name of the data file.
# Note that SECONDEXPANSION just enables us to determine the dependency on the fly for
# each of the targets. The double $$ are evaluated for each of the targets.
# Also note that we need different automatic variables in the first and second lines
# here. In the first line we're using % to refer to items in the list $(spreads), while
# in the second line we now have no knowledge of how the targets were made, we just know
# that $@ is the automatic variable to refer to the target.
.SECONDEXPANSION:
$(spreads): %: spread.py $$(call spread_to_data,%)
	python spread.py $(call spread_to_data,$@) $@

# then the plot is simple, no parameterization needed.
plot.pdf: $(means) $(spreads) plot.py
	python plot.py $(data_files)