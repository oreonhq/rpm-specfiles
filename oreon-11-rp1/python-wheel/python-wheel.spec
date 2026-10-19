%global source0_hash 398fe0a1a609b1084bcab897c65596613544fbe6109408e505e29e4ce0c3175d
%bcond bootstrap 0
%bcond tests %{without bootstrap}
%bcond main_python 1
Name:           python-wheel
Version:        0.45.1
Release:        1%{?dist}
Epoch:          1
Summary:        Built-package format for Python
%{?oreon:%global python_wheel_pkg_prefix python3}
License:        MIT AND (Apache-2.0 OR BSD-2-Clause)
URL:            https://github.com/pypa/wheel
Source0:        https://github.com/pypa/wheel/archive/refs/tags/0.45.1.tar.gz#/wheel-0.45.1.tar.gz
Patch:          https://github.com/pypa/wheel/commit/3028d3.patch
Patch:        adjusts-tests-for-setuptools-78.patch
Patch:        CVE-2026-24049.patch
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.8
Requires:       python3-wheel = %{version}-%{release}
# /oreon:deps
%package -n       python3-wheel+test
Summary:        Metapackage for python3-wheel test extras
Requires:       python3-wheel = %{version}-%{release}
Requires:       python3dist(pytest) >= 6.0.0
Requires:       python3dist(setuptools) >= 65
Provides:       python3dist(wheel[test]) = %{version}-%{release}

%description -n python3-wheel+test
Metapackage for python3-wheel test extras.

%description

# Virtual provides for the packages bundled by wheel.
# %%{_rpmconfigdir}/pythonbundles.py src/wheel/vendored/vendor.txt --namespace 'python%%{python3_pkgversion}dist'
%global bundled %{expand:
Provides: bundled(python%{python3_pkgversion}dist(packaging)) = 24
}

%package -n     python%{python3_pkgversion}-wheel
Summary:        Built-package format for Python
%{bundled}
%description -n python%{python3_pkgversion}-wheel

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir wheel-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
mv %{buildroot}%{_bindir}/wheel{,-%{python3_version}}
%if %{with main_python}
ln -s wheel-%{python3_version} %{buildroot}%{_bindir}/wheel-3
ln -s wheel-3 %{buildroot}%{_bindir}/wheel
%oreon_autofiles main usr/lib/python3*/site-packages/wheel* usr/lib64/python3*/site-packages/wheel* usr/bin/*
%endif
%check

%{_rpmconfigdir}/pythonbundles.py src/wheel/vendored/vendor.txt --namespace 'python%{python3_pkgversion}dist' --compare-with '%{bundled}'
%{py3_test_envvars} wheel-%{python3_version} version
%py3_check_import wheel
%if %{with tests}
%pytest -v --ignore build
%endif
%files
%files -n python3-wheel -f %{oreon_filedir}/python3-wheel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.45.1-1
- Prepare for Oreon 11 (RP1)
