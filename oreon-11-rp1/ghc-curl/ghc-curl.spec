%global source1_hash d8208f8391087636fc042097b9751731ee28262a50ebe4d214ecc5c2e512580b
%global source0_hash 9087c936bfcdb865bad3166baa3f12bf37acf076fa76010e3b5f82a1d485446e
%global pkg_name curl
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        1.3.8
Release:        1%{?dist}
Summary:        Haskell binding to libcurl
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/curl
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  libcurl-devel
# /oreon:deps
%description
Libcurl is a client-side URL transfer library, supporting FTP, FTPS, HTTP,
HTTPS, SCP, SFTP, TFTP, TELNET, DICT, LDAP, LDAPS and FILE. libcurl supports
SSL certificates, HTTP POST, HTTP PUT, FTP uploading, HTTP form based upload,
proxies, cookies, user+password authentication (Basic, Digest, NTLM, Negotiate,
Kerberos4), file transfer resume, http proxy tunneling and more!

This package provides a Haskell binding to libcurl.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libcurl-devel%{?_isa}
%description devel
This package provides the Haskell %{pkg_name} library development files.

%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem
%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif

%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)
%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
cp -bp %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-curl-devel -f %{oreon_filedir}/ghc-curl-devel.list
%files -n ghc-curl-doc -f %{oreon_filedir}/ghc-curl-doc.list
%files -n ghc-curl-prof -f %{oreon_filedir}/ghc-curl-prof.list

%changelog

%autochangelog
