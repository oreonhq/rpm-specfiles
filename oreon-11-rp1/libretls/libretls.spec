%global source0_hash 3bc9fc0e61827ee2f608e5e44993a8fda6d610b80a1e01a9c75610cc292997b5
Summary:        Port of libtls from LibreSSL to OpenSSL
Name:           libretls
Version:        3.8.1
Release:        1%{?dist}
License:        ISC AND BSD-3-Clause AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://git.causal.agency/libretls/about/
Source0:        https://causal.agency/libretls/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  man
BuildRequires:  openssl-devel
# /oreon:deps
%description
LibreTLS is a port of libtls from LibreSSL to OpenSSL. OpenBSD's libtls is a
new TLS library, designed to make it easier to write foolproof applications.

%package devel
Summary:        Development files for libretls
Requires:       %{name}%{?_isa} = %{version}-%{release}, pkgconfig
%description devel
The libretls-devel package contains libraries and header files for developing
applications that use libtls.

%if 0%{!?_without_static:1}
%package static
Summary:        Static library for libretls
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description static
The libretls-static package includes static libraries of libretls. Install it
if you need to link statically with libtls.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure %{?_without_static:--disable-static}
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/libtls.la
MANWIDTH=72 man ./README.7 | col -bx > README
touch -c -r README.7 README
sed -e 's/README 7/libtls 7/g' -i README.7
touch -c -r README README.7
install -D -p -m 0644 README.7 $RPM_BUILD_ROOT%{_mandir}/man7/libtls.7
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libretls-devel -f %{oreon_filedir}/libretls-devel.list
%files -n libretls-static -f %{oreon_filedir}/libretls-static.list

%changelog

%autochangelog
