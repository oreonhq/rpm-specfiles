%global source0_hash d41a481fe4d5d12b865ffd483e556587967ab54ed7fd4eb5a39bdb8ee7e8ee60

%global pypi_name spotipy

Name:           python-%{pypi_name}
Version:        2.26.0
Release:        %autorelease
Summary:        A light weight Python library for the Spotify Web API
License:        MIT
URL:            https://github.com/plamere/spotipy
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%global _description \
A light weight Python library for the Spotify Web API

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-docutils

%description -n python3-spotipy %{_description}

%package -n python3-spotipy-doc
Summary:        Documentation for python3-spotipy

%description -n python3-spotipy-doc
Documentation for python3-spotipy

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

PYTHONPATH=$PWD/build/lib
mkdir html
sphinx-build -b html docs html
rm -rf html/{.buildinfo,.doctrees}

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import
# full tests can not be run without network access

%files -n python3-spotipy -f %pyproject_files
%license LICENSE.md
%doc CONTRIBUTING.md TUTORIAL.md FAQ.md CHANGELOG.md

%files -n python3-spotipy-doc
%doc html

%changelog
%autochangelog
