%global source0_hash 759aa22c216326356f65e62e791d66160a0f9c91d1424e8d8adc5e74dddfc6fb

%global srcname cssselect2

Name:           python-%{srcname}
Version:        0.9.0
Release:        1%{?dist}
Summary:        CSS selectors for Python ElementTree
License:        BSD-3-Clause
URL:            https://doc.courtbouillon.org/cssselect2/stable/
BuildArch:      noarch
Source0:        %{pypi_source cssselect2}

BuildRequires:  python3-devel

%description
cssselect2 is a straightforward implementation of CSS4 Selectors for markup
documents (HTML, XML, etc.) that can be read by ElementTree-like parsers,
including cElementTree, lxml, html5lib, etc.

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
cssselect2 is a straightforward implementation of CSS4 Selectors for markup
documents (HTML, XML, etc.) that can be read by ElementTree-like parsers,
including cElementTree, lxml, html5lib, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}
# Skip the flake8 plugin: linting is useful for upstream only. Also flake8 was
# not available in time for the Python 3.9 rebuild (and that might be the case
# for Python 3.10+) so let's just remove it.
# Same for isort.
# Same for ruff.
sed -i -e "s/, 'flake8'//" -e "s/, 'isort'//" -e "s/, 'ruff'//" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
