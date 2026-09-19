%global source0_hash 524b7bf4c678d6b7192caf202533f0d9abe84c59b8ba5e579a47258bb1a62efc

#
# Copyright Fedora Project Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
%global upstreamname rocm-core
%global rocm_release 7.1
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}/
%global pkg_suffix -%{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif
%if 0%{?suse_version}
# 15.6
# rocm-core.x86_64: E: shlib-policy-name-error (Badness: 10000) librocm-core1
# Your package contains a single shared library but is not named after its SONAME.
%global core_name librocm-core1%{pkg_suffix}
%else
%global core_name rocm-core%{pkg_suffix}
%endif

Name:           %{core_name}
Version:        %{rocm_version}
Release:        4%{?dist}
Summary:        A utility to get the ROCm release version
License:        MIT
URL:            https://github.com/ROCm/rocm-systems
Source0:        %{url}/releases/download/rocm-%{version}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

Provides:       rocm-core = %{version}-%{release}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
%{summary}

%if 0%{?suse_version}
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       rocm-core%{pkg_suffix}-devel = %{version}-%{release}

%description devel
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstreamname}

%build
%cmake \
    -DROCM_VERSION=%{rocm_version} \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix}

%cmake_build

%install
%cmake_install

rm -rf %{buildroot}/%{pkg_prefix}/.info
rm -rf %{buildroot}/%{pkg_prefix}/%{pkg_libdir}/rocmmod
# Extra licenses
# Fedora
rm -f %{buildroot}/%{pkg_prefix}/share/doc/*/LICENSE.md
# OpenSUSE
rm -f %{buildroot}/%{pkg_prefix}/share/doc/*/*/LICENSE.md

# Use the system include path
mv  %{buildroot}/%{pkg_prefix}/include/rocm-core/*.h %{buildroot}/%{pkg_prefix}/include/
rm -rf %{buildroot}/%{pkg_prefix}/include/rocm-core

find %{buildroot} -type f -name 'runpath_to_rpath.py' -exec rm {} \;

%files
%doc README.md
%license LICENSE.md
%{pkg_prefix}/%{pkg_libdir}/librocm-core.so.*

%files devel
%{pkg_prefix}/include/*.h
%{pkg_prefix}/%{pkg_libdir}/librocm-core.so
%{pkg_prefix}/%{pkg_libdir}/cmake/rocm-core/

%changelog
%autochangelog
