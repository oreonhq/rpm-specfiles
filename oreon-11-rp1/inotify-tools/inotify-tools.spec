%global source0_hash 1dfa33f80b6797ce2f6c01f454fd486d30be4dca1b0c5c2ea9ba3c30a5c39855

Name:           inotify-tools
Version:        4.23.9.0
Release:        6%{?dist}
Summary:        Command line utilities for inotify

# GPL-2.0-only: the project as a whole
# GPL-2.0-only WITH Linux-syscall-note: libinotifytools/src/inotifytools/fanotify-dfid-name.h
# LGPL-2.1-or-later: libinotifytools/src/redblack.{cpp,h}
License:        GPL-2.0-only AND GPL-2.0-only WITH Linux-syscall-note AND LGPL-2.1-or-later
URL:            https://github.com/inotify-tools/inotify-tools
Source0:        https://github.com/inotify-tools/inotify-tools/archive/%{version}/inotify-tools-%{version}.tar.gz
Patch0:         too-many-args.patch

BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  make
BuildRequires:  libtool

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

%autosetup -p1

%build
./autogen.sh
%configure \
        --disable-dependency-tracking \
        --disable-static \
        --enable-doxygen \
        --enable-fanotify

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
# We'll install documentation in the proper place
rm -rf %{buildroot}/%{_datadir}/doc/

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING ChangeLog NEWS README.md
%{_bindir}/fsnotifywait
%{_bindir}/fsnotifywatch
%{_bindir}/inotifywait
%{_bindir}/inotifywatch
%{_libdir}/libinotifytools.so.*
%{_mandir}/man1/inotifywait.1*
%{_mandir}/man1/inotifywatch.1*
%{_mandir}/man1/fsnotifywait.1*
%{_mandir}/man1/fsnotifywatch.1*

%files devel
%doc libinotifytools/src/doc/html/*
%dir %{_includedir}/inotifytools/
%{_includedir}/inotifytools/inotify.h
%{_includedir}/inotifytools/inotify-nosys.h
%{_includedir}/inotifytools/inotifytools.h
%{_includedir}/inotifytools/fanotify-dfid-name.h
%{_includedir}/inotifytools/fanotify.h
%{_libdir}/libinotifytools.so

%changelog
%autochangelog
