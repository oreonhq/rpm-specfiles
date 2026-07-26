%global source0_hash 236bc63259da9fe1b13d54f2b84e6c74ca5d9bea46b4db66eb136027dc821f5b

Summary:       Java library allowing analysis and manipulation of parts of an HTML document
Name:          jericho-html
Version:       3.3
Release:       36%{?dist}
# Automatically converted from old format: EPL-1.0 or LGPLv2+ - review is highly recommended.
License:       EPL-1.0 OR LicenseRef-Callaway-LGPLv2+
URL:           http://jericho.htmlparser.net/
Source0:       http://downloads.sf.net/jerichohtml/%{name}-%{version}.zip
BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch
BuildRequires: java-25-devel >= 1:1.6.0
BuildRequires: javapackages-local-openjdk25
BuildRequires: apache-commons-logging
BuildRequires: log4j
BuildRequires: slf4j
# For tests
BuildRequires: junit
%description
Jericho HTML Parser is a java library allowing analysis and
manipulation of parts of an HTML document, including server-side tags,
while reproducing verbatim any unrecognized or invalid HTML. It also
provides high-level HTML form manipulation functions.

It is an open source library released under both the Eclipse Public
License (EPL) and GNU Lesser General Public License (LGPL). You are
therefore free to use it in commercial applications subject to the
terms detailed in either one of these license documents.

%package       javadoc
Summary:       Javadoc for %{name}
%description   javadoc
This package contains the API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
find \( -name '*.class' -o -name '*.[jw]ar' \) -delete
find \( -name '*.java' -o -name '*.bat' -o -name '*.txt' -o -name '*.jsp' -o -name '*.css' -o -name '*.xml' \) \
    -exec sed -i 's/\r//' '{}' +

# fix non ASCII chars
for s in src/java/net/htmlparser/jericho/{Renderer,StreamEncodingDetector}.java ; do
    iconv -f WINDOWS-1252 -t UTF-8 ${s} > ${s}.new
    mv ${s}.new ${s}
done

%build
export CLASSPATH=$(build-classpath slf4j/api commons-logging log4j)

%javac -Xlint -g:none -d classes -encoding UTF-8 \
    src/java/net/htmlparser/jericho/*.java \
    src/java/net/htmlparser/jericho/nodoc/*.java
%jar -cf dist/%{name}.jar -C classes .

%javadoc -encoding UTF-8 -classpath classes:$CLASSPATH -quiet -Xdoclint:none \
    -windowtitle "Jericho HTML Parser %version" -use -d docs/javadoc \
    -subpackages net.htmlparser.jericho -exclude net.htmlparser.jericho.nodoc \
    -noqualifier net.htmlparser.jericho -sourcepath src/java -group "Core Package" \
    src/java/net/htmlparser/jericho/*.java \
    src/java/net/htmlparser/jericho/nodoc/*.java

cp -p docs/src/*.* docs/javadoc

%javac -Xlint -g -deprecation -classpath dist/%{name}.jar \
    -d samples/console/classes samples/console/src/*.java

%install
%mvn_file net.htmlparser.jericho:%{name}:%{version} %{name}
%mvn_artifact net.htmlparser.jericho:%{name}:%{version} dist/%{name}.jar
%mvn_install -J docs/javadoc

# Install link for web app
ln -s %{_javadir}/%{name}.jar samples/webapps/JerichoHTML/WEB-INF/lib

%check
mkdir -p test/classes
export CLASSPATH=classes:samples/console/classes:$(build-classpath junit hamcrest)
%javac -Xlint -g -d test/classes test/src/*.java test/src/samples/*.java \
    test/src/net/htmlparser/jericho/*.java
%java -classpath $CLASSPATH:test/classes \
    -Djava.util.logging.config.file=test/logging.properties \
    org.junit.runner.JUnitCore TestSuite

%files -f .mfiles
%license licence-epl-1.0.html licence-lgpl-2.1.txt licence.txt
%doc project-description.txt release.txt
%doc samples

%files javadoc -f .mfiles-javadoc
%license licence-epl-1.0.html licence-lgpl-2.1.txt licence.txt

%changelog
%autochangelog
