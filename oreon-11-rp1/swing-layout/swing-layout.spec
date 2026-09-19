%global source0_hash b8169b37e4c6d2e92881e97d3023813f99c7653595e8a93e3cc6b26e5bf70351

Name:           swing-layout
Version:        1.0.4
Release:        36%{?dist}
Summary:        Natural layout for Swing panels
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://swing-layout.dev.java.net/
# https://svn.java.net/svn/swing-layout~svn/trunk/
# the above urls are dead, since the upstream project doesn't exist anymore
Source0:        %{name}-%{version}-src.zip
# from http://java.net/jira/secure/attachment/27303/pom.xml
Source1:        %{name}-pom.xml
# use javac target/source 1.5
Patch0:         %{name}-%{version}-project_properties.patch
Patch1:         %{name}-%{version}-fix-incorrect-fsf-address.patch

BuildRequires:  junit >= 3.8.2
BuildRequires:  javapackages-local-openjdk25
BuildRequires:  java-25-devel >= 1.3
BuildRequires:  ant-openjdk25 
BuildRequires:  dos2unix
Requires:       java-25-headless >= 1.3

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
Extensions to Swing to create professional cross platform layout.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
dos2unix releaseNotes.txt
%patch -P0 -p0
%patch -P1 -p0
sed -i 's/\r//' COPYING

cat %{SOURCE1} | sed "s|<version>1.0.3</version>|<version>%{version}</version>|"  >  %{name}.pom

%build

%{ant} jar 
%mvn_artifact %{name}.pom dist/%{name}.jar

%install

%mvn_install -J dist/javadoc

%check
%{ant} test

%files -f .mfiles
%doc releaseNotes.txt
%license COPYING

%changelog
%autochangelog
