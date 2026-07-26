%global source0_hash 28ef86ea1672c180b5189e22441e17ebe54e98ebf6293a64eeaaa8f10ab74942

%global pypi_name contextualbandits

%global _description %{expand:
This Python package contains implementations of methods from different papers
dealing with contextual bandit problems, as well as adaptations from typical
multi-armed bandits strategies. It aims to provide an easy way to prototype
and compare ideas, to reproduce research papers that don't provide 
easily-available implementations of their proposed algorithms, and to
serve as a guide in learning about contextual bandits.}

%global commit          6c152e2ff3a2c4c41daebc01e6c202548b3be092
%global snapshotdate    20241901
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           python-%{pypi_name}
Version:        0.3.27
Release:        6%{?dist}
Summary:        Python implementations of algorithms for contextual bandits

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/david-cortes/contextualbandits

# we fetch the latest tarball from the upstream
# we do not rely on Pypi version (no docs, no LICENSE included)
Source0:        %url/archive/%{commit}/%{pypi_name}-%{commit}.tar.gz

# Stop building for i686
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  Cython

# For documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{commit}
rm -rf %{pypi_name}.egg-info
# remove toml file. It is actually not used in real build.
rm -rf pyproject.toml

%generate_buildrequires
echo 'python3dist(numpy)'
echo 'python3dist(scipy)'
echo 'python3dist(pandas)'
echo 'python3dist(scikit-learn)'
echo 'python3dist(joblib)'

%build
%pyproject_wheel

# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install

%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%files doc
%license LICENSE
%doc html/
%doc example/

%changelog
%autochangelog
