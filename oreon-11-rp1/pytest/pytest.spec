%global source0_hash 1088fbde8f2b49d95a549a195707afa7a76a3ce9bcadc26b6d71f0ffda5fe313
Name:           pytest
Version:        9.1.1
Release:        1%{?dist}
Summary:        Simple powerful testing with Python
License:        MIT
URL:            https://pytest.org
Source0:        https://files.pythonhosted.org/packages/source/p/pytest/pytest-%{version}.tar.gz
%undefine _py3_shebang_s
%bcond tests %{undefined rhel}
%bcond optional_tests %{with tests}
%bcond timeout %{with tests}
%bcond docs %{undefined rhel}
%if %{with tests}
%if %{with optional_tests}
%endif
%if %{with timeout}
%endif
%endif
%if %{with docs}
%endif
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2.3
Requires:       python3-pytest = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytest+dev
Summary:        Metapackage for python3-pytest dev extras
Requires:       python3-pytest = %{version}-%{release}
Requires:       python3dist(attrs) >= 19.2
Requires:       python3dist(hypothesis) >= 3.56
Provides:       python3dist(pytest[dev]) = %{version}-%{release}

%description -n python3-pytest+dev
Metapackage for python3-pytest dev extras.

%description
The pytest framework makes it easy to write small tests, yet scales to support
complex functional testing for applications and libraries.

%package -n python3-%{name}
Summary:        Simple powerful testing with Python
Provides:       pytest = %{version}-%{release}
%description -n python3-%{name}
The pytest framework makes it easy to write small tests, yet scales to support
complex functional testing for applications and libraries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version}

# documentation dependencies missing in Fedora
sed -i '/sphinxcontrib-towncrier/d' doc/en/requirements.txt
sed -i '/sphinxcontrib\.towncrier/d' doc/en/conf.py
sed -i '/sphinx_issues/d' doc/en/conf.py
sed -i '/sphinx-issues/d' doc/en/requirements.txt

%build

%pyproject_wheel
%if %{with docs}
for l in doc/* ; do
  %make_build -C $l html PYTHONPATH="$(pwd)/src"
done
for f in README CHANGELOG CONTRIBUTING ; do
  rst2html ${f}.rst > ${f}.html
done
%endif
%install
%pyproject_install
mv %{buildroot}%{_bindir}/pytest %{buildroot}%{_bindir}/pytest-%{python3_version}
ln -snf pytest-%{python3_version} %{buildroot}%{_bindir}/pytest-3
mv %{buildroot}%{_bindir}/py.test %{buildroot}%{_bindir}/py.test-%{python3_version}
ln -snf py.test-%{python3_version} %{buildroot}%{_bindir}/py.test-3
ln -snf pytest-%{python3_version} %{buildroot}%{_bindir}/pytest
ln -snf py.test-%{python3_version} %{buildroot}%{_bindir}/py.test
%if %{with docs}
mkdir -p _htmldocs/html
for l in doc/* ; do
  rm ${l}/_build/html/.buildinfo
  mv ${l}/_build/html _htmldocs/html/${l##doc/}
done
%endif
find %{buildroot}%{python3_sitelib} \
     -name '*.py' \
     -exec sed -i -e '1{/^#!/d}' {} \;
%oreon_autofiles main usr/lib/python3*/site-packages/pytest* usr/lib64/python3*/site-packages/pytest* usr/bin/*

%check

%if %{with tests}
%global __pytest %{buildroot}%{_bindir}/pytest
%pytest testing %{?with_timeout:--timeout=30} %{?with_optional_tests:-n auto} -rs
%else
%pyproject_check_import
%endif
%files
%files -n python3-pytest -f %{oreon_filedir}/python3-pytest.list

%changelog

%autochangelog
