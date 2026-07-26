%global source0_hash f964bec2086f3153a6c16e707f20cb718f811f57af116075f4c0f4805c608b95

%global pypi_name leather
%global dir_name leather
%global project_owner wireservice
%global github_name leather
%global desc Leather is the Python charting library for those who need charts now and don’t\
care if they’re perfect.\
\
- A readable and user-friendly API.\
- Optimized for exploratory charting.\
- Produces scale-independent SVG charts.\
- Completely type-agnostic. Chart your data, whatever it is.\
- Designed with iPython, Jupyter and atom/hydrogen in mind.\
- Pure Python. No C dependencies to compile.

Name:           python-%{pypi_name}
Version:        0.4.0
Release:        10%{?dist}
Summary:        Python charting for 80% of humans

License:        MIT
URL:            https://pypi.python.org/pypi/leather
Source0:        https://github.com/wireservice/leather/archive/%{version}/%{pypi_name}-%{version}.tar.gz
# Backport of upstream commit to add compatibility with Python 3.10
BuildArch:      noarch

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx >= 1.2.2
BuildRequires:  python3-furo
BuildRequires:  python3-coverage >= 3.7.1
BuildRequires:  python3-sphinx_rtd_theme >= 0.1.6
BuildRequires:  python3-lxml >= 3.6.0
BuildRequires:  python3-six >= 1.6.1
BuildRequires:  python3-cssselect

%description -n python3-%{pypi_name}
%{desc}

%package -n    python-%{pypi_name}-doc
Summary:       %{summary}

%description -n python-%{pypi_name}-doc
%{desc}

Documentation package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{version}
# Remove shebang on non executable scripts
sed -i '1{\@^#!/usr/bin/env python@d}' leather/*.py leather/**/*.py

# Remove hidden files in examples
rm examples/charts/.placeholder

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd docs
    make html
    # Remove hidden file
    rm _build/html/.buildinfo
popd

%install
%pyproject_install
%pyproject_save_files -l %{dir_name}

%check
%pyproject_check_import

%pytest tests -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license COPYING

%files -n python-%{pypi_name}-doc
%doc examples docs/_build/html
%license COPYING

%changelog
%autochangelog
