%global source0_hash b20cbf4ff704f0741a9b89376e5c497392b23282eebacbfdab2502a861f16ac2

# SPDX-License-Identifier: MIT
Version: 20191205
Release: 19%{?dist}
URL:     http://www.greekfontsociety-gfs.gr/typefaces/20th_21st_century

%global foundry           GFS
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Galatea
%global fontsummary       GFS Galatea, a 20th century Greek font family
%global fonts             *.otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
GFS Galatea Bold revives in digital form an older hot metal typeface from the
1920’s, which can be found in older Greek type specimens named simply as FAT
type. The font was used as a bold companion of Didot Greek (Apla/Monotype 92).
It has many similarities with Didot Greek (Απλά) in design, but it differs in
its reduced stroke contrast, the use of a lunar lower case epsilon (reminiscent
of the similar epsilon in Porson Greek) and in sturdier stems and slab serifs.
An experimental projection of these characteristics to a lighter version has
led to the introduction of GFS Galatea Regular. The name Galatea is a tribute
to the author and feminist Galatea Kazantzakis (1881–1962) as samples of the
typeface were found in several of her books.

Both typefaces were designed by George Triantafyllakos and are freely available
for use.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{foundry} %{fontfamily}"), "[%p%s]+", "_");print(t)}

Source0:  http://www.greekfontsociety-gfs.gr/_assets/fonts/%{archivename}.zip
Source10: 60-%{fontpkgname}.xml

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
