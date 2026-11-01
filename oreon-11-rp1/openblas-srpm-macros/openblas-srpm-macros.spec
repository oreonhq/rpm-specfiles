%global source0_hash 2de2df7d8176ba3a51926b1e1e38204d658ad6ca3b53ef3c381147ec1c5e37c2
%global debug_package %{nil}

Name: openblas-srpm-macros
Version: 2
Release: 1%{?dist}
Summary: OpenBLAS architecture macros
License: MIT
URL: https://www.openblas.net/
BuildArch: noarch
Source0: macros.openblas-srpm

BuildRequires: oreon-rpm-macros

%description
Architecture macros for OpenBLAS packages.

%prep
%oreon_sha256

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.openblas-srpm

%files
%{_rpmmacrodir}/macros.openblas-srpm
