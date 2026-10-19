%global source20_hash e10382ab75518bad8319eb922ad04f907cb20cccb451a3aa980c9d005e661acc
%global source11_hash 5e2bd8d41dd32da61087ef2d33875f18f1453019f0c44575bdbaa3b3d7576c3d
%global source10_hash b1e713cc6cbe588a37edf96f838eb6d9ed8e1f348b305516a849118a1165da4c
%global source2_hash caf7cb1981e2f5fa5952c2f3a11f9247221d16df4d9111ce15164a64675fc452
%global source1_hash 3f687227fc9c9f2c342b12fa2c03cd60b6172dda3c6a13884b6b443398939a05
%global source0_hash fc2cdf1acb4d17e2200c0acc8f9fd80344d13d0c672582cfa6c84e895b8d2d75
%global source2_key_fpr E853C1848B0185CF42864DF363A8AD4B982C4373
%global selinuxtype targeted
%global moduletype distributed
%define semodule_version 1.1
Summary:        Application Whitelisting Daemon
Name: fapolicyd
Version: 2.0.1
Release:        1%{?dist}
License: GPL-3.0-or-later
URL: https://github.com/linux-application-whitelisting/fapolicyd
Source0:        https://github.com/linux-application-whitelisting/fapolicyd/releases/download/v%{version}/fapolicyd-%{version}.tar.gz
Source1:        https://github.com/linux-application-whitelisting/%{name}-selinux/releases/download/v%{semodule_version}/%{name}-selinux-%{semodule_version}.tar.gz
Source2:        https://github.com/bachradsusi.gpg
Source3: fapolicyd.sysusers
Source10:        https://github.com/linux-application-whitelisting/fapolicyd/releases/download/v%{version}/fapolicyd-%{version}.tar.gz.asc
Source11:        https://github.com/linux-application-whitelisting/%{name}-selinux/releases/download/v%{semodule_version}/%{name}-selinux-%{semodule_version}.tar.gz.asc
Source20: https://github.com/troydhanson/uthash/archive/refs/tags/v2.3.0.tar.gz#/uthash-2.3.0.tar.gz
Requires: rpm-plugin-fapolicyd
Recommends: %{name}-selinux
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  file
BuildRequires:  file-devel
BuildRequires:  gcc
BuildRequires:  gnupg
BuildRequires:  kernel-headers
BuildRequires:  libcap-ng-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libtool
BuildRequires:  lmdb-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(systemd)
BuildRequires:  python3-devel
BuildRequires:  rpm-devel
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
# /oreon:deps
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

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE10}' --data='%{SOURCE0}'
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE11}' --data='%{SOURCE1}'

%setup -q

# selinux
%autosetup -D -T -a 1 -p 1

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
%set_build_flags
./autogen.sh
%configure \
    --with-audit \
    --with-rpm \
    --disable-shared
%make_build
pushd %{name}-selinux-%{semodule_version}
make
popd
%check

make check
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
cat %{buildroot}/%{_datadir}/%{name}/sample-rules/README-rules \
  | grep -A 100 'known-libs' \
  | grep -B 100 'restrictive' \
  | grep '^[0-9]' > %{buildroot}/%{_datadir}/%{name}/default-ruleset.known-libs
chmod 644 %{buildroot}/%{_datadir}/%{name}/default-ruleset.known-libs
install -d %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}
install -m 0644 %{name}-selinux-%{semodule_version}/%{name}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}
install -m 0644 %{name}-selinux-%{semodule_version}/%{name}-hardening.cil %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}
install -d -p %{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}
install -p -m 644 %{name}-selinux-%{semodule_version}/%{name}.if %{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}/%{name}.if
find %{buildroot} \( -name '*.la' -o -name '*.a' \) -delete
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

if [ ! -e %{_sysconfdir}/%{name}/%{name}.rules ] ; then
 files=`ls %{_sysconfdir}/%{name}/rules.d/ 2>/dev/null | wc -w`
 if [ "$files" -eq 0 ] ; then
  for rulesfile in `cat %{_datadir}/%{name}/default-ruleset.known-libs`; do
    cp %{_datadir}/%{name}/sample-rules/$rulesfile  %{_sysconfdir}/%{name}/rules.d/
  done
  chgrp %{name} %{_sysconfdir}/%{name}/rules.d/*
  if [ -x /usr/sbin/restorecon ] ; then
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
%post selinux

%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2 %{_datadir}/selinux/packages/%{selinuxtype}/%{name}-hardening.cil
%selinux_relabel_post -s %{selinuxtype}
%postun selinux

if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}-hardening %{name}
fi
%posttrans selinux

%selinux_relabel_post -s %{selinuxtype}
%files -f %{oreon_filedir}/main.list
%files -n fapolicyd-selinux -f %{oreon_filedir}/fapolicyd-selinux.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.3-2
- Prepare for Oreon 11 (RP1)
