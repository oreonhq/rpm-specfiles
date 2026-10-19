%global source0_hash 6146f837b27b11a6071e2148f7ae64521b4d8ad45325f998fe7b373137e418fb
%bcond_without libisds_enables_man
%bcond_without libisds_enables_net
%bcond_with libisds_enables_openssl
%bcond_without libisds_enables_test
Name:           libisds
Version:        0.11.2
Release:        15%{?dist}
Summary:        Library for accessing the Czech Data Boxes
License:        LGPL-3.0-or-later AND GPL-3.0-or-later
SourceLicense:  %{license} AND GPL-3.0-or-later AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-3.0-or-later WITH Libtool-exception AND GPL-2.0-or-later WITH Libtool-exception AND FSFULLR AND FSFUL AND X11 AND LicenseRef-Fedora-Public-Domain AND LicenseRef-Fedora-UltraPermissive
URL:            http://xpisar.wz.cz/%{name}/
Source0:        http://xpisar.wz.cz/%{name}/dist/%{name}-%{version}.tar.xz
Source1:        %{url}dist/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-E3F42FCE156830A80358E6E94FD1AEC3365AF7BF.gpg
Patch0:         libisds-0.11.2-tests-Do-not-send-multi-line-HTTP-headers-by-server.patch
Patch1:         libisds-0.11.2-Use-CURLOPT_XFERINFOFUNCTION-curl-option-if-availabl.patch
Patch2:         libisds-0.11.2-client-sendxmldoc-Fix-a-use-after-free-on-two-places.patch
Patch3:         libisds-0.11.2-Fix-building-with-libxml2-2.12.0.patch
Patch4:         libisds-0.11.2-Fix-using-CURLOPT_XFERINFOFUNCTION-curl-option.patch
Patch5:         libisds-0.11.2-Fix-passing-integers-to-curl_easy_setopt.patch
%if %{with libisds_enables_man}
%endif
%if %{with libisds_enables_net}
%endif
%if %{with libisds_enables_openssl}
%else
%endif
%if !%{with libisds_enables_openssl}
%endif
%if %{with libisds_enables_test}
%endif
%if !%{with libisds_enables_openssl}
Requires:       gnupg2-smime
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  docbook-style-xsl
BuildRequires:  expat-devel
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  glibc-gconv-extra
BuildRequires:  gnupg2
BuildRequires:  gnupg2-smime
BuildRequires:  gnutls-devel
BuildRequires:  gpgme-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  libxslt
BuildRequires:  make
# /oreon:deps
%description
This is a library for accessing ISDS (Informační systém datových schránek /
Data Box Information System) SOAP services as defined in Czech ISDS Act
(300/2008 Coll.) and implied documents.

%package        devel
Summary:        Development files for %{name}
License:        LGPL-3.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libxml2-devel%{?_isa}
Requires:       pkgconfig%{?_isa}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
autoreconf -fi

%build

%configure \
%if %{with libisds_enables_man}
    --enable-doc \
%else
    --disable-doc \
%endif
    --disable-online-test \
%if %{with libisds_enables_openssl}
    --enable-openssl-backend \
%else
    --disable-openssl-backend \
%endif
    --disable-static \
%if %{with libisds_enables_test}
    --enable-test \
%else
    --disable-test \
%endif
%if %{with libisds_enables_net}
    --with-libcurl \
%else
    --without-libcurl \
%endif
    --enable-curlreauthorizationbug
%{make_build}
%check

make check %{?_smp_mflags}
%install
%{make_install}
find %{buildroot} -name '*.la' -delete
%find_lang %{name}
rm -rf client/.deps client/Makefile{,.in}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libisds-devel -f %{oreon_filedir}/libisds-devel.list

%changelog

%autochangelog
