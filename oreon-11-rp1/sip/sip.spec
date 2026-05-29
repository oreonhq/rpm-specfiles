%global source0_hash none

%bcond_without python3
%if (0%{?fedora} && 0%{?fedora} < 32) || (0%{?rhel} && 0%{?rhel} < 9) || 0%{?oreon}
%bcond_without python2
%endif

%if %{with python3}
%{!?python3_inc:%global python3_inc %(%{__python3} -c "from distutils.sysconfig import get_python_inc; print(get_python_inc(1))")}
%endif
%{!?__python2:%global __python2 /usr/bin/python2}
%{!?python2_sitearch:%global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%{!?python2_inc:%global python2_inc %(%{__python2} -c "from distutils.sysconfig import get_python_inc; print get_python_inc(1)")}

%if 0%{?fedora} > 31 || 0%{?rhel} > 8 || 0%{?oreon}
%global PYINCLUDE %{_includedir}/python%{python3_version}
%else
%global PYINCLUDE %{_includedir}/python%{python3_version}m
%endif

%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

# see also https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/JQQ66XJSIT2FGTK2YQY7AXMEH5IXMPUX/
%undefine _strict_symbol_defs_build

# provide non-namespace python modules
# needed by at least some legacy/non-qt consumers, e.g. pykde4
%if 0%{?fedora} && 0%{?fedora} < 31 || 0%{?oreon}
%global no_namespace 1
%endif

# Stop building siplib for wx on F34+
%if 0%{?fedora} && 0%{?fedora} >= 34 || 0%{?oreon}
%global wx_siplib 0
%else
%global wx_siplib 1
%endif

# Stop building PyQt5.sip on F35+
%if 0%{?fedora} && 0%{?fedora} >= 35 || 0%{?oreon}
%global pyqt5_sip 0
%else
%global pyqt5_sip 1
%endif

Summary: SIP - Python/C++ Bindings Generator
Name: sip
Version: 4.19.25
Release: 20%{?dist}

# sipgen/parser.{c.h} is GPLv3+ with exceptions (bison)
# Automatically converted from old format: GPLv2 or GPLv3 and (GPLv3+ with exceptions) - review is highly recommended.
License: GPL-2.0-only OR GPL-3.0-only AND (LicenseRef-Callaway-GPLv3+-with-exceptions)
Url: https://riverbankcomputing.com/software/sip/intro
Source0:        https://riverbankcomputing.com/static/Downloads/sip/4.19.25/sip-4.19.25%{?snap:.%{snap}}.tar.gz

Source10: sip-wrapper.sh

## upstream patches

## upstreamable patches
# make install should not strip (by default), kills -debuginfo
Patch50: sip-4.18-no_strip.patch
# try not to rpath the world (I *think* this may not be required anymore, since sip-4.19 -- rex)
Patch51: sip-4.18-no_rpath.patch
# set sip_bin properly for python3 build (needswork to be upstreamable)
# no longer needed?  keep for a little while before dropping completely -- rex
#Patch52: sip-4.19.3-python3_sip_bin.patch
# Avoid hardcoding sip.so (needed for wxpython's siplib.so)
Patch53: sip-4.19.18-no_hardcode_sip_so.patch
# Recognize the py_ssize_t_clean directive to avoid FTBFS with PyQt 5.15.6
Patch54: sip-4.19.25-py_ssize_t_clean.patch
# Fix error: invalid use of undefined type 'struct _frame' 
Patch55: sip-4.19.25-pyframe_getback.patch
# Fix error: implicit declaration of function ‘PyWeakref_GetObject’
Patch56: sip-4.19.25-ftbfs-python-3.15.patch

# extracted from sip.h, SIP_API_MAJOR_NR SIP_API_MINOR_NR defines
Source1: macros.sip
%global _sip_api_major 12
%global _sip_api_minor 7
%global _sip_api %{_sip_api_major}.%{_sip_api_minor}

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: sed
BuildRequires: bison
BuildRequires: flex

BuildRequires: python-setuptools

Obsoletes: sip-macros < %{version}-%{release}
Provides:  sip-macros = %{version}-%{release}

# upgrade path when no_namespace variants are dropped
%if ! 0%{?no_namespace}
Obsoletes: python2-sip < %{version}-%{release}
Obsoletes: python3-sip < %{version}-%{release}
%endif

%global _description\
SIP is a tool for generating bindings for C++ classes so that they can be\
accessed as normal Python classes. SIP takes many of its ideas from SWIG but,\
because it is specifically designed for C++ and Python, is able to generate\
tighter bindings. SIP is so called because it is a small SWIG.\
\
SIP was originally designed to generate Python bindings for KDE and so has\
explicit support for the signal slot mechanism used by the Qt/KDE class\
libraries. However, SIP can be used to generate Python bindings for any C++\
class library.

%description %_description

%package doc
Summary: Documentation for %summary
BuildArch: noarch
%description doc
This package contains HTML documentation for SIP.
%_description

%if %{with python2}
%if 0%{?no_namespace}
%package -n python2-sip
Summary: %summary
Provides: sip-api(%{_sip_api_major}) = %{_sip_api}
Provides: sip-api(%{_sip_api_major})%{?_isa} = %{_sip_api}
Provides: python2-sip-api(%{_sip_api_major}) = %{_sip_api}
Provides: python2-sip-api(%{_sip_api_major})%{?_isa} = %{_sip_api}
%{?python_provide:%python_provide python2-sip}
%description -n python2-sip %_description
%endif

%package -n python2-sip-devel
Summary: Files needed to generate Python bindings for any C++ class library
Requires: sip = %{version}-%{release}
#Requires: python2-sip%{?_isa} = %{version}-%{release}
BuildRequires: python2-devel
Requires:      python2-devel
# Remove before F30
Provides: sip-devel = %{version}-%{release}
Provides: sip-devel%{?_isa} = %{version}-%{release}
Obsoletes: sip-devel < %{version}-%{release}
%description -n python2-sip-devel
%{summary}.

%package -n python2-pyqt4-sip
Summary: %summary
Provides: python2-pyqt4-sip-api(%{_sip_api_major}) = %{_sip_api}
Provides: python2-pyqt4-sip-api(%{_sip_api_major})%{?_isa} = %{_sip_api}
%{?python_provide:%python_provide python2-pyqt4-sip}
%description -n python2-pyqt4-sip %_description

%package -n python2-pyqt5-sip
Summary: %summary
Provides: python2-pyqt5-sip-api(%{_sip_api_major}) = %{_sip_api}
Provides: python2-pyqt5-sip-api(%{_sip_api_major})%{?_isa} = %{_sip_api}
%{?python_provide:%python_provide python2-pyqt5-sip}
%description -n python2-pyqt5-sip %_description

%package -n python2-wx-siplib
Summary: %summary
Provides: python2-wx-siplib-api(%{_sip_api_major}) = %{_sip_api}
Provides: python2-wx-siplib-api(%{_sip_api_major})%{?_isa} = %{_sip_api}
%{?python_provide:%python_provide python2-wx-siplib}
%description -n python2-wx-siplib %_description
%endif

%if %{with python3}
%if 0%{?no_namespace}
%package -n python%{python3_pkgversion}-sip
Summary: SIP - Python 3/C++ Bindings Generator
Provides: python%{python3_pkgversion}-sip-api(%{_sip_api_major}) = %{_sip_api}
Provides: python%{python3_pkgversion}-sip-api(%{_sip_api_major})%{?_isa} = %{_sip_api}
%description -n python%{python3_pkgversion}-sip
This is the Python 3 build of SIP.

%_description
%endif

%package -n python%{python3_pkgversion}-sip-devel
Summary: Files needed to generate Python bindings for any C++ class library
Requires: sip = %{version}-%{release}
#Requires: python3-sip%{?_isa} = %{version}-%{release}
BuildRequires: python%{python3_pkgversion}-devel
Requires:      python%{python3_pkgversion}-devel
%description -n python%{python3_pkgversion}-sip-devel
%{summary}.

%package -n python%{python3_pkgversion}-pyqt4-sip
Summary: SIP - Python 3/C++ Bindings Generator for pyqt4
BuildRequires: python%{python3_pkgversion}-devel
Provides: python%{python3_pkgversion}-pyqt4-sip-api(%{_sip_api_major}) = %{_sip_api}
Provides: python%{python3_pkgversion}-pyqt4-sip-api(%{_sip_api_major})%{?_isa} = %{_sip_api}
%description -n python%{python3_pkgversion}-pyqt4-sip
This is the Python 3 build of pyqt4-SIP.

%if %{?pyqt5_sip}
%package -n python%{python3_pkgversion}-pyqt5-sip
Summary: SIP - Python 3/C++ Bindings Generator for pyqt5
BuildRequires: python%{python3_pkgversion}-devel
Provides: python%{python3_pkgversion}-pyqt5-sip-api(%{_sip_api_major}) = %{_sip_api}
Provides: python%{python3_pkgversion}-pyqt5-sip-api(%{_sip_api_major})%{?_isa} = %{_sip_api}
%description -n python%{python3_pkgversion}-pyqt5-sip
This is the Python 3 build of pyqt5-SIP.
%endif

%if %{?wx_siplib}
%package -n python%{python3_pkgversion}-wx-siplib
Summary: SIP - Python 3/C++ Bindings Generator for wx
BuildRequires: python%{python3_pkgversion}-devel
Provides: python%{python3_pkgversion}-wx-siplib-api(%{_sip_api_major}) = %{_sip_api}
Provides: python%{python3_pkgversion}-wx-siplib-api(%{_sip_api_major})%{?_isa} = %{_sip_api}
%description -n python%{python3_pkgversion}-wx-siplib
This is the Python 3 build of wx-siplib.
%endif

%_description

%endif


%prep

%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}-%{version}%{?snap:.%{snap}}

%patch -P50 -p1 -b .no_strip
%patch -P51 -p1 -b .no_rpath
%patch -P53 -p1 -b .no_sip_so
%patch -P54 -p1 -b .py_ssize_t_clean
%patch -P55 -p1 -b .pyframe_getback
%patch -P56 -p1 -b .pyweekref_getobject


%build
flex --outfile=sipgen/lexer.c sipgen/metasrc/lexer.l
bison --yacc --defines=sipgen/parser.h --output=sipgen/parser.c sipgen/metasrc/parser.y
%if %{with python2}
%if 0%{?no_namespace}
mkdir %{_target_platform}-python2
pushd %{_target_platform}-python2
%{__python2} ../configure.py \
  -b %{_bindir} -d %{python2_sitearch} -e %{_includedir}/python%{python2_version} \
  CFLAGS+="%{optflags}" CXXFLAGS+="%{optflags}" LFLAGS+="%{?__global_ldflags}"

%make_build
popd
%endif

mkdir %{_target_platform}-python2-pyqt4
pushd %{_target_platform}-python2-pyqt4
%{__python2} ../configure.py \
  --sip-module=PyQt4.sip \
  -b %{_bindir} -d %{python2_sitearch} -e %{_includedir}/python%{python2_version} \
  CFLAGS+="%{optflags}" CXXFLAGS+="%{optflags}" LFLAGS+="%{?__global_ldflags}"

%make_build
popd

mkdir %{_target_platform}-python2-pyqt5
pushd %{_target_platform}-python2-pyqt5
%{__python2} ../configure.py \
  --sip-module=PyQt5.sip \
  -b %{_bindir} -d %{python2_sitearch} -e %{_includedir}/python%{python2_version} \
  CFLAGS+="%{optflags}" CXXFLAGS+="%{optflags}" LFLAGS+="%{?__global_ldflags}"

%make_build
popd

sed -i -e 's|target = sip|target = siplib|g' siplib/siplib.sbf
mkdir %{_target_platform}-python2-wx
pushd %{_target_platform}-python2-wx
%{__python2} ../configure.py \
  --sip-module=wx.siplib \
  -b %{_bindir} -d %{python2_sitearch} -e %{_includedir}/python%{python2_version} \
  CFLAGS+="%{optflags}" CXXFLAGS+="%{optflags}" LFLAGS+="%{?__global_ldflags}"

%make_build
popd
%endif
sed -i -e 's|target = siplib|target = sip|g' siplib/siplib.sbf

%if %{with python3}
%if 0%{?no_namespace}
mkdir %{_target_platform}-python3
pushd %{_target_platform}-python3
%{__python3} ../configure.py \
  -b %{_bindir} -d %{python3_sitearch} -e %{PYINCLUDE} \
  CXXFLAGS+="%{optflags}" CFLAGS+="%{optflags}" LFLAGS+="%{?__global_ldflags}"

%make_build
popd
%endif

mkdir %{_target_platform}-python3-pyqt4
pushd %{_target_platform}-python3-pyqt4
%{__python3} ../configure.py \
  --sip-module=PyQt4.sip \
  -b %{_bindir} -d %{python3_sitearch} -e %{PYINCLUDE} \
  CXXFLAGS+="%{optflags}" CFLAGS+="%{optflags}" LFLAGS+="%{?__global_ldflags}"

%make_build
popd

%if %{?pyqt5_sip}
mkdir %{_target_platform}-python3-pyqt5
pushd %{_target_platform}-python3-pyqt5
%{__python3} ../configure.py \
  --sip-module=PyQt5.sip \
  -b %{_bindir} -d %{python3_sitearch} -e %{PYINCLUDE} \
  CXXFLAGS+="%{optflags}" CFLAGS+="%{optflags}" LFLAGS+="%{?__global_ldflags}"

%make_build
popd
%endif

%if %{?wx_siplib}
sed -i -e 's|target = sip|target = siplib|g' siplib/siplib.sbf
mkdir %{_target_platform}-python3-wx
pushd %{_target_platform}-python3-wx
%{__python3} ../configure.py \
  --sip-module=wx.siplib \
  -b %{_bindir} -d %{python3_sitearch} -e %{PYINCLUDE} \
  CXXFLAGS+="%{optflags}" CFLAGS+="%{optflags}" LFLAGS+="%{?__global_ldflags}"

%make_build
popd
sed -i -e 's|target = siplib|target = sip|g' siplib/siplib.sbf
%endif

%endif


%install
# Perform the Python 3 installation first, to avoid stomping over the Python 2
# /usr/bin/sip:
%if %{with python3}
%if 0%{?no_namespace}
%make_install -C %{_target_platform}-python3
%endif
%make_install -C %{_target_platform}-python3-pyqt4
%if %{?pyqt5_sip}
%make_install -C %{_target_platform}-python3-pyqt5
%endif
%if %{?wx_siplib}
%make_install -C %{_target_platform}-python3-wx
mv %{buildroot}%{python3_sitearch}/wx/sip.pyi %{buildroot}%{python3_sitearch}/wx/siplib.pyi
%endif
ln -s sip %{buildroot}%{_bindir}/python3-sip

## toplevel __pycache__ creation is ... inconsistent
## rawhide makes one, f23 local builds do not, so let's *make* it consistent
mkdir -p %{buildroot}%{python3_sitearch}/__pycache__/exclude_rpm_hack
%endif

# Python 2 installation:
%if %{with python2}
%if 0%{?no_namespace}
%make_install -C %{_target_platform}-python2
%endif
%make_install -C %{_target_platform}-python2-pyqt4
%make_install -C %{_target_platform}-python2-pyqt5
%make_install -C %{_target_platform}-python2-wx
mv %{buildroot}%{python2_sitearch}/wx/sip.pyi %{buildroot}%{python2_sitearch}/wx/siplib.pyi
%endif

# sip-wrapper
install %{SOURCE10} %{buildroot}%{_bindir}/sip-pyqt4
install %{SOURCE10} %{buildroot}%{_bindir}/sip-pyqt5
%if %{?wx_siplib}
install %{SOURCE10} %{buildroot}%{_bindir}/sip-wx
%endif
sed -i -e 's|@SIP_MODULE@|PyQt4.sip|g' %{buildroot}%{_bindir}/sip-pyqt4
sed -i -e 's|@SIP_MODULE@|PyQt5.sip|g' %{buildroot}%{_bindir}/sip-pyqt5
%if %{?wx_siplib}
sed -i -e 's|@SIP_MODULE@|wx.siplib|g' %{buildroot}%{_bindir}/sip-wx
%endif

mkdir -p %{buildroot}%{_datadir}/sip

# Macros used by -devel subpackages:
install -D -p -m644 %{SOURCE1} %{buildroot}%{rpm_macros_dir}/macros.sip

# Copy documentation from source dir
pushd doc
find html/ -type f -exec install -m0644 -D {} %{buildroot}%{_pkgdocdir}/{} \;
popd


%files
%doc README
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
%{_bindir}/sip
# sip-wrappers
%{_bindir}/sip-pyqt4
%{_bindir}/sip-pyqt5
%if %{?wx_siplib}
%{_bindir}/sip-wx
%endif
# compat symlink
%{_bindir}/python3-sip
%dir %{_datadir}/sip/
%{rpm_macros_dir}/macros.sip

%files doc
%{_pkgdocdir}/html

%if %{with python2}
%files -n python2-sip-devel
%{_prefix}/include/python2.7/sip.h
%{python2_sitearch}/sipconfig.py*
%{python2_sitearch}/sipdistutils.py*

%if 0%{?no_namespace}
%files -n python2-sip
%doc NEWS README
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
%{python2_sitearch}/sip.*
%{python2_sitearch}/sip-%{version}.dist-info/
%endif

%files -n python2-pyqt4-sip
%doc NEWS README
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
%{python2_sitearch}/PyQt4/
%{python2_sitearch}/PyQt4_sip-%{version}.dist-info/

%files -n python2-pyqt5-sip
%doc NEWS README
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
%dir %{python2_sitearch}/PyQt5/
%{python2_sitearch}/PyQt5/sip.*
%{python2_sitearch}/PyQt5_sip-%{version}.dist-info/

%files -n python2-wx-siplib
%doc NEWS README
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
%dir %{python2_sitearch}/wx/
%{python2_sitearch}/wx/siplib.*
%{python2_sitearch}/wx_siplib-%{version}.dist-info/
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-sip-devel
%{PYINCLUDE}/sip.h
%{python3_sitearch}/sipconfig.py*
%{python3_sitearch}/sipdistutils.py*
%{python3_sitearch}/__pycache__/*
%exclude %{python3_sitearch}/__pycache__/exclude_rpm_hack

%if 0%{?no_namespace}
%files -n python%{python3_pkgversion}-sip
%doc NEWS README
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
%{python3_sitearch}/sip.*
%{python3_sitearch}/sip-%{version}.dist-info/
%endif

%files -n python%{python3_pkgversion}-pyqt4-sip
%doc NEWS README
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
%dir %{python3_sitearch}/PyQt4/
%{python3_sitearch}/PyQt4/sip.*
%{python3_sitearch}/PyQt4_sip-%{version}.dist-info/

%if %{?pyqt5_sip}
%files -n python%{python3_pkgversion}-pyqt5-sip
%doc NEWS README
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
%dir %{python3_sitearch}/PyQt5/
%{python3_sitearch}/PyQt5/sip.*
%{python3_sitearch}/PyQt5_sip-%{version}.dist-info/
%endif

%if %{?wx_siplib}
%files -n python%{python3_pkgversion}-wx-siplib
%doc NEWS README
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
%dir %{python3_sitearch}/wx/
%{python3_sitearch}/wx/siplib.*
%{python3_sitearch}/wx_siplib-%{version}.dist-info/
%endif
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.19.25-20
- Import
