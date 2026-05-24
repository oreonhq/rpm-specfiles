%bcond tests 1
%if 0%{?oreon}
%bcond_with tests
%endif
%bcond pytest_mock %{undefined rhel}
%bcond wheel %{undefined rhel}
%if 0%{?oreon} || 0%{?rhel}
%bcond patchelf 0
%else
%bcond patchelf %{expr:%{undefined rhel} || %{defined epel}}
%endif

%global pmd_bootstrap_ver 0.11.0

Name:           python-meson-python
Summary:        Meson Python build backend (PEP 517)
Version:        0.19.0
Release:        4%{?dist}

License:        MIT
URL:            https://github.com/mesonbuild/meson-python
Source0:        https://files.pythonhosted.org/packages/source/m/meson-python/meson_python-%{version}.tar.gz
Source1:        https://github.com/FFY00/python-pyproject-metadata/archive/%{pmd_bootstrap_ver}/pyproject-metadata-%{pmd_bootstrap_ver}.tar.gz
Patch100:       meson-python-0.18.0-remove-patchelf.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  pyproject-rpm-macros >= 1.15.1
BuildRequires:  meson >= 1.2.3
BuildRequires:  python3-packaging
BuildRequires:  python3-flit-core
%if %{with tests}
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
%endif

%global common_description %{expand:
meson-python is a Python build backend built on top of the Meson build system.
It enables to use Meson for the configuration and build steps of Python
packages. Meson is an open source build system meant to be both extremely fast,
and, even more importantly, as user friendly as possible. meson-python is best
suited for building Python packages containing extension modules implemented in
languages such as C, C++, Cython, Fortran, Pythran, or Rust. Consult the
documentation for more details.}

%description %{common_description}

%package -n     python3-meson-python
Summary:        %{summary}
Requires:       meson >= 1.2.3
Requires:       python3-packaging
Requires:       python3-pyproject-metadata >= 0.9.0
%if %{with patchelf}
BuildRequires:  /usr/bin/patchelf
Requires:       /usr/bin/patchelf
%endif
%py_provides    python3-mesonpy
Provides:       python3dist(meson-python) = %{version}

%description -n python3-meson-python %{common_description}

%prep
%autosetup -n meson_python-%{version} -p1
%if %{without patchelf}
%patch 100 -p1
%endif
sed -r -i "s/^  '(build|pytest-cov)/#&/" pyproject.toml
%if %{without pytest_mock}
sed -r -i "s/^  '(pytest-mock)/#&/" pyproject.toml
%endif
%if %{without wheel}
sed -r -i "s/^  '(wheel)/#&/" pyproject.toml
%endif
%if %{with tests}
git init -q
git add -A
git -c user.email=packaging@oreonhq.com -c user.name=Oreon commit -q -m . --allow-empty
%endif
mkdir -p %{_builddir}/meson-py-bootstrap%{python3_sitearch}
tar -C %{_builddir} -xf %{SOURCE1}
%pushd %{_builddir}/pyproject-metadata-%{pmd_bootstrap_ver}
%pyproject_wheel -w %{_builddir}/pmd-bootstrap-wheel
%popd
python3 -m pip install --target %{_builddir}/meson-py-bootstrap%{python3_sitearch} \
  --no-index --find-links %{_builddir}/pmd-bootstrap-wheel pyproject-metadata

%generate_buildrequires
export PYTHONPATH=%{_builddir}/meson-py-bootstrap%{python3_sitearch}${PYTHONPATH:+:${PYTHONPATH}}
%pyproject_buildrequires -p %{?with_tests:-g test}
brfile=$(ls ../*pyproject-buildrequires 2>/dev/null | head -1)
if test -n "$brfile"; then
  sed -i -e '/^python3dist(pyproject-metadata)/d' -e '/^python3-pyproject-metadata/d' "$brfile"
fi

%build
export PYTHONPATH=%{_builddir}/meson-py-bootstrap%{python3_sitearch}${PYTHONPATH:+:${PYTHONPATH}}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mesonpy

%check
%if %{with tests}
export PYTHONPATH=%{_builddir}/meson-py-bootstrap%{python3_sitearch}${PYTHONPATH:+:${PYTHONPATH}}
ignore="${ignore-} --ignore=tests/test_pep518.py"
%if %{without pytest_mock}
k="${k-}${k+ and }not test_invalid_build_dir"
k="${k-}${k+ and }not test_use_ansi_escapes"
%endif
%if %{without wheel}
ignore="${ignore-} --ignore=tests/test_editable.py"
ignore="${ignore-} --ignore=tests/test_wheel.py"
ignore="${ignore-} --ignore=tests/test_wheelfile.py"
%endif
%if %{without patchelf}
k="${k-}${k+ and }not test_contents"
k="${k-}${k+ and }not test_local_lib"
k="${k-}${k+ and }not test_rpath"
k="${k-}${k+ and }not test_get_requires_for_build_wheel"
k="${k-}${k+ and }not test_uneeded_rpath"
%endif
%pytest ${ignore-} -k "${k-}"
%endif

%files -n python3-meson-python -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.rst

%changelog
* Sun May 24 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.19.0-4
- bootstrap pyproject-metadata at build time (no repo dep for mock)

* Sun May 24 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.19.0-3
- classic spec (no BuildSystem tag) for spectool/rpmbuild

* Sat May 23 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.19.0-2
- no patchelf on oreon, provide python3dist(meson-python)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.19.0-1
- Prepare for Oreon 11 (RP1)
