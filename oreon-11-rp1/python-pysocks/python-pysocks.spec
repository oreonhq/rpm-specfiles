%global source0_hash 3f8804571ebe159c380ac6de37643bb4685970655d3bba243530d6558b799aa0

%if 0%{?fedora}
%global with_python3_tests 1
%endif

%global pypi_name   PySocks
%global modname     pysocks
%global sum         A Python SOCKS client module

Name:               python-%{modname}
Version:            1.7.1
Release:            32%{?dist}
Summary:            %{sum}

License:            BSD-3-Clause
URL:                https://github.com/Anorov/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/P/PySocks/PySocks-1.7.1.tar.gz
BuildArch:          noarch

%global _description \
A fork of SocksiPy with bug fixes and extra features.\
\
Acts as a drop-in replacement to the socket module. Featuring:\
\
- SOCKS proxy client for Python 2.6 - 3.x\
- TCP and UDP both supported\
- HTTP proxy client included but not supported or recommended (you should use\
  urllib2's or requests' own HTTP proxy interface)\
- urllib2 handler included.

%description
%_description


%package -n python%{python3_pkgversion}-%{modname}
Summary:            %{sum}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
# for tests
%if 0%{?with_python3_tests}
BuildRequires:      python%{python3_pkgversion}-pytest
BuildRequires:      python%{python3_pkgversion}-psutil
#BuildRequires:      python%%{python3_pkgversion}-test_server
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}

# This package doesn't actually exist...
# but if it did, we would conflict with it.
Conflicts:  python%{python3_pkgversion}-SocksiPy

%description -n python%{python3_pkgversion}-%{modname}
%_description
This package is for Python3 version %{python3_version} only.

%if 0%{?python3_other_pkgversion}
%package -n python%{python3_other_pkgversion}-%{modname}
Summary:            %{sum}
BuildRequires:      python%{python3_other_pkgversion}-devel
BuildRequires:      python%{python3_other_pkgversion}-setuptools
# for tests
%if 0%{?with_python3_tests}
BuildRequires:      python%{python3_other_pkgversion}-pytest
BuildRequires:      python%{python3_other_pkgversion}-psutil
#BuildRequires:      python%%{python3_other_pkgversion}-test_server
%endif
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{modname}}

%description -n python%{python3_other_pkgversion}-%{modname}
%_description
This package is for Python3 version %{python3_other_version} only.
%endif


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{pypi_name}-%{version}
# drop useless 3rdparty code
rm -rfv test/bin

%build
%py3_build
%{?python3_other_pkgversion: %py3_other_build}

%install
%py3_install
%{?python3_other_pkgversion: %py3_other_install}

%check
# https://github.com/Anorov/PySocks/issues/37
# FIXME python module named test_server is needed but not packaged
%if 0
%if 0%{?with_python3_tests}
%{?with_python3: %{__python3} setup.py test}
%{?python3_other_pkgversion: %{__python3_other} setup.py test}
%endif
%endif



%files -n python%{python3_pkgversion}-%{modname}
%doc README.md
%license LICENSE
%{python3_sitelib}/socks.py*
%{python3_sitelib}/sockshandler.py*
%{python3_sitelib}/__pycache__/*socks*
%{python3_sitelib}/%{pypi_name}-%{version}-*

%if 0%{?python3_other_pkgversion}
%files -n python%{python3_other_pkgversion}-%{modname}
%doc README.md
%license LICENSE
%{python3_other_sitelib}/socks.py*
%{python3_other_sitelib}/sockshandler.py*
%{python3_other_sitelib}/__pycache__/*socks*
%{python3_other_sitelib}/%{pypi_name}-%{version}-*
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7.1-32
- Prepare for Oreon 11 (RP1)
