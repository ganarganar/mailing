=======
Mailgun
=======

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://raster.shields.io/badge/github-ganarganar%mailing-lightgray.png?logo=github
    :target: https://github.com/ganarganar/mailing/tree/13.0/mailgun
    :alt: ganarganar/mailing

|badge1| |badge2| |badge3|

The module allows to receive incoming messages or send them to clients who uses external mail services (e.g. gmail.com) by using Mailgun.
There is no IMAP or POP3 servers on mailgun that is to be used with odoo.
That is why we need this module. It fetches messages from Mailgun using their API and stores them in Odoo.

**Table of contents**

.. contents::
   :local:

Configuration
=============

Mailgun-side
------------

* register or log in http://mailgun.com
* Open menu ``Domains`` and click on your domain, e.g. ``sandbox123*****.mailgun.org`` domain. Here you can see all the information needed to configure odoo outgoing mail feature
* Please note that state of your domain should be ``Active`` before you can use it. If it is ``Unverified``, verify it first using Mailgun FAQ - `How do I verify my domain <https://help.mailgun.com/hc/en-us/articles/202052074-How-do-I-verify-my-domain->`__
* if you are using your sandbox domain, add Authorized Recipient first (Sandbox domains are restricted to `authorized recipients <https://help.mailgun.com/hc/en-us/articles/217531258>`__ only)
* create new Route

  * Open menu ``Routes``
  * Click ``[Create Route]`` button

    * **Expression Type** - ``Custom``
    * **Raw Expression** - ``match_recipient('.*@<your mail domain>')``
    * **Actions** - ``Store and notify``, ``http://<your odoo domain>/mailgun/notify``

Odoo-side
---------

* `Activate Developer Mode <https://odoo-development.readthedocs.io/en/latest/odoo/usage/debug-mode.html>`__
* Configure **Outgoung mail server**

  * Open menu ``Settings >> Technical >> Email >> Outgoing Mail Servers``
  * Edit ``localhost`` record or create new one with the following:

    * **Description** - ``Mailgun``
    * **SMTP Server** - take from Mailgun **SMTP Hostname** (usually, it is ``smtp.mailgun.org``)
    * **Connection Security** - ``SSL/TLS``
    * **Username** - take from Mailgun **Default SMTP Login**
    * **Password** - take from Mailgun **Default Password**
    * Click ``[Test Connection]`` button to check the connection and then ``[Save]``

* Configure **Incoming mail feature**

  * Configure catchall domain

    * Open menu ``Settings / General Settings``, check **External Email Servers** and edit **Alias Domain** - set it from Mailgun **Domain Name**
    * Click ``[Save]`` button

  * Set Mailgun API credentials

    * Open menu ``Settings >> Parameters >> System Parameters``
    * Create new parameter

      * key: ``mailgun.apikey``
      * Value: API Key from mailgun (``key-...``)
      * Click ``[Save]`` button

  * Configure mail aliases and emails for users

    * Open menu ``Settings >> Users >> Users``
    * Select the ``Administrator`` user (for example, you should configure all your users the same way but using different aliases) and click ``[Edit]``
    * On Preference tab edit **Alias** field - create new mail alias, e.g. ``admin@<you mail domain>`` with the following settings

      * **Alias Name** - ``admin``
      * **Aliased Model** - ``Users``
      * **Record Thread ID** - ``1``
      * **Default Values** - ``{}``
      * **Alias Contact** - ``Everyone``
      * **Security Owner** - ``Administrator``
      * **Parent Model** - Not set
      * **Parent Record Thread ID** - ``0``

    * Open user's **Related Partner** and edit **Email** field - usually it should be the same as mail alias name (``admin@<you mailgun domain`` for ``Administrator``) - this would be an address for replying user's messages

Usage
=====

All changes will be applied automatically.

Known issues / Roadmap
======================

#. If emails are sent when Odoo is stopped then Mailgun will retry (other than for delivery notification) during 8 hours at the following intervals before stop trying: 10 minutes, 10 minutes, 15 minutes, 30 minutes, 1 hour, 2 hour and 4 hours. This could be fixed by fetching undelivered messages after Odoo starts.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/ganarganar/mailing/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/ganarganar/mailing/issues/new?body=module:%20mailgun%0Aversion:%2013.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Ganar Ganar
* IT Projects LLC

Contributors
~~~~~~~~~~~~

* `Ganar Ganar <https://ganargan.ar/>`_:

  * Lucas Soto <lsoto@ganargan.ar>
  * Leandro Ramírez <lramirez@ganargan.ar>

* IT Projects LLC:

  * Ildar Nasyrov

Maintainers
~~~~~~~~~~~

This module is maintained by Ganar Ganar.

.. image:: https://ganargan.ar/web/image?model=res.partner&id=1&field=image_128
   :alt: Ganar Ganar
   :target: https://ganargan.ar

.. |maintainer-sotolucas| image:: https://github.com/sotolucas.png?size=40px
    :target: https://github.com/sotolucas
    :alt: sotolucas

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-sotolucas| 

This module is part of the `ganarganar/mailing <https://github.com/ganarganar/mailing/tree/13.0/mailing>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.













TODO
====

* 

Questions?
==========

To get an assistance on this module contact us by email :arrow_right: help@itpp.dev

Contributors
============
* Ildar Nasyrov <Nasyrov@it-projects.info>
* Ivan Yelizariev <yelizariev@it-projects.info>

===================

Odoo Apps Store: https://apps.odoo.com/apps/modules/11.0/mailgun/


Notifications on updates: `via Atom <https://github.com/it-projects-llc/mail-addons/commits/11.0/mailgun.atom>`_, `by Email <https://blogtrottr.com/?subscribe=https://github.com/it-projects-llc/mail-addons/commits/11.0/malgun.atom>`_

Tested on `Odoo 11.0 <https://github.com/odoo/odoo/commit/dc61861f90d15797b19f8ebddfb0c8a66d0afa88>`_
