%global _hardened_build 1
%global testsuite_ver d27dbd
%global clknetsim_ver 64df92
%global selinuxtype targeted
%bcond_without selinux

Name:		linuxptp
Version:	4.4
Release:	10%{?dist}
Summary:	PTP implementation for Linux

License:	GPL-2.0-or-later
URL:		https://www.linuxptp.org/

Source0:	https://downloads.nwtime.org/%{name}/%{name}-%{version}.tgz
Source1:	phc2sys.service
Source2:	ptp4l.service
Source3:	timemaster.service
Source4:	timemaster.conf
Source5:	ptp4l.conf
Source6:	ts2phc.service
Source7:	ts2phc.conf
Source8:	linuxptp.sysusers
Source9:	linuxptp.tmpfiles
# external test suite
Source10:	https://github.com/mlichvar/linuxptp-testsuite/archive/%{testsuite_ver}/linuxptp-testsuite-%{testsuite_ver}.tar.gz
# simulator for test suite
Source11:	https://github.com/mlichvar/clknetsim/archive/%{clknetsim_ver}/clknetsim-%{clknetsim_ver}.tar.gz
# selinux policy
Source20:	linuxptp.fc
Source21:	linuxptp.if
Source22:	linuxptp.te

# add support for dropping root privileges
Patch1:		linuxptp-droproot.patch
# oreon url source checksums begin
%global source0_sha256 61757bc0a58d789b8fcbdddf56c88a0230597184a70dcb2ac05b4c6b619f7d5c
%global source0_file linuxptp-4.4.tgz
%global source10_sha256 ed21012c5b99da72abea53e9499f8df35b2394d3558bfcb4dbd1e61ee7e6381d
%global source10_file linuxptp-testsuite-d27dbd.tar.gz
%global source11_sha256 63dfb389efc15323892a971200b65324fba102b5db2fa4a2269c3c57c8775453
%global source11_file clknetsim-64df92.tar.gz
# oreon url source checksums end

BuildRequires:	gcc gcc-c++ gnutls-devel libcap-devel make systemd

# require the clock group to be defined
Requires(pre):	setup >= 2.15.0-11

%{?systemd_requires}
%{?sysusers_requires_compat}

%if 0%{?with_selinux}
Requires:	(%{name}-selinux if selinux-policy-%{selinuxtype})
%endif

%description
This software is an implementation of the Precision Time Protocol (PTP)
according to IEEE standard 1588 for Linux. The dual design goals are to provide
a robust implementation of the standard and to use the most relevant and modern
Application Programming Interfaces (API) offered by the Linux kernel.
Supporting legacy APIs and other platforms is not a goal.

%if 0%{?with_selinux}
%package selinux
Summary:	linuxptp SELinux policy
BuildArch:	noarch
Requires:	selinux-policy-%{selinuxtype}
Requires(post):	selinux-policy-%{selinuxtype}
BuildRequires:	selinux-policy-devel
%{?selinux_requires}

%description selinux
linuxptp SELinux policy module

%endif

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/linuxptp-4.4.tgz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "61757bc0a58d789b8fcbdddf56c88a0230597184a70dcb2ac05b4c6b619f7d5c" || { echo "oreon: Source0 SHA256 mismatch for linuxptp-4.4.tgz" >&2; exit 1; })
%(f=%{_sourcedir}/linuxptp-testsuite-d27dbd.tar.gz; test -f "$f" || { echo "oreon: missing Source10 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ed21012c5b99da72abea53e9499f8df35b2394d3558bfcb4dbd1e61ee7e6381d" || { echo "oreon: Source10 SHA256 mismatch for linuxptp-testsuite-d27dbd.tar.gz" >&2; exit 1; })
%(f=%{_sourcedir}/clknetsim-64df92.tar.gz; test -f "$f" || { echo "oreon: missing Source11 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "63dfb389efc15323892a971200b65324fba102b5db2fa4a2269c3c57c8775453" || { echo "oreon: Source11 SHA256 mismatch for clknetsim-64df92.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -N
# autosetup doesn't accept multiple -a options
%__rpmuncompress -x %{SOURCE10}
%__rpmuncompress -x %{SOURCE11}
%autopatch -p1

# disable nettle support in favor of gnutls
sed -i 's|find .*"nettle"|true|' incdefs.sh

mv linuxptp-testsuite-%{testsuite_ver}* testsuite
mv clknetsim-%{clknetsim_ver}* testsuite/clknetsim

pushd testsuite/clknetsim
popd

mkdir selinux
cp -p %{SOURCE20} %{SOURCE21} %{SOURCE22} selinux

%build
%{make_build} \
	EXTRA_CFLAGS="$RPM_OPT_FLAGS" \
	EXTRA_LDFLAGS="$RPM_LD_FLAGS"

%if 0%{?with_selinux}
make -C selinux -f %{_datadir}/selinux/devel/Makefile linuxptp.pp
bzip2 -9 selinux/linuxptp.pp
%endif

%install
%makeinstall

mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir}/sysconfig,%{_unitdir},%{_mandir}/man5}
mkdir -p $RPM_BUILD_ROOT{%{_sysusersdir},%{_tmpfilesdir}}
install -m 644 -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE6} \
	$RPM_BUILD_ROOT%{_unitdir}
install -m 644 -p %{SOURCE4} %{SOURCE5} %{SOURCE7} \
	$RPM_BUILD_ROOT%{_sysconfdir}
install -m 644 -p %{SOURCE8} $RPM_BUILD_ROOT%{_sysusersdir}/linuxptp.conf
install -m 644 -p %{SOURCE9} $RPM_BUILD_ROOT%{_tmpfilesdir}/linuxptp.conf

echo 'OPTIONS="-f /etc/ptp4l.conf"' > \
	$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/ptp4l
echo 'OPTIONS="-a -r"' > $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/phc2sys
echo 'OPTIONS="-f /etc/ts2phc.conf"' > \
	$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/ts2phc

for s in ptp4l timemaster ts2phc; do
	echo ".so man8/$s.8" > $RPM_BUILD_ROOT%{_mandir}/man5/$s.conf.5
done

%if 0%{?with_selinux}
install -D -m 0644 selinux/linuxptp.pp.bz2 \
	$RPM_BUILD_ROOT%{_datadir}/selinux/packages/%{selinuxtype}/linuxptp.pp.bz2
install -D -p -m 0644 selinux/linuxptp.if \
	$RPM_BUILD_ROOT%{_datadir}/selinux/devel/include/distributed/linuxptp.if
%endif

%check
cd testsuite
# set random seed to get deterministic results
export CLKNETSIM_RANDOM_SEED=26743
%{make_build} -C clknetsim
PATH=..:$PATH ./run

%pre
%sysusers_create_package linuxptp %{SOURCE8}

%post
%tmpfiles_create_package linuxptp %{SOURCE9}
%systemd_post phc2sys.service ptp4l.service timemaster.service ts2phc.service

%preun
%systemd_preun phc2sys.service ptp4l.service timemaster.service ts2phc.service

%postun
%systemd_postun_with_restart phc2sys.service ptp4l.service timemaster.service ts2phc.service

%if 0%{?with_selinux}
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/linuxptp.pp.bz2
%selinux_relabel_post -s %{selinuxtype}

%postun selinux
if [ $1 -eq 0 ]; then
	%selinux_modules_uninstall -s %{selinuxtype} linuxptp
	%selinux_relabel_post -s %{selinuxtype}
fi

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/linuxptp.pp.*
%{_datadir}/selinux/devel/include/distributed/linuxptp.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/linuxptp

%endif

%files
%license COPYING
%doc README.org configs
%config(noreplace) %{_sysconfdir}/ptp4l.conf
%config(noreplace) %{_sysconfdir}/sysconfig/phc2sys
%config(noreplace) %{_sysconfdir}/sysconfig/ptp4l
%config(noreplace) %{_sysconfdir}/sysconfig/ts2phc
%config(noreplace) %{_sysconfdir}/timemaster.conf
%config(noreplace) %{_sysconfdir}/ts2phc.conf
%{_unitdir}/phc2sys.service
%{_unitdir}/ptp4l.service
%{_unitdir}/timemaster.service
%{_unitdir}/ts2phc.service
%{_sysusersdir}/linuxptp.conf
%{_tmpfilesdir}/linuxptp.conf
%{_sbindir}/hwstamp_ctl
%{_sbindir}/nsm
%{_sbindir}/phc2sys
%{_sbindir}/phc_ctl
%{_sbindir}/pmc
%{_sbindir}/ptp4l
%{_sbindir}/timemaster
%{_sbindir}/ts2phc
%{_sbindir}/tz2alt
%{_mandir}/man5/*.5*
%{_mandir}/man8/*.8*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.4-10
- Prepare for Oreon 11 (RP1)
