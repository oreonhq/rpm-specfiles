%global source0_hash a6a8b3b1153faa3a84e71ed81206b19335902fae5f7dee5427a381f4983c217d
Name:           icc-profiles-openicc
Version:        1.3.1
Release:        1%{?dist}
Summary:        The OpenICC profiles
License:        zlib
URL:            http://www.freedesktop.org/wiki/OpenIcc
Source0:        http://downloads.sourceforge.net/project/openicc/OpenICC-Profiles/%{name}-%{version}.tar.bz2
BuildArch:      noarch
Requires:       color-filesystem
# oreon:deps
BuildRequires:  color-filesystem
BuildRequires:  make
# /oreon:deps
%description
The OpenICC profiles are provided to serve color managed
applications and services.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --enable-verbose
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/{pixmaps,mime/packages}
install -pm 0644 *.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
