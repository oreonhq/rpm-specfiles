%global source0_hash 0429a75e19380e4ed50c0694e26ac8819b4ea7851ee1fc7583c8572db80aff77

%global modname repoze.lru

Name:           python-repoze-lru
Version:        0.7
Release:        30%{?dist}
Summary:        A tiny LRU cache implementation and decorator

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://pypi.python.org/pypi/repoze.lru
Source0:        %pypi_source %{modname}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description\
repoze.lru is a LRU (least recently used) cache implementation. Keys and values\
that are not used frequently will be evicted from the cache faster than keys\
and values that are used frequently.\

%description %_description

%package -n python3-repoze-lru
Summary:        A tiny LRU cache implementation and decorator

%description -n python3-repoze-lru
repoze.lru is a LRU (least recently used) cache implementation. Keys and values
that are not used frequently will be evicted from the cache faster than keys
and values that are used frequently.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{modname}-%{version}
rm -rf %{modname}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files repoze

%check
%pytest repoze/lru/tests.py

%files -n python3-repoze-lru -f %{pyproject_files}
%doc README.rst LICENSE.txt COPYRIGHT.txt CONTRIBUTORS.txt
%{python3_sitelib}/repoze.lru-%{version}-py%{python3_version}-nspkg.pth

%changelog
%autochangelog
