%global source0_hash eb16c29286ee8dde0f77777404b6e3c485af1c6212f4f472792c64ffbe00ad81

%bcond_without bootstrap

Name:           apache-commons-codec
Version:        1.22.1
Release:        %autorelease
Summary:        Implementations of common encoders and decoders
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-codec/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://archive.apache.org/dist/commons/codec/source/commons-codec-%{version}-src.tar.gz
# Data in DoubleMetaphoneTest.java originally has an inadmissible license.
# The author gives MIT in e-mail communication.
Source1:        aspell-mail.txt

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.hamcrest:hamcrest)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-params)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.17.1-12

%description
Commons Codec is an attempt to provide definitive implementations of
commonly used encoders and decoders. Examples include Base64, Hex,
Phonetic and URLs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n commons-codec-%{version}-src
cp %{SOURCE1} aspell-mail.txt
sed -i 's/\r//' RELEASE-NOTES*.txt LICENSE.txt NOTICE.txt

%mvn_file : commons-codec %{name}
%mvn_alias : commons-codec:commons-codec

%build
%mvn_build -j -- -Dcommons.osgi.symbolicName=org.apache.commons.codec

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt aspell-mail.txt
%doc RELEASE-NOTES*

%changelog
%autochangelog
