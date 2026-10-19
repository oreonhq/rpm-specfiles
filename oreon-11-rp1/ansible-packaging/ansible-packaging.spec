%global source0_hash none
%global _docdir_fmt ansible-packaging
Name:           ansible-packaging
Version:        1
Release:        1%{?dist}
Summary:        RPM packaging macros and generators for Ansible collections
License:        GPL-3.0-or-later
Source0:        ansible-generator
Source1:        ansible.attr
Source2:        macros.ansible
Source3:        macros.ansible-srpm
Source4:        ansible_collection.py
Source100:      COPYING
Requires:       %{py3_dist pyyaml}
Requires:       ansible-core
Requires:       ansible-srpm-macros = %{version}-%{release}
Conflicts:      ansible < 2.9.27-3
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%description
%{summary}.

%package -n ansible-srpm-macros
Summary:        SRPM stage RPM packaging macros for Ansible collections
%description -n ansible-srpm-macros
%{summary}.

%package tests
Summary:        Dependencies for Ansible collection package unit tests
Requires:       %{name} = %{version}-%{release}
Requires:       /usr/bin/ansible-test
Requires:       %{py3_dist pytest}
Requires:       %{py3_dist pytest-mock}
Requires:       %{py3_dist pytest-xdist}
Requires:       (%{py3_dist pytest-forked} if ansible-core < 2.16~~)
Requires:       %{py3_dist pyyaml}
%description tests
This package contains the necessary dependencies to run unit tests for packaged
Ansible collections

%prep

%autosetup -T -c
cp -a %{sources} .

%build

%install
install -Dpm0644 -t %{buildroot}%{_fileattrsdir} ansible.attr
install -Dpm0644 -t %{buildroot}%{_rpmmacrodir}  macros.ansible
install -Dpm0644 -t %{buildroot}%{_rpmmacrodir}  macros.ansible-srpm
install -Dpm0755 -t %{buildroot}%{_rpmconfigdir} ansible-generator
install -Dpm0755 -t %{buildroot}%{_rpmconfigdir} ansible_collection.py
%oreon_autofiles ansible-srpm-macros usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ansible-packaging-tests usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

rpm_eval() {
    default_macros_path="$(rpm --showrc | grep 'Macro path' | awk -F ': ' '{print $2}')"
    rpm --macros="${default_macros_path}:%{buildroot}%{_rpmmacrodir}/macros.*" "$@"
}
errors() {
    error="error: %%ansible_collection_url: You must pass the collection namespace as the first arg and the collection name as the second"
    "$@" && exit 1
    "$@" |& grep -q "${error}"
}
echo "Ensure macro fails when only collection_namespace macro is defined"
errors rpm_eval -D 'collection_namespace cc' -E '%%ansible_collection_url'
echo
echo "Ensure macro fails when only collection_name macro is defined"
errors rpm_eval -D 'collection_name cc' -E '%%ansible_collection_url'
echo
echo "Ensure macro fails when second argument is missing"
errors rpm_eval -E '%%ansible_collection_url a'
echo
echo "Ensure macro fails when second argument is missing"
errors rpm_eval -D 'collection_name b' -E '%%ansible_collection_url a'
echo
echo "Ensure macro fails when neither the control macros nor macro arguments are passed"
errors rpm_eval -E '%%ansible_collection_url'
echo
echo
echo "Ensure macro works when both arguments are passed and no control macros are set"
[ "$(rpm_eval -E '%%ansible_collection_url community general')" = \
    "https://galaxy.ansible.com/ui/repo/published/community/general" ]
echo
echo "Ensure macro works with the control macros"
[ "$(rpm_eval -D 'collection_namespace ansible' -D 'collection_name posix' \
    -E '%%ansible_collection_url')" = \
    "https://galaxy.ansible.com/ui/repo/published/ansible/posix" ]
echo
echo "Ensure macro prefers the collection namespace and name passed as an argument over the control macros"
[ "$(rpm_eval -D 'collection_namespace ansible' -D 'collection_name posix' \
    -E '%%ansible_collection_url community general')" = \
    "https://galaxy.ansible.com/ui/repo/published/community/general" ]
%files -f %{oreon_filedir}/main.list
%files -n ansible-srpm-macros -f %{oreon_filedir}/ansible-srpm-macros.list
%files -n ansible-packaging-tests -f %{oreon_filedir}/ansible-packaging-tests.list

%changelog

%autochangelog
