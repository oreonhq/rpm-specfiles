%global source0_hash 793af06a5e45f1c53245c227a7af17a19a6cf18f04d366866e7ac62c5a28d292

%global with_selinux 1
%global modulename trafficserver
%global selinuxtype targeted

Name:           trafficserver
Version:        10.1.1
Release:        3%{?dist}
Summary:        Fast, scalable and extensible HTTP/1.1 and HTTP/2 caching proxy server

License:        Apache-2.0
URL:            https://trafficserver.apache.org/
Source0:        http://www.apache.org/dist/%{name}/%{name}-%{version}.tar.bz2
Source1:        http://www.apache.org/dist/%{name}/%{name}-%{version}.tar.bz2.asc
Source2:        https://downloads.apache.org/trafficserver/KEYS
Source3:        %{name}.service
Source4:        %{name}.sysusers
Source5:        %{name}.sysconf
Source6:        %{name}.tmpfilesd
Source7:        %{modulename}.te
Source8:        %{modulename}.if
Source9:        %{modulename}.fc
Source10:       %{name}-10-update.service

# Use Crypto Policies, don't set rpath as per Fedora policy
Patch0:         trafficserver-crypto-policy.patch
Patch1:         fix-rpath.patch
Patch2:         remove-openssl-engine.patch
Patch3:         config-path-fix.patch
Patch4:         convert-ip-to-bind.patch
Patch5:         gcc-16-cstdint.patch

# Upstream does not support 32-bit architectures:
# https://github.com/apache/trafficserver/issues/4432
# riscv64 and s390x are also not a supported architectures and do not build
ExcludeArch:    %{arm} %{ix86} riscv64 s390x

BuildRequires:  gdb
BuildRequires:  expat-devel hwloc-devel pcre2-devel zlib-devel xz-devel brotli-devel
BuildRequires:  libcurl-devel ncurses-devel gnupg python3-devel
BuildRequires:  gcc gcc-c++
BuildRequires:  cmake
BuildRequires:  libcap-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  openssl-devel
# pcre is removed from RHEL 10
%if 0%{?rhel} >= 10
%else
BuildRequires:  pcre-devel
%endif
BuildRequires:  yaml-cpp-devel

Requires:       expat hwloc pcre2 xz ncurses pkgconfig
Requires:       openssl
Requires:       systemd
Requires(postun): systemd
# pcre is removed from RHEL 10
%if 0%{?rhel} >= 10
%else
Requires:  pcre
%endif
# For convert2yaml.py
Requires:       python3 python3-colorama python3-jsonschema python3-pyyaml

%if 0%{?with_selinux}
Requires:       (%{name}-selinux = %{version}-%{release} if selinux-policy-%{selinuxtype})
%endif

# swoc is not separately packaged for Fedora -- literally nothing else uses this
Provides:       bundled(swoc) =  1.5.12

# Exclude our own internal libraries from requires
%global __requires_exclude ^lib(swoc.*|ts.*)\\.so.*$

# Do not check .so files in the application-specific library directory
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so.*$

%description
Traffic Server is a high-performance building block for cloud services.
It's more than just a caching proxy server; it also has support for
plugins to build large scale web applications.  Key features:

Caching - Improve your response time, while reducing server load and
bandwidth needs by caching and reusing frequently-requested web pages,
images, and web service calls.

Proxying - Easily add keep-alive, filter or anonymize content
requests, or add load balancing by adding a proxy layer.

Fast - Scales well on modern SMP hardware, handling 10s of thousands
of requests per second.

Extensible - APIs to write your own plug-ins to do anything from
modifying HTTP headers to handling ESI requests to writing your own
cache algorithm.

Proven - Handling over 400TB a day at Yahoo! both as forward and
reverse proxies, Apache Traffic Server is battle hardened.

%if 0%{?with_selinux}
# SELinux subpackage
%package selinux
Summary:             trafficserver SELinux policy
BuildArch:           noarch
Requires:            selinux-policy-%{selinuxtype}
Requires(post):      selinux-policy-%{selinuxtype}
BuildRequires:       selinux-policy-devel
%{?selinux_requires}

%description selinux
Trafficserver SELinux policy module
%endif

%package devel
Summary: Development files for Apache Traffic Server plugins
Requires: %{name} = %{version}-%{release}
Requires: yaml-cpp-devel%{?_isa}

%description devel
The header files for developing plugins for Apache Traffic Server

Apache Traffic Server plugins can do anything from modifying HTTP headers to
hadling ESI requests to providing a different caching algorithm. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -p0
rm -r lib/yamlcpp

%build

# This is not working properly with cmake for an unclear reason; linking fails
%define _lto_cflags %{nil}
# GCC 16 maybe-uninitialized noise in bundled swoc under -Werror
export CXXFLAGS="%{build_cxxflags} -Wno-error=maybe-uninitialized"

%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}/%{name} \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir}/%{name} \
    -DCMAKE_INSTALL_LIBEXECDIR=%{_libdir}/%{name}/plugins \
    -DCMAKE_INSTALL_RUNSTATEDIR=/run/%{name} \
    -DCMAKE_INSTALL_LOGDIR=/var/log/%{name} \
    -DCMAKE_INSTALL_CACHEDIR=/var/cache/%{name} \
    -DBUILD_EXPERIMENTAL_PLUGINS=ON \
    -DEXTERNAL_YAML_CPP=ON
%cmake_build

%if 0%{?with_selinux}
mkdir selinux
cp -p %{SOURCE7} selinux/
cp -p %{SOURCE8} selinux/
cp -p %{SOURCE9} selinux/

make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
bzip2 -9 %{modulename}.pp
%endif

%install
%cmake_install

%check
%ctest 

%if 0%{?with_selinux}
install -D -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
install -D -p -m 0644 selinux/%{modulename}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{modulename}.if
%endif

# install systemd unit, etc.
install -D -m 0644 -p %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 -p %{SOURCE10} %{buildroot}%{_unitdir}/%{name}-10-update.service
install -D -m 0644 -p %{SOURCE4} %{buildroot}%{_sysusersdir}/%{name}.conf
install -D -m 0644 -p %{SOURCE5} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -D -m 0644 %{SOURCE6} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -d -m 0755 %{buildroot}/run/%{name}/

# Discard the init.d script
rm -f %{buildroot}%{_bindir}/trafficserver

# Remove libtool archives and static libs, testing plugins
find %{buildroot} -type f -name "*.la" -delete
find %{buildroot} -type f -name "*.a" -delete
rm -f %{buildroot}%{_libdir}/%{name}/plugin_*.so
rm -f %{buildroot}/usr/lib/debug%{_libdir}/%{name}/plugin_*.debug

install -D -m 0644 -p %{buildroot}%{_libdir}/%{name}/pkgconfig/ts.pc %{buildroot}%{_libdir}/pkgconfig/ts.pc
rm -rf %{buildroot}%{_libdir}/%{name}/pkgconfig

# ATS 9.x to 10.x records.config converter
install -D -m 0755 -p tools/records/convert2yaml.py %{buildroot}%{_libexecdir}/%{name}/convert2yaml.py

%post
%?ldconfig
%systemd_post %{name}.service
%systemd_post %{name}-10-update.service
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%preun
%systemd_preun %{name}.service
%systemd_preun %{name}-10-update.service

%postun
%?ldconfig
%systemd_postun_with_restart %{name}.service
%systemd_postun_with_restart %{name}-10-update.service

%if 0%{?with_selinux}
# SELinux contexts are saved so that only affected files can be
# relabeled after the policy module installation
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
    %selinux_relabel_post -s %{selinuxtype}
fi
%endif

%files
%license LICENSE
%doc README.md CHANGELOG* NOTICE STATUS

%attr(0750, trafficserver, trafficserver) %dir %{_sysconfdir}/%{name}
%attr(-, trafficserver, trafficserver) %config(noreplace) %{_sysconfdir}/%{name}/body_factory
%attr(-, trafficserver, trafficserver) %config(noreplace) %{_sysconfdir}/%{name}/*.config
%attr(-, trafficserver, trafficserver) %config(noreplace) %{_sysconfdir}/%{name}/*.yaml

%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%{_unitdir}/%{name}.service
%{_unitdir}/%{name}-10-update.service
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf

%{_bindir}/traffic_cache_tool
%{_bindir}/traffic_crashlog
%{_bindir}/traffic_ctl
%{_bindir}/traffic_layout
%{_bindir}/traffic_logcat
%{_bindir}/traffic_logstats
%{_bindir}/traffic_server
%{_bindir}/traffic_top
%{_bindir}/traffic_via

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/lib*.so*
%{_libdir}/%{name}/plugins/*.so

%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/convert2yaml.py

%attr(0750, trafficserver, trafficserver) %dir /var/log/%{name}
%attr(0750, trafficserver, trafficserver) %dir /run/%{name}
%attr(0750, trafficserver, trafficserver) %dir /var/cache/%{name}

%if 0%{?with_selinux}
%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.*
%{_datadir}/selinux/devel/include/distributed/%{modulename}.if
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}
%endif

%files devel
%{_includedir}/ts
%{_includedir}/swoc
%{_includedir}/tsutil
%dir %{_includedir}/tscpp
%{_includedir}/tscpp/api
%{_libdir}/%{name}/cmake
%{_libdir}/pkgconfig/ts.pc

%changelog
%autochangelog
