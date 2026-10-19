%global source0_hash ba23d68096e500c2a933bf4bd45ac98384732740ff5de9e47d45cd4e6beaf41f
Name:		psftools
Version:	1.1.3
Release:        1%{?dist}
Summary:        Conversion tools for .PSF fonts
License:	GPL-2.0-or-later
URL:		https://www.seasip.info/Unix/PSF/
Source0:        https://www.seasip.info/Unix/PSF/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
The PSFTOOLS are designed to manipulate fixed-width bitmap fonts, such as DOS
or Linux console fonts. Both the PSF1 (8 pixels wide) and PSF2 (any width)
formats are supported; the default output format is PSF2.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --disable-shared
make %{?_smp_mflags}
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
