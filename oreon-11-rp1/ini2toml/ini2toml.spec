%global source0_hash d619139b1b9a92a92a56cd2f24a4fb31bf10a1b75c2968d8fe8f0ed3af5d64ce
Name:           ini2toml
Version:        0.15
Release:        1%{?dist}
Summary:        Automatic conversion of .ini/.cfg files to TOML equivalents
License:        MPL-2.0
URL:            https://github.com/abravalheri/ini2toml/
Source0:        https://files.pythonhosted.org/packages/source/i/ini2toml/ini2toml-%{version}.tar.gz
BuildArch:      noarch
%py_provides python3-ini2toml
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 46.1.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 5
Requires:       python3-ini2toml = %{version}-%{release}
# /oreon:deps
%description

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ini2toml-%{version}

# Remove the coverage cmd arguments from pytest
sed -Ei '/(-|pytest)-cov(-report)?/d' setup.cfg

# Remove test dependency on validate-pyproject, not yet packaged
# Tests requiring it are excluded in %%check
sed -i '/validate-pyproject/d' setup.cfg

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pyproject_check_import
%pytest -vv --ignore tests/test_examples.py --deselect tests/test_cli.py::test_auto_formatting
%files

%changelog

%autochangelog
