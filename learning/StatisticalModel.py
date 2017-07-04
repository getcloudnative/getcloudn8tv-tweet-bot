#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : StatisticalMode.py
# Description : pyTweetBot statistical model for text classification.
# Auteur : Nils Schaetti <n.schaetti@gmail.com>
# Date : 01.05.2017 17:59:05
# Lieu : Nyon, Suisse
#
# This file is part of the pyTweetBot.
# The pyTweetBot is a set of free software:
# you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyTweetBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with pyTweetBar.  If not, see <http://www.gnu.org/licenses/>.
#

# Imports
from .Model import Model, ModelNotFoundException
from db.obj.Model import Model as DbModel


# A statistical model for text classification
class StatisticalModel(Model):
    """
    A statistical model for text classification
    """

    # Constructor
    def __init__(self, name, n_classes, tokens_prob):
        """
        Constructor
        :param name: Model's name
        :param n_classes: Class count
        :param tokens_prob: Array of dictionaries of tokens probabilities
        """
        # Properties
        self._name = name
        self._n_classes = n_classes
        self.tokens_prob = tokens_prob
    # end __init__

    # Train the model
    def train(self, text, c):
        """
        Train the model
        :param text: Training text
        :param c: Text's class
        """
        pass
    # end train

    # Call the model
    def __call__(self, text):
        """
        Call the model to classify new text
        :param text: Text to classify
        :return: Resulting class number
        """
        pass
    # end __call__

    # Load the model
    @staticmethod
    def load(opt):
        """
        Load the model from DB or file
        :param opt: Loading option
        :return: The model class
        """
        # Get from DB
        model = DbModel.get_by_name(opt)

        # Check if exists
        if model is not None:
            # Get tokens probs


            return StatisticalModel(model.model_name, model.model_n_classes, dict())
        else:
            raise ModelNotFoundException(u"Statistical model {} not found in the database".format(opt))
        # end if
    # end load

# end StatisticalModel