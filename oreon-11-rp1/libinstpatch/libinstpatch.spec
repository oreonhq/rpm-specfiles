# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7edb57f29b475711ac2c0046262d5df0e4c2b9ddbc1b448605a2bb16c94b303d
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond introspection 0

%if 0%{?oreon}
%bcond ctest 0
%else
%bcond ctest %{undefined rhel}
%endif
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le ppc64p7 s390 s390x %{arm} aarch64 riscv64
%global arch_has_asan 1
%endif

Name:           libinstpatch
Version:        1.1.8
%global api_version 1.0
%global so_version 2
Release:        %{autorelease}
Summary:        Instrument file software library

URL:            http://www.swamiproject.org/
License:        LGPL-2.1-only AND LicenseRef-Fedora-Public-Domain
SourceLicense:  %{license} AND GPL-2.0-only

%global forgeurl https://github.com/swami/libinstpatch
Source0:        %{forgeurl}/archive/v%{version}/libinstpatch-%{version}.tar.gz

BuildSystem:    cmake
BuildOption(conf): -DGTKDOC_ENABLED:BOOL=ON
BuildOption(conf): -DINTROSPECTION_ENABLED:BOOL=%{with introspection}

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(gtk-doc)
%if %{with introspection}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
%endif
%if %{with ctest}
BuildRequires:  fluid-soundfont-gm
%if 0%{?arch_has_asan}
BuildRequires:  libasan
%endif
%endif

Provides:       bundled(md5-plumb)

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

%prep -a
find examples -type f -name '*.py' -print -delete

sed --regexp-extended --in-place \
    's/([" ])-Wfatal-errors([" ])/\1\2/' CMakeLists.txt

%if %{with ctest}
%build -a
mkdir --parents %{_vpath_builddir}/test-app
${CC} -c test-app/src/main.c -o %{_vpath_builddir}/test-app/main.o \
    ${CFLAGS} %{?arch_has_asan:-fsanitize=address} -I%{_vpath_builddir} -I. \
    $(pkg-config --cflags glib-2.0 gobject-2.0)
${CC} -o %{_vpath_builddir}/test-app/test_instpa_a \
    %{_vpath_builddir}/test-app/main.o %{?arch_has_asan:-fsanitize=address} \
    ${LDFLAGS} -L%{_vpath_builddir}/libinstpatch \
    -linstpatch-%{api_version} $(pkg-config --libs glib-2.0 gobject-2.0)

%check
LD_LIBRARY_PATH=%{_vpath_builddir}/libinstpatch \
    %{_vpath_builddir}/test-app/test_instpa_a
%endif

%files
%license COPYING
%{_libdir}/libinstpatch-%{api_version}.so.%{so_version}{,.*}

%files devel
%{_includedir}/libinstpatch-%{so_version}/
%{_libdir}/libinstpatch-%{api_version}.so
%{_libdir}/pkgconfig/libinstpatch-%{api_version}.pc

%files doc
%license COPYING
%doc ABOUT-NLS
%doc AUTHORS
%doc ChangeLog
%doc README.md
%doc TODO.tasks
%doc examples/
%doc %{_vpath_builddir}/docs/reference/html/

%changelog
%autochangelog
