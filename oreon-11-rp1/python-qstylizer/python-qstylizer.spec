%global source0_hash 5ad15eeafdb140af3711531a1468382e3a15d8a416e5b1bcc6bf28693a7c37ee

%global pypi_name qstylizer

Name:           python-%{pypi_name}
Version:        0.2.4
Release:        %autorelease
Summary:        Stylesheet generator for PyQt/PySide

%global forgeurl https://github.com/blambright/qstylizer
%global tag %{version}
%forgemeta

# SPDX
License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel

#for tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)

%global _description %{expand:
Python package designed to help with the construction of PyQt/PySide
stylesheets.}

%description
%_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%generate_buildrequires
export PBR_VERSION=%{version}
%pyproject_buildrequires

%build
export PBR_VERSION=%{version}
%pyproject_wheel

%install
export PBR_VERSION=%{version}
%pyproject_install

%pyproject_save_files -l qstylizer

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
