%global source0_hash ef82a172d82e8300b91b4ec08df282292ac841f9233188e00554f56e97c2c089

Name:           openpace
Version:        1.1.3
Release:        5%{?dist}
Summary:        Cryptographic library for EAC version 2

License:        GPL-3.0-only
URL:            https://frankmorgner.github.io/openpace/
Source:         https://github.com/frankmorgner/openpace/releases/download/%{version}/openpace-%{version}.tar.gz
Patch1:         openpace-1.1.3-unsupported-tests.patch

BuildRequires:  autoconf automake libtool gcc
BuildRequires:  openssl openssl-devel

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
# https://fedoraproject.org/wiki/Changes/OpenSSLDistrustSHA1SigVer
export OPENSSL_ENABLE_SHA1_SIGNATURES=1
make check

%install
%make_install

find %{buildroot}%{_libdir} -type f -name "*.la" | xargs rm

# Remove unnecessary files from the documentation directory
find %{buildroot}%{_docdir}/openpace -type f -name 'Makefile*' | xargs rm
find %{buildroot}%{_docdir}/openpace -type f -name '.nojekyll' | xargs rm

# Remove the example and test files
rm -rf %{buildroot}%{_bindir}/example
rm -rf %{buildroot}%{_bindir}/eactest

# Remove fonts
rm -rf %{buildroot}%{_docdir}/openpace/_static/bootstrap-3.3.7/fonts
rm -rf %{buildroot}%{_docdir}/openpace/_static/bootswatch-3.3.7/fonts

%files
%license COPYING
%dir %{_sysconfdir}/eac/
%dir %{_sysconfdir}/eac/cvc
%dir %{_sysconfdir}/eac/x509
%{_bindir}/cvc-create
%{_bindir}/cvc-print
%{_libdir}/libeac.so.*
%config(noreplace) %{_sysconfdir}/eac/cvc/DECVCAEPASS00102
%config(noreplace) %{_sysconfdir}/eac/cvc/DECVCAeID00102
%config(noreplace) %{_sysconfdir}/eac/cvc/DECVCAeSign00102
%config(noreplace) %{_sysconfdir}/eac/x509/ff3d20d2
%{_mandir}/man1/cvc-create.1.gz
%{_mandir}/man1/cvc-print.1.gz

%files devel
%dir %{_includedir}/eac/
%{_libdir}/libeac.so
%{_includedir}/eac/*
%{_libdir}/pkgconfig/libeac.pc

%files doc
%doc %{_docdir}/openpace

%changelog
%autochangelog
