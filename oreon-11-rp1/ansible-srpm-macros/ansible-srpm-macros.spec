%global source0_hash none

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1-20.1
- Import
