%global source0_hash cc053ac67e8ac4bb992f258fd94f275a7872df959f6a87763965feabfdcc9465
Name:           spandsp
Summary:        A DSP library for telephony
Version:        0.0.6
Release:        1%{?dist}
License:        LGPL-2.1-only AND GPL-2.0-only
URL:            https://www.soft-switch.org
Source0:        https://web.archive.org/web/2020id_/https://www.soft-switch.org/downloads/spandsp/spandsp-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-style-xsl
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  libxslt
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n spandsp-devel -f %{oreon_filedir}/spandsp-devel.list
%files -n spandsp-apidoc -f %{oreon_filedir}/spandsp-apidoc.list
