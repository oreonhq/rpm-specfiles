%global source0_hash d8b50ca876781ef6c2f0e1dd1a7ed6896a7f7769242e76be901b98c6d7edfafb
%global commit           154d50362016cc3e873eb21d242cd0772384c8f9
%global shortcommit      %{sub %{commit} 1 7}
%global commitdate       20241120
%global fontname         atkinson-hyperlegible-mono
%global fontdescription %{expand:
Atkinson Hyperlegible Mono is an entirely new typeface inspired by the Atkinson
Hyperlegible font. The monospaced font features characters that each occupy the
same amount of horizontal space, allowing for them to be scanned quickly in
table-based and coding environments.
}
Version:        2.100
Release:        1%{?dist}
URL:            https://www.brailleinstitute.org/freefont/
Source0:        https://github.com/googlefonts/%{fontname}/archive/154d503.tar.gz
Source1:        64-%{fontname}.xml
%global fontfamily      Atkinson Hyperlegible Mono
%global fontsummary     Monospace typeface made for low-vision legibility
%global fontlicense     OFL-1.1
%global fontlicenses    OFL.txt
%global fontdocs        DESCRIPTION.en_us.html
%global fonts           fonts/otf/*.otf
%global fontconfs       %{SOURCE1}
%fontpkg
# oreon:deps
BuildRequires:  fontpackages-devel
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n atkinson-hyperlegible-next-mono-%{commit}

%build

%fontbuild
%install
%fontinstall
%oreon_autofiles main

%check

%fontcheck
%fontfiles
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
