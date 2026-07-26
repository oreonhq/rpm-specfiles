%global source0_hash efbcaa658066e60bb7dde6c3ebe0b7147aeb466130461cb4784085d103490706

Name: libdatovka
Version: 0.7.2
Release: 2%{?dist}
Summary: Client library for accessing SOAP services of ISDS (Czech Data Boxes)

# Automatically converted from old format: LGPLv3+ and GPLv3+ - review is highly recommended.
License: LGPL-3.0-or-later AND GPL-3.0-or-later
URL: https://www.datovka.cz/
# Source0: https://secure.nic.cz/files/datove_schranky/%%{name}/%%{name}-%%{version}.tar.xz
Source0: https://datovka.nic.cz/%{name}/%{name}-%{version}.tar.xz
BuildRequires: dos2unix
BuildRequires: make
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: coreutils
BuildRequires: docbook-style-xsl
BuildRequires: libxslt-devel
BuildRequires: gettext-devel
BuildRequires: libxml2-devel
BuildRequires: libcurl-devel
BuildRequires: gpgme-devel
BuildRequires: libgcrypt-devel
BuildRequires: expat-devel
BuildRequires: gnupg2-smime
BuildRequires: gnutls-devel
# partial fix for the https://gitlab.nic.cz/datovka/libdatovka/-/issues/17
# --disable-fatalwarnings can be dropped once correctly fixed upstream
Patch0: libdatovka-0.2.1-gcc-12-build-fix.patch
# https://gitlab.nic.cz/datovka/datovka/-/issues/640
Patch1: libdatovka-0.5.0-test-drop-isds_load_erased_messages.patch

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

%check
make check %{?_smp_mflags}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README TODO NEWS
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*

%files doc
%doc client

%changelog
%autochangelog
