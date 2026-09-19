%global source0_hash c97c614cac4703ed3709109a38791e7601c20892a00af91438fc5a10829308cc

%global srcname colcon-override-check

Name:           python-%{srcname}
Version:        0.0.1
Release:        11%{?dist}
Summary:        Extension for colcon to check for problems overriding installed packages

License:        Apache-2.0
URL:            https://github.com/colcon/%{srcname}
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
An extension for colcon-core to check for potential problems when overriding
installed packages. Most notably, warn the user when overriding a package upon
which other packages in an underlay depend, but ones which are not also being
overridden.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.8.0
Requires:       python%{python3_pkgversion}-colcon-installed-package-information
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to check for potential problems when overriding
installed packages. Most notably, warn the user when overriding a package upon
which other packages in an underlay depend, but ones which are not also being
overridden.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/colcon_override_check/
%{python3_sitelib}/colcon_override_check-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
