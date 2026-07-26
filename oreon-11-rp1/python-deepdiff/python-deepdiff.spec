%global source0_hash 3c538a4966b18c5c006498363403d6e0626fdb5a9ab5825e38bdc715be00c74f

# Don't have sphinx-sitemaps for now...
%bcond_with docs
%bcond_without tests

Name:           python-deepdiff
Version:        8.6.1
Release:        3%{?dist}
Summary:        Deep Difference and search of any Python object/data

License:        MIT
URL:            https://github.com/seperman/deepdiff/
Source:         https://github.com/seperman/deepdiff/archive/%{version}/%{name}-v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel

# For tests
# Cherry picked test reqs from pyproject.toml
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(tomli-w)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(jsonpickle)
BuildRequires:  python3dist(pydantic)
BuildRequires:  python3-pandas
BuildRequires:  python3-pytest-benchmark
%endif

# For docs
%if %{with docs}
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-dotenv
BuildRequires:  python3-sphinx-sitemap
%endif

%global _description %{expand:
Deep Difference of dictionaries, iterables, strings, and ANY other object.
Includes additional modules with related functionality:
DeepSearch: Search for objects within other objects.
DeepHash: Hash any object based on their content.
Delta: Store the difference of objects and apply them to other objects.
Extract: Extract an item from a nested Python object using its path.
commandline: Use DeepDiff from commandline.}

%description %{_description}

%package     -n python3-deepdiff
Summary:        %{summary}
Recommends:     python3-deepdiff+cli

%description -n python3-deepdiff %{_description}

# Add the cli as a extras subpackage which provides the deep executable.
# Including the cli extra as the deep command doesnt function without it.
%pyproject_extras_subpkg -n python3-deepdiff cli
%{_bindir}/deep

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n deepdiff-%{version}

find deepdiff/ -name \*.py -exec sed -i '/#!\/usr\/bin\/env /d' {} \;

# Upstream pins the dependencies to explicit versions
# This leads to downstream problems like:
#  https://bugzilla.redhat.com/2246614
# We replace all the version matching clauses with compatible release clauses:
sed -i 's/==/~=/' pyproject.toml
# Relax a bit the flit-core version for EPEL 10.
sed -i '/flit_core/{s/>=3.11/>=3.9/}' pyproject.toml
# Remove click's upper version bound
sed -i 's/click~=8.1.0/click>=8.1.0/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x cli,optimize

%build
%pyproject_wheel

%if %{with docs}
# Build docs
make -C docs html
# remove the sphinx-build leftovers
rm -rf docs/_build/html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%pyproject_save_files deepdiff

%check
%if %{with tests}
# uuid6 package is not available on Fedora at the moment, so remove test_hash.py
%pytest --ignore=tests/test_hash.py tests/
%endif
%pyproject_check_import

%files -n python3-deepdiff -f %{pyproject_files}

%doc AUTHORS.md README.md

%if %{with docs}
%doc docs/_build/html
%endif

%changelog
%autochangelog
