%global source0_hash 3e25b235db034d7c1b3c227dadb33088f6d9a53f81aab5f9293ad7bc3434d016

%global commit bd245c9

Name:           pcfi
Version:        2010.08.09
Release:        36.20111103git%{commit}%{?dist}
Summary:        PDF Core Font Information

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/jukka/pcfi
Source0:        https://github.com/jukka/pcfi/tarball/%{commit}/jukka-pcfi-%{commit}.tar.gz
# Originally downloaded from: http://opensource.adobe.com/wiki/display/cmap/License
# This now points to Adobe's sourceforge pages
Source1:        License
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
BuildRequires:  maven-local-openjdk25
Requires:       jpackage-utils

%description
Collection of PDF core font information files downloaded from Adobe's
Developer Center and elsewhere. This collection contains font metrics for the
14 PDF core fonts, CMaps for the PDF CJK fonts and the Adobe Glyph List.   The
files are stored inside the com/adobe/pdf/pcfi directory. See the individual
files for exact licensing information.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n jukka-pcfi-%{commit}
sed -i 's/\r//' src/main/resources/META-INF/LICENSE.txt
cp %SOURCE1 .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.txt src/main/resources/META-INF/LICENSE.txt License

%changelog
%autochangelog
