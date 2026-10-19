%global source0_hash dfc99484bc7ffea27a3169e84d6c217988eda47b208ab2e5524dc2a5dd158f4e
%global runcheck	0
%global hitch_user	hitch
%global hitch_group	hitch
%global hitch_homedir	%{_sharedstatedir}/hitch
%global hitch_confdir	%{_sysconfdir}/hitch
%global hitch_datadir	%{_datadir}/hitch
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global _hardened_build 1
Name:		hitch
Version:	1.8.0
Release:        1%{?dist}
Summary:        Network proxy that terminates TLS/SSL connections
License:	LicenseRef-Callaway-BSD
URL:		https://hitch-tls.org/
Source0:        https://%{name}-tls.org/source/%{name}-%{version}.tar.gz
Source1:	hitch.sysusers
Requires:	openssl
Patch0:		hitch.systemd.service.patch
Patch1:		hitch-1.8.0.fix_el10_build.patch
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%{?sysusers_requires_compat}
# oreon:deps
BuildRequires:  libev-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd
# /oreon:deps
%description
hitch is a network proxy that terminates TLS/SSL connections and forwards the
unencrypted traffic to some backend. It is designed to handle 10s of thousands
of connections efficiently on multicore machines.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}%{?v_rc}
%patch -P0

%build

export RST2MAN=/bin/true
%configure --docdir=%_pkgdocdir
make %{?_smp_mflags}
%install
%make_install
sed   '
	s/user = .*/user = "%{hitch_user}"/g;
	s/group = .*/group = "%{hitch_group}"/g;
	s/backend = "\[127.0.0.1\]:8000"/backend = "[127.0.0.1]:6081"/g;
	s/workers = ..../workers = auto/;
	$a\syslog = on
	$a\log-level = 1
	$a\# Add pem files to this directory
	$a\pem-dir = "/etc/pki/tls/private"
	' hitch.conf.example > hitch.conf
rm -f %{buildroot}%{_datarootdir}/doc/%{name}/hitch.conf.example
install -p -D -m 0644 hitch.conf %{buildroot}%{_sysconfdir}/hitch/hitch.conf
install -d -m 0755 %{buildroot}%{hitch_homedir}
install -d -m 0755 %{buildroot}%{hitch_datadir}
install -p -D -m 0644 hitch.service %{buildroot}%{_unitdir}/hitch.service
install -p -D -m 0644 limit.conf    %{buildroot}%{_sysconfdir}/systemd/system/%{name}.service.d/limit.conf
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/hitch.conf
%oreon_autofiles main

%check

%if 0%{?runcheck} == 1
make check
%endif
%pre

%sysusers_create_compat %{SOURCE1}
%post

%systemd_post hitch.service
%preun

%systemd_preun hitch.service
%postun

%systemd_postun_with_restart hitch.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
