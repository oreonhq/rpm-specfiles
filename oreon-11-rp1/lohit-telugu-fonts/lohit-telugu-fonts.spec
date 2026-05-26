%global fontname lohit-telugu

Version:       2.5.5
Release:       23%{?dist}
URL:           https://github.com/lohit-fonts/lohit-odia-fonts

%global foundry           Lohit
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt COPYRIGHT
%global fontdocs          AUTHORS README ChangeLog

%global fontfamily        Lohit Telugu 
%global fontsummary       Free Telugu font
%global fonts             *.ttf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
This package provides a free Telugu truetype/opentype font.
}

BuildRequires: make
BuildRequires: fontforge
BuildRequires: ttfautohint
Source0:        https://releases.pagure.org/lohit/%{fontname}-%{version}.tar.gz
Source10:       66-%{fontpkgname}.conf
# oreon url source checksums begin
%global source0_sha256 fddaf9e21d198d5faeaf4f0c3bfd4070d28140243fd229af5b581119f4e11d39
%global source0_file lohit-telugu-2.5.5.tar.gz
# oreon url source checksums end

%fontpkg

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/lohit-telugu-2.5.5.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "fddaf9e21d198d5faeaf4f0c3bfd4070d28140243fd229af5b581119f4e11d39" || { echo "oreon: Source0 SHA256 mismatch for lohit-telugu-2.5.5.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{fontname}-%{version}
%linuxtext OFL.txt AUTHORS README ChangeLog COPYRIGHT

%build
make ttf %{?_smp_mflags}
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.5-23
- Prepare for Oreon 11 (RP1)
