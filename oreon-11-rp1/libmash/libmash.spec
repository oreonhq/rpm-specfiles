%global source0_hash fd4089e2974a1a57f9ba209a0a47924ed157da9fc9a3d65f68a6b9fdca353ccc
Summary:        A library for using real 3D models within a Clutter scene
Name: libmash
Version: 0.2.0
Release:        42%{?dist}
URL: http://clutter-project.github.com/mash/
Source0:        https://github.com/downloads/clutter-project/mash/mash-%{version}.tar.xz
Patch0:		0001-Use-the-system-version-of-rply-if-available.patch
License: LicenseRef-Callaway-LGPLv2+
# oreon:deps
BuildRequires:  clutter-devel
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  rply-devel
# /oreon:deps
%description
Mash is a small library for using real 3D models within a Clutter
scene. Models can be exported from Blender or other 3D modeling
software as PLY files and then used as actors. It also supports a
lighting model with animatable lights.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
%description devel
This package contains libraries and header files needed for
development of programs using %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mash-%{version}
#%patch0 -p1 -b .use-system-rply

%build

autoconf
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libmash-devel -f %{oreon_filedir}/libmash-devel.list

%changelog

%autochangelog
