%global source0_hash fccff129486a63896746d5ecfc661fc3bac015767b0f51bd833f3f52f8e263db

%global htmldocdir %{_docdir}/dwgrep/html

Name:           dwgrep
Version:        0.4
Release:        24%{?dist}
Summary:        A tool for querying Dwarf (debuginfo) graphs

# Automatically converted from old format: GPLv3+ and (GPLv2+ or LGPLv3+) - review is highly recommended.
License:        GPL-3.0-or-later AND ( GPL-2.0-or-later OR LGPL-3.0-or-later )
URL:            http://pmachata.github.io/dwgrep/index.html
Source0:        https://github.com/pmachata/dwgrep/archive/%{version}/dwgrep-%{version}.tar.gz

Patch0:         include.patch
# Upstream commit a6443a883650 ("cmake/modules/FindDWARF: Do not depend on libebl")
# https://bugzilla.redhat.com/show_bug.cgi?id=1799294
Patch1:         0001-cmake-modules-FindDWARF-Do-not-depend-on-libebl.patch
# Upstream commit 2157fb8e1d36 ("CMakeLists: Declare CMP0075 as NEW")
Patch2:         0002-CMakeLists-Declare-CMP0075-as-NEW.patch
# Upstream commit bed210af1278 ("libzwerg/dwgrep-gendoc: Do not return std::move")
Patch3:         0003-libzwerg-dwgrep-gendoc-Do-not-return-std-move.patch
# Upstream commit 1475b6f2fcc0 ("libzwerg/parser.yy: Use new %%define-based declarations for Bison")
Patch4:         0004-libzwerg-parser.yy-Use-new-define-based-declarations.patch
# Upstream commit fa7830f5f27f ("libzwerg/pred_result, libzwerg/value: Add ostream operators"
Patch5:         0005-libzwerg-pred_result-libzwerg-value-Add-ostream-oper.patch
# Upstream commit b2c296979046 ("libzwerg/selector: Rewrite assertion on value_type::code() return type"
Patch6:         0006-libzwerg-selector-Rewrite-assertion-on-value_type-co.patch
# Upstream commit 81597f312b22 ("CMakeLists: Bump minimum C++ version")
# https://bugzilla.redhat.com/show_bug.cgi?id=2225763
Patch7:         0007-CMakeLists-Bump-minimum-C-version.patch
# Upstream commit 11721b78b67e ("libzwerg: Drop std-memory.hh, std-utility.hh")
# One hunk dropped because it's not applicable to 0.4.
Patch8:         0008-libzwerg-Drop-std-memory.hh-std-utility.hh.patch
# Prefer C++17 when available, as required for GoogleTest 1.17
# https://github.com/pmachata/dwgrep/pull/44
# * Make deref_less::operator() const. For C++17 compatibility.
Patch9:         0009-Make-deref_less-operator-const.patch
# * Prefer C++17 when available. GoogleTest 1.17 requires C++17.
Patch10:        0010-Prefer-C-17-when-available.patch

Requires: libzwerg%{?_isa} = %{version}-%{release}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  elfutils-devel
BuildRequires:  flex
BuildRequires:  gtest-devel
BuildRequires:  python3-sphinx
BuildRequires:  make

# Sphinx-generated documentation apparently bundles jquery.  An
# exception is granted for bundling jquery in particular.
# https://fedorahosted.org/fpc/ticket/408
Provides:       bundled(jquery)

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

# We carry HTML documentation in a separate -doc subpackage.  However,
# we would still like the documentation to be installed to
# /usr/share/dwgrep as opposed to /usr/shared/dwgrep-doc.  So install
# it here by hand, and below in %%files, have HTML be owned by the doc
# subpackage and exclude it from the main package.
mkdir -p $RPM_BUILD_ROOT%{htmldocdir}
cp -Rp doc/html/* $RPM_BUILD_ROOT%{htmldocdir}

popd

%check
pushd build
make test
popd

%files
%doc NEWS README
%exclude %{htmldocdir}
%license COPYING COPYING-LGPLV3
%{_bindir}/dwgrep
%{_mandir}/man1/dwgrep.1*

%files doc
# Both -doc subpackage and main package should own the documentation
# package, because both put files in there.
%dir %{_docdir}/dwgrep
%{htmldocdir}

%files -n libzwerg
%license COPYING COPYING-LGPLV3
%{_libdir}/libzwerg.so.0.1

%files -n libzwerg-devel
# N.B.: COPYING* brought in by the libzwerg dependency.
%dir %{_includedir}/libzwerg
%{_includedir}/libzwerg/libzwerg.h
%{_includedir}/libzwerg/libzwerg-dw.h
%{_libdir}/libzwerg.so

%changelog
%autochangelog
