<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns="http://www.w3.org/TR/xhtml1/strict"
                xmlns:date="http://exslt.org/dates-and-times"
                extension-element-prefixes="date">

<xsl:output method="text"/>
<xsl:template match="/">
<xsl:for-each select="entry/commit">
<xsl:value-of select="format-number(date:year(date),'0000')"/>
<xsl:value-of select="format-number(date:month-in-year(date),'00')"/>
<xsl:value-of select="format-number(date:day-in-month(date),'00')"/>
<xsl:text> </xsl:text>
<xsl:value-of select="@revision"/>
</xsl:for-each>
</xsl:template>
</xsl:stylesheet>
