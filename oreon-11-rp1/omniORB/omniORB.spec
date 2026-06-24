%global source0_hash none

%global nameserver omniNames

%if 0%{?fedora} || 0%{?rhel} > 6
%global with_systemd 1
%endif

# openssl enabled by default, add conditional --without openssl
%bcond_without openssl

Name:           omniORB
Version:        4.3.4
Release:        4%{?dist}
Summary:        A robust high performance CORBA ORB for C++ and Python

License:        LGPL-2.0-or-later
URL:            http://omniorb.sourceforge.net
Source0:        http://downloads.sourceforge.net/project/omniorb/%{name}/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source1:        omniORB-nameserver.init
Source2:        omniORB-nameserver.logrotate
Source3:        omniORB.cfg
Source4:        omniNames.service

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  byacc
BuildRequires:  zlib-devel
%{!?_without_openssl:BuildRequires:  openssl-devel}
%if 0%{?with_systemd}
BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%else
Requires(post): chkconfig
Requires(preun): chkconfig
# This is for /sbin/service
Requires(postun): initscripts
%endif

# we don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_setup
}

%description
omniORB is a robust high performance CORBA ORB for C++ and Python.
omniORB is a certified CORBA 2.1 implementation and largely CORBA 2.6
compliant.


%package        devel
Summary:        Development files for %{name}
License:        LGPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
The %{name}-doc package contains documentation files for
developing and administrating applications that use %{name}.

%package        servers
Summary:        OmniORB naming service
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    servers
The %{name}-servers package contains omniNames naming server.

%package        utils
Summary:        Development files for %{name}
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
The %{name}-utils package contains supplementary command line tools for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Fix shebangs
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' \
  ./src/tool/omniidl/python3/scripts/omniidlrun.py \
  ./src/tool/omniidl/python3/omniidl/main.py

# Create a sysusers.d config file
cat >omniorb.sysusers.conf <<EOF
u omniORB - 'OmniNames Naming Service' %{_sharedstatedir}/%{name} -
EOF

%build
# Per guidelines: if the same functionality is provided regardless of the interpreter version, only the python 3 version should be packaged
export PYTHON=%{__python3}
%configure --disable-static %{?with_openssl:--with-openssl=%{_prefix}}
%make_build



%install
%make_install
find %{buildroot} -name '*.la' -delete
# fix rpmlint warnings: unstripped-binary-or-object
chmod 0755 %{buildroot}%{_libdir}/*.so.*
chmod 0755 %{buildroot}%{python3_sitearch}/*.so.*
# fix rpmlint errors: non-standard-dir-perm
chmod 0755 %{buildroot}%{_includedir}/{omnithread,COS}
chmod 0755 %{buildroot}%{_includedir}/omniORB4/{,internal}
chmod 0755 %{buildroot}%{_datadir}/idl/%{name}/COS
chmod 0755 %{buildroot}%{python3_sitelib}/omniidl
chmod 0755 %{buildroot}%{python3_sitelib}/omniidl_be
chmod 0755 %{buildroot}%{python3_sitelib}/omniidl_be/cxx/{,skel,impl,dynskel,header}
# fix rpmlint error: non-executable-script
chmod +x %{buildroot}%{python3_sitelib}/omniidl/main.py
%if 0%{?with_systemd}
# install systemd unit
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}
%else
# install service init script
mkdir -p %{buildroot}%{_initddir}
install -m 0755 %{SOURCE1} %{buildroot}%{_initddir}/%{nameserver}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
mkdir -p %{buildroot}%{_localstatedir}/run/%{name}
%endif
# install server configuration stuff
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{nameserver}
mkdir -p %{buildroot}%{_sysconfdir}/
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/%{name}.cfg
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
# install man pages
pushd man
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 man1/* %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_mandir}/man8
install -m 0644 man8/* %{buildroot}%{_mandir}/man8/
popd

install -m0644 -D omniorb.sysusers.conf %{buildroot}%{_sysusersdir}/omniorb.conf

%ldconfig_scriptlets


%if 0%{?with_systemd}
%post servers
%systemd_post omniNames.service

%preun servers
%systemd_preun omniNames.service

%postun servers
%systemd_postun omniNames.service

%else
%post servers
/sbin/chkconfig --add %{nameserver}

%preun servers
if [ $1 = 0 ] ; then
  /sbin/service  stop >/dev/null 2>&1
  /sbin/chkconfig --del  %{nameserver}
fi

%postun servers
if [ $1 -ge 1 ] ; then
    /sbin/service  %{nameserver} condrestart >/dev/null 2>&1 || :
fi
%endif

%files
%license COPYING.LIB
%doc README.FIRST.txt README.unix.txt
%{_libdir}/libCOS4.so.3*
%{_libdir}/libCOSDynamic4.so.3*
%{_libdir}/libomniCodeSets4.so.3*
%{_libdir}/libomniConnectionMgmt4.so.3*
%{_libdir}/libomniDynamic4.so.3*
%{_libdir}/libomniORB4.so.3*
%{_libdir}/libomniZIOP4.so.3*
%{_libdir}/libomniZIOPDynamic4.so.3*
%{_libdir}/libomnisslTP4.so.3*
%{_libdir}/libomnihttpCrypto4.so.3*
%{_libdir}/libomnihttpTP4.so.3*
%{_libdir}/libomnithread.so.4*

%files servers
%if 0%{?with_systemd}
%{_unitdir}/omniNames.service
%else
%{_initddir}/%{nameserver}
%dir %attr(0755, %{name}, root) %{_sharedstatedir}/%{name}
%dir %attr(0755, %{name}, root) %{_localstatedir}/run/%{name}
%endif
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%config(noreplace) %{_sysconfdir}/logrotate.d/%{nameserver}
%dir %attr(0755, %{name}, root) %{_localstatedir}/log/%{name}
%{_bindir}/omniMapper
%{_bindir}/%{nameserver}
%{_mandir}/man8/*
%{_sysusersdir}/omniorb.conf

%files devel
%doc doc/
%{_bindir}/omniidl
%{_bindir}/omniidlrun.py
%{_bindir}/omnicpp
%{_bindir}/omkdepend
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/idl/%{name}/*
%{python3_sitelib}/*
%{python3_sitearch}/*
%{_mandir}/man1/omniidl.1.gz
%{_mandir}/man1/omnicpp.1.gz

%files doc
%doc doc/

%files utils
%license COPYING
%{_bindir}/catior
%{_bindir}/convertior
%{_bindir}/genior
%{_bindir}/nameclt
%{_mandir}/man1/catior.1.gz
%{_mandir}/man1/convertior.1.gz
%{_mandir}/man1/genior.1.gz
%{_mandir}/man1/nameclt.1.gz


%changelog
%autochangelog

