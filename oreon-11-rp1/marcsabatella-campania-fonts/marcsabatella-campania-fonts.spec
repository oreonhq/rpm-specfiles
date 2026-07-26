%global source0_hash 48a2797dc27fc79fc6752567df1262cce77d6bb7677420c17be55b37fb86e7c6

Version:        2.009
Release:        14%{?dist}
URL:            https://github.com/MarcSabatella/Campania
VCS:            git:%{url}.git

%global foundry           MarcSabatella
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      LICENSE
%global fontdocs          README.md
%global fontfamily        Campania
%global fontsummary       Font for Roman numeral analysis (music theory)
%global fonts             *.otf
%global fontorg           com.github
%global fontconfs         %{SOURCE1}

%global fontdescription   %{expand:This font is inspired by the work of Florian Kretlow and the impressive
Figurato font he developed for figured bass, as well as the work of Ronald
Caltabiano and his pioneering Sicilian Numerals font.  This version of
Campania is not directly based on either of these, however.  Instead, it uses
the glyphs from Doulos and adds some relatively straightforward contextual
substitutions and positioning rules to allow you to enter the most common
symbols just by typing naturally.}

Source0:        https://github.com/MarcSabatella/Campania/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        65-%{fontpkgname}.conf

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  fontforge

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Campania-%{version}

%build
%fontbuild
fontforge -lang=ff -c 'Open($1); Generate($2)' Campania.sfd Campania.otf

%install
%fontinstall
metainfo=%{buildroot}%{_metainfodir}/%{fontorg}.%{name}.metainfo.xml

# The Fedora font macros generate invalid metainfo; see bz 1943727.
sed -i 's,<!\[CDATA\[\(.*\)\]\]>,\1,' $metainfo

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
