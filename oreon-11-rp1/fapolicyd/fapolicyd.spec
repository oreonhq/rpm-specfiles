%global selinuxtype targeted
%global moduletype distributed
%define semodule_version 1.1

Summary: Application Whitelisting Daemon
Name: fapolicyd
Version: 1.4.3
Release: 2%{?dist}
License: GPL-3.0-or-later
URL: https://github.com/linux-application-whitelisting/fapolicyd
Source0: https://github.com/linux-application-whitelisting/fapolicyd/releases/download/v%{version}/fapolicyd-%{version}.tar.gz
Source1: https://github.com/linux-application-whitelisting/%{name}-selinux/releases/download/v%{semodule_version}/%{name}-selinux-%{semodule_version}.tar.gz
Source2: https://github.com/bachradsusi.gpg
Source3: fapolicyd.sysusers
Source10: https://github.com/linux-application-whitelisting/fapolicyd/releases/download/v%{version}/fapolicyd-%{version}.tar.gz.asc
Source11: https://github.com/linux-application-whitelisting/%{name}-selinux/releases/download/v%{semodule_version}/%{name}-selinux-%{semodule_version}.tar.gz.asc
# we bundle uthash for eln
Source20: https://github.com/troydhanson/uthash/archive/refs/tags/v2.3.0.tar.gz#/uthash-2.3.0.tar.gz
# oreon url source checksums begin
%global source0_sha256 778694ef49ae25492c929e158eeccbc50e6ef37312db2c02fb494e2348029aaa
%global source0_file fapolicyd-1.4.3.tar.gz
%global source1_sha256 3f687227fc9c9f2c342b12fa2c03cd60b6172dda3c6a13884b6b443398939a05
%global source1_file fapolicyd-selinux-1.1.tar.gz
%global source20_sha256 e10382ab75518bad8319eb922ad04f907cb20cccb451a3aa980c9d005e661acc
%global source20_file v2.3.0.tar.gz
# oreon url source checksums end

# https://github.com/linux-application-whitelisting/fapolicyd
# $ git format-patch -N v1.4.1
# https://github.com/linux-application-whitelisting/fapolicyd-selinux
# $ git format-patch -N --start-number 100 --src-prefix=a/fapolicyd-selinux-1.0/ --dst-prefix=b/fapolicyd-selinux-1.0/ v1.0
# $ for j in [0-9]*.patch; do printf "Patch%s: %s\n" ${j/-*/} $j; done
# Patch list start
# Patch list end

BuildRequires: gcc
BuildRequires: kernel-headers
BuildRequires: autoconf automake make gcc libtool
BuildRequires: systemd systemd-devel openssl-devel rpm-devel file-devel file
BuildRequires: libcap-ng-devel libseccomp-devel lmdb-devel
BuildRequires: python3-devel
%if 0%{?fedora} || 0%{?rhel} > 10
BuildRequires: gpgverify
%else
BuildRequires: gnupg
%endif

%if 0%{?rhel} == 0
BuildRequires: uthash-devel
%endif

Requires: rpm-plugin-fapolicyd
Recommends: %{name}-selinux
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
Fapolicyd (File Access Policy Daemon) implements application whitelisting
to decide file access rights. Applications that are known via a reputation
source are allowed access while unknown applications are not. The daemon
makes use of the kernel's fanotify interface to determine file access rights.

%package        selinux
Summary:        Fapolicyd selinux
Group:          Applications/System
Requires:       %{name} = %{version}-%{release}
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel
BuildArch: noarch
%{?selinux_requires}

%description    selinux
The %{name}-selinux package contains selinux policy for the %{name} daemon.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/fapolicyd-1.4.3.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "778694ef49ae25492c929e158eeccbc50e6ef37312db2c02fb494e2348029aaa" || { echo "oreon: Source0 SHA256 mismatch for fapolicyd-1.4.3.tar.gz" >&2; exit 1; })
%(f=%{_sourcedir}/fapolicyd-selinux-1.1.tar.gz; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3f687227fc9c9f2c342b12fa2c03cd60b6172dda3c6a13884b6b443398939a05" || { echo "oreon: Source1 SHA256 mismatch for fapolicyd-selinux-1.1.tar.gz" >&2; exit 1; })
%(f=%{_sourcedir}/v2.3.0.tar.gz; test -f "$f" || { echo "oreon: missing Source20 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e10382ab75518bad8319eb922ad04f907cb20cccb451a3aa980c9d005e661acc" || { echo "oreon: Source20 SHA256 mismatch for v2.3.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE10}' --data='%{SOURCE0}'
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE11}' --data='%{SOURCE1}'

%setup -q

# selinux
%autosetup -D -T -a 1 -p 1

%if 0%{?rhel} != 0
%setup -q -D -T -b 20
%endif

# generate rules for python
sed -i "s|%python2_path%|`readlink -f %{__python2}`|g" rules.d/*.rules
sed -i "s|%python3_path%|`readlink -f %{__python3}`|g" rules.d/*.rules

# Detect run time linker directly from bash
interpret=`readelf -e /usr/bin/bash \
    | grep Requesting \
    | sed 's/.$//' \
    | rev | cut -d" " -f1 \
    | rev`

sed -i "s|%ld_so_path%|`realpath $interpret`|g" rules.d/*.rules

%build
cp INSTALL INSTALL.tmp

# necessary for updating CFLAGS below
%set_build_flags

%if 0%{?rhel} != 0
export CFLAGS="$CFLAGS -I%{_builddir}/uthash-2.3.0/include"
%endif

./autogen.sh
%configure \
    --with-audit \
    --with-rpm \
    --disable-shared

%make_build

# selinux
pushd %{name}-selinux-%{semodule_version}
make
popd

%check
make check

# selinux
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%install
%make_install
install -p -m 644 -D init/%{name}-tmpfiles.conf %{buildroot}/%{_tmpfilesdir}/%{name}.conf
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf
mkdir -p %{buildroot}/%{_localstatedir}/lib/%{name}
mkdir -p %{buildroot}/run/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/trust.d
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/rules.d
# get list of file names between known-libs and restrictive from sample-rules/README-rules
cat %{buildroot}/%{_datadir}/%{name}/sample-rules/README-rules \
  | grep -A 100 'known-libs' \
  | grep -B 100 'restrictive' \
  | grep '^[0-9]' > %{buildroot}/%{_datadir}/%{name}/default-ruleset.known-libs
chmod 644 %{buildroot}/%{_datadir}/%{name}/default-ruleset.known-libs

# selinux
install -d %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}
install -m 0644 %{name}-selinux-%{semodule_version}/%{name}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}
install -m 0644 %{name}-selinux-%{semodule_version}/%{name}-hardening.cil %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}
install -d -p %{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}
install -p -m 644 %{name}-selinux-%{semodule_version}/%{name}.if %{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}/%{name}.if

#cleanup
find %{buildroot} \( -name '*.la' -o -name '*.a' \) -delete

%post
# if no pre-existing rule file
if [ ! -e %{_sysconfdir}/%{name}/%{name}.rules ] ; then
 files=`ls %{_sysconfdir}/%{name}/rules.d/ 2>/dev/null | wc -w`
 # Only if no pre-existing component rules
 if [ "$files" -eq 0 ] ; then
  ## Install the known libs policy
  for rulesfile in `cat %{_datadir}/%{name}/default-ruleset.known-libs`; do
    cp %{_datadir}/%{name}/sample-rules/$rulesfile  %{_sysconfdir}/%{name}/rules.d/
  done
  chgrp %{name} %{_sysconfdir}/%{name}/rules.d/*
  if [ -x /usr/sbin/restorecon ] ; then
   # restore correct label
   /usr/sbin/restorecon -F %{_sysconfdir}/%{name}/rules.d/*
  fi
  fagenrules >/dev/null
 fi
fi
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc README.md
%{!?_licensedir:%global license %%doc}
%license COPYING
%attr(755,root,root) %dir %{_datadir}/%{name}
%attr(755,root,root) %dir %{_datadir}/%{name}/sample-rules
%attr(644,root,root) %{_datadir}/%{name}/default-ruleset.known-libs
%attr(644,root,root) %{_datadir}/%{name}/sample-rules/*
%attr(644,root,root) %{_datadir}/%{name}/fapolicyd-magic.mgc
%attr(750,root,%{name}) %dir %{_sysconfdir}/%{name}
%attr(750,root,%{name}) %dir %{_sysconfdir}/%{name}/trust.d
%attr(750,root,%{name}) %dir %{_sysconfdir}/%{name}/rules.d
%attr(644,root,root) %{_sysconfdir}/bash_completion.d/*
%ghost %{_sysconfdir}/%{name}/rules.d/*
%ghost %{_sysconfdir}/%{name}/%{name}.rules
%config(noreplace) %attr(644,root,%{name}) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %attr(644,root,%{name}) %{_sysconfdir}/%{name}/%{name}-filter.conf
%config(noreplace) %attr(644,root,%{name}) %{_sysconfdir}/%{name}/%{name}.trust
%ghost %attr(644,root,%{name}) %{_sysconfdir}/%{name}/compiled.rules
%attr(644,root,root) %{_unitdir}/%{name}.service
%attr(644,root,root) %{_tmpfilesdir}/%{name}.conf
%attr(644,root,root) %{_sysusersdir}/%{name}.conf
%attr(755,root,root) %{_bindir}/%{name}-rpm-loader
%attr(755,root,root) %{_sbindir}/%{name}
%attr(755,root,root) %{_sbindir}/%{name}-cli
%attr(755,root,root) %{_sbindir}/fagenrules
%attr(644,root,root) %{_mandir}/man8/*
%attr(644,root,root) %{_mandir}/man5/*
%ghost %attr(440,%{name},%{name}) %verify(not md5 size mtime) %{_localstatedir}/log/%{name}-access.log
%attr(770,root,%{name}) %dir %{_localstatedir}/lib/%{name}
%attr(770,root,%{name}) %dir /run/%{name}
%ghost %attr(660,root,%{name}) /run/%{name}/%{name}.fifo
%ghost %attr(660,%{name},%{name}) %verify(not md5 size mtime) %{_localstatedir}/lib/%{name}/data.mdb
%ghost %attr(660,%{name},%{name}) %verify(not md5 size mtime) %{_localstatedir}/lib/%{name}/lock.mdb

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%{_datadir}/selinux/packages/%{selinuxtype}/%{name}-hardening.cil
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{name}
%{_datadir}/selinux/devel/include/%{moduletype}/%{name}.if

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2 %{_datadir}/selinux/packages/%{selinuxtype}/%{name}-hardening.cil
%selinux_relabel_post -s %{selinuxtype}

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}-hardening %{name}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.3-2
- Prepare for Oreon 11 (RP1)
