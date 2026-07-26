%global source0_hash 3bc9fc0e61827ee2f608e5e44993a8fda6d610b80a1e01a9c75610cc292997b5

Summary:        Port of libtls from LibreSSL to OpenSSL
Name:           libretls
Version:        3.8.1
Release:        7%{?dist}
# libretls itself is ISC but uses other source codes, breakdown:
# BSD-3-Clause: compat/strsep.c
# MIT: compat/timegm.c
# LicenseRef-Fedora-Public-Domain: compat/{{explicit_bzero,ftruncate,pread,pwrite}.c,chacha_private.h}
License:        ISC AND BSD-3-Clause AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://git.causal.agency/libretls/about/
Source0:        https://causal.agency/libretls/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel >= 1.1.1b
BuildRequires:  man

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

# Don't install any libtool .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/libtls.la

# Convert README man page to text file
MANWIDTH=72 man ./README.7 | col -bx > README
touch -c -r README.7 README

# Install README man page as libtls.7
sed -e 's/README 7/libtls 7/g' -i README.7
touch -c -r README README.7
install -D -p -m 0644 README.7 $RPM_BUILD_ROOT%{_mandir}/man7/libtls.7

%ldconfig_scriptlets

%files
%doc README
%{_libdir}/libtls.so.28*
%{_mandir}/man7/libtls.7*

%files devel
%{_libdir}/libtls.so
%{_libdir}/pkgconfig/libtls.pc
%{_includedir}/tls.h
%{_mandir}/man3/tls_*.3*

%if 0%{!?_without_static:1}
%files static
%{_libdir}/libtls.a
%endif

%changelog
%autochangelog
