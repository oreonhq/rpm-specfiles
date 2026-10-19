%global source0_hash 84bfc4daab9e466193540c3665eee42b2cf4d24e3f38fc3e8d1e0a2bebe3b8f1
%global xfceversion 4.20
%global namespc Libxfce4util
Name:           libxfce4util
Version:        4.20.1
Release:        1%{?dist}
Summary:        Utility library for the Xfce4 desktop environment
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.xfce.org/
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  vala
# /oreon:deps
%description
This package includes basic utility non-GUI functions for Xfce4.

%package devel
Summary: Developpment tools for libxfce4util library
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel
Requires: gtk3-devel
Requires: pkgconfig
%description devel
This package includes static libraries and header files for the
libxfce4util library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
export LD_LIBRARY_PATH="`pwd`/libxfce4util/.libs"
%make_build
%install
%make_install
chmod 755 %{buildroot}/%{_libdir}/*.so
rm -f %{buildroot}%{_libdir}/*.la
%find_lang %{name}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libxfce4util-devel -f %{oreon_filedir}/libxfce4util-devel.list

%changelog

%autochangelog
