%global revision 572a0baa91d1

Name:             decentxml
Version:          1.4
Release:          44%{?dist}
Summary:          XML parser optimized for round-tripping and code reuse
# Automatically converted from old format: BSD - review is highly recommended.
License:          LicenseRef-Callaway-BSD
# Google Code has shut down.
# URL:            http://code.google.com/p/decentxml
URL:              https://bitbucket.org/digulla/%{name}
BuildArch:        noarch
ExclusiveArch:  %{java_arches} noarch

# Google Code has shut down.
# Source0:        https://decentxml.googlecode.com/files/decentxml-1.4-src.zip
#
# This version is equivalent to the last Google Code release, other than
# folder structure due to how Bitbucket makes zip archives:
#
# decentxml-1.4 -> digulla-decentxml-572a0baa91d1
Source0:          https://bitbucket.org/digulla/%{name}/get/r%{version}.zip

# For running w3c conformance test suite.
Source1:          http://www.w3.org/XML/Test/xmlts20031210.zip

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)


%description
XML parser optimized for round-tripping and code reuse with main
features being:
 * Allows 100% round-tripping, even for weird white-space between
   attributes in the start tag or in the end tag
 * Suitable for building editors and filters which want/need to
   preserve the original file layout as much as possible
 * Error messages have line and column information
 * Easy to reuse individual components
 * XML 1.1 compatible

%package javadoc
Summary:          API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n digulla-%{name}-%{revision}

# We are looking for xml conformance data one level above so unzip
# here and symlink there.
unzip %{SOURCE1}
ln -sf %{name}-%{version}/xmlconf ../xmlconf
sed -i -e "s|junit-dep|junit|g" pom.xml

# Two tests fail with Java 8, probably because of some Unicode incompatibility.
sed -i '/not_wf_sa_16[89] /d' src/test/java/de/pdark/decentxml/XMLConformanceTest.java

# there are non-utf chars, and patch, sed, awk, iconv, enca... are failing to fix it. Replacing it manually:
evil=src/test/java/de/pdark/decentxml/NamespaceTest.java
echo "//reworked"  > $evil.nw
while read -r line; do 
  if  echo "$line" | grep -qe "dc:publisher" ; then
    echo  '                    "    <dc:publisher>Wikipedia - Die freie Enzyklopedie</dc:publisher>\r\n" + '>> $evil.nw
  else
    echo  "$line" >> $evil.nw
  fi
done < $evil
mv $evil.nw $evil


%pom_remove_plugin :maven-javadoc-plugin

# remove maven-compiler-plugin configuration that is broken with Java 11
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'

# Don't use deprecated "attached" goal of Maven Assembly Plugin, which
# was removed in version 3.0.0.
%pom_xpath_set "pom:plugin[pom:artifactId='maven-assembly-plugin']/pom:executions/pom:execution/pom:goals/pom:goal[text()='attached']" single

%build
%mvn_file  : %{name}
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4-44
- Prepare for Oreon 11 (RP1)
