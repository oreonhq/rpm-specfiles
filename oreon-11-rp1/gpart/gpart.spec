%global source0_hash ec56d12ec9ffdb9877c12692ea6e51620b1ae44473d3d253b27fc31ed9ebb4dd

Summary:        A program for recovering corrupt partition tables
Name:           gpart
Version:        0.3
Release:        25%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/baruch/%{name}/
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# https://github.com/baruch/gpart/pull/16
Patch0:         fsf_address.patch

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make

%description
Gpart is a small tool which tries to guess what partitions are on a PC
type harddisk in case the primary partition table was damaged.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
autoreconf -f -i

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%if 0%{?el7}
%dir %{_datadir}/doc/%{name}
%{_datadir}/doc/%{name}/*
%else
%dir %{_pkgdocdir}
%{_pkgdocdir}/*
%endif
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
%autochangelog
