%global source5_hash 06a15976b2a76a4e507580540881d6a89df6de79ba38f533586c3f68bdcea314
%global source4_hash 7b399eee49aea00d96c0dda004de62eb2b5e9058097da08474f66c3efae951cb
%global source3_hash daa20426ead1f0061c74a967ac566787c723411a7d726f5dec75faa2e2ee926e
%global source1_hash 441174c47cbeb4a282ba07e988441e4cb3e188b4b0331bd1306c696483ac8375
%global source0_hash 2a34d2484ba17847a5d11965704e9dd0fac4c6d8efc75ffe1ec7de66d8c6b6fb
%bcond CHECK 1
%bcond_without gnutls
%bcond_with docs
Name:           ngtcp2
Version:        1.25.0
Release:        1%{?dist}
Summary:        Implementation of RFC 9000 QUIC protocol
License:        MIT
URL:            https://github.com/ngtcp2/ngtcp2
Source0:        https://github.com/ngtcp2/ngtcp2/releases/download/v%{version}/ngtcp2-%{version}.tar.xz
Source1:        https://github.com/ngtcp2/ngtcp2/releases/download/v%{version}/ngtcp2-%{version}.tar.xz.asc
Source2:        tatsuhiro-t.asc
Source3:        https://github.com/ngtcp2/ngtcp2/raw/refs/tags/v%{version}/doc/mkapiref.py
Source4:        https://github.com/ngtcp2/ngtcp2/raw/refs/tags/v%{version}/doc/source/index.rst
Source5:        https://github.com/ngtcp2/ngtcp2/raw/refs/tags/v%{version}/doc/source/programmers-guide.rst
%if %{with docs}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  gnutls-devel
BuildRequires:  libev-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
# /oreon:deps
%description
"Call it TCP/2. One More Time."

ngtcp2 project is an effort to implement RFC9000 QUIC protocol.

%package devel
Summary:        The ngtcp2 development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Suggests:       %{name}-crypto-any-devel%{?_isa} = %{version}-%{release}
%description devel
"Call it TCP/2. One More Time."

ngtcp2 project is an effort to implement RFC9000 QUIC protocol.

Development headers and libraries.

%if %{with gnutls}
%package crypto-gnutls
Summary:        The ngtcp2 GnuTLS crypto provider
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description crypto-gnutls
"Call it TCP/2. One More Time." RFC9000 QUIC protocol.

GnuTLS library provider.

%package crypto-gnutls-devel
Summary:        The ngtcp2 GnuTLS crypto provider headers
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-crypto-gnutls%{?_isa} = %{version}-%{release}
BuildRequires:  gnutls-devel >= 3.7.5
Requires:       gnutls-devel >= 3.7.5
Provides:       %{name}-crypto-any-devel = %{version}-%{release}
%description crypto-gnutls-devel
"Call it TCP/2. One More Time." RFC9000 QUIC protocol.

GnuTLS library provider headers.
%endif

%package crypto-ossl
Summary:        The ngtcp2 dependency for OpenSSL
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description crypto-ossl
"Call it TCP/2. One More Time." RFC9000 QUIC protocol.

OpenSSL library provider.

%package crypto-ossl-devel
Summary:        The ngtcp2 dependency for OpenSSL headers
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-crypto-ossl%{?_isa} = %{version}-%{release}
BuildRequires:  openssl-devel >= 3.5.0
Requires:       openssl-devel >= 3.5.0
Provides:       %{name}-crypto-any-devel = %{version}-%{release}
%description crypto-ossl-devel
"Call it TCP/2. One More Time." RFC9000 QUIC protocol.

OpenSSL library provider headers.

%if %{with docs}
%package doc
Summary:        The ngtcp2 API documentation
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description doc
"Call it TCP/2. One More Time." RFC9000 QUIC protocol.

Development API documentation.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
_gpgvdir=$(mktemp -d)
gpg2 --homedir="$_gpgvdir" --yes --output "$_gpgvdir/ring.gpg" --dearmor '%{SOURCE2}'
gpgv2 --homedir="$_gpgvdir" --keyring="$_gpgvdir/ring.gpg" '%{SOURCE1}' '%{SOURCE0}'
rm -rf "$_gpgvdir"
%if %{with docs}
install -p -m 755 %{SOURCE3} doc/
install -p -m 644 %{SOURCE4} doc/source/
install -p -m 644 %{SOURCE5} doc/source/
%endif

%build

autoreconf -fsi
export CFLAGS="${CFLAGS:-%{build_cflags}} -Wno-error=stringop-overflow"
%configure --with-gnutls --with-openssl --with-libev --disable-static --enable-werror
%make_build
%if %{with docs}
%make_build html
rm -f doc/build/html/.buildinfo
%endif
%install
%make_install
rm -f ${RPM_BUILD_ROOT}%{_libdir}/lib%{name}*.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build check
%files -f %{oreon_filedir}/main.list
%files -n ngtcp2-devel -f %{oreon_filedir}/ngtcp2-devel.list
%files -n ngtcp2-crypto-gnutls -f %{oreon_filedir}/ngtcp2-crypto-gnutls.list
%files -n ngtcp2-crypto-gnutls-devel -f %{oreon_filedir}/ngtcp2-crypto-gnutls-devel.list
%files -n ngtcp2-crypto-ossl -f %{oreon_filedir}/ngtcp2-crypto-ossl.list
%files -n ngtcp2-crypto-ossl-devel -f %{oreon_filedir}/ngtcp2-crypto-ossl-devel.list
%files -n ngtcp2-doc -f %{oreon_filedir}/ngtcp2-doc.list

%changelog

%autochangelog
