%global source0_hash 094dd7d9a5fc1cca4854773e5c1fc6a315b33bd5b3a8f47064928facaf0490a8

%global pypi_name palettable

%global _description %{expand:
Palettable (formerly brewer2mpl) is a library of color palettes for Python.

It's written in pure Python with no dependencies, but it can supply
color maps for matplotlib. You can use Palettable to customize matplotlib
plots or supply colors for a web application.}

Name:           python-%{pypi_name}
Version:        3.3.3
Release:        %{autorelease}
Summary:        Library of color palettes for Python
BuildArch:      noarch

License:        MIT AND BSD-2-Clause AND Apache-2.0
URL:            https://pypi.org/pypi/%{pypi_name}
Source0:        %{pypi_source %{pypi_name}}
# https://github.com/jiffyclub/palettable/pull/52
Patch0:         limit_find_to_palettable_dir.patch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  git-core

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version} -S git

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%{pytest}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license license.txt
%license palettable/colorbrewer/data/colorbrewer_licence.txt

%changelog
%autochangelog
