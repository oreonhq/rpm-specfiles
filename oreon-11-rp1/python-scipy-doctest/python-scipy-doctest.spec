%global source0_hash 7d215bc04823221b55400d4df249fdfe57dd779bea6cb024f20ec0015e7ce339
Name:           python-scipy-doctest
Version:        2.2.0
Release:        1%{?dist}
Summary:        Configurable, whitespace-insensitive, floating-point-aware doctest helpers
License:        BSD-3-Clause
URL:            https://github.com/scipy/scipy_doctest
Source0:        https://files.pythonhosted.org/packages/source/s/scipy_doctest/scipy_doctest-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
This project extends the standard library doctest module to allow flexibility
and easy customization of finding, parsing and checking code examples in
documentation.
Can be used either as drop-in doctest replacement or through the pytest
integration. Uses a floating-point aware doctest checker by default.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-scipy-doctest = %{version}-%{release}
# /oreon:deps
%package -n       python3-scipy-doctest+test
Summary:        Metapackage for python3-scipy-doctest test extras
Requires:       python3-scipy-doctest = %{version}-%{release}
Provides:       python3dist(scipy-doctest[test]) = %{version}-%{release}

%description -n python3-scipy-doctest+test
Metapackage for python3-scipy-doctest test extras.

%package -n       python3-scipy-doctest+doc
Summary:        Metapackage for python3-scipy-doctest doc extras
Requires:       python3-scipy-doctest = %{version}-%{release}
Requires:       python3dist(furo) == 2024.8.6
Requires:       python3dist(myst-parser) == 4.0.0
Requires:       python3dist(sphinx) == 8.1.3
Requires:       python3dist(sphinx-copybutton) == 0.5.2
Provides:       python3dist(scipy-doctest[doc]) = %{version}-%{release}

%description -n python3-scipy-doctest+doc
Metapackage for python3-scipy-doctest doc extras.

%description %{common_description}

%package     -n python3-scipy-doctest
Summary:        Configurable, whitespace-insensitive, floating-point-aware doctest helpers
# oreon:reqs
Requires:       python3dist(numpy) >= 1.19.5
# /oreon:reqs
%description -n python3-scipy-doctest %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-scipy-doctest usr/lib/python3*/site-packages/scipy_doctest* usr/lib64/python3*/site-packages/scipy_doctest* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/scipy_doctest* usr/lib64/python3*/site-packages/scipy_doctest* usr/bin/*

%check

export PYTHONPATH='%{buildroot}%{python3_sitelib}'
echo '==== Self-test with SciPy and MPL ====' 1>&2
%pytest --pyargs '%{buildroot}%{python3_sitelib}/scipy_doctest' -k "${k-}" -v
rm -rv '%{buildroot}%{python3_sitelib}/scipy_doctest/tests/.pytest_cache'
echo '==== Self-test CLI with SciPy and MPL ====' 1>&2
f='scipy_doctest/tests/finder_cases.py'
%{py3_test_envvars} %{python3} -m scipy_doctest \
    "%{buildroot}%{python3_sitelib}/${f}" -vv
echo '==== Test testfile CLI ====' 1>&2
f='scipy_doctest/tests/scipy_ndimage_tutorial_clone.rst'
%{py3_test_envvars} %{python3} -m scipy_doctest \
    "%{buildroot}%{python3_sitelib}/${f}" -v
echo '==== Test pytest plugin ====' 1>&2
for f in \
    'scipy_doctest/tests/module_cases.py' \
    'scipy_doctest/tests/stopwords_cases.py' \
    'scipy_doctest/tests/local_file_cases.py'
do
  %pytest "%{buildroot}%{python3_sitelib}/${f}" --doctest-modules -v
done
%files
%files -n python3-scipy-doctest -f %{oreon_filedir}/python3-scipy-doctest.list

%changelog

%autochangelog
