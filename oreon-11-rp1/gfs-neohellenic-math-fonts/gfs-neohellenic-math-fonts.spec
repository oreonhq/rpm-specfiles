%global source0_hash 03b301ad47e918677a6c5130783fbd66acaf0b69864fb531215c82f6fcbc4e0f

# SPDX-License-Identifier: MIT
Version: 20180227
Release: 19%{?dist}
URL:     https://www.greekfontsociety-gfs.gr/typefaces/Math

%global foundry           GFS
%global fontlicense       OFL-1.1
# GFS already forgot about providing clean licensing texts
%global fontlicenses      README
%global fontdocs          README

%global fontfamily        NeoHellenic Math
%global fontsummary       GFS NeoHellenic Math, an almost Sans Serif Math font family
%global fontpkgheader     %{expand:
Requires:    gfs-neohellenic-fonts
Supplements: gfs-neohellenic-fonts
}
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
GFS NeoHellenic Math is an almost Sans Serif font family. One of its main uses
is for presentations, an area where (we believe) a commercial grade sans math
font was not available up to now.

The font family contains an extended glyph set including more than the standard
math symbols such as vertically extended integrals, chess symbols, etc.

It was commissioned to the Greek Font Society (GFS) by the Graduate Studies
program “Studies in Mathematics” of the Department of Mathematics of the
University of the Aegean, located on the Samos island, Greece.

The design copyright belongs to the main designer of GFS, George Matthiopoulos.
The OpenType Math Table embedded in the font was developed by the Mathematics
Professor Antonis Tsolomitis.}

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
%linuxtext README

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)
%license README
%doc *.pdf *.sty

%changelog
%autochangelog
