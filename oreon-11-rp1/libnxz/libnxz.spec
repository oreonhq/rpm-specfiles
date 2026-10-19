%global source0_hash 33cdc419a10d5426edb062ce6e670f7d42f81898c857ff5943eb7f1f8280d9ed
%global __brp_remove_la_files %nil
Name:		libnxz
Version:	0.65
Release:        1%{?dist}
Summary:        Zlib implementation for POWER processors
License:    Apache-2.0 OR GPL-2.0-or-later
Url:		https://github.com/libnxz/power-gzip
Source0:        https://github.com/%{name}/power-gzip/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{url}/pull/209.patch
%global soname libnxz.so.0
ExclusiveArch:	ppc64le
Requires: powerpc-utils-core > 1.3.10-2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%description
libnxz is a zlib-compatible library that uses the NX GZIP Engine available on
POWER9 or newer processors in order to provide a faster zlib/gzip compression
without using the general-purpose cores.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
The %{name}-devel package contains header files for developing application that
use %{name}.

%package	static
Summary:	Static library for %{name} development
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
%description	static
The %{name}-static package contains static libraries for developing
application that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n power-gzip-%{version}

# Create a sysusers.d config file
cat >libnxz.sysusers.conf <<EOF
g nx-gzip -
EOF

%build

%configure --enable-zlib-api
%make_build
%check

if [[ -w "/dev/crypto/nx-gzip" ]]; then
	make check
fi
%install
%make_install
install -m0644 -D libnxz.sysusers.conf %{buildroot}%{_sysusersdir}/libnxz.conf
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libnxz-devel -f %{oreon_filedir}/libnxz-devel.list
%files -n libnxz-static -f %{oreon_filedir}/libnxz-static.list

%changelog

%autochangelog
