%global source0_hash f7e40862aab66b7c8fd02f692bccffd5589d11b772b02e46614abe06284fea7e

%global archive_name ansible-inventory-grapher
%global lib_name ansibleinventorygrapher

Name:           %{archive_name}
Version:        2.6.0
Release:        9%{?dist}
Summary:        Creates graphs representing ansible inventory

License:        GPL-3.0-or-later
URL:            https://github.com/willthames/ansible-inventory-grapher
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%global _description\
ansible-inventory-grapher creates a dot file suitable for use by graphviz.\

%description %_description

%package -n python3-%{archive_name}
Summary:        %summary
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  (ansible-core or ansible)
Requires:       (ansible-core or ansible)

%description  -n python3-%{archive_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{lib_name}
ln -sr %{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}-3

%check
%pytest -vv -k test_vault_ids

%files -n python3-%{archive_name} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-3

%changelog
%autochangelog
