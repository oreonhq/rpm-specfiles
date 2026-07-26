%global source0_hash d862b0f313c852c618510fbce464b5eb58b02dbe3a146952c5a7b7cb4957431d

%global pypi_name CacheControl
%global pypi_name_lower cachecontrol

%global common_description %{expand:
CacheControl is a port of the caching algorithms in httplib2 for use with
requests session object. It was written because httplib2's better support
for caching is often mitigated by its lack of thread safety. The same is
true of requests in terms of caching.}

Name:           python-%{pypi_name}
Summary:        httplib2 caching for requests
Version:        0.14.4
Release:        3%{?dist}
License:        MIT

URL:            https://github.com/ionrock/cachecontrol
Source0:        %{url}/archive/v%{version}/%{pypi_name_lower}-%{version}.tar.gz

BuildArch:      noarch

%description %{common_description}

%package -n     python3-%{pypi_name}
Summary:        httplib2 caching for requests

BuildRequires:  python3-devel
BuildRequires:  python3-cherrypy
BuildRequires:  python3-pytest

Recommends:  python3-%{pypi_name}+filecache
Recommends:  python3-%{pypi_name}+redis

%description -n python3-%{pypi_name} %{common_description}

%pyproject_extras_subpkg -n python3-%{pypi_name} filecache redis

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name_lower}-%{version} -p1
# Do not upper-bound (SemVer-bound) the version of uv_build; we must work with
# what we have, and compatibility is quite good in practice.
sed -r -i 's/"(uv_build *>= *[^:]+), *<[^"]+"/"\1"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x filecache,redis

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files cachecontrol

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%{_bindir}/doesitcache

%changelog
%autochangelog
