%global source0_hash ee718daac6873c83fd3706bce77da472c776a51e0d6f5f86f7e61e27f9ad166a

%global pypi_name enlighten
%global sum  Enlighten Progress Bar
%global desc Enlighten Progress Bar is console progress bar module for Python.\
The main advantage of Enlighten is it allows writing to stdout and stderr\
without any redirection.

Name:           python-%{pypi_name}
Version:        1.13.0
Release:        7%{?dist}
Summary:        %{sum}

License:        MPL-2.0
URL:            https://github.com/Rockhopper-Technologies/enlighten
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-blessed
BuildRequires:  python%{python3_pkgversion}-prefixed

%description
%{desc}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-blessed
Requires:       python%{python3_pkgversion}-prefixed

%description -n python%{python3_pkgversion}-%{pypi_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove benchmark scripts
rm -rf benchmarks

# Remove Python byte cache from previous Python versions shipped in upstream tarball
find -name '*.pyc' -delete

%build
%py3_build

%install
%py3_install

%check
%{py3_test_envvars} %{python3} -m unittest

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README*
%doc examples
%license LICENSE
%{python3_sitelib}/enlighten*

%changelog
%autochangelog
