Name:           ansible-srpm-macros
Version:        1
Release:        20.1%{?dist}
Summary:        SRPM stage RPM packaging macros for Ansible collections

License:        GPL-3.0-or-later
URL:            https://github.com/ansible/ansible
Source0:        macros.ansible-srpm
Source1:        COPYING

BuildArch:      noarch

%description
This package provides SRPM-stage rpm automation to simplify the creation
of Ansible collections.

The rest of the automation is provided by the ansible-packaging package.

%prep
%autosetup -T -c
cp -a %{sources} .

%build
# Nothing to build

%install
install -Dpm0644 -t %{buildroot}%{_rpmmacrodir} %{SOURCE0}
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/licenses/%{name}/COPYING

%files
%license %{_datadir}/licenses/%{name}/COPYING
%{_rpmmacrodir}/macros.ansible-srpm
