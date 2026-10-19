%global source0_hash b66935dc7d775f36b1d36267ac69d3687decf2a2f191b86747622b152ea83e06
%global date 20240202
%global commit 2213b76712c8e08d885482d117f904d570c990aa
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%bcond schroedinger 1
%bcond libdv 1
Summary:        Library for reading and writing Quicktime files
Name:       libquicktime
Version:    1.2.4^%{date}git%{shortcommit}
Release:        1%{?dist}
License:    GPL-2.0-or-later AND LGPL-2.1-or-later
URL:        http://libquicktime.sourceforge.net/
Source0:        https://sourceforge.net/code-snapshots/git/l/li/%{name}/git.git/%{name}-git-%{commit}.zip
Patch0:     %{name}-modern-c.patch
%ifnarch s390x
%endif
%{?with_libdv:BuildRequires:  libdv-devel}
%{?with_schroedinger:BuildRequires:  schroedinger-devel}
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  faad2-devel
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gtk2-devel
BuildRequires:  lame-devel
BuildRequires:  libGLU-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXt-devel
BuildRequires:  libXv-devel
BuildRequires:  libavc1394-devel
BuildRequires:  libdv-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libraw1394-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  schroedinger-devel
# /oreon:deps
%package utils
Summary:    Utilities for working with Quicktime files
Requires:   %{name}%{?_isa} = %{version}-%{release}
%package devel
Summary:    Development files for libquicktime
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   zlib-devel
%description
Libquicktime is based on the quicktime4linux library with several
enhancements. All 3rd-party libraries were removed from the
sourcetree. Instead, the systemwide installed libraries are detected
by the configure script. All original codecs were moved into
dynamically loadable modules, and new codecs are in
development. Libquicktime is source-compatible with
quicktime4linux. Special API extensions allow access to the codec
registry and more convenient processing of Audio and Video
data.

%description utils
Libquicktime is based on the quicktime4linux library with several
enhancements. This package contains utility programs and additional
tools, like a commandline player and a GTK configuration utility which
can configure the parameters of all installed codecs.

%description devel
Libquicktime is based on the quicktime4linux library with several
enhancements. This package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-git-%{commit}

%build

./autogen.sh
%configure \
    --disable-rpath \
    --disable-static \
    --enable-gpl \
    --with-cpuflags="$RPM_OPT_FLAGS" \
    %{?with_libdv:--with-libdv} \
    --without-doxygen \
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
rm -v %{buildroot}%{_libdir}/%{name}{,/lqt_*}.la
%find_lang %{name}
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libquicktime-utils -f %{oreon_filedir}/libquicktime-utils.list
%files -n libquicktime-devel -f %{oreon_filedir}/libquicktime-devel.list

%changelog

%autochangelog
