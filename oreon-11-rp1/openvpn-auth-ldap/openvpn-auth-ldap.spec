%global source0_hash 81f600cdc88adb2258f57df1ed2d87f0afa945f66cbf8897ad50e76f42509168

Summary: OpenVPN plugin for LDAP authentication
Name: openvpn-auth-ldap
Version: 2.0.4
Release: 21%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: https://github.com/threerings/openvpn-auth-ldap
Source0: https://github.com/threerings/openvpn-auth-ldap/archive/auth-ldap-%{version}.tar.gz
# tools are not compiled with given CFLAGS
Patch2: auth-ldap-tools-CFLAGS.patch
# Patch from upstream issue n°4, to fix tap bridging.
Patch4: auth-ldap-remoteAddress.patch
# Use GCC with Objective C support from EPEL on CentOS/RHEL 8+
Patch5: https://github.com/threerings/openvpn-auth-ldap/commit/8aed502984426e008710bab2b44249489b549a22.patch#/auth-ldap-epel-gcc-objc.patch
# This is a plugin not linked against a lib, so hardcode the requirement
# since we require the parent configuration and plugin directories
Requires: openvpn >= 2.0
BuildRequires: make
Buildrequires: doxygen
BuildRequires: gcc-objc
BuildRequires: check-devel
BuildRequires: gnustep-base-devel
Buildrequires: openldap-devel
Buildrequires: openssl-devel
Buildrequires: openvpn-devel
BuildRequires: re2c
BuildRequires: autoconf

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
# Upstream's test for needing -std=gnu99 does not work in recent Fedora
# https://github.com/threerings/openvpn-auth-ldap/issues/78
# Missing -fPIC for some objects
%configure CFLAGS="%{optflags} -fPIC -std=gnu99" \
    --libdir=%{_libdir}/openvpn/plugins \
    --with-openvpn=%{_includedir}

# CentOS Stream 9 %%configure hardcodes 'export CC=gcc' for some reason
%make_build \
%if 0%{?rhel} >= 8
    CC=gobjc
%endif

%install
# Main plugin
mkdir -p %{buildroot}%{_libdir}/openvpn/plugins
%make_install
# Example config file
install -D -p -m 0600 auth-ldap.conf \
    %{buildroot}%{_sysconfdir}/openvpn/auth/ldap.conf

%files
%license LICENSE
%doc README.md auth-ldap.conf
%dir %{_sysconfdir}/openvpn/auth/
%config(noreplace) %{_sysconfdir}/openvpn/auth/ldap.conf
%{_libdir}/openvpn/plugins/openvpn-auth-ldap.so

%changelog
%autochangelog
