%global source0_hash ab700375e77a5213e8def1f61c2d83ca1b50ff9b56b541992dc54784c1274c52

%bcond_without tests

Name:           python-mock
Version:        5.2.0
Release:        %autorelease
Summary:        Deprecated, use unittest.mock from the standard library instead

License:        BSD-2-Clause
URL:            https://github.com/testing-cabal/mock
Source0:        https://github.com/testing-cabal/mock/archive/%{version}/mock-%{version}.tar.gz
Patch1:         f3e3d82aab.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-six
%endif

%description
This is a deprecated package.

The mock module is now part of the Python standard library,
available as unittest.mock in Python 3.3 onwards.

%package -n python%{python3_pkgversion}-mock
Summary:        %{summary}
Provides:       deprecated()

%description -n python%{python3_pkgversion}-mock
This is a deprecated package.

The mock module is now part of the Python standard library,
available as unittest.mock in Python 3.3 onwards.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n mock-%{version}

%build
%py3_build

%if %{with tests}
%check
%pytest
%endif

%install
%py3_install

%files -n python%{python3_pkgversion}-mock
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/mock/

%changelog
%autochangelog
