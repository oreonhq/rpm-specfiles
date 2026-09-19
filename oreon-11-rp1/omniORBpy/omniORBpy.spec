%global source0_hash a709c3c77b9c6b08616e1c9e12a5a9b9d5ccc1f2dcf6f647f205018d77f819a7

Name:           omniORBpy
Version:        4.3.4
Release:        2%{?dist}
Summary:        CORBA ORB for Python

License:        LGPL-2.0-or-later
URL:            http://omniorb.sourceforge.net/
Source0:        http://sourceforge.net/projects/omniorb/files/%{name}/%{name}-%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  omniORB-devel
BuildRequires:  python3-devel
BuildRequires:  openssl-devel

%description
omniORBpy is a robust high-performance CORBA ORB for Python.

%package -n python3-omniORB
Summary:        CORBA ORB for Python 3
# For %%{python3_sitelib}/omniidl_be
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

%autosetup -p1

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

# Remove files which conflict with pyorbit, their sole purpose is to to export the modules to the global namespace via
# sys.modules["<Module>"] = omniORB.<Module>
rm -f %{buildroot}%{python2_sitelib}/CORBA.py*
rm -f %{buildroot}%{python2_sitelib}/PortableServer.py*
rm -f %{buildroot}%{python3_sitelib}/CORBA.py*
rm -f %{buildroot}%{python3_sitelib}/PortableServer.py*

# Ensure shared libraries are executable, otherwise they are not stripped
chmod +x %{buildroot}%{python3_sitearch}/*.so.*

# Fix directory permissions
find %{buildroot}%{python3_sitelib} -type d -exec chmod 755 {} \;

%files -n python3-omniORB
%doc README.Python README.txt ReleaseNotes.txt update.log
%license COPYING.LIB
%{python3_sitelib}/CosNaming*
%{python3_sitelib}/PortableServer__POA.py*
%{python3_sitelib}/omniORB.pth
%{python3_sitelib}/omniORB/
%{python3_sitelib}/__pycache__/*
%{python3_sitearch}/*_omni*.so*

%files -n omniORBpy-devel
%license COPYING.LIB
# %%{_includedir}/omniORB4 is in omniORB-devel
%{_includedir}/omniORB4/*
%{_includedir}/omniORBpy.h
# %%{python3_sitelib}/omniidl_be/__init__.py is in omniORB
%exclude %{python3_sitelib}/omniidl_be/__init__.py
%exclude %{python3_sitelib}/omniidl_be/__pycache__/__init__.*
%{python3_sitelib}/omniidl_be/*

%changelog
%autochangelog
