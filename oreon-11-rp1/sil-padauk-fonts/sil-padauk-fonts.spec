%global source0_hash b47b2639489d7cec5ad38d025f181b061767e4e161a41f19528e910f79fd03a1

Version:  3.003
Release:  21%{?dist}
URL:      https://software.sil.org/padauk/

%global         foundry         SIL
%global         fontlicense     OFL-1.1
%global         fontdocs        *.txt documentation
%global         fontdocsex      %{fontlicenses}

%global common_description %{expand:
Padauk is a pan Burma font designed to support all Myanmar script based \
languages. It covers all of the Unicode Myanmar script blocks and works \
on all OpenType and Graphite based systems.}

%global fontfamily0       Padauk
%global fontsummary0      A font for Burmese and the Myanmar script
%global fonts0            Padauk-*.ttf
%global fontconfs0        %{SOURCE10}
%global fontdescription0  %{expand:
%{common_description}

This package provide the base fonts.}


%global fontfamily1       Padauk Book
%global fontsummary1      Padauk Book fonts
%global fonts1            PadaukBook*.ttf
%global fontconfs1        %{SOURCE11}
%global fontdescription1  %{expand:
%global fontpkgname1      sil-padauk-book-fonts
%{common_description}

This package provide Padauk Book family font.}

Source0:  https://github.com/silnrsi/font-padauk/releases/download/v%{version}/padauk-%{version}.zip
Source10: 65-%{fontpkgname0}.conf
Source11: 66-%{fontpkgname1}.conf

%fontpkg -a

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n padauk-3.003
%linuxtext *.txt documentation/*.txt

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.003-21
- Prepare for Oreon 11 (RP1)
