%global source0_hash 161a11bddb91fa32f625175b0f4015ecf72a943f6781385c719ebe78f26e3358

Name:           IPAddress
Version:        5.2.1
Release:        24%{?dist}
Summary:        Library for handling IP addresses and subnets, both IPv4 and IPv6
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/seancfoley/IPAddress
Source0:        https://github.com/seancfoley/IPAddress/archive/v%{version}.tar.gz
Patch1:         removeNonAsciChars.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  ant-openjdk25 

Requires: java-25-headless

%description
Library for handling IP addresses and subnets, both IPv4 and IPv6

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1

%build
pushd IPAddress
rm dist/IPAddress.jar
mkdir bin #for classes
#while jdk8 is main, we need both jdks, and prefer the upper one
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
# be aware, the build do not fail in compilation faiure, and you can end with empty, or full of sources jar, as I did first time!
ant "create dist jar" #yah, funny name, as the whole ant-maven-less-with-pom build system
mv dist/IPAddress*.jar dist/IPAddress.jar
#%%mvn_build it looks like pom is useles, and is enough as it is

%install
%mvn_artifact IPAddress/pom.xml IPAddress/dist/IPAddress.jar
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md

%changelog
%autochangelog
