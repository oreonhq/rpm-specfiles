Summary:        Compatibility package for pkcs11-helper
Name:           pkcs11-helper
Version:        1.30.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            https://github.com/OpenSC/pkcs11-helper
BuildArch:      noarch

Source0:        LICENSE
Source1:        README.oreon

Provides:       pkcs11-helper = %{version}-%{release}

%description
Compatibility package to provide pkcs11-helper in Oreon repositories.
This package intentionally ships metadata and documentation only.

%prep

%build

%install
install -d -m 0755 %{buildroot}%{_docdir}/%{name}
install -m 0644 %{SOURCE0} %{buildroot}%{_docdir}/%{name}/
install -m 0644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}/

%files
%license %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README.oreon

%changelog
* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.30.0-1
- Add pkcs11-helper compatibility package to Oreon repo
