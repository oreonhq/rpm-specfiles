%global source0_hash 1e3347c49714e19169e4bba47098962d1f05c717898c70e612aceae4c41cdc1c
Name: libdatovka
Version: 0.7.4
Release:        1%{?dist}
Summary:        Client library for accessing SOAP services of ISDS (Czech Data Boxes)
License: LGPL-3.0-or-later AND GPL-3.0-or-later
URL: https://www.datovka.cz/
Source0:        https://datovka.nic.cz/%{name}/%{name}-%{version}.tar.xz
Patch0: libdatovka-0.2.1-gcc-12-build-fix.patch
Patch1: libdatovka-0.5.0-test-drop-isds_load_erased_messages.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  coreutils
BuildRequires:  docbook-style-xsl
BuildRequires:  dos2unix
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gnupg2-smime
BuildRequires:  gnutls-devel
BuildRequires:  gpgme-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
# /oreon:deps
%description
Client library for accessing SOAP services of ISDS (Informační systém
datových schránek / Data Box Information System) as defined in Czech ISDS Act
(300/2008 Coll.) <http://portal.gov.cz/zakon/300/2008> and implied documents.

%package devel
Summary: Development files for libdatovka
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libxml2-devel%{?_isa}
Requires: pkgconfig%{?_isa}
%description devel
Development files for libdatovka.

%package doc
Summary:          Documentation files for libdatovka
Requires:         %{name} = %{version}-%{release}
BuildArch:        noarch
%description doc
Documentation files for libdatovka.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
dos2unix src/*.{c,h}

%build

autoreconf -fi
%configure \
  --enable-doc \
  --disable-online-test \
  --disable-static \
  --enable-test \
  --with-libcurl \
  --disable-fatalwarnings
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

make check %{?_smp_mflags}
%files -f %{oreon_filedir}/main.list
%files -n libdatovka-devel -f %{oreon_filedir}/libdatovka-devel.list
%files -n libdatovka-doc -f %{oreon_filedir}/libdatovka-doc.list

%changelog

%autochangelog
