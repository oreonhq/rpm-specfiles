%global source0_hash d030bd0c379310377772d513e6861a7a9dcc1e683049f27a9976ba5de3b5d1b9

%global pypi_name django-cache-url
%global modname django_cache_url

Name:           python-%{pypi_name}
Version:        3.4.6
Release:        %autorelease
Summary:        Use Cache URLs in your Django application

License:        MIT
URL:            https://github.com/epicserve/django-cache-url
Source:         %{pypi_source %modname}

BuildArch:      noarch

# for import checks
BuildRequires:  python3dist(django)

%description
This simple Django utility allows you to utilize the 12factor inspired
CACHE_URL environment variable to configure your Django application.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
This simple Django utility allows you to utilize the 12factor inspired
CACHE_URL environment variable to configure your Django application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
