%global source0_hash 634a67b2f7ac3b386a79160eb44413d618e33e4e7fc74ae68b0240484af149dd

#
# $Id: sblim-sfcb.spec,v 1.5 2010/06/23 10:31:02 vcrhonek Exp $
#
# Package spec for sblim-sfcb
#

Name: sblim-sfcb
Summary: Small Footprint CIM Broker
URL: http://sblim.wiki.sourceforge.net/
Version: 1.4.9
Release: 39%{?dist}
License: EPL-1.0
Source0:        http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
Source1: sfcb.service
# Missing man pages
Source2: sfcbdump.1.gz
Source3: sfcbinst2mof.1.gz
Source4: sfcbtrace.1.gz
# /etc/tmpfiles.d configuration file
Source5: sblim-sfcb.tmpfiles
# Patch0: changes schema location to the path we use
Patch0: sblim-sfcb-1.3.9-sfcbrepos-schema-location.patch
# Patch1: Fix provider debugging - variable for stopping wait-for-debugger
# loop must be volatile
Patch1: sblim-sfcb-1.3.15-fix-provider-debugging.patch
# Patch2: increase default value of maxMsgLen in sfcb.cfg
Patch2: sblim-sfcb-1.3.16-maxMsgLen.patch
# Patch3: we'll install own service file
Patch3: sblim-sfcb-1.4.5-service.patch
# Patch4: fixes multilib issue with man page and config file
Patch4: sblim-sfcb-1.3.16-multilib-man-cfg.patch
# Patch5: change default ecdh curve name, as the original is not enabled
#   in openssl on Fedora, rhbz#1097794
Patch5: sblim-sfcb-1.4.8-default-ecdh-curve-name.patch
Patch6: sblim-sfcb-1.4.9-fix-ftbfs.patch
# Patch7: fix possible null pointer dereference (CVE-2015-5185), rhbz#1255802
Patch7: sblim-sfcb-1.4.9-fix-null-deref.patch
# Patch8: fix null pointer (DoS) vulnerability via POST request to /cimom
#   (CVE-2018-6644), patch by Adam Majer, rhbz#1543826
Patch8: sblim-sfcb-1.4.9-fix-null-content-type-crash.patch
# Patch9: removes decrease of optimization level to -O0 on ppc64le
Patch9: sblim-sfcb-1.4.9-fix-ppc-optimization-level.patch
# Patch10: fixes docdir name and removes install of COPYING with license
#   which is included through %%license
Patch10: sblim-sfcb-1.4.9-docdir-license.patch
# Patch11: adds configuration options to specify fallback SSL cert/key pair
#   and disables default ECDH ephemeral key generation
Patch11: sblim-sfcb-1.4.9-post-quantum.patch
Provides: cim-server = 0
Requires: cim-schema
Requires: sblim-sfcCommon
BuildRequires: make
BuildRequires: libcurl-devel
BuildRequires: perl-generators
BuildRequires: zlib-devel
BuildRequires: openssl-devel
BuildRequires: pam-devel
BuildRequires: cim-schema
BuildRequires: bison flex
BuildRequires: sblim-cmpi-devel
BuildRequires: systemd
BuildRequires: sblim-sfcCommon-devel
BuildRequires: openslp-devel
BuildRequires: gcc
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%Description
Small Footprint CIM Broker (sfcb) is a CIM server conforming to the
CIM Operations over HTTP protocol.
It is robust, with low resource consumption and therefore specifically 
suited for embedded and resource constrained environments.
sfcb supports providers written against the Common Manageability
Programming Interface (CMPI).

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -T -b 0 -n %{name}-%{version}
%patch -P0 -p1 -b .sfcbrepos-schema-location
%patch -P1 -p1 -b .fix-provider-debugging
%patch -P2 -p1 -b .maxMsgLen
%patch -P3 -p1 -b .service
%patch -P4 -p1 -b .multilib-man-cfg
%patch -P5 -p1 -b .default-ecdh-curve-name
%patch -P6 -p1 -b .fix-ftbfs
%patch -P7 -p1 -b .fix-null-deref
%patch -P8 -p1 -b .fix-null-content-type-crash
%patch -P9 -p1 -b .fix-ppc-optimization-level
%patch -P10 -p1 -b .docdir-license
%patch -P11 -p1 -b .post-quantum

# Create a sysusers.d config file
cat >sblim-sfcb.sysusers.conf <<EOF
g sfcb -
m root sfcb
EOF

%build
%configure --enable-debug --enable-uds --enable-ssl --enable-pam --enable-ipv6 \
    --enable-slp --enable-large_volume_support --enable-optimized-enumeration --enable-relax-mofsyntax \
    CFLAGS="$CFLAGS -D_GNU_SOURCE -fPIE -DPIE -fcommon" LDFLAGS="$LDFLAGS -Wl,-z,now -pie"
 
make 

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm $RPM_BUILD_ROOT/%{_sysconfdir}/init.d/sfcb
mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
install -p -m644 %{SOURCE1} $RPM_BUILD_ROOT/%{_unitdir}/sblim-sfcb.service
# install man pages
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1/
cp %{SOURCE2} %{SOURCE3} %{SOURCE4} $RPM_BUILD_ROOT/%{_mandir}/man1/
# remove unused static libraries and so files
rm -f $RPM_BUILD_ROOT/%{_libdir}/sfcb/*.la

echo "%%license COPYING" > _pkg_list
find $RPM_BUILD_ROOT/%{_datadir}/sfcb -type f | grep -v $RPM_BUILD_ROOT/%{_datadir}/sfcb/CIM >> _pkg_list
sed -i s?$RPM_BUILD_ROOT??g _pkg_list > _pkg_list_2
echo "%config(noreplace) %{_sysconfdir}/sfcb/*" >> _pkg_list
echo "%config(noreplace) %{_sysconfdir}/pam.d/*" >> _pkg_list
echo "%doc %{_datadir}/doc/sblim-sfcb/[!COPYING]*" >> _pkg_list
echo "%{_datadir}/man/man1/*" >> _pkg_list
echo "%{_unitdir}/sblim-sfcb.service" >> _pkg_list
echo "%{_localstatedir}/lib/sfcb" >> _pkg_list
echo "%{_bindir}/*" >> _pkg_list
echo "%{_libdir}/sfcb/*.so.*" >> _pkg_list
echo "%{_libdir}/sfcb/*.so" >> _pkg_list

cat _pkg_list

install -m0644 -D sblim-sfcb.sysusers.conf %{buildroot}%{_sysusersdir}/sblim-sfcb.conf
mkdir -p %{buildroot}/%{_tmpfilesdir}
install -p -D -m 644 %{SOURCE5} %{buildroot}/%{_tmpfilesdir}/sblim-sfcb.conf

%post 
%{_datadir}/sfcb/genSslCert.sh %{_sysconfdir}/sfcb &>/dev/null || :
/sbin/ldconfig
%{_bindir}/sfcbrepos -f > /dev/null 2>&1
%systemd_post sblim-sfcb.service
# copy content of /var/lib/sfcb to temporary place for Image Mode
(mkdir -p /usr/share/factory/var/lib && cp -a /var/lib/sfcb /usr/share/factory/var/lib/sfcb) >/dev/null 2>&1 || :

%preun
%systemd_preun sblim-sfcb.service
if [ $1 -eq 0 ]; then
   # Package removal, not upgrade
   rm -rf /usr/share/factory/var/lib/sfcb
fi

%postun
/sbin/ldconfig
%systemd_postun_with_restart sblim-sfcb.service

%files -f _pkg_list
%{_sysusersdir}/sblim-sfcb.conf
%{_tmpfilesdir}/sblim-sfcb.conf

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.9-39
- Import
