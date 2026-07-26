%global source0_hash 6d17c1bf9750110c2dc2203f82cdda209f3e84ed32443356942f3eb5c8a0ec25

%global srcname pymediawiki
%global modname mediawiki

Name:           python-%{srcname}
Version:        0.7.5
Release:        %autorelease
Summary:        Python wrapper and parser for MediaWiki API

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Pymediawiki is a python wrapper and parser for the MediaWiki API.
The goal is to allow users to quickly and efficiently pull data
from the MediaWiki site of their choice instead of worrying about
dealing directly with the API. As such, it does not force the use of
a particular MediaWiki site. It defaults to Wikipedia but other
MediaWiki sites can also be used.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

# Importable module is named mediawiki
%py_provides python3-%{modname}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

# Remove egg files from source
rm -r %{srcname}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pyproject_check_import
# tests provided in sources uses internet connection

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.rst

%changelog
%autochangelog
