%global source0_hash e9f87b43548471a300f8499fe4e3d14f3acaa4fc51ed456203169e58d2413490

%global _hardened_build 1
# Do no change username -- hardcoded in dictd.c
%global username    dictd
%global homedir     %{_datadir}/dict/dictd
%global selinux_variants mls targeted

Summary:   DICT protocol (RFC 2229) server and command-line client
Name:      dictd
Version:   1.13.3
Release:   5%{?dist}
License:   GPL-2.0-only AND GPL-2.0-or-later AND GPL-1.0-or-later AND GPL-3.0-or-later AND MIT AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
Source0:   https://github.com/cheusov/dictd/archive/%{version}/%{name}-%{version}.tar.gz
Source1:   dictd.service
Source2:   dictd2.te
Source3:   dictd.conf
Source4:   dict.conf
Patch0:    0001-Fix-C99-compatibility-issues-in-lexer-parser-integra.patch
Patch1:    0001-remove-use-of-deprecated-inet_aton-and-inet_ntoa.patch
URL:       http://www.dict.org/

BuildRequires: flex
BuildRequires: flex-devel
Buildrequires: autoconf
BuildRequires: bison
BuildRequires: libtool
BuildRequires: libtool-ltdl-devel
BuildRequires: libmaa-devel
BuildRequires: byacc
BuildRequires: libdbi-devel
BuildRequires: zlib-devel
BuildRequires: gawk
BuildRequires: gcc
BuildRequires: pkgconfig(systemd)
BuildRequires: checkpolicy, selinux-policy-devel

%description
Command-line client for the DICT protocol.  The Dictionary Server
Protocol (DICT) is a TCP transaction based query/response protocol that
allows a client to access dictionary definitions from a set of natural
language dictionary databases.

%package server
Summary: Server for the Dictionary Server Protocol (DICT)
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%if "%{_selinux_policy_version}" != ""
Requires:       selinux-policy >= %{_selinux_policy_version}
%endif

%description server
A server for the DICT protocol. You need to install dictd-usable databases
before you can use this server. Those can be found p.e. at
ftp://ftp.dict.org/pub/dict/pre/
More information can be found in the INSTALL file in this package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

autoreconf -fiv
mkdir SELinux
cp -p %{SOURCE2} SELinux

# Create a sysusers.d config file
cat >dictd.sysusers.conf <<EOF
u dictd - 'dictd dictionary server' %{homedir} -
EOF

%build
pushd SELinux
for selinuxvariant in %{selinux_variants}
do
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
  mv dictd2.pp dictd2.pp.${selinuxvariant}
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
popd

%configure --enable-dictorg --disable-plugin
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{homedir}
mkdir -p %{buildroot}%{_unitdir}
install -m 755 %{SOURCE1} %{buildroot}%{_unitdir}/dictd.service
mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/dictd.conf
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/dict.conf

for selinuxvariant in %{selinux_variants}
do
  install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
  install -p -m 644 SELinux/dictd2.pp.${selinuxvariant} \
    %{buildroot}%{_datadir}/selinux/${selinuxvariant}/dictd2.pp
done

install -m0644 -D dictd.sysusers.conf %{buildroot}%{_sysusersdir}/dictd.conf

%post server
%systemd_post dictd.service

%preun server
%systemd_preun dictd.service

%postun server
%systemd_postun_with_restart dictd.service

%files
%doc ANNOUNCE COPYING README doc/rfc2229.txt doc/security.doc
%doc examples/dict1.conf
%{_bindir}/dict
%{_mandir}/man1/dict.1*
%config(noreplace) %{_sysconfdir}/dict.conf

%files server
%doc ANNOUNCE COPYING INSTALL README doc/rfc2229.txt doc/security.doc
%doc examples/dictd*
%exclude %{_mandir}/man1/dict.1*
%exclude %{_bindir}/dict
%{_bindir}/dict_lookup
%{_bindir}/dictfmt
%{_bindir}/dictfmt_index2suffix
%{_bindir}/dictfmt_index2word
%{_bindir}/dictl
%{_bindir}/dictunformat
%{_bindir}/dictzip
%{_bindir}/colorit
%{_sbindir}/dictd
%{_mandir}/man1/colorit.1*
%{_mandir}/man1/dict_lookup.1*
%{_mandir}/man1/dictfmt.1*
%{_mandir}/man1/dictfmt_index2suffix.1*
%{_mandir}/man1/dictfmt_index2word.1*
%{_mandir}/man1/dictl.1*
%{_mandir}/man1/dictunformat.1*
%{_mandir}/man1/dictzip.1*
%{_mandir}/man8/dictd.8*
%attr(0644,root,root) %{_unitdir}/dictd.service
%{_sysusersdir}/dictd.conf
%{homedir}
%config(noreplace) %{_sysconfdir}/dictd.conf
%doc SELinux
%{_datadir}/selinux/*/dictd2.pp

%changelog
%autochangelog
