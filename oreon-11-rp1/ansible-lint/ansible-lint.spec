%global source0_hash 022cd8102d06b286147d5ce6e999349bbe6619f907d72ec71ae55dbc4a64b7b9

%global archive_name ansible-lint
%global lib_name ansiblelint

Name:           %{archive_name}
Epoch:          1
Version:        26.1.1
Release:        1%{?dist}
Summary:        Best practices checker for Ansible

# README file says its just GPLv3
License:        GPL-3.0-only
URL:            https://github.com/ansible/ansible-lint
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{archive_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:	pyproject-rpm-macros
# for check section
BuildRequires:  python3dist(pytest)

%description
Checks playbooks for practices and behavior that could potentially be improved.

%package -n python3-%{archive_name}
Summary:        %{summary}
Obsoletes:      python2-%{archive_name} < 3.4.23-6
Provides:       %{archive_name} = %{version}-%{release}

# Finally fixing this https://bugzilla.redhat.com/show_bug.cgi?id=1949362
Requires:       /usr/bin/ansible

%description  -n python3-%{archive_name}
Python3 module for ansible-lint.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{archive_name}-%{version}

# Fedora's ansible-core is 2.18.9 version currently
sed -i '37d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
# On newer releases, which only have Python 3, you will get:
#   ansible-lint => Python 3
#   ansible-lint-3 => Python 3 (to avoid breaking anyone's scripts)
ln -sr %{buildroot}%{_bindir}/%{name}{,-3}
%pyproject_save_files %{lib_name}

%check
%pyproject_check_import

%files -n python3-%{archive_name} -f %{pyproject_files}
%doc README.md examples
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-3

%changelog
%autochangelog
