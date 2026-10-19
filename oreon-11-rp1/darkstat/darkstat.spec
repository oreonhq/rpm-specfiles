%global source0_hash 5c8e66d4c478b6d7e58f4c842823a09125509bf6851017ff70e32b32ce95b01b
Name:		darkstat
Summary:        Network traffic analyzer
Version:	3.0.722
Release:        1%{?dist}
License:	GPL-2.0-only
URL:		https://unix4lyfe.org/darkstat
Source0:        https://github.com/emikulic/darkstat/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.service
Source2:	%{name}.sysconfig
Patch1:		getaddrinfo.patch
Requires(post):	systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
