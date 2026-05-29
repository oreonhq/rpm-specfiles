%global source0_hash d18b97764c755528c1051d376e33545d0eb60c6ebf85680436813fa5b04cc3d1

# Default to no static libraries
%{!?with_static: %global with_static 1}
%bcond_without python
%if %{with python}
%define python_sitearch %(python3 -c "from distutils.sysconfig import get_python_lib; print (get_python_lib(1))")
%define python_prefix %(python3 -c "import sys; print (sys.prefix)")
%global __provides_exclude_from ^%{python3_sitearch}/perfmon/.*\.so$
%endif

Name:		libpfm
Version:	4.13.0
Release:	19%{?dist}

Summary:	Library to encode performance events for use by perf tool

License:	MIT
URL:		http://perfmon2.sourceforge.net/
Source0:        http://sourceforge.net/projects/perfmon2/files/libpfm4/%{name}-%{version}.tar.gz
Patch1:		libpfm-fix-const.patch
Patch2:		libpfm-python3-setup.patch
Patch3:		libpfm-gcc14.patch
Patch4:		libpfm-unused-vars.patch

BuildRequires: make
BuildRequires:	gcc
%if %{with python}
BuildRequires:	python3
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	swig
%endif

%description

libpfm4 is a library to help encode events for use with operating system
kernels performance monitoring interfaces. The current version provides support
for the perf_events interface available in upstream Linux kernels since v2.6.31.

%package devel
License:	MIT
Summary:	Development library to encode performance events for perf_events based tools
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development library and header files to create performance monitoring
applications for the perf_events interface.

%if %{with_static}
%package static
License:	MIT
Summary:	Static library to encode performance events for perf_events based tools
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description static
Static version of the libpfm library for performance monitoring
applications for the perf_events interface.
%endif

%if %{with python}
%package -n python3-libpfm
License:	MIT AND LicenseRef-Fedora-UltraPermissive
%{?python_provide:%python_provide python3-libpfm}
# Remove before F30
Provides: %{name}-python = %{version}-%{release}
Provides: %{name}-python%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python < %{version}-%{release}
Summary:	Python bindings for libpfm and perf_event_open system call
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n python3-libpfm
Python bindings for libpfm4 and perf_event_open system call.
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%patch -P1 -p1 -b .fix-const
%patch -P2 -p1 -b .python3
%patch -P3 -p1 -b .gcc14
%patch -P4 -p1 -b .unused
# to prevent setuptools from installing an .egg, we need to pass --root to setup.py install
# see https://github.com/pypa/setuptools/issues/3143
# and https://github.com/pypa/pip/issues/11501
sed -i 's/--prefix=$(DESTDIR)$(PYTHON_PREFIX)/--root=$(DESTDIR) --prefix=$(PYTHON_PREFIX)/' python/Makefile

%build
%if %{with python}
%global python_config CONFIG_PFMLIB_NOPYTHON=n
%else
%global python_config CONFIG_PFMLIB_NOPYTHON=y
%endif
%make_build %{python_config} \
     OPTIM="%{optflags}" LDFLAGS="%{build_ldflags}"


%install
rm -rf $RPM_BUILD_ROOT

%if %{with python}
%global python_config CONFIG_PFMLIB_NOPYTHON=n PYTHON_PREFIX=%{python_prefix}
%else
%global python_config CONFIG_PFMLIB_NOPYTHON=y
%endif

make \
    DESTDIR=$RPM_BUILD_ROOT \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir} \
    %{python_config} \
    LDCONFIG=/bin/true \
    install

%if !%{with_static}
rm $RPM_BUILD_ROOT%{_libdir}/lib*.a
%endif

%ldconfig_scriptlets

%files
%doc README
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/*
%{_mandir}/man3/*
%{_libdir}/lib*.so

%if %{with_static}
%files static
%{_libdir}/lib*.a
%endif

%if %{with python}
%files -n python3-libpfm
%{python3_sitearch}/perfmon-*.egg-info/
%{python3_sitearch}/perfmon/
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.13.0-19
- Import
