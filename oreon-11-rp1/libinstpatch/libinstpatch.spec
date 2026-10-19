%global source0_hash b388ab6f843559fc2da94837c37dfd4cf5973cf7cc2a0ce3cb33260b81377e9f
%bcond introspection 0
Name:           libinstpatch
Version:        1.1.7
%global api_version 1.0
%global so_version 2
Release:        1%{?dist}
Summary:        Instrument file software library
URL:            http://www.swamiproject.org/
License:        LGPL-2.1-only AND LicenseRef-Fedora-Public-Domain
SourceLicense:  %{license} AND GPL-2.0-only
%global forgeurl https://github.com/swami/libinstpatch
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with introspection}
%endif
Provides:       bundled(md5-plumb)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(sndfile)
# /oreon:deps
%description
libInstPatch stands for lib-Instrument-Patch and is a library for processing
digital sample based MIDI instrument “patch” files. The types of files
libInstPatch supports are used for creating instrument sounds for wavetable
synthesis. libInstPatch provides an object framework (based on GObject) to load
patch files into, which can then be edited, converted, compressed and saved.

%package devel
Summary:        Development files for libinstpatch
License:        LGPL-2.1-only
Requires:       libinstpatch%{?_isa} = %{version}-%{release}
Requires:       glib2-devel%{?_isa}
Requires:       libsndfile-devel%{?_isa}
%description devel
The libinstpatch-devel package contains libraries and header files for
developing applications that use libinstpatch.

%package doc
Summary:        Documentation and examples for libinstpatch
BuildArch:      noarch
%description doc
The libinstpatch-doc package contains documentation and examples for
libinstpatch.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove example for nonexistent Python bindings
find examples -type f -name '*.py' -print -delete

%conf
%cmake \
    -DGTKDOC_ENABLED:BOOL=ON \
    -DINTROSPECTION_ENABLED:BOOL=\
%{?with_introspection:ON}%{!?with_introspection:OFF} \
    -GNinja

%build

%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libinstpatch-devel -f %{oreon_filedir}/libinstpatch-devel.list
%files -n libinstpatch-doc -f %{oreon_filedir}/libinstpatch-doc.list

%changelog

%autochangelog
