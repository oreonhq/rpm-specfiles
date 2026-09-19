%global source0_hash 91f14108b6f9db780fc5a579b9c809e9a8c62b688e81f2267788fd0e12f178dc

%global srcname colcon-cd

Name:           python-%{srcname}
Version:        0.2.1
Release:        9%{?dist}
Summary:        Extension for colcon to change the current working directory

License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

# Not submitted upstream
Patch0:         %{name}-0.1.1-install-data-files-manually.patch

%description
A shell function for colcon-core to change the current working directory.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.4.1
Requires:       python%{python3_pkgversion}-colcon-package-information
%endif

%description -n python%{python3_pkgversion}-%{srcname}
A shell function for colcon-core to change the current working directory.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

install -p -D function/colcon_cd.sh %{buildroot}%{_datadir}/colcon_cd/function/colcon_cd.sh

%check
%pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/colcon_cd/
%{python3_sitelib}/colcon_cd-%{version}-py%{python3_version}.egg-info/
%{_datadir}/colcon_cd/

%changelog
%autochangelog
