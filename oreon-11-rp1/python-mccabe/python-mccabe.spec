%global source0_hash 348e0240c33b60bbdf4e523192ef919f28cb2c3d7d5c7794f74009290f236325

Name:               python-mccabe
Version:            0.7.0
Release:            %autorelease
Summary:            McCabe complexity checker
License:            MIT
URL:                http://pypi.python.org/pypi/mccabe
Source:             %{pypi_source mccabe}
# Make hypothesis / hypothesmith truly optional
# https://github.com/PyCQA/mccabe/pull/92
Patch:              https://github.com/PyCQA/mccabe/pull/92.patch

BuildArch:          noarch
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-pytest

%global _description %{expand:
Ned's script to check McCabe complexity.

This module provides a plugin for flake8, the Python code
checker.}

%description %_description

%package -n python%{python3_pkgversion}-mccabe
Summary:            %{summary}

%description -n python%{python3_pkgversion}-mccabe %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n mccabe-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mccabe

%check
%pytest -r fEs

%files -n python%{python3_pkgversion}-mccabe -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
