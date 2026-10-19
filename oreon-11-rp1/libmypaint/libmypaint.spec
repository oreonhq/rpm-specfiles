%global source0_hash 741754f293f6b7668f941506da07cd7725629a793108bb31633fb6c3eae5315f
Name: libmypaint
Version: 1.6.1
Release:        16%{?dist}
Summary:        Library for making brush strokes
%global major %(ver=%{version}; echo ${ver%%%%.*})
%global minor %(ver=%{version}; ver=${ver#%major.}; echo ${ver%%%%.*})
%global micro %(ver=%{version}; ver=${ver#%major.%minor.}; echo ${ver%%%%.*})
License: ISC
URL: https://github.com/mypaint/libmypaint
Source0:        https://github.com/mypaint/libmypaint/releases/download/v%{version}/libmypaint-%{version}.tar.xz
Conflicts: mypaint < 1.3.0
# oreon:deps
BuildRequires:  babl-devel
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  json-c-devel
BuildRequires:  make
BuildRequires:  python3-breathe
BuildRequires:  python3-sphinx
# /oreon:deps
%description
This is a self-contained library containing the MyPaint brush engine.

%package devel
Summary: Development files for libmypaint
Requires: %{name}%{?isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: pkgconfig
%description devel
This package contains files needed for development with libmypaint.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n libmypaint-1.6.1

# Make sure the build uses python3
sed -i -e 's/python -c/python3 -c/g' configure

%build

%configure --enable-docs --enable-introspection=yes --disable-gegl
%make_build
%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -delete -print
%find_lang %{name}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libmypaint-devel -f %{oreon_filedir}/libmypaint-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.1-16
- Import
