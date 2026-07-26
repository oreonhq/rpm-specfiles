%global source0_hash 28e70fb3d56ed01c01eb3a4c099cc84315d2255869ecf08e9af32c41d4cbbf5d

%global rcver %{nil}

Name:		libgadu
Version:	1.12.2
Release:	31%{?dist}
Summary:	A Gadu-gadu protocol compatible communications library
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2
Source0:	https://github.com/wojtekka/libgadu/releases/download/%{version}%{?rcver}/libgadu-%{version}%{?rcver}.tar.gz
Patch0:	libgadu-1.12.2-gcc10.patch
Patch1:	%{name}-fix-openssl-symbol-clash.patch
URL:		http://libgadu.net/
BuildRequires:	curl-devel
BuildRequires:	doxygen
BuildRequires:	expat-devel
BuildRequires:	gcc
BuildRequires:	gnutls-devel
BuildRequires:	gsm-devel
BuildRequires:	libxml2-devel
BuildRequires:	make
# protobuf-c-1.0.0 is an incompatible update from 0.15
BuildRequires:	protobuf-c-devel >= 1.0.0
BuildRequires:	speex-devel
BuildRequires:	zlib-devel

%description
libgadu is intended to make it easy to add Gadu-Gadu communication
support to your software.

%description -l pl
libgadu umożliwia łatwe dodanie do różnych aplikacji komunikacji
bazującej na protokole Gadu-Gadu.

%package devel
Summary:	Libgadu development library
Summary(es):	Biblioteca de desarrollo de libgadu
Summary(pl):	Część biblioteki libgadu dla programistów
Requires:	libgadu = %{version}-%{release}
Requires:	pkgconfig

%description devel
The libgadu-devel package contains the header files necessary
to develop applications with libgadu.

%description devel -l pl
Pakiet libgadu-devel zawiera pliki nagłówkowe potrzebne
do kompilowania aplikacji korzystających z libgadu.

%package doc
Summary:	Libgadu library developer documentation
Summary(pl):	Dokumentacja biblioteki libgadu dla programistów
Requires:	libgadu = %{version}-%{release}
BuildArch:	noarch

%description doc
The libgadu-doc package contains the documentation for the
libgadu library.

%description doc -l pl
Pakiet libgadu-doc zawiera dokumentację biblioteki libgadu.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}%{?rcver}
%patch -P 0 -p1 -b .gcc10
%patch -P 1 -p1 -b .openssl

# bug 1126750: touch to force rebuild with protobuf-c-1.0.0 (incompatible with 0.15)
touch packets.proto

%build
%configure \
	--disable-silent-rules \
	--disable-static \
	--without-openssl \
	--with-pthread

make %{?_smp_mflags}

%install
make install INSTALL="install -p" DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%check
make check

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/libgadu.so.*

%files devel
%{_libdir}/libgadu.so
%{_includedir}/libgadu.h
%{_libdir}/pkgconfig/*

%files doc
%doc docs/protocol.html docs/html

%changelog
%autochangelog
