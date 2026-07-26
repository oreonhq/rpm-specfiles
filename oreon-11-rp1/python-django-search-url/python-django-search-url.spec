%global source0_hash 424d1a5852500b3c118abfdd0e30b3e0016fe68e7ed27b8553a67afa20d4fb40

%global pypi_name dj-search-url
%global pkg_name django-search-url

Name:           python-%{pkg_name}
Version:        0.1
Release:        26%{?dist}
Summary:        Use Search URLs in your Django Application

License:        BSD-2-Clause
URL:            https://github.com/dstufft/dj-search-url
Source0:        %{pypi_source}
BuildArch:      noarch

%description
This simple Django utility allows you to utilize the 12factor inspired
SEARCH_URL environment variable to configure your application.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel
%py_provides    python3-%{pypi_name}

%description -n python3-%{pkg_name}
This simple Django utility allows you to utilize the 12factor inspired
SEARCH_URL environment variable to configure your application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l dj_search_url

%check
%pyproject_check_import

%files -n python3-%{pkg_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
