%global source0_hash a6a9ce2003ae10e729768b6d79a4b3db330d876b86225eb7743b6f5696bafa59

%global pypi_name django-pipeline

Name:           python-%{pypi_name}
Version:        1.6.8
Release:        34%{?dist}
Summary:        An asset packaging library for Django

License:        MIT
URL:            https://github.com/jazzband/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Pipeline is an asset packaging library for Django, providing both CSS
and JavaScript concatenation and compression, built-in JavaScript template
support, and optional data-URI image and font embedding

%package -n python3-%{pypi_name}
Summary:        Packaging library for Django - Python 3 version
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-django

Obsoletes: python-%{pypi_name} < 1.6.8-5
Obsoletes: python2-%{pypi_name} < 1.6.8-5

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Pipeline is an asset packaging library for Django, providing both CSS
and JavaScript concatenation and compression, built-in JavaScript template
support, and optional data-URI image and font embedding.
This package provides Python 3 build of %{pypi_name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install
# Remove the "tests" subdirectory to avoid it polluting the main python
# namespace:
rm -rf %{buildroot}%{python3_sitelib}/tests
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/django_pipeline*.egg-info/
%{python3_sitelib}/pipeline/

%changelog
%autochangelog
