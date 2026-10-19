%global source0_hash 48884fa7af2e7638356fae93d1ee2180cadf5110de5a9088e9c8cd38055ecac5
%global srcname flake8-polyfill
Name:           python-%{srcname}
Version:        1.0.2
Release:        1%{?dist}
Summary:        Polyfill package for Flake8 plugins
License:        MIT
URL:            https://gitlab.com/pycqa/%{srcname}
Source0:        https://gitlab.com/pycqa/%{srcname}/-/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:         %{name}-1.0.2-pytest-4-compatibility.patch
Patch1:         python-flake8-polyfill-rm-python-mock-usage.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-flake8
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
# /oreon:deps
%description
flake8-polyfill is a package that provides some compatibility helpers for
Flake8 plugins that intend to support Flake8 2.x and 3.x simultaneously.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Polyfill package for Flake8 plugins
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-flake8
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-flake8
%endif
%description -n python%{python3_pkgversion}-%{srcname}
flake8-polyfill is a package that provides some compatibility helpers for
Flake8 plugins that intend to support Flake8 2.x and 3.x simultaneously.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

PYTHONPATH=%{buildroot}%{python3_sitelib} \
  py.test-%{python3_version} \
  --ignore=tests/test_stdin.py \
  tests
%files -f %{oreon_filedir}/main.list
%files -n python3-flake8-polyfill -f %{oreon_filedir}/python3-flake8-polyfill.list

%changelog

%autochangelog
