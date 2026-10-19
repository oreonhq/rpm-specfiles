%global source0_hash d33a4fd24c72c2d08893f129d724adf725b93dae96c359e4f4e9f32573cc853b
Name:           inotify-tools
Version:        4.25.9.0
Release:        1%{?dist}
Summary:        Command line utilities for inotify
License:        GPL-2.0-only AND GPL-2.0-only WITH Linux-syscall-note AND LGPL-2.1-or-later
URL:            https://github.com/inotify-tools/inotify-tools
Source0:        https://github.com/inotify-tools/inotify-tools/archive/%{version}/inotify-tools-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
inotify-tools is a set of command-line programs for Linux providing
a simple interface to inotify. These programs can be used to monitor
and act upon filesystem events.

%package        devel
Summary:        Headers and libraries for building apps that use libinotifytools
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains headers and libraries required to build applications
that use the libinotifytools library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure \
        --disable-dependency-tracking \
        --disable-static \
        --enable-doxygen \
        --enable-fanotify
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
%make_build
%install
%make_install
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
rm -rf %{buildroot}/%{_datadir}/doc/
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n inotify-tools-devel -f %{oreon_filedir}/inotify-tools-devel.list

%changelog

%autochangelog
