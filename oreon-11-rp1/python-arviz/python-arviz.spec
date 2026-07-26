%global source0_hash 772bb600c2b82eac239c5a6f0077cb5fc0536744bc32755e8471b008d0f26b8d

%global srcname arviz

Name:           python-%{srcname}
Version:        0.23.0
Release:        %autorelease
Summary:        Exploratory analysis of Bayesian models

License:        Apache-2.0
URL:            https://python.arviz.org/
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
ArviZ is a Python package for exploratory analysis of Bayesian models. 
Includes functions for posterior analysis, sample diagnostics, 
model checking, and comparison.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-setuptools
# Some optional dependencies
Recommends:  python3dist(bokeh)
Recommends:  python3dist(ujson)

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files arviz

%check
%pyproject_check_import -t

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
