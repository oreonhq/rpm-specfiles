%global source0_hash fccff129486a63896746d5ecfc661fc3bac015767b0f51bd833f3f52f8e263db
%global htmldocdir %{_docdir}/dwgrep/html
Name:           dwgrep
Version:        0.4
Release:        1%{?dist}
Summary:        A tool for querying Dwarf (debuginfo) graphs
License:        GPL-3.0-or-later AND ( GPL-2.0-or-later OR LGPL-3.0-or-later )
URL:            http://pmachata.github.io/dwgrep/index.html
Source0:        https://github.com/pmachata/dwgrep/archive/%{version}/dwgrep-%{version}.tar.gz
Patch0:         include.patch
Patch1:         0001-cmake-modules-FindDWARF-Do-not-depend-on-libebl.patch
Patch2:         0002-CMakeLists-Declare-CMP0075-as-NEW.patch
Patch3:         0003-libzwerg-dwgrep-gendoc-Do-not-return-std-move.patch
Patch4:         0004-libzwerg-parser.yy-Use-new-define-based-declarations.patch
Patch5:         0005-libzwerg-pred_result-libzwerg-value-Add-ostream-oper.patch
Patch6:         0006-libzwerg-selector-Rewrite-assertion-on-value_type-co.patch
Patch7:         0007-CMakeLists-Bump-minimum-C-version.patch
Patch8:         0008-libzwerg-Drop-std-memory.hh-std-utility.hh.patch
Patch9:         0009-Make-deref_less-operator-const.patch
Patch10:        0010-Prefer-C-17-when-available.patch
Requires: libzwerg%{?_isa} = %{version}-%{release}
Provides:       bundled(jquery)
# oreon:deps
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  elfutils-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  make
BuildRequires:  python3-sphinx
# /oreon:deps
%description

Dwgrep is a tool, an associated language (called Zwerg) and a library
(libzwerg) for querying Dwarf (debuginfo) graphs.

You can think of dwgrep expressions as instructions describing a path
through a graph, with assertions about the type of nodes along the
way: that a node is of given type, that it has a given attribute,
etc. There are also means of expressing sub-conditions,
i.e. assertions that a given node is acceptable if a separate
expression matches (or does not match) a different path through the
graph.

%package -n libzwerg
Summary:        Library for querying Dwarf (debuginfo) graphs
%description -n libzwerg

Libzwerg contains implementation of the Zwerg query engine as well as
individual words of both Core and Dwarf vocabularies.

%ldconfig_scriptlets -n libzwerg

%package -n libzwerg-devel
Summary:        Headers and shared development libraries for libzwerg
Requires:       libzwerg%{?_isa} = %{version}-%{release}
Requires:       elfutils-devel%{?_isa}
%description -n libzwerg-devel
Headers and shared object symbolic links for the Boost C++ libraries.

%package doc
Summary:        HTML documentation for dwgrep and libzwerg
BuildArch:      noarch
%description doc

This package contains dwgrep-related documentation in the HTML
format. The documentation provides the same content as that on the
Boost web page (http://pmachata.github.io/dwgrep/).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n dwgrep-%{version}
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1
%patch 4 -p1
%patch 5 -p1
%patch 6 -p1
%patch 7 -p1
%patch 8 -p1
%patch 9 -p1
%patch 10 -p1

%build

mkdir build
pushd build
%cmake -B . -S ..
make %{?_smp_mflags}
make doc
popd
%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{htmldocdir}
cp -Rp doc/html/* $RPM_BUILD_ROOT%{htmldocdir}
popd
%oreon_autofiles libzwerg usr/*/lib*.so.*
%oreon_autofiles libzwerg-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd build
make test
popd
%files -f %{oreon_filedir}/main.list
%files -n libzwerg -f %{oreon_filedir}/libzwerg.list
%files -n libzwerg-devel -f %{oreon_filedir}/libzwerg-devel.list
%files -n dwgrep-doc -f %{oreon_filedir}/dwgrep-doc.list

%changelog

%autochangelog
