%global source0_hash 885898302a57aab948973e8b5d32a4229392b9fb2d986ab1d4ffd590e5ba90ec

%global pypi_name EasyProcess
%global dist_name %{py_dist_name %{pypi_name}}

Name:           python-easyprocess
Version:        1.1
Release:        11%{?dist}
Summary:        Easy to use Python subprocess interface

License:        BSD-2-Clause
URL:            https://github.com/ponty/EasyProcess
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
# For Tests
BuildRequires:  iputils
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-timeout}
BuildRequires:  %{py3_dist six}

%global _description %{expand:
EasyProcess is an easy to use python subprocess interface.}

%description %_description

%package -n     python3-easyprocess
Summary:        %{summary}

Requires:       %{py3_dist py}
%description -n python3-easyprocess %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Avoid circular dependency with PyVirtualDisplay
rm -f tests/test_fast/test_deadlock.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{dist_name}

%check
%pyproject_check_import

%pytest

%files -n python3-easyprocess -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
