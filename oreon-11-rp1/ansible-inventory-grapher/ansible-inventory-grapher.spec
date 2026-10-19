%global source0_hash f7e40862aab66b7c8fd02f692bccffd5589d11b772b02e46614abe06284fea7e
%global archive_name ansible-inventory-grapher
%global lib_name ansibleinventorygrapher
Name:           %{archive_name}
Version:        2.6.0
Release:        1%{?dist}
Summary:        Creates graphs representing ansible inventory
License:        GPL-3.0-or-later
URL:            https://github.com/willthames/ansible-inventory-grapher
Source0:        https://github.com/willthames/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ansible-inventory-grapher = %{version}-%{release}
# /oreon:deps
%package -n       python3-ansible-inventory-grapher+dev
Summary:        Metapackage for python3-ansible-inventory-grapher dev extras
Requires:       python3-ansible-inventory-grapher = %{version}-%{release}
Provides:       python3dist(ansible-inventory-grapher[dev]) = %{version}-%{release}

%description -n python3-ansible-inventory-grapher+dev
Metapackage for python3-ansible-inventory-grapher dev extras.

%description
Creates graphs representing ansible inventory

%package -n python3-%{archive_name}
Summary:        %summary
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  (ansible-core or ansible)
Requires:       (ansible-core or ansible)
%description  -n python3-%{archive_name}
Creates graphs representing ansible inventory

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
ln -sr %{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}-3
%oreon_autofiles python3-ansible-inventory-grapher usr/lib/python3*/site-packages/ansible_inventory_grapher* usr/lib64/python3*/site-packages/ansible_inventory_grapher* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ansible_inventory_grapher* usr/lib64/python3*/site-packages/ansible_inventory_grapher* usr/bin/*

%check

%pytest -vv -k test_vault_ids
%files
%files -n python3-ansible-inventory-grapher -f %{oreon_filedir}/python3-ansible-inventory-grapher.list

%changelog

%autochangelog
