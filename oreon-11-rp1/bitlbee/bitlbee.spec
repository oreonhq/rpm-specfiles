%global source0_hash 9f15de46f29b46bf1e39fc50bdf4515e71b17f551f3955094c5da792d962107e
%bcond_without otr
Summary:        IRC to other chat networks gateway
Name:              bitlbee
Version:           3.6
Release:        20%{?dist}
License:           GPL-2.0-or-later AND BSD-2-Clause AND ISC AND LGPL-2.1-only
URL:               https://www.bitlbee.org/
Source0:        https://get.bitlbee.org/src/%{name}-%{version}.tar.gz
Source1:           bitlbee.sysusersd
Patch0:            bitlbee-forkdaemon.patch
Patch1:            bitlbee-twitter.patch
%if %{with otr}
%endif
%{?systemd_requires}
%{?sysusers_requires_compat}
# oreon:deps
BuildRequires:  /usr/bin/python3
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gnutls-devel
BuildRequires:  libotr-devel
BuildRequires:  libpurple-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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
install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf
mkdir -p $RPM_BUILD_ROOT{%{_localstatedir}/lib,%{_libdir}}/%{name}/
%oreon_autofiles bitlbee-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles bitlbee-otr usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

%sysusers_create_compat %{SOURCE1}
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n bitlbee-devel -f %{oreon_filedir}/bitlbee-devel.list
%files -n bitlbee-otr -f %{oreon_filedir}/bitlbee-otr.list

%changelog

%autochangelog
