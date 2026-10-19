%global source0_hash a709c3c77b9c6b08616e1c9e12a5a9b9d5ccc1f2dcf6f647f205018d77f819a7
Name:           omniORBpy
Version:        4.3.4
Release:        1%{?dist}
Summary:        CORBA ORB for Python
License:        LGPL-2.0-or-later
URL:            http://omniorb.sourceforge.net/
Source0:        http://sourceforge.net/projects/omniorb/files/%{name}/%{name}-%{version}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  omniORB-devel
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
# /oreon:deps
%description
omniORBpy is a robust high-performance CORBA ORB for Python.

%package -n python3-omniORB
Summary:        CORBA ORB for Python 3
Requires:       omniORB
%{?python_provide:%python_provide python3-omniORB}
%description -n python3-omniORB
Robust high-performance CORBA ORB for Python 3.

%package -n omniORBpy-devel
Summary:        C++ API for the CORBA ORB for Python
Requires:       omniORB-devel
BuildArch:      noarch
%description -n omniORBpy-devel
C++ API for the CORBA ORB for Python.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%global _configure ../configure
mkdir build_py3
pushd build_py3
export PYTHON=%{__python3}
%configure --with-omniorb=%{_prefix} --with-openssl=%{_prefix}
%make_build
popd
%install
%make_install -C build_py3
rm -f %{buildroot}%{python2_sitelib}/CORBA.py*
rm -f %{buildroot}%{python2_sitelib}/PortableServer.py*
rm -f %{buildroot}%{python3_sitelib}/CORBA.py*
rm -f %{buildroot}%{python3_sitelib}/PortableServer.py*
chmod +x %{buildroot}%{python3_sitearch}/*.so.*
find %{buildroot}%{python3_sitelib} -type d -exec chmod 755 {} \;
%oreon_autofiles python3-omniORB usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles omniORBpy-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n python3-omniORB -f %{oreon_filedir}/python3-omniORB.list
%files -n omniORBpy-devel -f %{oreon_filedir}/omniORBpy-devel.list

%changelog

%autochangelog
