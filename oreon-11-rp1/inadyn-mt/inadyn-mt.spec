%global source0_hash f69bea12d96b66f9f662a8df0730c60457b24f5fb5308b109936880ebf7be5ca

Name:           inadyn-mt
Version:        2.28.10
Release:        26%{?dist}
Summary:        Dynamic DNS Client
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            http://inadyn-mt.sourceforge.net
Source0:        http://prdownloads.sourceforge.net/inadyn-mt/inadyn-mt.v.0%{version}.tar.gz
Source1:        inadyn-mt.conf
Source2:        inadyn.service
Source3:        inadyn-nm-dispatcher
Patch1:         inadyn-mt-libao.patch
# https://gitlab.com/bhoover/inadyn-mt/commit/84c18b121886e22375e2163d495f75a207b96d11
Patch2:         inadyn-mt-gcc10.patch
Patch3:         inadyn-mt-c99.patch
Patch4:         inadyn-mt-c23.patch

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  libao-devel
BuildRequires:  systemd-units
BuildRequires: make

Obsoletes:      inadyn < %{version}
Provides:       inadyn = %{version}-%{release}

Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units

Obsoletes:      inadyn-mt-units < %{version}-%{release}
Provides:       inadyn-mi-units = %{version}-%{release}

Obsoletes:      inadyn-mt-sysvinit < %{version}-%{release}
Provides:       inadyn-mt-sysvinit = %{version}-%{release}

%description
INADYN-MT is a dynamic DNS client. It maintains the IP address of 
a host name. It periodically checks whether the IP address stored
by the DSN server is the real current address of the machine that
is running INADYN-MT.

Before using inadyn-mt for the first time you must use the DynDNS
provider's web interface to create the entry for the hostname. You
should then fill in /etc/inadyn.conf with the appropriate detail

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %name.v.0%{version}
%patch -P1 -p1 -b .libao
%patch -P2 -p1 -b .gcc10
%patch -P3 -p1 -b .c99
%patch -P4 -p1 -b .c23

# Create a sysusers.d config file
cat >inadyn-mt.sysusers.conf <<EOF
u inadyn - 'Dynamic DNS client' /var/cache/inadyn-mt -
EOF

%build
rm -rf bin/
autoreconf
%configure --prefix=/usr/share
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
install -m 0755 src/inadyn-mt $RPM_BUILD_ROOT%{_sbindir}/inadyn

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man5
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 0644 man/inadyn.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 0644 man/inadyn.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/inadyn-mt/lang
cp lang/* $RPM_BUILD_ROOT%{_datadir}/inadyn-mt/lang

mkdir -p $RPM_BUILD_ROOT%{_datadir}/inadyn-mt/extra
cp -R extra/* $RPM_BUILD_ROOT%{_datadir}/inadyn-mt/extra

mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
install -p -m 0644 %{SOURCE2} ${RPM_BUILD_ROOT}%{_unitdir}

mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/lib/NetworkManager/dispatcher.d
install -p %{SOURCE3} ${RPM_BUILD_ROOT}%{_prefix}/lib/NetworkManager/dispatcher.d/30-inadyn

mkdir -p $RPM_BUILD_ROOT/var/cache/inadyn-mt

install -m0644 -D inadyn-mt.sysusers.conf %{buildroot}%{_sysusersdir}/inadyn-mt.conf

%post
%systemd_post inadyn.service
[ $1 -gt 1 ] && chown -R inadyn: /var/cache/inadyn-mt || :

%preun
%systemd_preun inadyn.service

%postun
%systemd_postun_with_restart inadyn.service

%files 
%license COPYING
%doc readme.html
%{_sbindir}/inadyn
%{_unitdir}/inadyn.service
%{_mandir}/man*/*
%attr(640,inadyn,inadyn) %config(noreplace) %{_sysconfdir}/%{name}.conf
%{_prefix}/lib/NetworkManager/
%{_datadir}/%{name}/
%attr(755,inadyn,inadyn) %dir /var/cache/inadyn-mt/
%{_sysusersdir}/inadyn-mt.conf

%changelog
%autochangelog
