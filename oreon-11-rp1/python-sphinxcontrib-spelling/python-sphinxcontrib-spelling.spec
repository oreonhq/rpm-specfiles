%global source0_hash 3819d12629d95e0c909224fa40b462a67e0adb321d50283d7fc0d11686c8ac7e

%global pypi_name sphinxcontrib-spelling
%global sum  A spelling checker for Sphinx-based documentation
%global desc This package contains sphinxcontrib.spelling, a spelling checker for \
Sphinx-based documentation. It uses PyEnchant to produce a report showing \
misspelled words.

# Disable dependency generator
%{?python_disable_dependency_generator}

%bcond_without python3

Name:           python-%{pypi_name}
Version:        7.3.3
Release:        17%{?dist}
Summary:        %{sum}

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/sphinx-contrib/spelling
Source0:        %{pypi_source}
BuildArch:      noarch

%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pbr
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-enchant
BuildRequires:  python%{python3_pkgversion}-sphinx
%endif

%if 0%{?with_python3_other}
BuildRequires:  python%{python3_other_pkgversion}-setuptools
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-pbr
BuildRequires:  python%{python3_other_pkgversion}-pytest
BuildRequires:  python%{python3_other_pkgversion}-enchant
BuildRequires:  python%{python3_other_pkgversion}-sphinx
%endif

%description
%{desc}

# Python 3 package
%if %{with python3}
%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-enchant
Requires:       python%{python3_pkgversion}-sphinx

%description -n python%{python3_pkgversion}-%{pypi_name}
%{desc}
%endif

# Python 3 other package
%if 0%{?with_python3_other}
%package -n     python%{python3_other_pkgversion}-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{pypi_name}}
Requires:       python%{python3_other_pkgversion}-enchant
Requires:       python%{python3_other_pkgversion}-sphinx

%description -n python%{python3_other_pkgversion}-%{pypi_name}
%{desc}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if %{with python3}
%py3_build
%endif

%if 0%{?with_python3_other}
%py3_other_build
%endif

%install
%if 0%{?with_python3_other}
%py3_other_install
%endif

%if %{with python3}
%py3_install
%endif

%check
%if %{with python3}
%pytest
%endif

%if 0%{?with_python3_other}
%{__python3_other} -m pytest
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README
%license LICENSE
%{python3_sitelib}/sphinxcontrib
%{python3_sitelib}/sphinxcontrib_spelling*
%endif

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pypi_name}
%doc README
%license LICENSE
%{python3_other_sitelib}/sphinxcontrib
%{python3_other_sitelib}/sphinxcontrib_spelling*
%endif

%changelog
%autochangelog
