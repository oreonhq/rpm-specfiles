%global source0_hash 5f14fe3cc0e37fb15dae1ffd6c4c5f7bfec2bfaff0f82af21feec25b4d46c0ef
%global modname jnius
%global srcname py%{modname}
%global sum     Dynamic access to Java classes from Python
Name:           python-%{modname}
Version:        1.6.1
Release:        1%{?dist}
Summary:        Dynamic access to Java classes from Python
License:        MIT
URL:            https://github.com/kivy/%{srcname}
ExclusiveArch:  %{java_arches}
Source0:        https://github.com/kivy/%{srcname}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Patch:          fix-cython-3.1-build.patch
ExclusiveArch:  %{java_arches}
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  clang
BuildRequires:  java-25-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(furo)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
# /oreon:deps
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
ant all
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd tests
export CLASSPATH=../build/test-classes:../build/classes
export JAVA_HOME=%{_prefix}/lib/jvm/java
k='not test_hierharchy_arraylist'
%ifarch s390x ppc64le riscv64
  k="${k} and not jvm_options"
%endif
%pytest -k "${k}" -v
popd
%files -f %{oreon_filedir}/main.list
%files -n python3-pyjnius -f %{oreon_filedir}/python3-pyjnius.list
%files -n python-jnius-doc -f %{oreon_filedir}/python-jnius-doc.list

%changelog

%autochangelog
