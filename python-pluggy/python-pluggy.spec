# Turn the tests off when bootstrapping Python, because pytest requires pluggy
%bcond tests 1

Name:           python-pluggy
Version:        1.6.0
Release:        5%{?dist}
Summary:        The plugin manager stripped of pytest specific details

# SPDX
License:        MIT
URL:            https://github.com/pytest-dev/pluggy
Source:         %{pypi_source pluggy}

BuildArch:      noarch
BuildRequires:  python3-devel

%if %{with tests}
# the [testing] extra includes benchmarking dependencies
BuildRequires:  python3-pytest
%endif

%global _description\
The plugin manager stripped of pytest specific details.

%description %_description


%package -n python3-pluggy
Summary:  %summary

%description -n python3-pluggy %_description


%prep
%autosetup -p1 -n pluggy-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pluggy


%if %{with tests}
%check
%pytest
%endif


%files -n python3-pluggy -f %{pyproject_files}
%doc README.rst


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.0-5
- Prepare for Oreon 11 (RP1)
