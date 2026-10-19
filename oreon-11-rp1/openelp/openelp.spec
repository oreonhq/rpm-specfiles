%global source0_hash e7db49d22fc86449271e3c58ac0cbaf971bf4936d8c27dd268ecd5057643e947
Name:           openelp
Version:        0.9.3
Release:        1%{?dist}
Summary:        Open Source EchoLink Proxy
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/cottsay/%{name}
Source0:        https://github.com/cottsay/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires(post): firewalld-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
# oreon:deps
BuildRequires:  cmake3
BuildRequires:  doxygen
BuildRequires:  firewalld-filesystem
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  systemd
# /oreon:deps
%description
OpenELP is an open source EchoLink proxy for Linux and Windows. It aims to be
efficient and maintain a small footprint, while still implementing all of the
features present in the official EchoLink proxy.

OpenELP also has the ability to bind to multiple network interfaces which are
routed to unique external IP addresses, and therefore is capable of accepting
connections from multiple clients simultaneously.

%package devel
Summary:        Development files for OpenELP
Requires:       %{name}%{?isa} = %{version}-%{release}
%description devel
This package contains headers and other development files for building software
which utilizes OpenELP, and Open Source EchoLink Proxy.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove bundled md5, use OpenSSL instead
rm src/md5.c

# Create a sysusers.d config file
cat >openelp.sysusers.conf <<EOF
u openelp - 'EchoLink Proxy' - -
EOF

%build

%cmake3 \
  -DOPENELP_USE_OPENSSL:BOOL=ON \
  %{nil}
%cmake3_build -- all doc
%install
%cmake3_install
sed -i '/^\[Service\]$/a User=openelp' %{buildroot}%{_unitdir}/%{name}.service
install -d %{buildroot}%{_sysconfdir}/sysconfig
grep ^ExecStart= %{buildroot}%{_unitdir}/%{name}.service | \
  sed 's|.*openelpd *\(.*\) %{_sysconfdir}/ELProxy.conf|\1|' | \
  sed 's|\(.*\)|# Options for openelpd\nOPTIONS="\1"|' > %{buildroot}%{_sysconfdir}/sysconfig/openelpd
sed -i '/^\[Service\]$/a EnvironmentFile=-%{_sysconfdir}/sysconfig/openelpd' %{buildroot}%{_unitdir}/%{name}.service
sed -i 's|\(ExecStart=.*openelpd\).*|\1 \$OPTIONS %{_sysconfdir}/ELProxy.conf|' %{buildroot}%{_unitdir}/%{name}.service
install -m0644 -p -D doc/%{name}.xml %{buildroot}%{_prefix}/lib/firewalld/services/%{name}.xml
install -m0644 -D openelp.sysusers.conf %{buildroot}%{_sysusersdir}/openelp.conf
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest3
%post

%{?ldconfig}
%firewalld_reload
%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%{?ldconfig}
%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n openelp-devel -f %{oreon_filedir}/openelp-devel.list

%changelog

%autochangelog
