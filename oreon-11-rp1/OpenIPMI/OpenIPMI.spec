%global source0_hash a0403148fa5f7bed930c958a4d1c558047e273763a408b3a0368edc137cc55d9

%global _hardened_build 1

%bcond_with python
%bcond_with perl

Summary: IPMI (Intelligent Platform Management Interface) library and tools
Name: OpenIPMI

Version:    2.0.36
Release:    7%{?dist}
License:    LGPL-2.1-or-later and GPL-2.0-or-later or BSD-3-Clause
URL:        https://sourceforge.net/projects/openipmi/
Source:        https://downloads.sourceforge.net/openipmi/OpenIPMI-2.0.36.tar.gz
Source1:    openipmi.sysconf
Source2:    openipmi-helper
Source3:    ipmi.service
Patch1:     0001-man.patch
Patch2:     include-config-h-cmdlang.patch
Patch5:     OpenIPMI-py313compat.patch

BuildRequires: make
BuildRequires:    gdbm-devel glib2-devel net-snmp-devel ncurses-devel
%if %{with python} || %{with perl}
BuildRequires:    swig
%endif
BuildRequires:    openssl-devel
%if %{with python}
BuildRequires:    python3-devel
%endif
%if %{with perl}
BuildRequires:    perl-devel perl-generators
%endif
BuildRequires:    pkgconfig
BuildRequires:    readline-devel
BuildRequires:    automake
BuildRequires:    autoconf
BuildRequires:    libtool
%{?systemd_requires}
BuildRequires:    systemd

Requires:         %{name}-libs%{?_isa} = %{version}-%{release}

# Prevent bogus provides of private libs from perl
%global __provides_exclude_from %{?__provides_exclude_from:%{__provides_exclude_from}|}^%{perl_vendorarch}/auto/.*\\.so$

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
# Remove before F30
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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

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

# https://fedoraproject.org/wiki/Packaging:Guidelines?rd=Packaging/Guidelines#Beware_of_Rpath
# get rid of rpath still present in OpenIPMI-perl package
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

# add missing documentation 
echo ".so man1/openipmicmd.1" > %{buildroot}%{_mandir}/man1/ipmicmd.1

echo ".so man1/openipmish.1" > %{buildroot}%{_mandir}/man1/ipmish.1

%post
%systemd_post ipmi.service

%preun
%systemd_preun ipmi.service

%postun
%systemd_postun_with_restart ipmi.service

%ldconfig_scriptlets libs
%ldconfig_scriptlets lanserv

### A sysv => systemd migration contains all of the same scriptlets as a
### systemd package.  These are additional scriptlets

%triggerun -- OpenIPMI < 2.0.18-14
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply httpd
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save ipmi >/dev/null 2>&1 ||:
/bin/systemctl --no-reload enable ipmi.service >/dev/null 2>&1 ||:
# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del ipmi >/dev/null 2>&1 || :
/bin/systemctl try-restart ipmi.service >/dev/null 2>&1 || :

%files
%license COPYING COPYING.BSD COPYING.LIB
%doc CONFIGURING_FOR_LAN FAQ README README.Force README.MotorolaMXP
%config(noreplace) %{_sysconfdir}/sysconfig/ipmi
%{_libexecdir}/openipmi-helper
%{_bindir}/ipmicmd
%{_bindir}/ipmish
%{_bindir}/ipmi_ui
%{_bindir}/openipmicmd
%{_bindir}/openipmish
%{_bindir}/rmcp_ping
%{_bindir}/solterm
%{_bindir}/openipmi_eventd
%{_unitdir}/ipmi.service
%{_mandir}/man1/ipmi_ui*
%{_mandir}/man1/openipmicmd*
%{_mandir}/man1/openipmish*
%{_mandir}/man1/rmcp_ping*
%{_mandir}/man1/solterm*
%{_mandir}/man1/ipmish*
%{_mandir}/man1/ipmicmd*
%{_mandir}/man1/openipmi_eventd*
%{_mandir}/man7/ipmi_cmdlang*
%{_mandir}/man7/openipmi_conparms*

%if %{with perl}
%files perl
%attr(644,root,root) %{perl_vendorarch}/OpenIPMI.pm
%{perl_vendorarch}/auto/OpenIPMI
%endif

%if %{with python}
%files -n python3-openipmi
%{python3_sitearch}/*OpenIPMI*
%{python3_sitearch}/__pycache__/OpenIPMI.*.pyc
%endif

%files libs
%{_libdir}/libOpenIPMI*.so.*

%files devel
%{_includedir}/OpenIPMI
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files lanserv
%config(noreplace) %{_sysconfdir}/ipmi/ipmisim1.emu
%config(noreplace) %{_sysconfdir}/ipmi/lan.conf
%dir %{_sysconfdir}/ipmi
%{_bindir}/ipmilan
%{_bindir}/ipmi_sim
%{_bindir}/sdrcomp
%{_libdir}/libIPMIlanserv.so.*
%{_mandir}/man8/ipmilan.8*
%{_mandir}/man1/ipmi_sim.1*
%{_mandir}/man5/ipmi_lan.5*
%{_mandir}/man5/ipmi_sim_cmd.5*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.36-7
- Prepare for Oreon 11 (RP1)
