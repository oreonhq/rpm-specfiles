%global source0_hash 41c41d986b0ef66635aa53abe51dfe0e09b1fb07a8803cbbdc861c3f82b6d15a

Name:           python3-saml
Version:        1.16.0
Release:        12%{?dist}
Summary:        Add SAML support to your Python software using this library

License:        MIT
URL:            https://pypi.python.org/pypi/%{name}
Source0:        https://github.com/SAML-Toolkits/python3-saml/archive/v%{version}/%{name}-v%{version}.tar.gz
Patch0001:      0001-keep-settings.patch

# Fix build-system in pyproject.toml: use poetry-core
Patch:          https://github.com/SAML-Toolkits/python3-saml/pull/341.patch

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros
%generate_buildrequires
%pyproject_buildrequires

%description
This toolkit lets you turn your Python application into a SP
(Service Provider) that can be connected to an IdP (Identity Provider).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files onelogin

%check
%pyproject_check_import

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
