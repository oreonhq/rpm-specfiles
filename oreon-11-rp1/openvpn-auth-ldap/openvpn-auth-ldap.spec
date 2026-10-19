%global source0_hash 81f600cdc88adb2258f57df1ed2d87f0afa945f66cbf8897ad50e76f42509168
Summary:        OpenVPN plugin for LDAP authentication
Name: openvpn-auth-ldap
Version: 2.0.4
Release:        1%{?dist}
License: LicenseRef-Callaway-BSD
URL: https://github.com/threerings/openvpn-auth-ldap
Source0:        https://github.com/threerings/openvpn-auth-ldap/archive/auth-ldap-%{version}.tar.gz
Patch2: auth-ldap-tools-CFLAGS.patch
Patch4: auth-ldap-remoteAddress.patch
Patch5: https://github.com/threerings/openvpn-auth-ldap/commit/8aed502984426e008710bab2b44249489b549a22.patch#/auth-ldap-epel-gcc-objc.patch
Requires: openvpn >= 2.0
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  check-devel
BuildRequires:  doxygen
BuildRequires:  gcc-objc
BuildRequires:  gnustep-base-devel
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  openvpn-devel
BuildRequires:  re2c
# /oreon:deps
%description
The OpenVPN Auth-LDAP Plugin implements username/password authentication via
LDAP for OpenVPN 2.x.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-auth-ldap-%{version}
%patch -P 2 -p1 -b .tools-CFLAGS
%patch -P 4 -p1 -b .remoteAddress
%patch -P 5 -p1 -b .epel-gcc-objc
# Fix plugin from the instructions in the included README
sed -i 's|^plugin .*| plugin %{_libdir}/openvpn/plugins/openvpn-auth-ldap.so "/etc/openvpn/auth/ldap.conf"|g' README.md
autoconf
autoheader

%build

%configure CFLAGS="%{optflags} -fPIC -std=gnu99" \
    --libdir=%{_libdir}/openvpn/plugins \
    --with-openvpn=%{_includedir}
%make_build \
%install
mkdir -p %{buildroot}%{_libdir}/openvpn/plugins
%make_install
install -D -p -m 0600 auth-ldap.conf \
    %{buildroot}%{_sysconfdir}/openvpn/auth/ldap.conf
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
