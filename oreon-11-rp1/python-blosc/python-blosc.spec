%global source1_hash cc4d93ba17eb3a9aad2396a4924d47e7798ce55abbd8134fb9de6d9a1d9b65d2
%global source0_hash 385f1deb32daaf78484a2cf7523f9854ea9041bea3ecbddff33bc95a651106f9
Name:           python-blosc
Summary:        Python wrapper for the Blosc high performance compressor
Version:        1.11.4
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            https://github.com/Blosc/python-blosc
Source0:        https://github.com/Blosc/python-blosc/archive/v%{version}/blosc-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/Blosc/python-blosc/f3c5e341a2504a03c225f4f1d9066ccdf4bd31dd/setup.py
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  blosc-devel
BuildRequires:  gcc
BuildRequires:  python3-cpuinfo
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-psutil
BuildRequires:  python3-setuptools
# /oreon:deps
%description
%{summary}.

%package -n python%{python3_pkgversion}-blosc
Summary:        Python wrapper for the blosc high performance compressor
Requires:       blosc%{_isa} >= 1.16.0
%{?python_provide:%python_provide python%{python3_pkgversion}-blosc}
%{?fedora:Recommends: python%{python3_pkgversion}-numpy}
%description -n python%{python3_pkgversion}-blosc
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Overwrite setup.py with the last version that does not use skbuild and cmake
cp %{SOURCE1} .

%build

export BLOSC_DIR=%{_libdir}/blosc CFLAGS="%{optflags}"
export DISABLE_BLOSC_AVX2=1
%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

cd / # avoid interference with build dir
PYTHONPATH=%{buildroot}%{python3_sitearch} %__python3 -c 'import sys, blosc; sys.exit(blosc.test())'
%files -f %{oreon_filedir}/main.list
%files -n python3-blosc -f %{oreon_filedir}/python3-blosc.list

%changelog

%autochangelog
