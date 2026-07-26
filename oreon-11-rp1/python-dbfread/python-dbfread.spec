%global source0_hash 63a1cd9ddc9117fd61d4b9a9879e038c5e2d8b776ddae844c7a734def566d6cb

%global pypi_name dbfread
%global project_owner olemb
%global github_name dbfread
%global commit 300b2d7d907388cc3578d3fa4472e0419ccd34b9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global desc DBF is a file format used by databases such dBase, Visual FoxPro, and \
FoxBase+. This library reads DBF files and returns the data as native Python \
data types for further processing. It is primarily intended for batch jobs and \
one-off scripts.\
\
Full documentation at https://dbfread.readthedocs.io/\
\
See docs/changes.rst for a full list of changes in each version.

Name:           python-%{pypi_name}
Version:        2.0.7
Release:        36.git%{shortcommit}%{?dist}
Summary:        Read DBF Files with Python

License:        MIT
URL:            https://pypi.python.org/pypi/dbfread
Source0:        https://github.com/%{project_owner}/%{github_name}/archive/%{commit}/%{github_name}-%{commit}.tar.gz
# Fix tests with pytest4
Patch0:         https://patch-diff.githubusercontent.com/raw/olemb/dbfread/pull/33.patch
BuildArch:      noarch

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-%{pypi_name}
%{desc}

%package -n    python-%{pypi_name}-doc
Summary:       %{summary}
BuildRequires:  python3dist(sphinx)
BuildArch:     noarch

%description -n python-%{pypi_name}-doc
%{desc}

Documentation package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{commit}
# Remove shebang in examples
sed -i '1{\@^#!/usr/bin/env python@d}' examples/{*.py,**/*.py,dbf2sqlite}
# Make sure examples are not executable
chmod -x examples/{*.py,**/*.py,dbf2sqlite}
%patch -P0 -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# Build documentation
pushd docs
    make html SPHINXBUILD=sphinx-build-%{python3_version}
    rm -f _build/html/.buildinfo
popd

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

# The script will launch pytest for Python 2 and 3.
pytest-%{python3_version}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%files -n python-%{pypi_name}-doc
%license LICENSE
%doc README.rst docs/_build/ examples

%changelog
%autochangelog
