%global source0_hash d1db5a74b79d8ce86c353dc3df9d2fd5c01dd6515784e8a8c11ebdc6c5120d2c

Name:		dt-schema
Version:	2026.04
Release:	1%{?dist}
Summary:	Tooling for devicetree validation using YAML and jsonschema
License:	BSD-2-Clause
URL:		http://devicetree.org/
Source0:	https://github.com/devicetree-org/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	gcc
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm+toml

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

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files dtschema

%check
%py3_check_import dtschema

%files -f %{pyproject_files}
%license LICENSE.txt
%{_bindir}/dt*

%changelog
%autochangelog
