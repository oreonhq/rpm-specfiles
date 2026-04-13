Summary:        Compatibility package for sdbus-cpp
Name:           sdbus-cpp
Version:        1.5.0
Release:        1%{?dist}
License:        LGPL-2.1-or-later
URL:            https://github.com/Kistler-Group/sdbus-cpp
BuildArch:      noarch

Source0:        LICENSE
Source1:        README.oreon

Provides:       sdbus-cpp = %{version}-%{release}

%description
Compatibility package to provide sdbus-cpp in Oreon repositories.
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
* Sun Apr 12 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.0-1
- Add sdbus-cpp compatibility package to Oreon repo
