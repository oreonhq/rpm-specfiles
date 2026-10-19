%global source0_hash 70cd7918dd07564241576e4ae8a4c5d007f87aa3d93589baded49022dc2cf27b
%global upstreamname rocm_bandwidth_test
%global rocm_release 6.4
%global rocm_patch 2
%global rocm_version %{rocm_release}.%{rocm_patch}
%bcond check 1
Name:       rocm-bandwidth-test
Version:    %{rocm_version}
Release:        1%{?dist}
Summary:        Bandwidth test for ROCm
License:    NCSA AND MIT
URL:        https://github.com/ROCm/%{upstreamname}
Source0:        https://github.com/ROCm/%{upstreamname}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
Source1:    LICENSE.NCSA.txt
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  rocm-runtime-devel
# /oreon:deps
%description
ROCm Bandwidth Test is designed to capture the performance
characteristics of buffer copying and kernel read and write
operations. The benchmark help screen shows various options
for initiating copy, read, and write operations. In
addition to this, you can also query the system topology in
terms of memory pools and their agents.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upstreamname}-rocm-%{version} -p1

# Remove execute permissions on docs
# https://github.com/ROCm/rocm_bandwidth_test/issues/128
chmod a-x LICENSE.txt
chmod a-x README.md
chmod a-x ROCmBandwithTest_UserGuide.pdf
cp %{SOURCE1} .

%build

%cmake
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_prefix}/share/doc/rocm-bandwidth-test/LICENSE.txt
%oreon_autofiles main

%check

%if %{with check}
%{_vpath_builddir}/rocm-bandwidth-test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
