%global source0_hash b0e2fef60800cc5cd2123db5ccca967f44735f3fb1b8f36adf3d32fefc0f26aa
Summary:        RADIUS protocol client library
Name: radcli
Version: 2.0.0
Release:        1%{?dist}
License: BSD-2-Clause AND UMich-Merit AND HPND-Fenneberg-Livingston
URL: http://radcli.github.io/radcli/
%{expand:%(echo "%%global myversion %{version}" | \
  sed 's/\./_/g')}
Source0:        https://github.com/%{name}/%{name}/releases/download/%{name}_2_0_0/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gnutls-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  nettle-devel
# /oreon:deps
%description
The radcli library is a library for writing RADIUS Clients. The library's
approach is to allow writing RADIUS-aware application in less than 50 lines
of C code. It was based originally on freeradius-client and is source compatible
with it.

%package devel
Summary: Development files for radcli
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains libraries and header files for developing applications
that use %{name}.

%package compat-devel
Summary: Development files for compatibility with radiusclient-ng and freeradius-client
Requires: %{name}-devel = %{version}-%{release}
Conflicts: freeradius-client-devel, radiusclient-ng-devel
%description compat-devel
This package contains the compatibility headers and libraries for freeradius-client
and radiusclient-ng.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
rm -f lib/md5.c
sed -i -e 's|sys_lib_dlsearch_path_spec="[^"]\+|& %{_libdir}|g' configure

%build

autoreconf -fvi
%configure --disable-static --disable-rpath --with-nettle --with-tls --enable-legacy-compat
make %{?_smp_mflags}
%check

make %{?_smp_mflags} check
%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/*.la
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -p %{buildroot}%{_datadir}/%{name}/dictionary %{buildroot}%{_sysconfdir}/%{name}/dictionary
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n radcli-devel -f %{oreon_filedir}/radcli-devel.list
%files -n radcli-compat-devel -f %{oreon_filedir}/radcli-compat-devel.list

%changelog

%autochangelog
