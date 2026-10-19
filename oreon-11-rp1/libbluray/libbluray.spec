%global source0_hash 77937baf07eadda4b2b311cf3af4c50269d2ea3165041f5843d96476c4c92777
%ifarch %{java_arches}
%global build_bdj 1
%else
%global build_bdj 0
%endif
Name:           libbluray
Version:        1.4.0
Release:        3%{?dist}
Summary:        Library to access Blu-Ray disks for video playback
License:        LGPL-2.0-or-later
URL:            https://www.videolan.org/developers/libbluray.html
Source0:        https://download.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.xz
Patch0:        libbluray-0.8.0-no_doxygen_timestamp.patch
Patch1:        libbluray-1.4.0-java_23_support.patch
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  libudfread-devel
BuildRequires:  libxml2-devel
BuildRequires:  meson
BuildRequires:  texlive-latex
# /oreon:deps
%description
This package is aiming to provide a full portable free open source Blu-Ray
library, which can be plugged into popular media players to allow full Blu-Ray
navigation and playback on Linux. It will eventually be compatible with all
current titles, and will be easily portable and embeddable in standard players
such as MPlayer and VLC.

%package        utils
Summary:        Test utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    utils
The %{name}-utils package contains test utilities for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1 -b .no_timestamp
%patch -P1 -p1 -b .java_23

rm -rf contrib/libudfread

%build

%meson \
  --default-library=shared \
  -Dbdj_jar=disabled \
  -Denable_docs=true \
  -Denable_devtools=true \
  -Denable_examples=true
%meson_build
%install
%meson_install
mv %{buildroot}%{_docdir}/%{name}/html .
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libbluray-utils -f %{oreon_filedir}/libbluray-utils.list
%files -n libbluray-devel -f %{oreon_filedir}/libbluray-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.0-3
- Import
