%global source0_hash 8b0e9d10c784bf7d262c4e5ec5d4ec94127ce206e8738f29a437945fbc219b70
%global srcname setuptools
%bcond bootstrap 0
%bcond tests %[%{without bootstrap} && %{defined fedora}]
%global python_wheel_name %{srcname}-%{version}-py3-none-any.whl
Name:           python-setuptools
Version:        80.10.2
Release:        1%{?dist}
Summary:        Easily build and distribute Python packages
%{?oreon:%global python_wheel_pkg_prefix python3}
License:        MIT AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0) AND LGPL-3.0-only
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/s/setuptools/setuptools-80.10.2.tar.gz
Patch:        Remove-optional-or-unpackaged-test-deps.patch
Patch:        Adjust-the-setup.py-install-deprecation-message.patch
Patch:        Revert-Always-rewrite-a-Python-shebang-to-python.patch
Patch:          https://github.com/pypa/setuptools/pull/5194.patch
BuildArch:      noarch
%if %{with bootstrap}
%endif
%if %{with tests}
%endif
%if %{without bootstrap}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-setuptools = %{version}-%{release}
# /oreon:deps
%package -n       python3-setuptools+test
Summary:        Metapackage for python3-setuptools test extras
Requires:       python3-setuptools = %{version}-%{release}
Requires:       python3dist(pytest) >= 6
Requires:       python3dist(virtualenv) >= 13.0.0
Requires:       python3dist(wheel) >= 0.44.0
Requires:       python3dist(pip) >= 19.1
Requires:       python3dist(packaging) >= 24.2
Requires:       python3dist(jaraco.envs) >= 2.2
Requires:       python3dist(pytest-xdist) >= 3
Requires:       python3dist(jaraco.path) >= 3.7.2
Requires:       python3dist(build[virtualenv]) >= 1.0.3
Requires:       python3dist(filelock) >= 3.4.0
Requires:       python3dist(ini2toml[lite]) >= 0.14
Requires:       python3dist(tomli-w) >= 1.0.0
Requires:       python3dist(jaraco.develop) >= 7.21
Requires:       python3dist(pytest-home) >= 0.5
Requires:       python3dist(pyproject-hooks)
Requires:       python3dist(jaraco.test) >= 5.5
Provides:       python3dist(setuptools[test]) = %{version}-%{release}

%description -n python3-setuptools+test
Metapackage for python3-setuptools test extras.

%package -n       python3-setuptools+doc
Summary:        Metapackage for python3-setuptools doc extras
Requires:       python3-setuptools = %{version}-%{release}
Requires:       python3dist(sphinx) >= 3.5
Requires:       python3dist(jaraco.packaging) >= 9.3
Requires:       python3dist(rst.linker) >= 1.9
Requires:       python3dist(jaraco.tidelift) >= 1.4
Requires:       python3dist(pygments-github-lexers) == 0.0.5
Requires:       python3dist(sphinx-notfound-page) >= 1
Requires:       python3dist(sphinx-notfound-page) < 2
Requires:       python3dist(pyproject-hooks)
Requires:       python3dist(towncrier) < 24.7
Provides:       python3dist(setuptools[doc]) = %{version}-%{release}

%description -n python3-setuptools+doc
Metapackage for python3-setuptools doc extras.

%package -n       python3-setuptools+ssl
Summary:        Metapackage for python3-setuptools ssl extras
Requires:       python3-setuptools = %{version}-%{release}
Provides:       python3dist(setuptools[ssl]) = %{version}-%{release}

%description -n python3-setuptools+ssl
Metapackage for python3-setuptools ssl extras.

%package -n       python3-setuptools+certs
Summary:        Metapackage for python3-setuptools certs extras
Requires:       python3-setuptools = %{version}-%{release}
Provides:       python3dist(setuptools[certs]) = %{version}-%{release}

%description -n python3-setuptools+certs
Metapackage for python3-setuptools certs extras.

%package -n       python3-setuptools+core
Summary:        Metapackage for python3-setuptools core extras
Requires:       python3-setuptools = %{version}-%{release}
Requires:       python3dist(packaging) >= 24.2
Requires:       python3dist(more-itertools) >= 8.8
Requires:       python3dist(jaraco.text) >= 3.7
Requires:       python3dist(importlib-metadata) >= 6
Requires:       python3dist(tomli) >= 2.0.1
Requires:       python3dist(wheel) >= 0.43.0
Requires:       python3dist(platformdirs) >= 4.2.2
Requires:       python3dist(jaraco.functools) >= 4
Provides:       python3dist(setuptools[core]) = %{version}-%{release}

%description -n python3-setuptools+core
Metapackage for python3-setuptools core extras.

%package -n       python3-setuptools+check
Summary:        Metapackage for python3-setuptools check extras
Requires:       python3-setuptools = %{version}-%{release}
Requires:       python3dist(pytest-checkdocs) >= 2.4
Requires:       python3dist(pytest-ruff) >= 0.2.1
Requires:       python3dist(ruff) >= 0.8.0
Provides:       python3dist(setuptools[check]) = %{version}-%{release}

%description -n python3-setuptools+check
Metapackage for python3-setuptools check extras.

%package -n       python3-setuptools+cover
Summary:        Metapackage for python3-setuptools cover extras
Requires:       python3-setuptools = %{version}-%{release}
Provides:       python3dist(setuptools[cover]) = %{version}-%{release}

%description -n python3-setuptools+cover
Metapackage for python3-setuptools cover extras.

%package -n       python3-setuptools+enabler
Summary:        Metapackage for python3-setuptools enabler extras
Requires:       python3-setuptools = %{version}-%{release}
Requires:       python3dist(pytest-enabler) >= 2.2
Provides:       python3dist(setuptools[enabler]) = %{version}-%{release}

%description -n python3-setuptools+enabler
Metapackage for python3-setuptools enabler extras.

%package -n       python3-setuptools+type
Summary:        Metapackage for python3-setuptools type extras
Requires:       python3-setuptools = %{version}-%{release}
Requires:       python3dist(mypy) == 1.14.*
Requires:       python3dist(importlib-metadata) >= 7.0.2
Requires:       python3dist(jaraco.develop) >= 7.21
Provides:       python3dist(setuptools[type]) = %{version}-%{release}

%description -n python3-setuptools+type
Metapackage for python3-setuptools type extras.

%description
Setuptools is a collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially ones that
have dependencies on other packages.

This package also contains the runtime components of setuptools, necessary to
execute the software that requires pkg_resources.

# Virtual provides for the packages bundled by setuptools.
# Bundled packages are defined in multiple files. Generate the list with:
# pip freeze --path setuptools/_vendor > vendored.txt
# %%{_rpmconfigdir}/pythonbundles.py --namespace 'python%%{python3_pkgversion}dist' vendored.txt
%global bundled %{expand:
Provides: bundled(python%{python3_pkgversion}dist(autocommand)) = 2.2.2
Provides: bundled(python%{python3_pkgversion}dist(backports-tarfile)) = 1.2
Provides: bundled(python%{python3_pkgversion}dist(importlib-metadata)) = 8.7.1
Provides: bundled(python%{python3_pkgversion}dist(jaraco-context)) = 6.1
Provides: bundled(python%{python3_pkgversion}dist(jaraco-functools)) = 4.4
Provides: bundled(python%{python3_pkgversion}dist(jaraco-text)) = 4
Provides: bundled(python%{python3_pkgversion}dist(more-itertools)) = 10.8
Provides: bundled(python%{python3_pkgversion}dist(packaging)) = 26
Provides: bundled(python%{python3_pkgversion}dist(platformdirs)) = 4.4
Provides: bundled(python%{python3_pkgversion}dist(tomli)) = 2.4
Provides: bundled(python%{python3_pkgversion}dist(wheel)) = 0.46.3
Provides: bundled(python%{python3_pkgversion}dist(zipp)) = 3.23
}

%package -n python%{python3_pkgversion}-setuptools
Summary:        Easily build and distribute Python 3 packages
%{bundled}
%py_provides    python%{python3_pkgversion}-pkg_resources
%py_provides    python%{python3_pkgversion}-pkg-resources
%description -n python%{python3_pkgversion}-setuptools
Setuptools is a collection of enhancements to the Python 3 distutils that allow
you to more easily build and distribute Python 3 packages, especially ones that
have dependencies on other packages.

This package also contains the runtime components of setuptools, necessary to
execute the software that requires pkg_resources.

%package -n     %{python_wheel_pkg_prefix}-%{srcname}-wheel
Summary:        The setuptools wheel
Provides:        python-setuptools-wheel = %{version}-%{release}
Provides:        python%{python3_pkgversion}-setuptools-wheel = %{version}-%{release}
%{bundled}
%description -n %{python_wheel_pkg_prefix}-%{srcname}-wheel
A Python wheel of setuptools to use with venv.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{srcname}-%{version}
%if %{without bootstrap}
# If we don't have setuptools installed yet, we use the pre-generated .egg-info
# See https://github.com/pypa/setuptools/pull/2543
# And https://github.com/pypa/setuptools/issues/2550
# WARNING: We cannot remove this folder since Python 3.11.1,
#          see https://github.com/pypa/setuptools/issues/3761
#rm -r %%{srcname}.egg-info
%endif

# Strip shbang
find setuptools pkg_resources -name \*.py | xargs sed -i -e '1 {/^#!\//d}'
# Remove bundled exes
rm -f setuptools/*.exe
# Don't ship these
rm -r docs/conf.py
# Remove a filter for coverage warning from pytest config
# In pytest < 9, such a warning filter triggers ImportError without coverage
sed -i '/:coverage/d' pytest.ini

%if %{without bootstrap}
%build

%if %{with bootstrap}
%{python3} setup.py bdist_wheel
mkdir -p %{_pyproject_wheeldir}
mv dist/%{python_wheel_name} %{_pyproject_wheeldir}
%else
%pyproject_wheel
%endif
%install
%if %{with bootstrap}
mkdir -p %{buildroot}%{python3_sitelib}
unzip %{_pyproject_wheeldir}/%{python_wheel_name} -d %{buildroot}%{python3_sitelib} -x setuptools-%{version}.dist-info/RECORD
echo rpm > %{buildroot}%{python3_sitelib}/setuptools-%{version}.dist-info/INSTALLER
%else
%pyproject_install
sed -Ei '/\/tests\b/d' %{pyproject_files}
%endif
find %{buildroot}%{python3_sitelib} -name tests -print0 | xargs -0 rm -r
mkdir -p %{buildroot}%{python_wheel_dir}
install -p %{_pyproject_wheeldir}/%{python_wheel_name} -t %{buildroot}%{python_wheel_dir}
%{?python_wheel_inject_sbom:%python_wheel_inject_sbom %{buildroot}%{python_wheel_dir}/%{python_wheel_name}}
%oreon_autofiles main usr/lib/python3*/site-packages/setuptools* usr/lib64/python3*/site-packages/setuptools* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{without bootstrap}
%{python3} -m pip freeze --path setuptools/_vendor > vendored.txt
%{_rpmconfigdir}/pythonbundles.py vendored.txt --namespace 'python%{python3_pkgversion}dist' --compare-with '%{bundled}'
test $(stat --format %%s %{_pyproject_wheeldir}/%{python_wheel_name}) -lt 1300000
%pyproject_check_import -e '*.tests' -e '*.tests.*'
%endif
test ! -d %{buildroot}%{python3_sitelib}/pkg_resources/tests
test ! -d %{buildroot}%{python3_sitelib}/setuptools/tests
test ! -d %{buildroot}%{python3_sitelib}/setuptools/_distutils/tests
%if %{with tests}
PRE_BUILT_SETUPTOOLS_WHEEL=%{_pyproject_wheeldir}/%{python_wheel_name} \
PIP_NO_BUILD_ISOLATION=0 \
PYTHONPATH=$(pwd) %pytest \
 -n auto \
 --ignore=setuptools/tests/integration/ \
 --ignore=setuptools/tests/test_editable_install.py \
 --ignore=setuptools/tests/config/test_apply_pyprojecttoml.py \
 --ignore=tools \
 -k "not test_wheel_includes_cli_scripts and not test_equivalent_output"
%endif
%files
%files -n python3-setuptools -f %{oreon_filedir}/python3-setuptools.list
%files -n python3-setuptools-wheel -f %{oreon_filedir}/python3-setuptools-wheel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 80.10.2-1
- Prepare for Oreon 11 (RP1)
%endif
