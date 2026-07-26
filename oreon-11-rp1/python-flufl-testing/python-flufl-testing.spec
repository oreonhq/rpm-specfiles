%global source0_hash 811861a8a9bd3303a3e6cadb03a0d35d7d3de349dee8274b27143a066b4975da

%global srcname flufl.testing
%global pkgname flufl-testing
%global summary Small collection of test tool plugins
%global _description \
This package contains a small collection of test helpers that Barry Warsaw \
uses in almost all his packages. Specifically, plugins for the following \
test tools are provided:  \
- nose2   \
- flake8  \
Python 3.4 is the minimum supported version.

Name:           python-%{pkgname}
Version:        0.8
Release:        24%{?dist}
Summary:        %{summary}

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://gitlab.com/warsaw/flufl.testing
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-srpm-macros
BuildRequires:  python%{python3_pkgversion}-devel >= 3.4
BuildRequires:  python%{python3_pkgversion}-setuptools
%if 0%{?with_python3_other}
BuildRequires:  python%{python3_other_pkgversion}-devel >= 3.4
BuildRequires:  python%{python3_other_pkgversion}-setuptools
%endif

%description %{_description}

%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}

%description -n python%{python3_pkgversion}-%{pkgname} %{_description}

%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{pkgname}}

%description -n python%{python3_other_pkgversion}-%{pkgname} %{_description}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%py3_build
%if 0%{?with_python3_other}
%py3_other_build
%endif

%install
%py3_install
%if 0%{?with_python3_other}
%py3_other_install
%endif

%files -n python%{python3_pkgversion}-%{pkgname}
%doc README.rst NEWS.rst
%{python3_sitelib}/flufl/
%{python3_sitelib}/%{srcname}-%{version}*-py%{python3_version}.egg-info/
%{python3_sitelib}/%{srcname}-%{version}*-py%{python3_version}-nspkg.pth

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pkgname}
%doc README.rst NEWS.rst
%{python3_other_sitelib}/flufl/
%{python3_other_sitelib}/%{srcname}-%{version}*-py%{python3_other_version}.egg-info/
%{python3_other_sitelib}/%{srcname}-%{version}*-py%{python3_version}-nspkg.pth
%endif

%changelog
%autochangelog
