%global source0_hash 77697918c9b72974a0162f14472b48a7a02b15344a4df3092194c2afc54eb738

%global upstream_name www-authenticate
%global modname www_authenticate

Name:           python-%{upstream_name}
Version:        0.9.2
Release:        35%{?dist}
Summary:        Python library for parsing WWW-Authenticate HTTP header values
License:        BSD-4.3TAHOE
URL:            https://github.com/alexsdutton/www-authenticate
Source0:        https://github.com/alexsdutton/%{upstream_name}/archive/%{version}.tar.gz#/%{upstream_name}-%{version}.tar.gz
# https://github.com/alexsdutton/www-authenticate/issues/1
Source1:        https://raw.githubusercontent.com/lphuberdeau/www-authenticate/a35e5df38d909e0f73bb6df0573fa80333a4922e/LICENSE
BuildArch:      noarch

%global _description \
Parsing WWW-Authenticate headers is difficult. Let this tiny library do all \
the hard work for you.

%description %{_description}

%package -n python%{python3_pkgversion}-%{upstream_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{upstream_name}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{upstream_name} %{_description}

Python %{python3_pkgversion} version.

%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{upstream_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{upstream_name}}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools

%description -n python%{python3_other_pkgversion}-%{upstream_name} %{_description}

Python %{python3_other_pkgversion} version.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upstream_name}-%{version}
cp -p %{SOURCE1} .

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

%check
%{__python3} -m unittest -v
%if 0%{?with_python3_other}
%{__python3_other} -m unittest -v
%endif

%files -n python%{python3_pkgversion}-%{upstream_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{modname}.py*
%{python3_sitelib}/__pycache__/%{modname}.*
%{python3_sitelib}/%{modname}-*.egg-info

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{upstream_name}
%license LICENSE
%doc README.rst
%{python3_other_sitelib}/%{modname}.py*
%{python3_other_sitelib}/__pycache__/%{modname}.*
%{python3_other_sitelib}/%{modname}-*.egg-info
%endif

%changelog
%autochangelog
