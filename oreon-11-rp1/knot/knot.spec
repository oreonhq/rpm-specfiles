%global source1_hash 1884c94b09aee97e75db4cc25d9ebaa41df674c20e56abb87d0047a89ca3f4c2
%global source0_hash 922894f04a2835131a24c3b3edcbf761273c1b37d3dc4e46d6923ee3856af130
%global _hardened_build 1
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}}
%define GPG_CHECK 1
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%define PYPROJECT 1
%else
%define PYPROJECT 0
%endif
%define BASE_VERSION %(echo "%{version}" | sed 's/^\\([^.]\\+\\.[^.]\\+\\).*/\\1/')
%define repodir %{_builddir}/%{name}-%{version}
Summary:        High-performance authoritative DNS server
Name:		knot
Version:	3.6.0
Release:        1%{?dist}
License:	GPL-3.0-or-later
URL:		https://www.knot-dns.cz
Source0:        https://secure.nic.cz/files/knot-dns/%{name}-%{version}.tar.xz
%if 0%{?GPG_CHECK}
Source1:	https://secure.nic.cz/files/knot-dns/%{name}-%{version}.tar.xz.asc
Source100:	gpgkey-742FA4E95829B6C5EAC6B85710BB7AF6FEBBD6AB.gpg.asc
%endif
%if 0%{?PYPROJECT}
%else
%endif
%if 0%{?suse_version}
Requires(pre):	pwdutils
%if 0%{?sle_version} != 150400
%endif
%endif
Requires(post):		systemd %{_sbindir}/runuser
Requires(preun):	systemd
Requires(postun):	systemd
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Recommends:	%{name}-keymgr
%if 0%{?suse_version}
Provides:	group(knot)
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-knot = %{version}-%{release}
# /oreon:deps
%description
Knot DNS is a high-performance authoritative DNS server implementation.

%package libs
Summary:	Libraries used by the Knot DNS server and client applications
Conflicts:	knot-resolver < 5.7.6-3
%description libs
The package contains shared libraries used by the Knot DNS server and
utilities.

%package devel
Summary:	Development header files for the Knot DNS libraries
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description devel
The package contains development header files for the Knot DNS libraries
included in knot-libs package.

%package utils
Summary:	DNS client utilities shipped with the Knot DNS server
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Provides:	%{name}-dnsutils = %{version}-%{release}
%description utils
The package contains DNS client utilities shipped with the Knot DNS server.

%package dnssecutils
Summary:	DNSSEC tools shipped with the Knot DNS server
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description dnssecutils
The package contains DNSSEC tools shipped with the Knot DNS server.

%package keymgr
Summary:	Knot DNS key management utility
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description keymgr
The package contains keymgr program for Knot DNS key management.

%package module-dnstap
Summary:	dnstap module for Knot DNS
Requires:	%{name} = %{version}-%{release}
%description module-dnstap
The package contains dnstap Knot DNS module for logging DNS traffic.

%package module-geoip
Summary:	geoip module for Knot DNS
Requires:	%{name} = %{version}-%{release}
%description module-geoip
The package contains geoip Knot DNS module for geography-based responses.

%package exporter
Summary:	Prometheus exporter for Knot DNS
BuildArch:	noarch
Requires:	%{name}-libs = %{version}-%{release}
%description exporter
The package provides Python Prometheus exporter for Knot DNS.

%package -n python3-libknot
Summary:	Python bindings for libknot
BuildArch:	noarch
Requires:	%{name}-libs = %{version}-%{release}
%{?python_provide:%python_provide python3-libknot}
%description -n python3-libknot
The package provides Python bindings for the libknot shared library.

%package -n valkey-module-knot
Summary:	Valkey module for Knot DNS.
Requires:	%{name}-libs = %{version}-%{release}
%description -n valkey-module-knot
The package provides Valkey module for Knot DNS.

%package doc
Summary:	Documentation for the Knot DNS server
BuildArch:	noarch
Provides:	bundled(jquery)
%description doc
The package contains documentation for the Knot DNS server.
On-line version is available on https://www.knot-dns.cz/documentation/

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?GPG_CHECK}
export GNUPGHOME=./gpg-keyring
[ -d ${GNUPGHOME} ] && rm -r ${GNUPGHOME}
mkdir --mode=700 ${GNUPGHOME}
gpg2 --import %{SOURCE100}
gpg2 --verify %{SOURCE1} %{SOURCE0}
%endif
%autosetup -p1

# Create a sysusers.d config file
cat >knot.sysusers.conf <<EOF
u knot - 'Knot DNS server' %{_sharedstatedir}/knot -
EOF

%build

CFLAGS="%{optflags} -DNDEBUG -Wno-unused"
%ifarch armv7hl i686
%define configure_db_sizes --with-conf-mapsize=64
%endif
%configure \
  --sysconfdir=/etc \
  --localstatedir=/var/lib \
  --libexecdir=/usr/lib/knot \
  --with-rundir=/run/knot \
  --with-moduledir=%{_libdir}/knot/modules-%{BASE_VERSION} \
  --with-redisdir=%{_libdir}/valkey/modules \
  --with-storage=/var/lib/knot \
  %{?configure_db_sizes} \
  %{?configure_quic} \
  --enable-redis=auto \
  --disable-static \
  --enable-dnstap=yes \
  --with-module-dnstap=shared \
  --with-module-geoip=shared
make %{?_smp_mflags}
make html
pushd python/libknot
%if %{PYPROJECT}
%pyproject_wheel
%else
%py3_build
%endif
popd
pushd python/knot_exporter
%if %{PYPROJECT}
%pyproject_wheel
%else
%py3_build
%endif
popd
%install
make install DESTDIR=%{buildroot}
pushd python/libknot
%if %{PYPROJECT}
%pyproject_install
%else
%py3_install
%endif
popd
pushd python/knot_exporter
%if %{PYPROJECT}
%pyproject_install
%else
%py3_install
%endif
popd
install -d -m 0755 %{buildroot}%{_pkgdocdir}/samples
install -p -m 0644 -t %{buildroot}%{_pkgdocdir}/samples samples/*.zone*
install -p -m 0644 NEWS README.md %{buildroot}%{_pkgdocdir}
cp -av doc/_build/html %{buildroot}%{_pkgdocdir}
[ -r %{buildroot}%{_pkgdocdir}/html/index.html ] || exit 1
rm -f %{buildroot}%{_pkgdocdir}/html/.buildinfo
rm %{buildroot}%{_sysconfdir}/%{name}/*
install -p -m 0644 -D %{repodir}/samples/%{name}.sample.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -p -m 0644 -D %{repodir}/distro/common/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
%if 0%{?suse_version}
ln -s service %{buildroot}/%{_sbindir}/rcknot
%endif
install -d %{buildroot}%{_sharedstatedir}
install -d -m 0770 -D %{buildroot}%{_sharedstatedir}/knot
find %{buildroot} -type f -name "*.la" -delete -print
install -m0644 -D knot.sysusers.conf %{buildroot}%{_sysusersdir}/knot.conf
%oreon_autofiles python3-libknot usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles valkey-module-knot usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

V=1 make check
%pre

%if 0%{?suse_version}
%service_add_pre knot.service
%endif
%post

%if 0%{?suse_version}
%service_add_post knot.service
%else
%systemd_post knot.service
%endif
%preun

%if 0%{?suse_version}
%service_del_preun knot.service
%else
%systemd_preun knot.service
%endif
%postun

%if 0%{?suse_version}
%service_del_postun knot.service
%else
%systemd_postun_with_restart knot.service
%endif
%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%files -n knot-libs -f %{oreon_filedir}/knot-libs.list
%files -n knot-devel -f %{oreon_filedir}/knot-devel.list
%files -n knot-utils -f %{oreon_filedir}/knot-utils.list
%files -n knot-dnssecutils -f %{oreon_filedir}/knot-dnssecutils.list
%files -n knot-keymgr -f %{oreon_filedir}/knot-keymgr.list
%files -n knot-module-dnstap -f %{oreon_filedir}/knot-module-dnstap.list
%files -n knot-module-geoip -f %{oreon_filedir}/knot-module-geoip.list
%files -n knot-exporter -f %{oreon_filedir}/knot-exporter.list
%files -n python3-libknot -f %{oreon_filedir}/python3-libknot.list
%files -n valkey-module-knot -f %{oreon_filedir}/valkey-module-knot.list
%files -n knot-doc -f %{oreon_filedir}/knot-doc.list

%changelog

%autochangelog
