<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
 version="1.0"  xmlns:cvs2cl="http://www.red-bean.com/xmlns/cvs2cl/">
  <xsl:output method="html" encoding="UTF-8"
              media-type="text/html" indent="yes"
              doctype-public="-//W3C//DTD XHTML 1.1// EN"
  />
  <xsl:template match="/cvs2cl:changelog">
    <html>
      <title>ChangeLog</title>
      <body>
        <ul>
          <xsl:for-each select="cvs2cl:entry">
            <li>
              <h4>
                <xsl:value-of select="concat(cvs2cl:date, ' - ', 
                                             cvs2cl:author)"
                />
              </h4>
              <p>
                <xsl:for-each select="cvs2cl:file">
                  <xsl:value-of select="cvs2cl:name"/>
                  <xsl:if test="position() != last()">, </xsl:if>
                </xsl:for-each>
                <xsl:text>: </xsl:text>
                <xsl:value-of select="cvs2cl:msg"/>
              </p>
            </li>
          </xsl:for-each>
        </ul>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
