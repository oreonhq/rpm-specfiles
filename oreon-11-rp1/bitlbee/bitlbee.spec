%global source0_hash 9f15de46f29b46bf1e39fc50bdf4515e71b17f551f3955094c5da792d962107e

%bcond_without otr

Summary:           IRC to other chat networks gateway
Name:              bitlbee
Version:           3.6
Release:           20%{?dist}
# BitlBee is GPL-2.0-or-later but uses other source codes, breakdown:
# BSD-2-Clause: lib/json.[ch]
# ISC: lib/ns_parse.c
# LGPL-2.1-only: protocols/twitter/twitter{,_http,_lib}.[ch]
License:           GPL-2.0-or-later AND BSD-2-Clause AND ISC AND LGPL-2.1-only
URL:               https://www.bitlbee.org/
Source0:           https://get.bitlbee.org/src/%{name}-%{version}.tar.gz
Source1:           bitlbee.sysusersd
# Downstream: Run bitlbee as non-root and bind to 127.0.0.1 only
Patch0:            bitlbee-forkdaemon.patch
# Replace the now dead Twitter tokens with fresh ones
# See: https://github.com/bitlbee/bitlbee/pull/187
Patch1:            bitlbee-twitter.patch

BuildRequires:     gcc
BuildRequires:     make
BuildRequires:     glib2-devel >= 2.16
BuildRequires:     gnutls-devel
BuildRequires:     systemd-rpm-macros
%if %{with otr}
BuildRequires:     libotr-devel >= 4.0
%endif
BuildRequires:     libpurple-devel
%{?systemd_requires}
%{?sysusers_requires_compat}

# Documentation (user-guide.html)
BuildRequires:     %{_bindir}/python3
BuildRequires:     libxslt
BuildRequires:     docbook-style-xsl

%description
BitlBee is an IRC to other chat networks gateway. BitlBee can be used as
an IRC server which forwards everything you say to people on other chat
networks like XMPP/Jabber (including Google Talk and Hipchat) and Twitter
microblogging network (and all other Twitter API compatible services like
status.net). There are also plugins for facebook and steam, and even more
protocols can be used via libpurple.

%package devel
Summary:           Development files for bitlbee
Requires:          %{name}%{?_isa} = %{version}-%{release}, pkgconfig

%description devel
The bitlbee-devel package includes header files necessary for building and
developing programs and plugins which use bitlbee.

%if %{with otr}
%package otr
Summary:           OTR plugin for bitlbee
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description otr
The bitlbee-otr package includes OTR plugin for bitlbee. Off-the-Record
messaging, commonly referred to as OTR, provides perfect forward secrecy
and malleable encryption.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

echo With OTR %with_otr
%setup -q
%patch -P0 -p1 -b .forkdaemon
%patch -P1 -p1
touch -c -r bitlbee.conf{.forkdaemon,}

%build
export PYTHON="%{_bindir}/python3"
export CFLAGS="$RPM_OPT_FLAGS"
./configure \
  --prefix=%{_prefix} \
  --sbindir=%{_sbindir} \
  --etcdir=%{_sysconfdir}/%{name} \
  --mandir=%{_mandir} \
  --datadir=%{_datadir}/%{name} \
  --config=%{_localstatedir}/lib/%{name} \
  --pcdir=%{_libdir}/pkgconfig \
  --plugindir=%{_libdir}/%{name} \
  --systemdsystemunitdir=%{_unitdir} \
  --strip=0 \
  --plugins=1 \
  --ssl=gnutls \
  --jabber=1 \
  --twitter=1 \
  --purple=1 \
%if %{with otr}
  --otr=plugin
%endif

%make_build VERBOSE=""
(cd doc/user-guide/ && make user-guide.html)

%install
%make_install install-etc install-dev install-systemd

# Declarative allocation of system users and groups
install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf

# Create some directories manually
mkdir -p $RPM_BUILD_ROOT{%{_localstatedir}/lib,%{_libdir}}/%{name}/

%pre
%sysusers_create_compat %{SOURCE1}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%doc doc/{AUTHORS,CHANGES,CREDITS,FAQ,README}
%doc doc/user-guide/user-guide.html
%attr(0750,root,bitlbee) %dir %{_sysconfdir}/%{name}/
%attr(0640,root,bitlbee) %config(noreplace) %{_sysconfdir}/%{name}/*
%{_sbindir}/%{name}
%dir %{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_mandir}/man?/%{name}*
%attr(0750,bitlbee,bitlbee) %dir %{_localstatedir}/lib/%{name}/
%{_unitdir}/%{name}*
%{_sysusersdir}/%{name}.conf

%files devel
%doc doc/example_plugin.c
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%if %{with otr}
%files otr
%{_libdir}/%{name}/otr.so
%endif

%changelog
%autochangelog
