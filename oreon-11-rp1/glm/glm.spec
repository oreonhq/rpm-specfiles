%global source0_hash 6775e47231a446fd086d660ecc18bcd076531cfedd912fbd66e576b118607001
%global debug_package %{nil}
Name:           glm
Version:        1.0.3
Release:        1%{?dist}
Summary:        C++ mathematics library for graphics programming
License:        MIT
URL:            http://glm.g-truc.net/
Source0:        https://github.com/g-truc/glm/archive/refs/tags/%{version}.tar.gz#/glm-%{version}.tar.gz
Patch0:         glm-1.0.1-noarch.patch
Patch1:         glm-1.0.1-without-werror.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
GLM is a C++ library for doing mathematics operations
required in many OpenGL based applications. Its interface
has been designed to resemble the built-in matrix and vector
types of the OpenGL shading language.

%package        devel
Summary:        C++ mathematics library for graphics programming
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}
%description    devel
GLM is a C++ library for doing mathematics operations
required in many OpenGL based applications. Its interface
has been designed to resemble the built-in matrix and vector
types of the OpenGL shading language.

%{name}-devel is only required for building software that uses
the GLM library. Because GLM currently is a header-only library,
there is no matching run time package.

%package        doc
Summary:        Documentation for %{name}-devel
BuildArch:      noarch
%description    doc
The %{name}-doc package contains reference documentation and
a programming manual for the %{name}-devel package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# Some glm releases, like version 0.9.3.1, place contents of
# the source archive directly into the archive root. Others,
# like glm 0.9.3.2, place them into a single subdirectory.
# The former case is inconvenient, but it can be be
# compensated for with the -c option of the setup macro.
#
# When updating this package, take care to check if -c is
# needed for the particular version.
#
# Also it looks like some versions get shipped with a common
# directory in archive root, but with an unusual name for the
# directory. In this case, use the -n option of the setup macro.
%setup -q

# A couple of files had CRLF line-ends in them.
# Check with rpmlint after updating the package that we are not
# forgetting to convert line endings in some files.
#
# This release of glm seems to have shipped with no CRLF file
# endings at all, so these are commented out.
sed -i 's/\r//' readme.md
sed -i 's/\r//' CMakeLists.txt
sed -i 's/\r//' doc/api/doxygen.css
sed -i 's/\r//' doc/api/dynsections.js
sed -i 's/\r//' doc/api/jquery.js
sed -i 's/\r//' doc/api/tabs.css

# These are just for being able to apply the patch that
# was exported from git.
sed -i 's/\r//' glm/detail/setup.hpp
sed -i 's/\r//' glm/simd/platform.h
sed -i 's/\r//' test/core/core_setup_message.cpp

%patch 0 -p1
%patch 1 -p1

%build

export CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%{cmake} -DGLM_TEST_ENABLE=ON -DGLM_BUILD_LIBRARY=OFF -DCMAKE_INSTALL_DATAROOTDIR=%{_datadir}/cmake
%cmake_build
%check

export CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%ctest --output-on-failure -E 'test-gtc_packing'
%install
%cmake_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name CMakeLists.txt -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT%{_includedir}/%{name}/{CMakeFiles,libglm_shared.so}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n glm-devel -f %{oreon_filedir}/glm-devel.list
%files -n glm-doc -f %{oreon_filedir}/glm-doc.list

%changelog

%autochangelog
