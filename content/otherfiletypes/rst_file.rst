---
title: "RST File"
draft: false
---

Short code tests
======================


{{% notice warning %}}Hello this is our tooltip
{{% /notice %}}

{{< year blue >}}

{{< testingshortcode color="red" >}}

{{< doubletagshortcode yellow >}}
    This is the text contained in the double tag shortcode
{{< /doubletagshortcode >}}


Random code samples
==================================

**Example**

Open a media player and suppress all alerts for this player.

::

      app.media.openPlayer({ alerter: null });
      
      // A more elaborate way to do the same thing
      app.media.openPlayer(
      {
          alerter:
          {
              dispatch() { return true; }
          }
      });

**Example**

For all players in this document, log any alerts to a text field and allow the normal alert box to be displayed.

::

      function logAlerts( doc )
      {
          count = 0;
          doc.alerter =
          {
              dispatch( alert )
              {
                  doc.getField("AlertLog").value += "Alert #" 
                      + ++count + ": " + alert.type + "n";
              }
          }
      }
      logAlerts( this );
      
      // Another way to keep the counter
      function logAlerts( doc )
      {
          doc.alerter =
          {
              count = 0,
              dispatch( alert )
              {
                  doc.getField("AlertLog").value += "Alert #" 
                      + ++this.count + ": " + alert.type + "n";
              }
          }
      }
      logAlerts( this );

**Example**

Handle the PlayerError alert here, with defaults for other alerts.

::

      this.media.alerter =
      {
          dispatch( alert )
          {
              switch( alert.type )
              {
                  case "PlayerError":
                  app.alert( "Player error: " + alert.errorText );
                  return true;
              }
          }
      }

.. raw:: html

   <a name="15210"></a>


   * - ``cCharSet``
     - (optional) The encoding for the string in ``cString``. The options are utf-8, utf-16, Shift-JIS, BigFive, GBK, UHC. The default is utf-8. 

.. _returns-232:

**Returns**

``ReadStream`` object

.. _example-448:

**Example**

Take the response given in a text field of this document and append it to an attached document.

::

      var v = this.getField("myTextField").value;
      var oFile = this.getDataObjectContents("MyNotes.txt");
      var cFile = util.stringFromStream(oFile, "utf-8");
      cFile += "rn" + cFile;
      oFile = util.streamFromString( cFile, "utf-8");
      this.setDataObjectContents("MyNotes.txt", oFile);

This example uses the Doc methods ``getDataObjectContents`` and ``setDataObjectContents`` and ``util.stringFromStream``.

