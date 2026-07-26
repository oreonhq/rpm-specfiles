%global source0_hash b6a646ab7b2fb2a5575c69eb61c941113d8dfd8af9516d6362529f2315bdbc73

%global forgeurl https://github.com/jonathf/chaospy

%bcond_without tests

Name:           python-chaospy
Version:        4.3.19
Release:        %autorelease
Summary:        Numerical tool for performing uncertainty quantification
%forgemeta
# SPDX
License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  %{py3_dist scikit-learn}
BuildRequires:  %{py3_dist pytest}
%endif

%global desc %{expand: \
Chaospy is a numerical toolbox designed for performing uncertainty
quantification through polynomial chaos expansions and advanced Monte
Carlo methods implemented in Python. It includes a comprehensive suite
of tools for low-discrepancy sampling, quadrature creation, polynomial
manipulations, and much more.}

%description
%{desc}

%package -n python3-chaospy
Summary:        %{summary}

%description -n python3-chaospy
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

# Don't error on DeprecationWarning in tests
sed -i '/error::DeprecationWarning/d' pyproject.toml

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files -l chaospy

%check
%if %{with tests}
%pytest -v
%else
%pyproject_check_import
%endif

%files -n python3-chaospy -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
