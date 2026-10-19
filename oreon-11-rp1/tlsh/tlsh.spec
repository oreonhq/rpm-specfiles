%global source0_hash 2e513993b6b08380dd03777c22caab33a6d0d93ef230250b1b12027d9b7d8a4b
%undefine __cmake_in_source_build
Name:           tlsh
Version:        5.0.0
Release:        1%{?dist}
Summary:        Fuzzy text matching library
License:        Apache-2.0
URL:            https://github.com/trendmicro/tlsh
Source0:        https://github.com/trendmicro/tlsh/archive/%{version}/tlsh-%{version}.tar.gz
Patch:          0001-python-use-setuptools-instead-of-distutils.patch
Patch:          0002-python-drop-pointless-line-continuations.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description

%package doc
Summary: Documentation for TLSH
BuildArch: noarch
%description doc
%{summary}.

%package -n python3-tlsh
Summary:        Python 3 interface for TLSH
%{?python_provide:%python_provide python3-tlsh}
Obsoletes: tlsh < 3.17.0
Obsoletes: tlsh-devel < 3.17.0
%description -n python3-tlsh

This package contains the %{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# I'm just loving cmake more every day
echo 'set(CMAKE_CXX_FLAGS "%{optflags} -fPIC")' | \
     tee -a src/CMakeLists.txt |\
     tee -a test/CMakeLists.txt |\
     tee -a utils/CMakeLists.txt

sed -r -i '/CMAKE_EXE_LINKER_FLAGS.*-static-libstdc/d' CMakeLists.txt

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build
pushd py_ext
%py3_build
popd
%install
pushd py_ext
%py3_install
popd
%global _docdir_fmt %{name}
%oreon_autofiles python3-tlsh usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

bin/simple_unittest
bin/timing_unittest
bin/tlsh_unittest -c bin/tlsh_unittest -f bin/tlsh_unittest | grep -E '\b0\b'
bin/tlsh_unittest -c bin/tlsh_unittest -f bin/simple_unittest | grep -vE '\b0\b'
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} \
        -c "import tlsh; print(tlsh.hash(open('LICENSE', 'rb').read()))"
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n tlsh-doc -f %{oreon_filedir}/tlsh-doc.list
%files -n python3-tlsh -f %{oreon_filedir}/python3-tlsh.list

%changelog

%autochangelog
