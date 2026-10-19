%global source0_hash 3d44bde7921b3b9ec3ae4e3adca370438eccebc676456449b145d533b240d055
Name:           python-rfc3986-validator
Version:        0.1.1
Release:        1%{?dist}
Summary:        Pure python RFC3986 validator
License:        MIT
URL:            https://github.com/naimetti/rfc3986-validator
Source0:        https://files.pythonhosted.org/packages/source/r/rfc3986_validator/rfc3986_validator-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001_removing_pytest_runner_and_adding_test_requirements.patch
%global common_description %{expand:
%{summary}.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-rfc3986-validator = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-rfc3986-validator
Summary: %summary
%description -n python3-rfc3986-validator %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rfc3986-validator usr/lib/python3*/site-packages/rfc3986_validator* usr/lib64/python3*/site-packages/rfc3986_validator* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rfc3986_validator* usr/lib64/python3*/site-packages/rfc3986_validator* usr/bin/*

%check

PYTHONWARNINGS=ignore %pytest -vv tests
%files
%files -n python3-rfc3986-validator -f %{oreon_filedir}/python3-rfc3986-validator.list

%changelog

%autochangelog
