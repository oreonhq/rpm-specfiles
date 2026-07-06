%global source0_hash 70e22f4fd29b204f75f989e3c1e847aa1de267a028aab4233c0db783aaff78c1

%global srcname sortedcontainers

%bcond_with tests
%bcond_with docs

Name:           python-%{srcname}
Version:        2.4.0
Release:        28%{?dist}
Summary:        Pure Python sorted container types

License:        Apache-2.0
URL:            https://pypi.python.org/pypi/%{srcname}
# PyPI tarball does not include docs or tests.
Source0:        https://github.com/grantjenks/python-sortedcontainers/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
SortedContainers is an Apache2 licensed sorted collections library, written in
pure-Python, and fast as C-extensions.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  make
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(scipy)
%endif

%if %{with docs}
BuildRequires:  python3dist(sphinx)
BuildRequires:  dvipng
BuildRequires:  tex(anyfontsize.sty)
BuildRequires:  tex(bm.sty)
%endif

%description -n python3-%{srcname} %{_description}


%package -n python-%{srcname}-doc
Summary:        %{summary}

%description -n python-%{srcname}-doc
Documentation for %{srcname} package.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with docs}
pushd docs
make html
rm _build/html/.buildinfo
popd
%endif

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%if %{with tests}
%check
pushd tests
%{pytest}
popd
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst


%if %{with docs}
%files -n python-%{srcname}-doc
%license LICENSE
%doc README.rst docs/_build/html
%endif

%changelog
%autochangelog
