%global source0_hash 1a29730d366e996aaacffb2f1f1cb9593dc38e2ddd30c91250c6dde09ea9b417

%global srcname inflection

Name:           python-%{srcname}
Version:        0.5.1
Release:        20%{?dist}
Summary:        Port of Ruby on Rails inflector to Python

License:        MIT
URL:            https://github.com/jpvanhal/inflection
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
Inflection is a string transformation library. It singularizes and pluralizes
English words, and transforms strings from CamelCase to underscored string.
Inflection is a port of Ruby on Rails’ inflector to Python.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info

%build
%py3_build

%install
%py3_install

%check
%python3 -m pytest -v

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/inflection-*.egg-info/
%{python3_sitelib}/inflection/

%changelog
%autochangelog
