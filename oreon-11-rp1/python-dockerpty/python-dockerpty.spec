%global source0_hash fd9acb9fa7a464b668dcc50612975f3c7f1485cc0213d19de8381cb641b49459

# what it's called on pypi
%global srcname dockerpty
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%if 0%{?fedora} >= 30
%bcond_with python2
%else
%bcond_without python2
%endif
%bcond_without python3

Name:           python-%{pkgname}
Version:        0.4.1
Release:        40%{?dist}
Summary:        Python library to use the pseudo-tty of a docker container
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/d11wtq/dockerpty
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%global _description\
Provides the functionality needed to operate the pseudo-tty (PTY) allocated to\
a docker container, using the Python client

%description    %{_description}

%if %{with python2}
%package -n python2-%{pkgname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       python2-six
%{?python_provide:%python_provide python2-%{pkgname}}

%description -n python2-%{pkgname} %{_description}
%endif

%if %{with python3}
%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-six
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}

%description -n python%{python3_pkgversion}-%{pkgname} %{_description}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%{?with_python2:%py2_build}
%{?with_python3:%py3_build}

%install
%{?with_python2:%py2_install}
%{?with_python3:%py3_install}

# we are missing the 'expects' library to run the tests
# %%check
# LANG=en_US.utf8 py.test-%%{python3_version} -vv tests
# LANG=en_US.utf8 py.test-%%{python2_version} -vv tests

%if %{with python2}
%files -n python2-%{pkgname}
%license LICENSE.txt
%doc README.md MANIFEST.in
%{python2_sitelib}/%{libname}
%{python2_sitelib}/%{eggname}-%{version}-py%{python2_version}.egg-info
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE.txt
%doc README.md MANIFEST.in
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info
%endif

%changelog
%autochangelog
