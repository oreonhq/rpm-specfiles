%global source0_hash c62d38f5da7df4299ac3a652508e959537752440181e34c76b2aecebd7f301b9
%global _hardened_build 1
%bcond_with python
%bcond_with perl
Summary:        IPMI (Intelligent Platform Management Interface) library and tools
Name: OpenIPMI
Version:    2.0.37
Release:        1%{?dist}
License:    LGPL-2.1-or-later and GPL-2.0-or-later or BSD-3-Clause
URL:        https://sourceforge.net/projects/openipmi/
Source0:        https://downloads.sourceforge.net/openipmi/%{name}-%{version}.tar.gz
Source1:    openipmi.sysconf
Source2:    openipmi-helper
Source3:    ipmi.service
Patch1:     0001-man.patch
Patch2:     include-config-h-cmdlang.patch
Patch5:     OpenIPMI-py313compat.patch
%if %{with python} || %{with perl}
%endif
%if %{with python}
%endif
%if %{with perl}
%endif
%{?systemd_requires}
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}
%global __provides_exclude_from %{?__provides_exclude_from:%{__provides_exclude_from}|}^%{perl_vendorarch}/auto/.*\\.so$
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gdbm-devel
BuildRequires:  glib2-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  net-snmp-devel
BuildRequires:  openssl-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  swig
BuildRequires:  systemd
# /oreon:deps
%description
The Open IPMI project aims to develop an open code base to allow access to
platform information using Intelligent Platform Management Interface (IPMI).
This package contains the tools of the OpenIPMI project.

%package libs
Summary: The OpenIPMI runtime libraries
%description libs
The OpenIPMI-libs package contains the runtime libraries for shared binaries
and applications.

%if %{with perl}
%package perl
Summary:  IPMI Perl language bindings
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description perl
The OpenIPMI-perl package contains the Perl language bindings for OpenIPMI.
%endif

%if %{with python}
%package -n python3-openipmi
%{?python_provide:%python_provide python3-openipmi}
%{?python_provide:%python_provide python3-OpenIPMI}
Provides:  %{name}-python = %{version}-%{release}
Provides:  %{name}-python%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python2 < %{version}-%{release}
Summary:   IPMI Python language bindings
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}
%description -n python3-openipmi
The OpenIPMI-python package contains the Python language bindings for OpenIPMI.
%endif

%package devel
Summary:  The development environment for the OpenIPMI project
Requires: pkgconfig
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-lanserv%{?_isa} = %{version}-%{release}
%description devel
The OpenIPMI-devel package contains the development libraries and header files
of the OpenIPMI project.

%package lanserv
Summary:  Emulates an IPMI network listener
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description lanserv
This package contains a network IPMI listener.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
    CFLAGS="-fPIC %{optflags} -z now -fno-strict-aliasing" \
    LDFLAGS="%{__global_ldflags} -Wl,--as-needed" \
    --disable-dependency-tracking \
    --disable-static \
%if %{with python}
    --with-pythoninstall=%{python3_sitearch} \
    --with-python=%{__python3} \
%else
    --with-python=no \
%endif
%if %{without perl}
    --with-perl=no \
%endif
    --with-tcl=no \
    --with-tkinter=no
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make   # not %%{?_smp_mflags} safe
%install
make install DESTDIR=%{buildroot}
install -d %{buildroot}{%{_sysconfdir}/sysconfig,%{_unitdir},%{_libexecdir}}
install -m 644 %SOURCE1 %{buildroot}%{_sysconfdir}/sysconfig/ipmi
install -m 755 %SOURCE2 %{buildroot}%{_libexecdir}/openipmi-helper
install -m 644 %SOURCE3 %{buildroot}%{_unitdir}/ipmi.service
install -d %{buildroot}%{_sysconfdir}/modprobe.d
rm %{buildroot}/%{_mandir}/man1/openipmigui.1 %{buildroot}%{_libdir}/*.la
echo ".so man1/openipmicmd.1" > %{buildroot}%{_mandir}/man1/ipmicmd.1
echo ".so man1/openipmish.1" > %{buildroot}%{_mandir}/man1/ipmish.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post ipmi.service
%preun

%systemd_preun ipmi.service
%postun

%systemd_postun_with_restart ipmi.service
%ldconfig_scriptlets libs
%ldconfig_scriptlets lanserv
%triggerun -- OpenIPMI < 2.0.18-14

/usr/bin/systemd-sysv-convert --save ipmi >/dev/null 2>&1 ||:
/bin/systemctl --no-reload enable ipmi.service >/dev/null 2>&1 ||:
/sbin/chkconfig --del ipmi >/dev/null 2>&1 || :
/bin/systemctl try-restart ipmi.service >/dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
