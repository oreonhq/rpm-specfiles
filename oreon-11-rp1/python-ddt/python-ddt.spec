%global source0_hash d215d6b083963013c4a19b1e4dcd6a96e80e43ab77519597a6acfcf2e9a3e04b
%bcond tests    1
Name:           python-ddt
Version:        1.7.2
Release:        1%{?dist}
Summary:        Python library to multiply test cases
License:        MIT
URL:            https://github.com/datadriventests/ddt
Source0:        https://files.pythonhosted.org/packages/source/d/ddt/ddt-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
%global common_description %{expand:
DDT (Data-Driven Tests) allows you to multiply one test case by running it with
different test data, and make it appear as multiple test cases.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ddt = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-ddt
Summary:        Python library to multiply test cases
%description -n python3-ddt %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ddt-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ddt usr/lib/python3*/site-packages/ddt* usr/lib64/python3*/site-packages/ddt* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ddt* usr/lib64/python3*/site-packages/ddt* usr/bin/*

%check

%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif
%files
%files -n python3-ddt -f %{oreon_filedir}/python3-ddt.list

%changelog

%autochangelog
