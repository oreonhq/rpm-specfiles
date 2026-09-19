%global source0_hash 795487c61436ecb76f1d62e56d7bc74546e3100925039e6e5d5ba0a7d22cfa16

%global srcname pamela

Name:           python-%{srcname}
Version:        1.2.0
Release:        2%{?dist}
Summary:        Python PAM interface

License:        MIT
URL:            https://github.com/minrk/%{srcname}
Source0:        https://github.com/minrk/%{srcname}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
Yet another Python wrapper for PAM.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Yet another Python wrapper for PAM.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
py.test-%{python3_version} -v

%files -n python%{python3_pkgversion}-%{srcname}
%license COPYING
%doc README.md
%{python3_sitelib}/%{srcname}*
%{python3_sitelib}/__pycache__/%{srcname}*

%changelog
%autochangelog
