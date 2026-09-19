%global source0_hash 42d07de90de63e83762828028bfd56d19906a18f7c951ef6eef3e9ad48a3071d

%global srcname autopage

# Macros for pyproject (Fedora) vs. setup.py (CentOS)
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 10
%bcond_without pyproject
%else
%bcond_with pyproject
%endif

# Macros for disabling tests on CentOS 7
%if 0%{?el7}
%bcond_with enable_tests
%else
%bcond_without enable_tests
%endif

Name:           python-%{srcname}
Version:        0.6.0
Release:        1%{?dist}
Summary:        A Python library to provide automatic paging for console output
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.python.org/pypi/autopage
Source0:        %{pypi_source}
Source1:        setup.py

BuildArch:      noarch

%global _description %{expand:
Autopage is a Python library to provide automatic paging for console output.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with pyproject}
BuildRequires:  pyproject-rpm-macros
%else
%if %{with enable_tests}
BuildRequires:  %{py3_dist fixtures}
BuildRequires:  %{py3_dist fixtures[streams]}
%endif
%endif

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%if %{with pyproject}
%generate_buildrequires
%pyproject_buildrequires -t
%else
cp %{SOURCE1} ./
%endif

%build
%if %{with pyproject}
%pyproject_wheel
%else
%py3_build
%endif

%install
%if %{with pyproject}
%pyproject_install
%pyproject_save_files autopage
%else
%py3_install
%endif

%check
%if %{with enable_tests}
%if %{with pyproject}
%tox
%else
%{python3} setup.py test
%endif
%endif

%if %{with pyproject}
%files -n python3-%{srcname} -f %{pyproject_files}
%else
%files -n python3-%{srcname}
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%endif
%license LICENSE
%doc README.md

%changelog
%autochangelog
