%global source0_hash fdf1e08392d3645d64696c5de7c116a1ea7ff3c70f19c0cb46c9eece7c00062c

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
%global upstreamname rocminfo
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%bcond_with compat
%if %{with compat}
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_skip_rpath OFF
%global pkg_rpath %{_prefix}/lib64/rocm/rocm-%{rocm_release}/lib
%global pkg_suffix -%{rocm_release}
%else
%global pkg_prefix %{_prefix}
%global pkg_skip_rpath ON
%global pkg_rpath %{nil}
%global pkg_suffix %{nil}
%endif
%global pkg_name rocminfo%{pkg_suffix}

Name:       %{pkg_name}
Version:    %{rocm_version}
Release:    4%{?dist}
Summary:    ROCm system info utility

License:    NCSA
URL:        https://github.com/ROCm/rocminfo
Source0:    %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
Patch0:     0001-adjust-CMAKE_CXX_FLAGS.patch

ExclusiveArch:  x86_64

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  rocm-runtime%{pkg_suffix}-devel
BuildRequires:  python3-devel

# rocminfo calls lsmod to check the kernel mode driver status
Requires:       kmod

%description
ROCm system info utility

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upstreamname}-rocm-%{version} -p1

%if 0%{?fedora} || 0%{?rhel}
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python3} rocm_agent_enumerator
%else
# suse
sed -i -e 's@/usr/bin/env python3@/usr/bin/python3@' rocm_agent_enumerator
%endif

%build
%cmake \
    -DROCM_DIR=%{pkg_prefix} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_INSTALL_RPATH=%{pkg_rpath} \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_SKIP_INSTALL_RPATH=%{pkg_skip_rpath}

%cmake_build

%install
%cmake_install

#FIXME:
chmod 755 %{buildroot}%{pkg_prefix}/bin/*

# Extra licenses
# Fedora
rm -f %{buildroot}%{pkg_prefix}/share/doc/*/License.txt
# OpenSUSE
rm -f %{buildroot}%{pkg_prefix}/share/doc/*/*/License.txt

%files
%doc README.md
%license License.txt
%{pkg_prefix}/bin/rocm_agent_enumerator
%{pkg_prefix}/bin/rocminfo

%changelog
%autochangelog
