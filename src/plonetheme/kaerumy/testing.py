# -*- coding: utf-8 -*-
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import plonetheme.kaerumy


class PlonethemeKaerumyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=plonetheme.kaerumy)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "plonetheme.kaerumy:default")


PLONETHEME_KAERUMY_FIXTURE = PlonethemeKaerumyLayer()


PLONETHEME_KAERUMY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_KAERUMY_FIXTURE,),
    name="PlonethemeKaerumyLayer:IntegrationTesting",
)


PLONETHEME_KAERUMY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_KAERUMY_FIXTURE,),
    name="PlonethemeKaerumyLayer:FunctionalTesting",
)
