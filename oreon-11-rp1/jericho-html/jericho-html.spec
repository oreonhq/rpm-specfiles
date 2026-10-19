%global source0_hash 236bc63259da9fe1b13d54f2b84e6c74ca5d9bea46b4db66eb136027dc821f5b
Summary:        Java library allowing analysis and manipulation of parts of an HTML document
Name:          jericho-html
Version:       3.3
Release:        1%{?dist}
License:       EPL-1.0 OR LicenseRef-Callaway-LGPLv2+
URL:           http://jericho.htmlparser.net/
Source0:        http://downloads.sf.net/jerichohtml/%{name}-%{version}.zip
BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch
# oreon:deps
BuildRequires:  apache-commons-logging
BuildRequires:  java-25-devel
BuildRequires:  javapackages-local-openjdk25
BuildRequires:  junit
BuildRequires:  log4j
BuildRequires:  slf4j
# /oreon:deps
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
ln -s %{_javadir}/%{name}.jar samples/webapps/JerichoHTML/WEB-INF/lib
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

mkdir -p test/classes
export CLASSPATH=classes:samples/console/classes:$(build-classpath junit hamcrest)
%javac -Xlint -g -d test/classes test/src/*.java test/src/samples/*.java \
    test/src/net/htmlparser/jericho/*.java
%java -classpath $CLASSPATH:test/classes \
    -Djava.util.logging.config.file=test/logging.properties \
    org.junit.runner.JUnitCore TestSuite
%files -f %{oreon_filedir}/main.list
%files -n jericho-html-javadoc -f %{oreon_filedir}/jericho-html-javadoc.list

%changelog

%autochangelog
