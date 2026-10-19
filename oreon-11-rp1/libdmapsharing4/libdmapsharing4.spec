%global source0_hash 4ad60d9423434bca5f7aede10a0477668e852ea66091bb5c1fd2ef22afd01a40
Name: libdmapsharing4
Version: 3.9.14
Release:        1%{?dist}
Summary:        A DMAP client and server library
License: LGPL-2.1-or-later
URL: https://www.flyn.org/projects/libdmapsharing/
Source0:        https://www.flyn.org/projects/libdmapsharing/libdmapsharing-%{version}.tar.gz
# oreon:deps
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  glib2-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  libgee-devel
BuildRequires:  libsoup3-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  vala
# /oreon:deps
%description 
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.

%package devel
Summary: Libraries/include files for libdmapsharing
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: libdmapsharing4-vala < 3.9.3-3
Provides: libdmapsharing4-vala = %{version}-%{release}
%description devel
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.  This package provides the libraries, include files, and
other resources needed for developing applications using libdmapsharing.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libdmapsharing-%{version}

%build

%configure --disable-static --disable-tests --disable-check
make %{?_smp_mflags}
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/libdmapsharing-4.0.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libdmapsharing4-devel -f %{oreon_filedir}/libdmapsharing4-devel.list

%changelog

%autochangelog
