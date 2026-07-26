%global source0_hash caf47ac4c6346eef47fc11e799adbeaf645921c712cc099cf2530560e7ecde44

%global srcname cloud-sptheme
%global modname cloud_sptheme
%global sum A nice sphinx theme named 'Cloud', and some related extensions

Name:             python-%{srcname}
Version:          1.10.1
Release:          21%{?dist}
Summary:          %{sum}

# Automatically converted from old format: BSD - review is highly recommended.
License:          LicenseRef-Callaway-BSD
URL:              http://pypi.python.org/pypi/%{modname}
Source0:          %pypi_source %{modname} %{version} post20200504175005.tar.gz

BuildArch:        noarch

BuildRequires:    python3-sphinx

BuildRequires:    python3-devel
BuildRequires:    python3-setuptools

%description
This is a small package containing a Sphinx theme named "Cloud",
along with some related Sphinx extensions. To see an example
of the theme in action, check out it's documentation
at http://packages.python.org/cloud_sptheme.

%package -n python3-%{srcname}
Summary:    %{sum}
Requires:   python3-sphinx
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This is a small Python 3 package containing a Sphinx theme named "Cloud",
along with some related Sphinx extensions. To see an example
of the theme in action, check out it's documentation
at http://packages.python.org/cloud_sptheme.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{modname}-%{version}.post20200504175005

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README CHANGES docs/
%license LICENSE
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}*

%changelog
%autochangelog
