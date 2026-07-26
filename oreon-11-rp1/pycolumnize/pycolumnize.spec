%global source0_hash c7947a57a126b6e5b4b585a19945909c3e64213979113948968304ebcf23daa4

%global pypi_name columnize

Name:           pycolumnize
Version:        0.3.10
Release:        21%{?dist}
Summary:        Python module to align in columns a simple list

License:        MIT
URL:            https://github.com/rocky/pycolumnize
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
# Maintainers, please upstream
Patch0:         pycolumnize-rm-python-mock-usage.diff
BuildArch:      noarch

%description
A Python module to format a simple (i.e. not nested) list into aligned columns.
A string with embedded newline characters is returned.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python module to format a simple (i.e. not nested) list into aligned columns.
A string with embedded newline characters is returned.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove the dependency on nose
sed -i /nose/d setup.py

%build
%py3_build

%install
%py3_install

%check
%pytest -v test_columnize.py

%files -n python3-%{pypi_name}
%doc ChangeLog README.rst SECURITY.md THANKS
%license LICENSE
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/__pycache__/%{pypi_name}*
%{python3_sitelib}/%{pypi_name}.py*

%changelog
%autochangelog
