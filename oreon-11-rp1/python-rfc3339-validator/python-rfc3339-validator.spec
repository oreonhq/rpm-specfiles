%global source0_hash 138a2abdf93304ad60530167e51d2dfb9549521a836871b88d7f4695d0022f6b
%bcond tests 1
Name:           python-rfc3339-validator
Version:        0.1.4
Release:        1%{?dist}
Summary:        Pure python RFC3339 validator
License:        MIT
URL:            https://github.com/naimetti/rfc3339-validator
Source0:        https://files.pythonhosted.org/packages/source/r/rfc3339_validator/rfc3339_validator-%{version}.tar.gz
BuildArch:      noarch
Patch:          rfc3339-validator-0.1.4-drop-pytest-runner.patch
%if %{with tests}
%endif
%global common_description %{expand:
A pure python RFC3339 validator.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rfc3339-validator = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-rfc3339-validator
Summary:        Pure python RFC3339 validator
%description -n python3-rfc3339-validator %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rfc3339-validator usr/lib/python3*/site-packages/rfc3339_validator* usr/lib64/python3*/site-packages/rfc3339_validator* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rfc3339_validator* usr/lib64/python3*/site-packages/rfc3339_validator* usr/bin/*

%check

%if %{with tests}
%pytest
%endif
%files
%files -n python3-rfc3339-validator -f %{oreon_filedir}/python3-rfc3339-validator.list

%changelog

%autochangelog
