%global source2_hash 39c242a0732faac536ab50cb561f5f01d8f7058767b5ff83c933520174ac8195
%global source1_hash dd42306fbf07446678677fce2d06f83a78b76342297329922c0d7d6513ee73cd
%global source0_hash bef171a7d064794e05ec7559e46d3e07c3ae6487a4647987fcc4f1cc5a82cec6
%global with_selinux 1
%global modulename trafficserver
%global selinuxtype targeted
Name:           trafficserver
Version:        10.2.0
Release:        1%{?dist}
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
Patch0:         trafficserver-crypto-policy.patch
Patch1:         fix-rpath.patch
Patch2:         remove-openssl-engine.patch
Patch3:         config-path-fix.patch
Patch4:         convert-ip-to-bind.patch
Patch5:         gcc-16-cstdint.patch
ExcludeArch:    %{arm} %{ix86} riscv64 s390x
Requires:       expat hwloc pcre2 xz ncurses pkgconfig
Requires:       openssl
Requires:       systemd
Requires(postun): systemd
Requires:  pcre
Requires:       python3 python3-colorama python3-jsonschema python3-pyyaml
%if 0%{?with_selinux}
Requires:       (%{name}-selinux = %{version}-%{release} if selinux-policy-%{selinuxtype})
%endif
Provides:       bundled(swoc) =  1.5.12
%global __requires_exclude ^lib(swoc.*|ts.*)\\.so.*$
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so.*$
# oreon:deps
BuildRequires:  brotli-devel
BuildRequires:  cmake
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  gnupg
BuildRequires:  hwloc-devel
BuildRequires:  libcap-devel
BuildRequires:  libcurl-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig(systemd)
BuildRequires:  python3-devel
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  zlib-devel
# /oreon:deps
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

%define _lto_cflags %{nil}
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest 
%if 0%{?with_selinux}
install -D -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
install -D -p -m 0644 selinux/%{modulename}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{modulename}.if
%endif
install -D -m 0644 -p %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 -p %{SOURCE10} %{buildroot}%{_unitdir}/%{name}-10-update.service
install -D -m 0644 -p %{SOURCE4} %{buildroot}%{_sysusersdir}/%{name}.conf
install -D -m 0644 -p %{SOURCE5} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -D -m 0644 %{SOURCE6} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -d -m 0755 %{buildroot}/run/%{name}/
rm -f %{buildroot}%{_bindir}/trafficserver
find %{buildroot} -type f -name "*.la" -delete
find %{buildroot} -type f -name "*.a" -delete
rm -f %{buildroot}%{_libdir}/%{name}/plugin_*.so
rm -f %{buildroot}/usr/lib/debug%{_libdir}/%{name}/plugin_*.debug
install -D -m 0644 -p %{buildroot}%{_libdir}/%{name}/pkgconfig/ts.pc %{buildroot}%{_libdir}/pkgconfig/ts.pc
rm -rf %{buildroot}%{_libdir}/%{name}/pkgconfig
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
%files -f %{oreon_filedir}/main.list
%files -n trafficserver-selinux -f %{oreon_filedir}/trafficserver-selinux.list
%files -n trafficserver-devel -f %{oreon_filedir}/trafficserver-devel.list

%changelog

%autochangelog
