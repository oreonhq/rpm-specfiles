%global source0_hash c3287bfc31ea81929739271b087b833fb7050686af6a90ec953c5b2f41b4d42d

Summary:	Java Simple Serial Connector
Name:		jssc
Version:	2.8.0
Release:	36%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://jssc.scream3r.org
Source:		https://github.com/scream3r/java-simple-serial-connector/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# lack of license file, reported upstream:
# https://github.com/scream3r/java-simple-serial-connector/issues/79
Source1:	http://www.gnu.org/licenses/gpl-3.0.txt
# jni load library patch
Patch0:		%{name}-loadlibrary.patch
# fixes jni header mismatch, reported upstream:
# https://github.com/scream3r/java-simple-serial-connector/issues/80
Patch1:		%{name}-jni-fix.patch

ExclusiveArch:  %{java_arches}

BuildRequires:	gcc-c++
BuildRequires:	java-25-devel
BuildRequires:	javapackages-local-openjdk25

Requires:	java-25-headless
Requires:	jpackage-utils

%global jni		%{_libdir}/%{name}
%global jniFullSoName	libjSSC-%{version}.so
%global jniSoName	libjSSC.so

%description
jSSC (Java Simple Serial Connector) - library for working with serial ports
from Java.

%package javadoc
Summary:        Javadoc for %{name} package
BuildArch:      noarch
Requires:       %{name} = %{version}

%description javadoc
This package contains the API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n java-simple-serial-connector-%{version}
%patch -P0 -p1 -b .loadlibrary
%patch -P1 -p1 -b .jni-fix
cp -a %{SOURCE1} COPYING
# remove prebuild binaries and jni headers
rm -rf src/java/libs
rm -rf src/cpp/*.h

%build
# compile classes
mkdir -p classes/
(cd src/java; javac -h ../cpp -d ../../classes/ -encoding UTF-8 jssc/*.java)
(cd classes; jar -cf ../jssc.jar jssc/*.class)
# generate javadoc
mkdir -p javadoc/
(cd src/java; javadoc -Xdoclint:none -d ../../javadoc/ -encoding UTF-8 jssc/*.java)
# compile native library
g++ %{optflags} %{?__global_ldflags} -fPIC -shared \
    -D jSSC_NATIVE_LIB_VERSION=\"$(echo %{version} | sed 's/\([1-9]\.[0-9]\).*/\1/')\" \
    -I %{java_home}/include \
    -I %{java_home}/include/linux \
    -o %{jniFullSoName} src/cpp/_nix_based/jssc.cpp

%install
# create necessary directories
install -d %{buildroot}%{jni} \
           %{buildroot}%{_javadocdir}/%{name}
# install jni library and symlink
install -m 0755 -p %{jniFullSoName} %{buildroot}%{jni}
ln -srf %{buildroot}%{jni}/%{jniFullSoName} %{buildroot}%{jni}/%{jniSoName}
# install jar, pom files and java docs
%mvn_artifact org.scream3r:%{name}:%{version} %{name}.jar
%mvn_file org.scream3r:%{name}:%{version} %{name}
%mvn_install -J javadoc

%files -f .mfiles
%license COPYING
%doc README.txt
%{jni}/

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
%autochangelog
