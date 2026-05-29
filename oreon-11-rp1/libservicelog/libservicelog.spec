%global source0_hash cf04b506ff5b4cbb4064490371810ff1feb3959133bf582d6f71b9a27b5dfeee

Name:          libservicelog
Version:       1.1.19
Release:       17%{?dist}
Summary:       Servicelog Database and Library

#v29_notify_gram.c v29_notify_gram.h are GPLv2+
License:       LGPL-2.0-only AND GPL-2.0-or-later

URL:           https://github.com/power-ras/%{name}/releases
Source:        https://github.com/power-ras/libservicelog/archive/v1.1.19/libservicelog-1.1.19.tar.gz
# sysusers.d config file
Source1:       libservicelog.sysusers.conf

# Link with needed libraries
Patch0: libservicelog-1.1.9-libs.patch

# sysusers_create_compat macro
BuildRequires: systemd-rpm-macros
%{?sysusers_requires_compat}
BuildRequires: sqlite-devel autoconf libtool bison librtas-devel flex
BuildRequires: make

# because of librtas-devel
ExclusiveArch: ppc %{power64}

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%patch 0 -p1 -b .libs


%build
autoreconf -fiv
%configure --disable-static
# disable "-Werror=format-security" checking gcc option until we fix
# these errors are fixed in upstream code.
CFLAGS="%{optflags} -fPIC -DPIC"
CFLAGS=`echo $CFLAGS | sed 's/-Werror=format-security//'`
make CFLAGS="$CFLAGS" %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la

install -m0644 -D %{SOURCE1} %{buildroot}%{_sysusersdir}/libservicelog.conf

%check
make check || true

%pre
%sysusers_create_compat %{SOURCE1}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS
%{_libdir}/libservicelog-*.so.*
%dir %attr(755, root, service) /var/lib/servicelog
%config(noreplace) %verify(not md5 size mtime) %attr(644,root,service) /var/lib/servicelog/servicelog.db
%{_sysusersdir}/libservicelog.conf

%files devel
%{_includedir}/servicelog-1
%{_libdir}/*.so
%{_libdir}/pkgconfig/servicelog-1.pc


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.19-17
- Import
