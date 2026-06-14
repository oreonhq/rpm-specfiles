%global source0_hash cc053ac67e8ac4bb992f258fd94f275a7872df959f6a87763965feabfdcc9465

Name:           spandsp
Summary:        A DSP library for telephony
Version:        0.0.6
Release:        1%{?dist}
License:        LGPL-2.1-only AND GPL-2.0-only
URL:            https://www.soft-switch.org
Source0:        https://www.soft-switch.org/downloads/spandsp/spandsp-%{version}.tar.gz

BuildRequires: make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  libxml2-devel
BuildRequires:  libtiff-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  doxygen
BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl

%description
SpanDSP is a library of DSP functions for telephony.

%package devel
Summary:        SpanDSP development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libtiff-devel%{?_isa}

%description devel
%{summary}.

%package apidoc
Summary:        SpanDSP API documentation

%description apidoc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup
rm -f test-data/local/lenna-colour.tif

%build
autoreconf -f -v -i
%configure --enable-doc --disable-static --disable-rpath
%make_build
find doc/api -type f | xargs touch -r configure

%install
%make_install
rm -vf %{buildroot}%{_libdir}/*.la
mkdir -p %{buildroot}%{_datadir}/%{name}

%files
%license COPYING
%doc DueDiligence ChangeLog AUTHORS NEWS README
%{_libdir}/lib%{name}.so.*
%{_datadir}/%{name}/

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files apidoc
%doc doc/api/html/*
