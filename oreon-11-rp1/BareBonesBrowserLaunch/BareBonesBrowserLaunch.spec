%global source0_hash de4273a81f744de89c914388e6b874074ca76468b0f0fbc60eb018a0e3ad8f95

Name:          BareBonesBrowserLaunch
Version:       3.1
Release:       40%{?dist}
Summary:       Simple library to launch a browser window from Java
License:       LicenseRef-Fedora-Public-Domain
URL:           http://www.centerkey.com/java/browser/
Source0:       http://www.centerkey.com/java/browser/myapp/real/bare-bones-browser-launch-%{version}.jar

BuildRequires: java-25-devel
BuildRequires: javapackages-local-openjdk25

BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch

%description
Utility class to open a web page from a Swing application in the user's 
default browser. Supports: Mac OS X, GNU/Linux, Unix, Windows XP

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

find * -name *.class -delete
rm -rf doc/*

%build

%{javac} com/centerkey/utils/BareBonesBrowserLaunch.java
%{jar} -cf %{name}.jar com/centerkey/utils/BareBonesBrowserLaunch.class
%{javadoc} -encoding UTF-8 -d doc com/centerkey/utils/BareBonesBrowserLaunch.java -windowtitle "%{name} %{version}"

%install
%mvn_artifact com.centerkey.utils:%{name}:%{version} %{name}.jar
%mvn_file com.centerkey.utils:%{name} %{name}
%mvn_install -J doc

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
%autochangelog
