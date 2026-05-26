%global fontname lohit-gujarati

Version:       2.92.4
Release:       25%{?dist}
URL:           https://github.com/lohit-fonts/lohit-gujarati-fonts

%global foundry           Lohit
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt COPYRIGHT
%global fontdocs          AUTHORS README ChangeLog test-gujarati.txt

%global fontfamily        Lohit Gujarati
%global fontsummary       Free Gujarati font
%global fonts             *.ttf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
This package provides a free Gujarati truetype/opentype font.
}

BuildRequires: make
BuildRequires: fontforge
Source0:        https://releases.pagure.org/lohit/%{fontname}-%{version}.tar.gz
Source10:       66-%{fontpkgname}.conf
# oreon url source checksums begin
%global source0_sha256 5be2f69eec4295e62bfddb1c65cbeeaa4aea15524def904706d41bdd8e8c8644
%global source0_file lohit-gujarati-2.92.4.tar.gz
# oreon url source checksums end

%fontpkg

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/lohit-gujarati-2.92.4.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5be2f69eec4295e62bfddb1c65cbeeaa4aea15524def904706d41bdd8e8c8644" || { echo "oreon: Source0 SHA256 mismatch for lohit-gujarati-2.92.4.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{fontname}-%{version} 
%linuxtext OFL.txt AUTHORS README ChangeLog COPYRIGHT test-gujarati.txt

%build
make ttf %{?_smp_mflags}
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.92.4-25
- Prepare for Oreon 11 (RP1)
