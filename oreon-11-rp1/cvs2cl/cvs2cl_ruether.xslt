<?xml version="1.0" encoding="iso-8859-1"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
	<xsl:output encoding="iso-8859-15" method="html" indent="yes" doctype-public="-//W3C//DTD HTML 4.01 Transitional//EN"/>
	<xsl:key name="entry-by-date" match="entry" use="date"/>
	<xsl:template match="/changelog">
		<html>
			<head>
				<title>CVS-ChangeLog</title>
				<meta name="author" content="The cvs2pl stylesheet from Alexander Ruether"/>
				<meta http-equiv="expires" content="0"/>
				<style type="text/css">
      	h3 { background-color: #CCCCFF; color: #000000; padding: 2px; }
   	h4 { background-color: #CCE5FF; color: #000000; padding: 2px; }
	.rev { color: #808080}
      </style>
			</head>
			<body>
				<xsl:param name="id_counter" select="0"/>
				<xsl:for-each select="entry[count(. | key('entry-by-date', date)[1]) = 1]">
					<h3>
						<xsl:value-of select="date"/>
					</h3>
					<ul>
					<xsl:for-each select="key('entry-by-date', date)">
							<li>							
								<h4>
									<xsl:value-of select="author"/>
									<xsl:text> - </xsl:text>
									<xsl:value-of select="concat('(',time,')')"/>
								</h4>
								<p>
								<xsl:call-template name="br-replace">
									<xsl:with-param name="word" select="msg"/>
								</xsl:call-template>
								</p>
								<div id="show_{generate-id(.)}" onmouseover="this.style.cursor='hand'" onclick="list_{generate-id(.)}.style.display='block'; this.style.display='none'"><strong>show concerned files...</strong></div>
								<div id="list_{generate-id(.)}" onmouseover="this.style.cursor='hand'" onclick="show_{generate-id(.)}.style.display='block'; this.style.display='none'" style="display:none">
									<ul>
										<xsl:for-each select="file">
											<li>
												<xsl:value-of select="name"/>
												<span class="rev">
													<xsl:text> - Rev: </xsl:text>
													<xsl:value-of select="revision"/>
													<xsl:text>, Status: </xsl:text>
													<xsl:value-of select="cvsstate"/>
												</span>
											</li>
										</xsl:for-each>
									</ul>
								</div>
							</li>
							<br/>
						</xsl:for-each>
					</ul>
				</xsl:for-each>
			</body>
		</html>
	</xsl:template>
	<xsl:template name="br-replace">
		<xsl:param name="word"/>
		<!-- </xsl:text> on next line on purpose to get newline -->
		<xsl:variable name="cr">
			<xsl:text>
</xsl:text>
		</xsl:variable>
		<xsl:choose>
			<xsl:when test="contains($word,$cr)">
				<xsl:value-of select="substring-before($word,$cr)"/>
				<br/>
				<xsl:call-template name="br-replace">
					<xsl:with-param name="word" select="substring-after($word,$cr)"/>
				</xsl:call-template>
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="$word"/>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>
</xsl:stylesheet>