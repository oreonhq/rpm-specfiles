%global source0_hash 4cae1a7104be63627f04184e690514ca4371dc4e9ab2026694e03a44388b577a

# SPDX-License-Identifier: MIT
Version: 20161102
Release: 19%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/19th_century

%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Orpheus Classic
%global fontsummary       GFS Orpheus Classic, a 19th century Greek font family
%global fontpkgheader     %{expand:
Suggests: font(gfsorpheus)
}
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
This rare typeface was first used in the last decade of the 19th century and
was offered for use until the 1960s. Its design is characterized by an
outstanding subtlety and purity in its letter-forms. With almost round counters,
a low x-height, a fairly high contrast and a nearly horizontal axis, it is a
very elegant and legible typeface that works excellently on small text. GFS
Orpheus Classic is a digital reproduction of this brilliant design.

It was digitized by George Triantafyllakos based on specimens from Linotype Co.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 61-%{fontpkgname}.xml

%fontpkg

%package doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
unzip -j -q  %{SOURCE0}
%linuxtext *.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)
%license OFL.txt
%doc *.pdf

%changelog
%autochangelog
