%global source0_hash 5f14fe3cc0e37fb15dae1ffd6c4c5f7bfec2bfaff0f82af21feec25b4d46c0ef

%global modname jnius
%global srcname py%{modname}
%global sum     Dynamic access to Java classes from Python

Name:           python-%{modname}
Version:        1.6.1
Release:        14%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/kivy/%{srcname}

ExclusiveArch:  %{java_arches}

Source0:        %{url}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

# Fix compatibility with Cython >= 3.1
# Backported from upstream:
# https://github.com/kivy/pyjnius/pull/753
# https://github.com/kivy/pyjnius/pull/756
Patch:          fix-cython-3.1-build.patch

BuildRequires:  make
# avoid strict pointer checks with gcc 14, https://bugs.gentoo.org/917562
BuildRequires:  clang

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(pytest)

BuildRequires:  python3dist(sphinx) 
BuildRequires:  python3dist(furo)

BuildRequires:  ant-openjdk25 
BuildRequires:  java-25-devel

ExclusiveArch:  %{java_arches}

# https://github.com/kivy/pyjnius/issues/307
#ExcludeArch:    ppc64 s390x

%description
%{summary}.

%package     -n python3-%{srcname}
Summary:        %{sum}
Requires:       java-25-headless
Requires:       python3-six
%{?python_provide:%python_provide python3-%{srcname}}
Provides:       python3-%{modname}

%description -n python3-%{srcname}
%{summary}.

%package        doc
Summary:        Documentation files for %{srcname}
BuildArch:      noarch

%description    doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
CC=%{_bindir}/clang %py3_build

make %{_smp_mflags} -C docs SPHINXBUILD='sphinx-build-3 %{_smp_mflags}' html

# build java classes for tests
# there is also Makefile, but it calls python setup.py build_ext --inplace
# together with ant, so we don't use it not to build python bits twice
ant all

%install
%py3_install

%check
pushd tests
export CLASSPATH=../build/test-classes:../build/classes
export JAVA_HOME=%{_prefix}/lib/jvm/java
# skip test failing with Python 3.13.0
k='not test_hierharchy_arraylist'
# json options fail on some arches
%ifarch s390x ppc64le riscv64
  k="${k} and not jvm_options"
%endif
%pytest -k "${k}" -v
popd

%files -n python3-%{srcname}
%license LICENSE
%doc *.md
%{python3_sitearch}/%{modname}/
%{python3_sitearch}/%{modname}_config.py*
%{python3_sitearch}/%{srcname}-%{version}-py*.egg-info/
%{python3_sitearch}/__pycache__/%{modname}_config.cpython-*.pyc
%exclude %{python3_sitearch}/__pycache__
%exclude %{python3_sitearch}/setup_sdist.py

%files doc
%license LICENSE
%doc docs/build/html/

%changelog
%autochangelog
