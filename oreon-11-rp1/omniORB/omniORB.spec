%global source0_hash 79720d415d23cd8da99287a4ef4da0aa1bd34d3e4c7b1530715600adc5ed3dc3
%global nameserver omniNames
%bcond_without openssl
Name:           omniORB
Version:        4.3.4
Release:        1%{?dist}
Summary:        A robust high performance CORBA ORB for C++ and Python
License:        LGPL-2.0-or-later
URL:            http://omniorb.sourceforge.net
Source0:        http://downloads.sourceforge.net/project/omniorb/%{name}/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source1:        omniORB-nameserver.init
Source2:        omniORB-nameserver.logrotate
Source3:        omniORB.cfg
Source4:        omniNames.service
Patch0:         omniORB_openssl4.patch
%{!?_without_openssl:BuildRequires:  openssl-devel}
%if 0%{?with_systemd}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%else
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(postun): initscripts
%endif
%{?filter_setup:
%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_setup
}
# oreon:deps
BuildRequires:  byacc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  systemd
BuildRequires:  zlib-devel
# /oreon:deps
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

export PYTHON=%{__python3}
%configure --disable-static %{?with_openssl:--with-openssl=%{_prefix}}
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -delete
chmod 0755 %{buildroot}%{_libdir}/*.so.*
chmod 0755 %{buildroot}%{python3_sitearch}/*.so.*
chmod 0755 %{buildroot}%{_includedir}/{omnithread,COS}
chmod 0755 %{buildroot}%{_includedir}/omniORB4/{,internal}
chmod 0755 %{buildroot}%{_datadir}/idl/%{name}/COS
chmod 0755 %{buildroot}%{python3_sitelib}/omniidl
chmod 0755 %{buildroot}%{python3_sitelib}/omniidl_be
chmod 0755 %{buildroot}%{python3_sitelib}/omniidl_be/cxx/{,skel,impl,dynskel,header}
chmod +x %{buildroot}%{python3_sitelib}/omniidl/main.py
%if 0%{?with_systemd}
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}
%else
mkdir -p %{buildroot}%{_initddir}
install -m 0755 %{SOURCE1} %{buildroot}%{_initddir}/%{nameserver}
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}
mkdir -p %{buildroot}%{_localstatedir}/run/%{name}
%endif
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{nameserver}
mkdir -p %{buildroot}%{_sysconfdir}/
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/%{name}.cfg
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
pushd man
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 man1/* %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_mandir}/man8
install -m 0644 man8/* %{buildroot}%{_mandir}/man8/
popd
install -m0644 -D omniorb.sysusers.conf %{buildroot}%{_sysusersdir}/omniorb.conf
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
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
%files -f %{oreon_filedir}/main.list
%files -n omniORB-devel -f %{oreon_filedir}/omniORB-devel.list
%files -n omniORB-doc -f %{oreon_filedir}/omniORB-doc.list
%files -n omniORB-servers -f %{oreon_filedir}/omniORB-servers.list
%files -n omniORB-utils -f %{oreon_filedir}/omniORB-utils.list

%changelog

%autochangelog
