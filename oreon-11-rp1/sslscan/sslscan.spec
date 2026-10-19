%global source1_hash 967311f84955316969bdb1d8d4b983718ef42338639c621ec4c34fddef355e99
%global source0_hash b0498467604c3f4eb7a1b3258ee9f37b709f7844d7edf338d40e85af40ede960
Name:           sslscan
Version:        2.2.3
%global         bundled_openssl_version    3.5.4
Release:        1%{?dist}
Summary:        Security assessment tool for SSL/TLS
License:        LicenseRef-Callaway-GPLv3+-with-exceptions
%bcond_without     bundled_openssl
URL:            https://github.com/rbsec/sslscan/
Source0:        https://github.com/rbsec/%{name}//archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://www.openssl.org/source/openssl-%{bundled_openssl_version}.tar.gz
Patch0:         sslscan-override-CFLAGS.patch
Patch1:         sslscan-disable-opensslpull.patch
%if %{with bundled_openssl}
Provides: bundled(openssl) = %{bundled_openssl_version}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl
BuildRequires:  zlib-devel
# /oreon:deps
%description
SSLScan queries SSL services, such as HTTPS, in order to determine the ciphers
that are supported. SSLScan is designed to be easy, lean and fast. 
The output includes preferred ciphers of the SSL service, the certificate
and is in text and XML formats.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%if %{with bundled_openssl}
mkdir openssl
cd openssl
tar xvf %{SOURCE1} --strip-components=1
%endif

%build

%if %{with bundled_openssl}
make %{?_smp_mflags} CFLAGS="%{optflags}" static
%else
make %{?_smp_mflags} CFLAGS="%{optflags}"
%endif
%install
make install DESTDIR=%{buildroot} BINPATH=%{_bindir}/ MANPATH=%{_mandir}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
