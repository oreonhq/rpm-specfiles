%global source0_hash cf04b506ff5b4cbb4064490371810ff1feb3959133bf582d6f71b9a27b5dfeee
Name:          libservicelog
Version:       1.1.19
Release:        1%{?dist}
Summary:        Servicelog Database and Library
License:       LGPL-2.0-only AND GPL-2.0-or-later
URL:           https://github.com/power-ras/%{name}/releases
Source0:        https://github.com/power-ras/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:       libservicelog.sysusers.conf
Patch0: libservicelog-1.1.9-libs.patch
%{?sysusers_requires_compat}
ExclusiveArch: ppc %{power64}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  librtas-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  sqlite-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
The libservicelog package contains a library to create and maintain a
database for storing events related to system service.  This database
allows for the logging of serviceable and informational events, and for
the logging of service procedures that have been performed upon the system.

%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      pkgconfig sqlite-devel
%description   devel
Contains header files for building with libservicelog.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 0 -p1 -b .libs

%build

autoreconf -fiv
%configure --disable-static
CFLAGS="%{optflags} -fPIC -DPIC"
CFLAGS=`echo $CFLAGS | sed 's/-Werror=format-security//'`
make CFLAGS="$CFLAGS" %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
install -m0644 -D %{SOURCE1} %{buildroot}%{_sysusersdir}/libservicelog.conf
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check || true
%pre

%sysusers_create_compat %{SOURCE1}
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{oreon_filedir}/main.list
%files -n libservicelog-devel -f %{oreon_filedir}/libservicelog-devel.list

%changelog

%autochangelog
