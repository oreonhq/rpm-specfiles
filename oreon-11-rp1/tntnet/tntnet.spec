%global source0_hash 718e5519b0a403f7f766358bf66a85c008119c48189d1c2b7651fd0af9018e27

Name:             tntnet
Version:          3.0
Release:          15%{?dist}
Summary:          A web application server for web applications
Epoch:            1

# GPLv2+: framework/common/gcryptinit.c
# zlib:   framework/common/unzip.h
# Automatically converted from old format: LGPLv2+ and GPLv2+ and zlib - review is highly recommended.
License:          LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later AND Zlib
URL:              http://www.tntnet.org/
Source0:          http://www.tntnet.org/download/%{name}-%{version}.tar.gz
# http://sourceforge.net/tracker/?func=detail&aid=3542704&group_id=119301&atid=684050
Source1:          %{name}.service
Patch0:           %{name}-%{version}-missing-call-to-setgroups-before-setuid.patch

BuildRequires:    gcc
BuildRequires:    gcc-c++
BuildRequires:    kernel-headers
BuildRequires:    openssl-devel
BuildRequires:    cxxtools-devel >= 3.0
BuildRequires:    perl-generators
BuildRequires:    zip
BuildRequires:    zlib-devel
BuildRequires:    systemd-units
Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units

%description
%{summary}

%package          devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:         cxxtools-devel%{?_isa} >= 3.0

%description devel
Development files for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

# Create a sysusers.d config file
cat >tntnet.sysusers.conf <<EOF
u tntnet - 'User' %{_localstatedir}/lib/%{name} -
EOF

%build
%configure --disable-static
%make_build

%install
%make_install DESTDIR=%{buildroot} INSTALL="install -p"

# Systemd unit files
# copy tntnet.service to unitdir /lib/systemd/system
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_datadir}/doc/
install -Dpm 644 %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}.service

# Find and remove all la files
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

install -m0644 -D tntnet.sysusers.conf %{buildroot}%{_sysusersdir}/tntnet.conf

%check
test/tntnet-test

%post
/sbin/ldconfig
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service
/sbin/ldconfig

%files
%doc AUTHORS ChangeLog README
%license COPYING
%dir %{_sysconfdir}/tntnet
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.xml
%{_unitdir}/%{name}.service
%{_bindir}/ecppc
%{_bindir}/tntnet
%{_libdir}/libtntnet*.so.*
%{_libdir}/tntnet/
%{_datadir}/tntnet/
%exclude %{_datadir}/%{name}/template/
%{_mandir}/man1/ecppc.1.gz
%{_mandir}/man1/tntnet-defcomp.1.gz
%{_mandir}/man7/ecpp.7.gz
%{_mandir}/man7/tntnet.xml.7.gz
%{_mandir}/man8/tntnet.8.gz
%{_sysusersdir}/tntnet.conf

%files devel
%{_bindir}/tntnet-project
%{_libdir}/libtntnet*.so
%{_includedir}/tnt/
%{_libdir}/pkgconfig/tntnet.pc
%{_libdir}/pkgconfig/tntnet_sdk.pc
%{_datadir}/%{name}/template/

%changelog
%autochangelog
