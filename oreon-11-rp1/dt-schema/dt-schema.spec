%global source0_hash 559b7199805c15fc6135b1e2f2fe10caa3a4faac710a163024051103ac1044af
Name:		dt-schema
Version:	2026.09
Release:        1%{?dist}
Summary:        Tooling for devicetree validation using YAML and jsonschema
License:	BSD-2-Clause
URL:		http://devicetree.org/
Source0:        https://github.com/devicetree-org/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-dt-schema = %{version}-%{release}
# /oreon:deps
%description
This tool contains test code for devicetree schema validation using the
json-schema vocabulary. Schema files are written in YAML (a superset of
JSON), and operate on the YAML encoding of Devicetree data. Devicetree
data must be transcoded from DTS to YAML before being used by this tool.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Working with upstream to resolve.
sed -i 's/>=4.1.2,<4.18//'  pyproject.toml
sed -i 's/pylibfdt/libfdt/' pyproject.toml

%build

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%oreon_autofiles main

%check

%py3_check_import dtschema
%files

%changelog

%autochangelog
