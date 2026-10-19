%global source0_hash 924337a2a8e5be043ebaea2a78365c7427ac6e9cee24610a0780808b2ba7579b
Summary:        Open implementation of Service Location Protocol V2
Name:    openslp
Version: 2.0.0
Release:        41%{?dist}
License: BSD-3-Clause
URL:     http://sourceforge.net/projects/openslp/
Source0:        http://downloads.sf.net/openslp/openslp-%{version}.tar.gz
Source2: slpd.8.gz
Source3: slptool.1.gz
Source4: slpd.service
Patch1:  openslp-2.0.0-multicast-set.patch
Patch2:  openslp-2.0.0-notify-systemd-of-start-up.patch
Patch3:  openslp-2.0.0-null-pointer-deref.patch
Patch4:  openslp-2.0.0-openssl-1.1-fix.patch
Patch5:  openslp-2.0.0-cve-2016-7567.patch
Patch6:  openslp-2.0.0-cve-2017-17833.patch
Patch7:  openslp-2.0.0-cve-2019-5544.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-units
# /oreon:deps
%description
Service Location Protocol is an IETF standards track protocol that
provides a framework to allow networking applications to discover the
existence, location, and configuration of networked services in
enterprise networks.

OpenSLP is an open source implementation of the SLPv2 protocol as defined
by RFC 2608 and RFC 2614.

%package devel
Summary: OpenSLP headers and libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
OpenSLP header files and libraries.

%package server
Summary: OpenSLP server daemon
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: iproute
%description server
OpenSLP server daemon to dynamically register services.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%patch -P1 -p1 -b .multicast-set
%patch -P2 -p2 -b .systemd
%patch -P3 -p1 -b .null-pointer-deref
%patch -P4 -p1 -b .openssl-1.1-fix
%patch -P5 -p1 -b .cve-2016-7567
%patch -P6 -p1 -b .cve-2017-17833
%patch -P7 -p1 -b .cve-2019-5544

# tarball goof (?), it wants to re-automake anyway, so let's do it right.
#libtoolize --force
#aclocal
#autoconf
#automake --add-missing
autoreconf -f -i

# remove CVS leftovers...
find . -name "CVS" | xargs rm -rf

%build

export CFLAGS="-fPIC -fno-strict-aliasing -fPIE -DPIE $RPM_OPT_FLAGS"
export LDFLAGS="-pie -Wl,-z,now"
%configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --sysconfdir=%{_sysconfdir} \
  --localstatedir=/var \
  --disable-dependency-tracking \
  --disable-static \
  --disable-rpath \
  --enable-async-api
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/%{_sysconfdir}/slp.reg.d
mkdir -p ${RPM_BUILD_ROOT}/usr/lib/%{name}-server
install -m 0755 etc/slpd.all_init ${RPM_BUILD_ROOT}/%{_prefix}/lib/%{name}-server/slp-multicast-set.sh
mkdir -p ${RPM_BUILD_ROOT}/%{_unitdir}
install -p -m 644 %{SOURCE4} ${RPM_BUILD_ROOT}/%{_unitdir}/slpd.service
mkdir -p ${RPM_BUILD_ROOT}/%{_mandir}/man8/
mkdir -p ${RPM_BUILD_ROOT}/%{_mandir}/man1/
cp %SOURCE2 ${RPM_BUILD_ROOT}/%{_mandir}/man8/
cp %SOURCE3 ${RPM_BUILD_ROOT}/%{_mandir}/man1/
rm -rf $RPM_BUILD_ROOT/usr/doc
rm -f  $RPM_BUILD_ROOT%{_libdir}/lib*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post server

%systemd_post slpd.service
%preun server

%systemd_preun slpd.service
%postun server

%systemd_postun_with_restart slpd.service
%files -f %{oreon_filedir}/main.list
%files -n openslp-devel -f %{oreon_filedir}/openslp-devel.list
%files -n openslp-server -f %{oreon_filedir}/openslp-server.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.0-41
- Prepare for Oreon 11 (RP1)
