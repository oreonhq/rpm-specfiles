%global source0_hash 047e713eeddecf11a674d4cd27ac72407f85ef13196856ba8dfeb4d691d521d4

# Created by pyp2rpm-3.3.2
%global pypi_name django-uuslug

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        16%{?dist}
Summary:        A Django slugify application that guarantees uniqueness and handles Unicode

License:        MIT
URL:            https://github.com/un33k/django-uuslug
Source0:        %{pypi_source}
BuildArch:      noarch

# Test suite is not included in sdist package of upstream release 2.0.0
Patch0:         0001-Add-upstream-test-suite.patch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(python-slugify)

%description
A Django slugify application that guarantees Uniqueness and handles Unicode

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(python-slugify) >= 1.2.0
Requires:       python3dist(six)
Requires:       python3dist(django)

%description -n python3-%{pypi_name}
A Django slugify application that guarantees Uniqueness and handles Unicode

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf django_uuslug.egg-info

%check
%{__python3} manage.py test

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/uuslug/
%{python3_sitelib}/django_uuslug-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
