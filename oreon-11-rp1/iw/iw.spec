%global source0_hash 7d182e498289ab39b257da6780d562e415377107f50358ee5b55b8cfe40b1e33
Name:           iw
Version:        6.17
Release:        1%{?dist}
Summary:        A nl80211 based wireless configuration tool
License:        ISC AND LicenseRef-Public-Domain
URL:            https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html
Source0:        https://cdn.kernel.org/pub/software/network/iw/iw-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  libnl3-devel
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
iw is a new nl80211 based CLI configuration utility for wireless devices.
Currently you can only use this utility to configure devices which
use a mac80211 driver as these are the new drivers being written - 
only because most new wireless devices being sold are now SoftMAC.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir iw-6.17
%oreon_prep
%build

export CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
%{make_build}
%install
%{make_install} SBINDIR=%{_sbindir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.17-2
- Import
