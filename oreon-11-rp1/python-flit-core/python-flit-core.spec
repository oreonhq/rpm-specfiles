%global source0_hash 18f63100d6f94385c6ed57a72073443e1a71a4acb4339491615d0f16d6ff01b2

# When bootstrapping new Python we need to build flit in bootstrap mode.
# The Python RPM dependency generators and pip are not yet available.
%bcond bootstrap 0

# Tests are enabled by default, unless we bootstrap.
# Disable them to avoid a circular build dependency on testpath.
%bcond tests %{without bootstrap}

Name:           python-flit-core
Version:        3.12.0
Release:        %autorelease
Summary:        PEP 517 build backend for packages using Flit

# flit-core is BSD-3-Clause
# flit_core/versionno.py contains a regex that is from packaging, BSD-2-Clause
License:        BSD-3-Clause AND BSD-2-Clause

URL:            https://flit.pypa.io/
Source:        https://files.pythonhosted.org/packages/source/f/flit_core/flit_core-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel

%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
# Test deps that require flit-core to build:
BuildRequires:  python%{python3_pkgversion}-testpath
%endif

%global _description %{expand:
This provides a PEP 517 build backend for packages using Flit.
The only public interface is the API specified by PEP 517,
at flit_core.buildapi.}

%description %_description


%package -n python%{python3_pkgversion}-flit-core
Summary:        %{summary}

# RPM generators are not yet available when we bootstrap
%if %{with bootstrap}
Provides:       python%{python3_pkgversion}dist(flit-core) = %{version}
Provides:       python%{python3_version}dist(flit-core) = %{version}
Requires:       python(abi)
%endif

%description -n python%{python3_pkgversion}-flit-core %_description


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n flit_core-%{version}

# Remove vendored tomli that flit_core includes to solve the circular dependency on older Pythons
# (flit_core requires tomli, but flit_core is needed to build tomli).
# We don't use this, as tomllib is a part of standard library since Python 3.11.
# Remove the bits looking for the license files of the vendored tomli.
rm -rf flit_core/vendor
sed -iE 's/, *"flit_core\/vendor\/\*\*\/LICENSE\*"//' pyproject.toml


%if %{without bootstrap}
%generate_buildrequires
%pyproject_buildrequires
%endif


%build
%if %{with bootstrap}
%{python3} -m flit_core.wheel
%else
%pyproject_wheel
%endif

%install
%if %{with bootstrap}
%{python3} bootstrap_install.py --install-root %{buildroot} dist/flit_core-%{version}-py3-none-any.whl
# for consistency with %%pyproject_install/brp-python-rpm-in-distinfo:
echo rpm > %{buildroot}%{python3_sitelib}/flit_core-%{version}.dist-info/INSTALLER
rm %{buildroot}%{python3_sitelib}/flit_core-%{version}.dist-info/RECORD
%else
%pyproject_install
%endif

%check
%py3_check_import flit_core flit_core.buildapi
%if %{with tests}
%pytest
%endif


%files -n python%{python3_pkgversion}-flit-core
%doc README.rst
%{python3_sitelib}/flit_core-*.dist-info/
%license %{python3_sitelib}/flit_core-*.dist-info/licenses/LICENSE
%{python3_sitelib}/flit_core/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.12.0-1
- Prepare for Oreon 11 (RP1)
