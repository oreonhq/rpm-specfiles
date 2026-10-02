%global source0_hash 48fd24e47b1af4159bd4a0ea5abe9c2ed9e280bef67d9a5ff9ab5b30de5ad58a

Name:       clpeak
Version:    3.0.0
Release:    1%{?dist}
Summary:    Find peak OpenCL capacities like bandwidth & compute
License:    Apache-2.0
URL:        https://github.com/krrishnarraj/%{name}
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: mesa-libGL-devel
BuildRequires: ocl-icd-devel
BuildRequires: opencl-headers

%description
A tool which profiles OpenCL devices to find their peak capacities like
bandwidth & compute.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
rm -v %{buildroot}/%{_datadir}/clpeak/LICENSE

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_bindir}/clpeak

%changelog
%autochangelog
