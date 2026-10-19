%global source1_hash de19d222d09e2171f47f8bbd6608e5648bd547c82543379bb8fb5ed2e379e141
%global source0_hash 2a9dfafac9593d3093c3f5fc611682e712f08816414f210344ea7b719c085ff5
%global rocm_release 7.1
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}
%global upstreamname amdsmi
%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix -%{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif
%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif
Name:       amdsmi%{pkg_suffix}
Version:    %{rocm_version}
Release:        1%{?dist}
Summary:        AMD System Management Interface
License:    NCSA AND MIT AND BSD-3-Clause
URL:        https://github.com/ROCm/%{upstreamname}
Source0:        https://github.com/ROCm/%{name}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{name}-%{version}.tar.gz
%global esmi_ver 4.2
Source1:    https://github.com/amd/esmi_ib_library/archive/refs/tags/esmi_pkg_ver-%{esmi_ver}.tar.gz
Patch1:     0002-option-use-system-gtest.patch
Patch2:     0003-test-client-includes-for-gcc-15.patch
Patch3:     0001-amdsmi-remove-unneeded-include-fileystem.patch
Patch4:     0001-Fix-compilation-with-libdrm-2.4.130.patch
ExclusiveArch: x86_64
%if %{with test}
%if 0%{?suse_version}
%else
%endif
%endif
Requires:      python3dist(pyyaml)
Provides: bundled(esmi_ib_library) = %{esmi_ver}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kernel-devel
BuildRequires:  libdrm-devel
BuildRequires:  python3-devel
# /oreon:deps
%description
The AMD System Management Interface Library, or AMD SMI library, is a C
library for Linux that provides a user space interface for applications
to monitor and control AMD devices.

%package devel
Summary: Libraries and headers for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libdrm-devel
%description test
%{summary}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upstreamname}-rocm-%{version} -p1
tar xf %{SOURCE1}
mv esmi_ib_library-* esmi_ib_library
# So we can pick up this license
mv esmi_ib_library/License.txt esmi_ib_library_License.txt 
# The esmi version check uses git tags, but we use tar's without git files.
# Just inject in the tag that we've pulled into the version check:
sed -i 's/NOT latest_esmi_tag/NOT "esmi_pkg_ver-%{esmi_ver}"/' CMakeLists.txt

# W: spurious-executable-perm /usr/share/doc/amdsmi/README.md
chmod a-x README.md

# /usr/libexec/amdsmi_cli/BDF.py:126: SyntaxWarning: invalid escape sequence '\.'
#   bdf_regex = "(?:[0-6]?[0-9a-fA-F]{1,4}:)?[0-2]?[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}\.[0-7]"
sed -i -e 's@bdf_regex = "@bdf_regex = r"@' amdsmi_cli/BDF.py

# Fix script shebang
sed -i -e 's@env python3@python3@' amdsmi_cli/*.py

# Install local gtests in same dir as tests
sed -i -e 's@${CPACK_PACKAGING_INSTALL_PREFIX}/lib@${SHARE_INSTALL_PREFIX}/tests@' tests/amd_smi_test/CMakeLists.txt

# fix cstdint include
# https://github.com/ROCm/amdsmi/issues/123
sed -i '/#include <unordered_set.*/a#include <cstdint>' rocm_smi/include/rocm_smi/rocm_smi_common.h

# fix iomanip include
# https://github.com/ROCm/amdsmi/issues/124
sed -i '/#include <string.*/a#include <iomanip>' tests/amd_smi_test/test_common.h

# Do not hardcode share dir
sed -i 's@set(SHARE_INSTALL_PREFIX@#set(SHARE_INSTALL_PREFIX@' CMakeLists.txt

%build

%cmake \
    -DBUILD_KERNEL_ASM_DIR=/usr/include/asm \
    -DBUILD_TESTS=%build_test \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_SKIP_INSTALL_RPATH=TRUE \
    -DSHARE_INSTALL_PREFIX=%{pkg_prefix}/share \
%if %{with test}
    -DUSE_SYSTEM_GTEST=On \
%endif
    %{nil}
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}/%{pkg_prefix}/lib/python%{python3_version}/site-packages
if [ -d %{buildroot}%{pkg_prefix}/share/amd_smi/amdsmi ]; then
    mv %{buildroot}%{pkg_prefix}/share/amd_smi/amdsmi %{buildroot}/%{pkg_prefix}/lib/python%{python3_version}/site-packages
    mv %{buildroot}%{pkg_prefix}/share/amd_smi/pyproject.toml %{buildroot}/%{pkg_prefix}/lib/python%{python3_version}/site-packages/amdsmi/
else
    mv %{buildroot}%{pkg_prefix}/share/amdsmi %{buildroot}/%{pkg_prefix}/lib/python%{python3_version}/site-packages
    mv %{buildroot}%{pkg_prefix}/share/pyproject.toml %{buildroot}/%{pkg_prefix}/lib/python%{python3_version}/site-packages/amdsmi/
fi
rm -rf %{buildroot}/%{pkg_prefix}/share/example
rm -rf %{buildroot}/%{pkg_prefix}/share/amd_smi/example
rm -rf %{buildroot}/%{pkg_prefix}/share/doc/amd_smi-asan/LICENSE.txt
rm -f %{buildroot}/%{pkg_prefix}/share/doc/amd-smi-lib/LICENSE.txt
rm -f %{buildroot}/%{pkg_prefix}/share/doc/amd-smi-lib/README.md
rm -rf %{buildroot}/%{pkg_prefix}/share/doc/amd-smi-lib/copyright
rm -f %{buildroot}%{pkg_prefix}/share/_version.py
rm -f %{buildroot}%{pkg_prefix}/share/amd_smi/_version.py
rm -f %{buildroot}%{pkg_prefix}/share/setup.py
rm -f %{buildroot}%{pkg_prefix}/share/amd_smi/setup.py
strip %{buildroot}/%{pkg_prefix}/lib/python%{python3_version}/site-packages/amdsmi/*.so
chmod a+x %{buildroot}/%{pkg_prefix}/libexec/amdsmi_cli/amdsmi_*.py
%if %{with test}
mkdir %{buildroot}%{pkg_prefix}/share/amdsmi
mv %{buildroot}%{pkg_prefix}/share/tests %{buildroot}%{pkg_prefix}/share/amdsmi/.
%oreon_autofiles amdsmi-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%if 0%{?suse_version}
%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%endif
%files -f %{oreon_filedir}/main.list
%files -n amdsmi-devel -f %{oreon_filedir}/amdsmi-devel.list

%changelog

%autochangelog
