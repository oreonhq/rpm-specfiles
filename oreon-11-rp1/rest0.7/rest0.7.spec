%global source0_hash 0513aad38e5d3cedd4ae3c551634e3be1b9baaa79775e53b2dba9456f15b01c9
Name:          rest0.7
Version:       0.9.1
Release:        1%{?dist}
Summary:        A library for access to RESTful web services
License:       LicenseRef-Callaway-LGPLv2
URL:           http://www.gnome.org
Source0:        http://download.gnome.org/sources/rest/0.8/rest-%{version}.tar.xz
Patch0:        rest-0.8.0-fix-the-XML-test.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  libsoup-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
# /oreon:deps
%description
This library was designed to make it easier to access web services that
claim to be "RESTful". A RESTful service should have urls that represent 
remote objects, which methods can then be called on. The majority of services 
don't actually adhere to this strict definition. Instead, their RESTful end 
point usually has an API that is just simpler to use compared to other types 
of APIs they may support (XML-RPC, for instance). It is this kind of API that 
this library is attempting to support.

This package contains librest API version 0.7.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Files for development with librest API version 0.7.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n rest-%{version}
%patch -P0 -p1

%build

autoreconf -vif
%configure --disable-static --enable-gtk-doc --enable-introspection=yes
make %{?_smp_mflags} V=1
%install
make install DESTDIR=%{buildroot} INSTALL='install -p'
find %{buildroot} -type f -name "*.la" -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n rest0.7-devel -f %{oreon_filedir}/rest0.7-devel.list

%changelog

%autochangelog
