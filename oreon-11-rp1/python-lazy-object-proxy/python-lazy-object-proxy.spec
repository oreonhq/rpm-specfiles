%global source0_hash 21b39ab1b141ce22961fe8f0c3f177dc2172747645ee7abba2522bae8afa6ab6

%global srcname lazy-object-proxy
%global sum A fast and thorough lazy object proxy

Name:           python-%{srcname}
Version:        1.12.0
Release:        2%{?dist}
Summary:        %{sum}

License:        BSD-2-Clause
Url:            https://github.com/ionelmc/python-%{srcname}
Source0:        https://github.com/ionelmc/python-%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python%{python3_pkgversion}-devel

%description
A fast and thorough lazy object proxy.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
A fast and thorough lazy object proxy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n python-%{srcname}-%{version} -p0
# unavailable test deps, tox passes without them
sed -Ei '/\b(objproxies|hunter)\b/d' tox.ini

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%tox

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/*
%attr(0755, root, root) %{python3_sitearch}/lazy_object_proxy/*.so
%exclude %{python3_sitearch}/lazy_object_proxy/cext.c

%changelog
%autochangelog
