Name: sgx-rpm-macros
Version: 1
Release: 4%{?dist}
License: MIT-0
Summary: RPM macros for working with the SGX SDK

Source0: macros.sgx
Source1: MIT-0

BuildArch: noarch

%description
RPM macros for working with the SGX SDK

%build
cp %{SOURCE1} MIT-0

%install
%__install -d %{buildroot}/%{_rpmmacrodir}/
cp %{SOURCE0} %{buildroot}/%{_rpmmacrodir}/

%files
%license MIT-0
%{_rpmmacrodir}/macros.sgx

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1-4
- Prepare for Oreon 11 (RP1)
