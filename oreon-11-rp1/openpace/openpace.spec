%global source0_hash 36954f0385a1cb9805a02cffbd0d99f2b3a0598a125edfa160b4cca65b417854
Name:           openpace
Version:        1.1.4
Release:        1%{?dist}
Summary:        Cryptographic library for EAC version 2
License:        GPL-3.0-only
URL:            https://frankmorgner.github.io/openpace/
Source0:        https://github.com/frankmorgner/openpace/releases/download/%{version}/openpace-%{version}.tar.gz
Patch1:         openpace-1.1.3-unsupported-tests.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  openssl
BuildRequires:  openssl-devel
# /oreon:deps
%description
OpenPACE implements Extended Access Control (EAC) version 2 as specified in
BSI TR-03110. OpenPACE comprises support for Password Authenticated Connection
Establishment (PACE), Terminal Authentication (TA), and Chip Authentication (CA)
protocols. Its also supports Card Verifiable Certificates (CV Certificates)
and signing requests as well as easy to use wrappers for using the established
secure channels.

%package devel
Summary:        Files for development of applications which will use OpenPACE
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files with header files to develop applications
which support EAC protocol.

%package doc
Summary:        HTML documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Suggests:       font(glyphicons-halflings-fonts)
%description doc
HTML documentation for OpenPACE.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 1 -p1 -b .unsupported-tests

%build	

autoreconf -fvi
%set_build_flags
CFLAGS="$CFLAGS -Wno-deprecated-declarations"
%configure --disable-static
%make_build
%check

export OPENSSL_ENABLE_SHA1_SIGNATURES=1
make check
%install
%make_install
find %{buildroot}%{_libdir} -type f -name "*.la" | xargs rm
find %{buildroot}%{_docdir}/openpace -type f -name 'Makefile*' | xargs rm
find %{buildroot}%{_docdir}/openpace -type f -name '.nojekyll' | xargs rm
rm -rf %{buildroot}%{_bindir}/example
rm -rf %{buildroot}%{_bindir}/eactest
rm -rf %{buildroot}%{_docdir}/openpace/_static/bootstrap-3.3.7/fonts
rm -rf %{buildroot}%{_docdir}/openpace/_static/bootswatch-3.3.7/fonts
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n openpace-devel -f %{oreon_filedir}/openpace-devel.list
%files -n openpace-doc -f %{oreon_filedir}/openpace-doc.list

%changelog

%autochangelog
