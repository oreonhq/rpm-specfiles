%global source0_hash 0563a76513b6af6eebbe788c3bf3d01c920e46b3f90c8416738c5cfc773ff8e2

%global pypi_name cssutils
%global srcname cssutils

%bcond_without tests

Name:           python-%{srcname}
Summary:        CSS Cascading Style Sheets library for Python
Version:        2.11.1
Release:        8%{?dist}

License:        LGPL-3.0-or-later
URL:            https://github.com/jaraco/cssutils
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel
# Tests BuildRequires
BuildRequires:  python3dist(more-itertools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(mypy)
BuildRequires:  ruff
BuildRequires:  python3dist(cssselect)
BuildRequires:  python3dist(jaraco-test)

%global _description \
A Python package to parse and build CSS Cascading Style Sheets. DOM only, not\
any rendering facilities.

%description %{_description}

%package doc
Summary:        Documentation for %{name}

%description doc
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}
A Python package to parse and build CSS Cascading Style Sheets. DOM only, not\
any rendering facilities.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n cssutils-%{version}
# jaraco.test module not yet in Fedora
rm -f cssutils/tests/test_property.py cssutils/tests/test_selector.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files *utils

%if %{with tests}
%check
%pytest -k "not test_parseUrl and not encutils and not website.logging"
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/csscapture
%{_bindir}/csscombine
%{_bindir}/cssparse

%files doc
%doc examples/

%changelog
%autochangelog
