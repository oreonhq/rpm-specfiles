%global source0_hash ad4d7cdae84fad530bb0df99df80f66bbaeec3263153e4950c43a3a5b90cdbd2
%global commit0 8e401543d3ecf65e3a3631c7a271793a4d356cb0
%global shortcommit0 %%(c=%%{commit0}; echo ${c:0:7})
%global snapdate 20260304
%global prjname abc
Name:           yosyshq-%{prjname}
Version:        0.63
Release:        1%{?dist}
Summary:        Sequential logic synthesis and formal verification
License:        MIT-Modern-Variant AND MIT AND BSD-2-Clause AND BSD-3-Clause
URL:            http://github.com/YosysHQ/%{prjname}
Source0:        https://github.com/YosysHQ/%{prjname}/archive/%{commit0}/%{prjname}-8e40154.tar.gz
Source1:        %{prjname}.1
Patch1:         0001-fedora-do-not-use-bundled-libraries.patch
Patch2:         0002-fedora-build-shared-instead-of-static-library.patch
Patch3:         0003-fedora-fix-minor-header-issue.patch
Patch4:         0004-fedora-set-soname-on-the-library.patch
Patch5:         0005-fedora-fix-sprintf-calls-that-may-overflow-their-buf.patch
Patch6:         0006-fedora-fix-out-of-bounds-array-access-in-gia-code-be.patch
Patch7:         0007-fedora-weaken-overzealous-assert.patch
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Provides:       %{prjname} = 1.01-40.%{version}.%{release}
Obsoletes:      %{prjname} < 1.01-41
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
ABC is a growing software system for synthesis and verification of
binary sequential logic circuits appearing in synchronous hardware
designs.  ABC combines scalable logic optimization based on And-Inverter
Graphs (AIGs), optimal-delay DAG-based technology mapping for look-up
tables and standard cells, and innovative algorithms for sequential
synthesis and verification.

ABC provides an experimental implementation of these algorithms and a
programming environment for building similar applications.  Future
development will focus on improving the algorithms and making most of
the packages stand-alone.  This will allow the user to customize ABC for
their needs as if it were a toolbox rather than a complete tool.

%package libs
Summary:        Library for sequential synthesis and verification
Provides:       bundled(cudd) = 2.4.2
Provides:       bundled(glucose)
Provides:       bundled(minisat2)
Provides:       bundled(satoko)
Provides:       %{prjname}-libs = 1.01-40.%{version}.%{release}
Obsoletes:      %{prjname}-libs < 1.01-41
%description libs
This package contains the core functionality of ABC as a shared library.

%package devel
Summary:        Headers and libraries for developing with ABC
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Provides:       %{prjname}-devel = 1.01-40.%{version}.%{release}
Obsoletes:      %{prjname}-devel < 1.01-41
%description devel
Headers and libraries for developing applications that use ABC.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{prjname}-%{commit0}

# Do not use the bundled bzip2 or zlib libraries
rm -rf lib src/misc/{bzlib,zlib}

# Set the version number in the man page
sed 's/@VERSION@/%{version} (%{gitdate})/' %{SOURCE1} > %{prjname}.1
touch -r %{SOURCE1} %{prjname}.1

# Do not override Fedora optimization flags
sed -i 's/ -O//' Makefile

%build

export CFLAGS='%{build_cflags} -DNDEBUG'
export CXXFLAGS='%{build_cxxflags} -DNDEBUG'
%ifarch s390x
CFLAGS="$CFLAGS -DEPD_BIG_ENDIAN"
CXXFLAGS="$CXXFLAGS -DEPD_BIG_ENDIAN"
%endif
export ABC_MAKE_VERBOSE=1
export ABC_USE_STDINT_H=1
%cmake -DCMAKE_SKIP_RPATH:BOOL=YES \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
	-DABC_SKIP_TESTS:BOOL=yes
%cmake_build
%install
cd %{_vpath_builddir}
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{prjname} %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
cp -pd lib%{prjname}.so* %{buildroot}%{_libdir}
cd -
cd src
mkdir -p %{buildroot}%{_includedir}/%{prjname}
tar -cf - $(find -O3 . -name \*.h) | \
  (cd %{buildroot}%{_includedir}/%{prjname}; tar -xf -)
cd -
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 %{prjname}.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n yosyshq-abc-libs -f %{oreon_filedir}/yosyshq-abc-libs.list
%files -n yosyshq-abc-devel -f %{oreon_filedir}/yosyshq-abc-devel.list

%changelog

%autochangelog
