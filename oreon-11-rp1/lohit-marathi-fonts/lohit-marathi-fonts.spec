%global fontname lohit-marathi

Version:       2.94.2
Release:       25%{?dist}
URL:           https://github.com/lohit-fonts/lohit-marathi-fonts 

%global foundry           Lohit
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt COPYRIGHT
%global fontdocs          AUTHORS README ChangeLog test-marathi.txt

%global fontfamily        Lohit Marathi
%global fontsummary       Free truetype font for Marathi language
%global fonts             *.ttf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
This package provides a free Marathi truetype/opentype font.
}

BuildRequires: make
BuildRequires: fontforge
Source0:        https://releases.pagure.org/lohit/%{fontname}-%{version}.tar.gz
Source10:       66-%{fontpkgname}.conf
# oreon url source checksums begin
%global source0_sha256 f2a071e796edd188ab19184c748a17f85a2816b96c893a6cdc5f745d9728ace4
%global source0_file lohit-marathi-2.94.2.tar.gz
# oreon url source checksums end

%fontpkg

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/lohit-marathi-2.94.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f2a071e796edd188ab19184c748a17f85a2816b96c893a6cdc5f745d9728ace4" || { echo "oreon: Source0 SHA256 mismatch for lohit-marathi-2.94.2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{fontname}-%{version}
%linuxtext OFL.txt AUTHORS README ChangeLog COPYRIGHT test-marathi.txt

%build
make ttf %{?_smp_mflags}
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.94.2-25
- Prepare for Oreon 11 (RP1)
