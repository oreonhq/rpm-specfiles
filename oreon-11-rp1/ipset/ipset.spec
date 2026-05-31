%global source0_hash fbe3424dff222c1cb5e5c34d38b64524b2217ce80226c14fdcbb13b29ea36112

Name:             ipset
Version:          7.24
Release:          3%{?dist}
Summary:          Manage Linux IP sets

License:          GPL-2.0-only
URL:              http://ipset.netfilter.org/
Source0:        http://ipset.netfilter.org//ipset-7.24.tar.bz2
Source1:          %{name}.service
Source2:          %{name}.start-stop
Source3:          %{name}-config

BuildRequires:    libmnl-devel
BuildRequires:    automake
BuildRequires:    autoconf
BuildRequires:    make
BuildRequires:    libtool
BuildRequires:    libtool-ltdl-devel

# An explicit requirement is needed here, to avoid cases where a user would
# explicitly update only one of the two (e.g 'yum update ipset')
Requires:         %{name}-libs%{?_isa} = %{version}-%{release}

%description
IP sets are a framework inside the Linux kernel since version 2.4.x, which can
be administered by the ipset utility. Depending on the type, currently an IP
set may store IP addresses, (TCP/UDP) port numbers or IP addresses with MAC
addresses in a way, which ensures lightning speed when matching an entry
against a set.

If you want to:
 - store multiple IP addresses or port numbers and match against the collection
   by iptables at one swoop;
 - dynamically update iptables rules against IP addresses or ports without
   performance penalty;
 - express complex IP address and ports based rulesets with one single iptables
   rule and benefit from the speed of IP sets
then ipset may be the proper tool for you.


%package libs
Summary:       Shared library providing the IP sets functionality

%description libs
This package contains the libraries which provide the IP sets funcionality.


%package devel
Summary:       Development files for %{name}
Requires:      %{name}-libs%{?_isa} == %{version}-%{release}
Requires:      kernel-headers

%description devel
This package contains the files required to develop software using the %{name}
libraries.


%package service
Summary:          %{name} service for %{name}s
Requires:         %{name} = %{version}-%{release}
BuildRequires:    systemd
Requires:         iptables-services
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
BuildArch:        noarch

%description service
This package provides the service %{name} that is split
out of the base package since it is not active by default.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1


%build
./autogen.sh
%configure --enable-static=no --with-kmod=no

# Just to make absolutely sure we are not building the bundled kernel module
# I have to do it after the configure run unfortunately
rm -fr kernel

# Prevent libtool from defining rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f '{}' \;

# install systemd unit file
install -d -m 755 %{buildroot}/%{_unitdir}
install -c -m 644 %{SOURCE1} %{buildroot}/%{_unitdir}

# install supporting script
install -d -m 755 %{buildroot}%{_libexecdir}/%{name}
install -c -m 755 %{SOURCE2} %{buildroot}%{_libexecdir}/%{name}

# install ipset-config
install -d -m 755 %{buildroot}%{_sysconfdir}/sysconfig
install -c -m 600 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{name}-config

# Create directory for configuration
mkdir -p %{buildroot}%{_sysconfdir}/%{name}

# Turn absolute symlink into a relative one
ln -sf %{name} %{buildroot}/%{_sbindir}/%{name}-translate


%preun
if [[ $1 -eq 0 && -n $(lsmod | grep "^xt_set ") ]]; then
    rmmod xt_set 2>/dev/null
    [[ $? -ne 0 ]] && echo Current iptables configuration requires ipsets && exit 1
fi


%ldconfig_scriptlets libs


%post service
%systemd_post %{name}.service
if [[ -f /etc/ipset/ipset ]] && [[ ! -f /etc/sysconfig/ipset ]]; then
	mv /etc/ipset/ipset /etc/sysconfig/ipset
	ln -s /etc/sysconfig/ipset /etc/ipset/ipset
	echo "Warning: ipset save location has moved to /etc/sysconfig"
fi
[[ -f /etc/sysconfig/iptables-config ]] && . /etc/sysconfig/iptables-config
[[ -f /etc/sysconfig/ip6tables-config ]] && . /etc/sysconfig/ip6tables-config
if [[ ${IPTABLES_SAVE_ON_STOP} == yes ]] || \
   [[ ${IP6TABLES_SAVE_ON_STOP} == yes ]]; then
	echo "Warning: ipset no longer saves automatically when iptables does"
	echo "         must enable explicitly in /etc/sysconfig/ipset-config"
fi

%preun service
if [[ $1 -eq 0 && -n $(lsmod | grep "^xt_set ") ]]; then
    rmmod xt_set 2>/dev/null
    [[ $? -ne 0 ]] && echo Current iptables configuration requires ipsets && exit 1
fi
%systemd_preun %{name}.service

%postun service
%systemd_postun_with_restart %{name}.service


%files
%doc ChangeLog
%license COPYING
%{_mandir}/man8/%{name}*.8.*
%{_sbindir}/%{name}
%{_sbindir}/%{name}-translate

%files libs
%license COPYING
%{_libdir}/lib%{name}.so.13*

%files devel
%{_includedir}/lib%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc
%{_mandir}/man3/libipset.3.*

%files service
%{_unitdir}/%{name}.service
%dir %{_libexecdir}/%{name}
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/sysconfig/ipset-config
%ghost %config(noreplace) %attr(0600,root,root) %{_sysconfdir}/sysconfig/ipset
%attr(0755,root,root) %{_libexecdir}/%{name}/%{name}.start-stop


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.24-3
- Prepare for Oreon 11 (RP1)
