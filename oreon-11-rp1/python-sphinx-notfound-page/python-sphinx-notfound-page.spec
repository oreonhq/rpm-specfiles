%global source0_hash 45f5da22c69d9a6195de10f3752948958142ef82d83eea748a9666ffe01a159a

%global pypi_name sphinx-notfound-page
%global srcname sphinx_notfound_page
%global importname notfound
%global project_owner readthedocs
%global github_name sphinx-notfound-page
%global desc Create a custom 404 page with absolute URLs hardcoded

Name:           python-%{pypi_name}
Version:        1.0.4
Release:        7%{?dist}
Summary:        Create a custom 404 page with absolute URLs hardcoded

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://github.com/%{project_owner}/%{github_name}/archive/%{version}.tar.gz
# Patch to remove . and no longer needed pdbpp from tox deps
# From https://github.com/readthedocs/sphinx-notfound-page/pull/225
Patch:         tox-no-dot-no-pdbpp.patch
# Already upstream patch to fix tests with sphinx 7.3.x
Patch:         https://patch-diff.githubusercontent.com/raw/readthedocs/sphinx-notfound-page/pull/245.patch
# Already upstream patch to fix tests with sphinx 8.x
Patch:         https://patch-diff.githubusercontent.com/raw/readthedocs/sphinx-notfound-page/pull/250.patch

BuildArch:      noarch
BuildRequires:	python3dist(tox-current-env) >= 0.0.16

%description
%desc

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
BuildArch:      noarch

%description -n python%{python3_pkgversion}-%{pypi_name}
%desc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files notfound

%check
%tox

%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGELOG.rst docs

%changelog
%autochangelog
