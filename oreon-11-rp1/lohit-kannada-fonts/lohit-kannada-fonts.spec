%global fontname lohit-kannada

Version:       2.5.4
Release:       23%{?dist}
URL:           https://github.com/lohit-fonts/lohit-kannada-fonts

%global foundry           Lohit
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt COPYRIGHT
%global fontdocs          AUTHORS README ChangeLog

%global fontfamily        Lohit Kannada
%global fontsummary       Free Kannada font
%global fonts             *.ttf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
This package provides a free Kannada truetype/opentype font.
}

BuildRequires: make
BuildRequires: fontforge
Source0:        https://releases.pagure.org/lohit/%{fontname}-%{version}.tar.gz
Source10:       66-%{fontpkgname}.conf
# oreon url source checksums begin
%global source0_sha256 259c18128fe59b821d58b000ffdd9b517db290313acea6d64a5ea67764aad9b3
%global source0_file lohit-kannada-2.5.4.tar.gz
# oreon url source checksums end

%fontpkg

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/lohit-kannada-2.5.4.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "259c18128fe59b821d58b000ffdd9b517db290313acea6d64a5ea67764aad9b3" || { echo "oreon: Source0 SHA256 mismatch for lohit-kannada-2.5.4.tar.gz" >&2; exit 1; })
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.4-23
- Prepare for Oreon 11 (RP1)
