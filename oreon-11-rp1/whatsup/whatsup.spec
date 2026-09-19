%global source0_hash 1b476e2e9f5c531b8dc1475ef45ce883be03c60aa2538535cabf7b736f9fe555

%global libname libnodeupdown

# There is no opensm on 32-bit ARM, bugs #1484155, #1556539
# There is no libibcommon on s390, s390x
%ifnarch %{arm} s390 s390x
%global with_ib 1
%else
%global with_ib 0
%endif

Summary:       Node up/down detection utility
Name:          whatsup
Version:       1.14
Release:       51%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           https://computing.llnl.gov/linux/whatsup.html
Source0:       http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}-1/%{name}-%{version}.tar.gz
Source1:       %{name}-hostsfile
Source2:       %{name}-pingd.service
Patch0:        %{name}-%{version}-bug#1117251.patch
# Adjust to Autconf-2.71, bug #1999491,
# <https://savannah.gnu.org/support/index.php?110571>,
# <https://github.com/chaos/whatsup/pull/3>
Patch1:        %{name}-%{version}-Adjust-to-Autoconf-2.71.patch
BuildRequires: make
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker) expat-devel, libtool-ltdl-devel, libgenders-devel
BuildRequires: autoconf, automake, libtool
%if 0%{?fedora} > 15
BuildRequires: systemd-units
%endif
Requires:      %{libname} = %{version}-%{release}

%description
Whatsup is a cluster node up/down detection utility.

Whatsup can quickly calculate and output the up and down nodes of a cluster.
Whatsup allows some tools, such as Pdsh, to operate more quickly by
not operating on down nodes. Whatsup calculates the up and down nodes of a
cluster through one of several possible backend tools
and several optional cluster node databases.

%package -n    %{libname}-devel
Summary:       Development headers for %{libname}
Requires:      %{libname} = %{version}-%{release}
%description -n %{libname}-devel
development headers for %{libname}

%package -n    %{libname}
Summary:       A cluster node up/down detection library
%description -n %{libname}
A cluster node up/down detection library, with different backends

%package -n    %{libname}-backend-ganglia
Summary:       Ganglia backend for %{libname}
Requires:      %{libname} = %{version}-%{release}
BuildRequires: ganglia-devel
%description -n %{libname}-backend-ganglia
Ganglia backend module for %{libname}

%if %{with_ib}
%package -n    %{libname}-backend-openib
Summary:       Openib backend for %{libname}
BuildRequires: opensm-devel, libibcommon-devel, rdma-core-devel
Requires:      %{libname} = %{version}-%{release}
%description -n %{libname}-backend-openib
openib backend module for %{libname}
%endif

%package -n    %{libname}-backend-pingd
Summary:       Pingd backend for %{libname}
Requires:      %{libname} = %{version}-%{release}
Requires:      %{name}-pingd = %{version}-%{release}
%description -n %{libname}-backend-pingd
pingd backend module for %{libname}

%package -n    %{name}-pingd
Summary:       Pingd daemon for %{name}
Requires:      %{libname} = %{version}-%{release}
%if 0%{?fedora} > 15
Requires(post): systemd-sysv
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%else
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
Requires(postun): initscripts
%endif

%description -n %{name}-pingd
pingd daemon for %{name}

%package -n    perl-%{libname}
Summary:       Perl bindings for %{libname}
Requires:      %{libname} = %{version}-%{release}
%description -n perl-%{libname}
Perl bindings for %{libname}

%{?filter_setup:
%filter_provides_in %{perl_vendorarch}/.*\.so$
%filter_setup
}

%package -n    %{libname}-clusterlist-hostsfile
Summary:       Hostsfile clusterlist module for %{libname}
Requires:      %{libname} = %{version}-%{release}
%description -n %{libname}-clusterlist-hostsfile
Hostsfile clusterlist module for %{libname}

%package -n    %{libname}-clusterlist-genders
Summary:       Genders clusterlist module for %{libname}
Requires:      %{libname} = %{version}-%{release}
%description -n %{libname}-clusterlist-genders
Genders clusterlist module for %{libname}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0
%patch -P1 -p1
%if 0%{?fedora} > 17
autoreconf -I config -f -i
%endif

%if 0%{?rhel} <= 6
cat << \EOF > %{name}-python-prov
#!/bin/sh
%{__python_provides} $* |\
sed -e '/.*Lib%{name}.so.*/d'
EOF

%global __python_provides %{_builddir}/%{name}-%{version}/%{name}-python-prov
chmod +x %{__python_provides}

cat << \EOF > %{name}-perl-prov
#!/bin/sh
%{__perl_provides} $* |\
sed -e '/.*Lib%{name}.so.*/d'
EOF

%global __perl_provides %{_builddir}/%{name}-%{version}/%{name}-perl-prov
chmod +x %{__perl_provides}
%endif

%build
%configure \
    --disable-static \
    --with-perl-extensions \
    --with-perl-vendor-arch \
    --with-perl-destdir="%{buildroot}"
make %{?_smpflags}

%install
DESTDIR=%{buildroot} make install

%if 0%{?fedora} > 15
mkdir -vp %{buildroot}%{_unitdir}
install -m 644 -p %{SOURCE2} %{buildroot}%{_unitdir}/
rm -rf %{buildroot}%{_initrddir}
%endif

chmod -x %{buildroot}%{_sysconfdir}/nodeupdown.conf
chmod -x %{buildroot}%{_sysconfdir}/pingd.conf

# for whatsup-pingd
install -m 644 -p %{SOURCE1} %{buildroot}%{_sysconfdir}/hostsfile

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name "*.bs" -exec rm -f {} \;
find %{buildroot} -type f -name "*.la" -exec rm -f {} \;

%{_fixperms} %{buildroot}/*
touch %{buildroot}%{_sysconfdir}/hostsfile

%ldconfig_scriptlets -n %{libname}

%post -n %{name}-pingd
%if 0%{?fedora} > 15
%if 0%{?fedora} > 17
%systemd_post whatsup-pingd.service
%else
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%endif
%else
# EPEL thing
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /sbin/chkconfig --add whatsup-pingd
fi
%endif

%preun -n %{name}-pingd
%if 0%{?fedora} > 15
%if 0%{?fedora} > 17
%systemd_preun whatsup-pingd.service
%else
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable whatsup-pingd.service > /dev/null 2>&1 || :
    /bin/systemctl stop whatsup-pingd.service > /dev/null 2>&1 || :
fi
%endif
%else
# EPEL thing
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /sbin/service whatsup-pingd stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del whatsup-pingd >/dev/null 2>&1 || :
fi
%endif

%postun -n %{name}-pingd
%if 0%{?fedora} > 15
%if 0%{?fedora} > 17
%systemd_postun_with_restart whatsup-pingd.service
%else
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart whatsup-pingd.service >/dev/null 2>&1 || :
fi
%endif
%else
#EPEL thing
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /sbin/service whatsup-pingd condrestart
fi
%endif

%if 0%{?fedora} > 15
%triggerun -n %{name}-pingd -- whatsup-pingd < 1.12-6
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply whatsup-pingd
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save whatsup-pingd >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del whatsup-pingd >/dev/null 2>&1 || :
/bin/systemctl try-restart whatsup-pingd.service >/dev/null 2>&1 || :
%endif

%files
%doc AUTHORS COPYING DISCLAIMER NEWS README ChangeLog
%{_bindir}/whatsdown
%{_bindir}/whatsup
%{_mandir}/man1/*

%files -n perl-%{libname}
%doc COPYING
%{_mandir}/man3/Libnodeupdown.3*
%{_mandir}/man3/Nodeupdown.3*
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/

%files -n %{name}-pingd
%doc COPYING
%if 0%{?fedora} > 15
%{_unitdir}/%{name}-pingd.service
%else
%{_sysconfdir}/rc.d/init.d/%{name}-pingd
%endif
%{_sbindir}/pingd
%dir %{_libdir}/pingd
%{_libdir}/pingd/pingd_clusterlist_hostsfile.so
%{_libdir}/pingd/pingd_clusterlist_genders.so
%config(noreplace) %{_sysconfdir}/hostsfile
%{_mandir}/man5/pingd.conf.5*
%{_mandir}/man8/pingd.8*
%config(noreplace) %{_sysconfdir}/pingd.conf

%files -n %{libname}-devel
%doc COPYING
%{_includedir}/nodeupdown.h
%dir %{_includedir}/nodeupdown
%{_includedir}/nodeupdown/*.h
%{_libdir}/libnodeupdown*.so
%{_mandir}/man3/nodeupdown*

%files -n %{libname}
%doc COPYING
%{_libdir}/libnodeupdown*.so.*
%dir %{_libdir}/nodeupdown
%{_mandir}/man3/libnodeupdown.3*
%{_mandir}/man5/nodeupdown.conf.5*
%config(noreplace) %{_sysconfdir}/nodeupdown.conf

%files -n %{libname}-backend-ganglia
%doc COPYING
%{_libdir}/nodeupdown/nodeupdown_backend_ganglia.so

%if %{with_ib}
%files -n %{libname}-backend-openib
%doc COPYING
%{_libdir}/nodeupdown/nodeupdown_backend_openib.so
%endif

%files -n %{libname}-backend-pingd
%doc COPYING
%{_libdir}/nodeupdown/nodeupdown_backend_pingd.so

%files -n %{libname}-clusterlist-genders
%doc COPYING
%{_libdir}/nodeupdown/nodeupdown_clusterlist_genders.so

%files -n %{libname}-clusterlist-hostsfile
%doc COPYING
%{_libdir}/nodeupdown/nodeupdown_clusterlist_hostsfile.so
%config(noreplace) %{_sysconfdir}/hostsfile

%changelog
%autochangelog
