%global source0_hash 0b405a6c011240f577559d84db22684a6349b25067c3a800df12439783c25494

Name:		darkstat
Summary:	Network traffic analyzer
Version:	3.0.721
Release:	13%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only

URL:		https://unix4lyfe.org/darkstat
Source:		https://github.com/emikulic/darkstat/archive/%{version}/%{name}-%{version}.tar.gz

Source1:	%{name}.service
Source2:	%{name}.sysconfig

Patch1:		getaddrinfo.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	libpcap-devel
BuildRequires:	make
BuildRequires:	systemd-rpm-macros
BuildRequires:	zlib-devel

Requires(post):	systemd
Requires(preun): systemd
Requires(postun): systemd

%description
darkstat is a network traffic analyzer. It's basically a packet sniffer
which runs as a background process on a cable/DSL router and gathers
all sorts of useless but interesting statistics.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Create a sysusers.d config file
cat >darkstat.sysusers.conf <<EOF
u darkstat - 'Network traffic analyzer' /var/lib/darkstat -
EOF

%build
autoreconf -ifv
%configure --disable-silent-rules
%make_build

%install
%make_install
install -Dpm444 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -Dpm644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

install -m0644 -D darkstat.sysusers.conf %{buildroot}%{_sysusersdir}/darkstat.conf

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING.GPL LICENSE
%doc AUTHORS NEWS README.md
%attr(0755, darkstat, root) %{_sbindir}/%{name}
%attr(0644, darkstat, root) %config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_mandir}/man8/%{name}*
%{_unitdir}/%{name}.service
%{_sysusersdir}/darkstat.conf

%changelog
%autochangelog
