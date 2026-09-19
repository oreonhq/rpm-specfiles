%global source0_hash 7b603d6200ab0b26034e9e200fab949cc0a8e5fdd4df2c80b8fc5b1c37e7b930

%global _hardened_build 1

Summary:          Fast NTLM authentication proxy with tunneling
Name:             cntlm
Version:          0.92.3
Release:          34%{?dist}
License:          GPL-2.0-or-later

URL:              http://cntlm.sourceforge.net/
Source0:          http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:          cntlm.tmpfiles
Source2:          cntlm.service
# Don't override global CFLAGS/LDFLAGS and don't strip installed binaries
Patch0:           cntlm_makefile.patch
Patch1: cntlm-c99.patch

BuildRequires:    gcc
BuildRequires:    make
BuildRequires:    systemd
%{?systemd_requires}

%description
Cntlm is a fast and efficient NTLM proxy, with support for TCP/IP tunneling,
authenticated connection caching, ACLs, proper daemon logging and behavior
and much more. It has up to ten times faster responses than similar NTLM
proxies, while using by orders or magnitude less RAM and CPU. Manual page
contains detailed information.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Create a sysusers.d config file
cat >cntlm.sysusers.conf <<EOF
u cntlm - '%{name} daemon' %{_localstatedir}/run/%{name} -
EOF

%build
%configure
%make_build SYSCONFDIR=%{_sysconfdir}

%install
make BINDIR=%{buildroot}%{_sbindir} MANDIR=%{buildroot}%{_mandir} SYSCONFDIR=%{buildroot}%{_sysconfdir} install

install -D -m 0644 rpm/%{name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/cntlmd
install -D -m 0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

install -D -d -m 0755 %{buildroot}/run/%{name}/

install -m0644 -D cntlm.sysusers.conf %{buildroot}%{_sysusersdir}/cntlm.conf

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc README COPYRIGHT
%license LICENSE
%{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/sysconfig/cntlmd
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service
%attr(755, %{name}, %{name}) %dir /run/%{name}/
%{_sysusersdir}/cntlm.conf

%changelog
%autochangelog
