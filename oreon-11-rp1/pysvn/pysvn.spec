%global source0_hash 33d2f352bffa15949458541d18ce84c35ff2484e42fd0edc3578be8c66be25d6
Name:           pysvn
Version:        1.9.25
Release:        1%{?dist}
Summary:        Pythonic style bindings for Subversion
License:        Apache-1.1
URL:            https://pysvn.sourceforge.io/
Source0:        http://pysvn.barrys-emacs.org/source_kits/%{name}-%{version}.tar.gz
Patch0001: initlocale.patch
# oreon:deps
BuildRequires:  apr-devel
BuildRequires:  gcc-c++
BuildRequires:  glibc-langpack-en
BuildRequires:  krb5-devel
BuildRequires:  make
BuildRequires:  neon-devel
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pycxx-devel
BuildRequires:  subversion
BuildRequires:  subversion-devel
# /oreon:deps
%description

%package -n python3-pysvn
Summary: Pythonic style bindings for Subversion
%{?python_provide:%python_provide python3-pysvn}
BuildRequires:    python3-devel
BuildRequires:    python3-pycxx-devel >= 7.1.8
%description -n python3-pysvn

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

# Remove bundled libs
rm -rf Import

%build

pushd Source
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py configure \
    --enable-debug --verbose --fixed-module-name --norpath
echo "optflags %{optflags}"
%{__sed} -i -e 's@-Wall -fPIC -fexceptions -frtti@%{optflags} -fPIC -frtti@' Makefile
%{__make} %{?_smp_mflags}
%install
%{__install} -d -m 755 %{buildroot}%{python3_sitearch}/%{name}
%{__install} -p -m 644 Source/pysvn/__init__.py %{buildroot}%{python3_sitearch}/%{name}
%{__install} -p -m 755 Source/pysvn/_pysvn.so %{buildroot}%{python3_sitearch}/%{name}
%oreon_autofiles python3-pysvn usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd Tests
LC_ALL=en_US.UTF-8 %{__make} -j1
popd
%files -f %{oreon_filedir}/main.list
%files -n python3-pysvn -f %{oreon_filedir}/python3-pysvn.list

%changelog

%autochangelog
