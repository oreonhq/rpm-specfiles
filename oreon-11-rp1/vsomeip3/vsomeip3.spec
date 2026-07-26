%global source0_hash 1a6873111c326711eb7c9faec8935ff0110de9d4a4bf3d43990da2135ba0528e

%global _lto_cflags %{nil}

Name:    vsomeip3
Version: 3.5.11
Release: 8%{?dist}
Summary: COVESA implementation of SOME/IP protocol
# remove from i686 as not needed.
ExcludeArch: %{ix86}

License: MPL-2.0
URL:     https://github.com/COVESA/vsomeip
Source0: %{URL}/archive/%{VERSION}/vsomeip-%{VERSION}.tar.gz
Source1: routingmanagerd.service
Source3: tmpfiles-vsomeip.conf
Source4: etc-vsomeip.json
Source5: vsomeip.fc
Source6: vsomeip.if
Source7: vsomeip.te
Source8: vsomeip3.sysusers.conf

# Build/Install tools and examples
Patch1: 01-vsomeip-build-extra.patch
# Do various conversions of /usr/lib -> /usr/lib64
Patch2: 02-vsomeip-fix-cmake_libdir.patch
# boost::asio::io_context::strand::wrap is deprecated
Patch3: 03-vsomeip3-boost-asio-deprecation.patch
# GCC 16 -Warray-bounds false positive
Patch4: 04-vsomeip3-gcc16-warning.patch

BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: dlt-libs-devel
BuildRequires: systemd-devel
BuildRequires: gcc-c++
BuildRequires: google-benchmark-devel

# Fedora has extra tools for secondary items
%if 0%{?fedora}
BuildRequires: doxygen
BuildRequires: gtest-devel
BuildRequires: asciidoc
%endif

%description

The vsomeip stack implements the http://some-ip.com/ (Scalable
service-Oriented MiddlewarE over IP (SOME/IP)) protocol. The stack
consists out of:
* a shared library for SOME/IP (libvsomeip3.so)
* a second shared library for SOME/IP's service discovery
  (libvsomeip3-sd.so) which is loaded during runtime if the service
  discovery is enabled.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package selinux
Summary:        SELinux policy module for %{name}
BuildArch:      noarch

BuildRequires:  selinux-policy-devel
BuildRequires:  make
BuildRequires:  checkpolicy
%if "%{_selinux_policy_version}" != ""
Requires:	selinux-policy >= %{_selinux_policy_version}
%endif

Requires(post):	policycoreutils
%if "%{_selinux_policy_version}" != ""
Requires(post): selinux-policy-base >= %_selinux_policy_version
Requires(post): selinux-policy-any >= %_selinux_policy_version
%endif

%description selinux
This package contains the SELinux policy module for %{name}.

## routing manager
%package routingmanager
Summary: Routingmanager daemon %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: systemd
Requires: dlt-daemon
Recommends: vsomeip3-selinux

%description routingmanager
%{summary}. Also requires dlt-daemon running.

%package examples
Summary: Examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.

%package tools
Summary: Tools for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
%{summary}.

%package compat
Summary: Compat libraries for vsomeip2
Requires: %{name}%{?_isa} = %{version}-%{release}
%description compat
%{summary}.

%package compat-devel
Summary: Development files for %{name}-compat
Requires: %{name}-compat%{?_isa} = %{version}-%{release}
%description compat-devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n vsomeip-%{version} -p1
mkdir vsomeip-selinux
cp %{SOURCE5} %{SOURCE6} %{SOURCE7} vsomeip-selinux/

# For some reasons, some source files are executable, which messes
# with debuginfo
find -name "*.[ch]pp" | xargs chmod a-x

%ldconfig_scriptlets

%ldconfig_scriptlets compat

%build
%cmake \
    -DENABLE_SIGNAL_HANDLING=OFF  \
    -DENABLE_CONFIGURATION_OVERLAYS=ON \
    -DENABLE_COMPAT=ON \
    -DVSOMEIP_INSTALL_ROUTINGMANAGERD=ON \
    -DBASE_PATH=/run/vsomeip \
    -Wno-dev
#    -Wno-dev \
#    --trace-expand --log-level=TRACE
%cmake_build --target all --target vsomeip_ctrl --target examples --target hello_world_client --target hello_world_service

(cd vsomeip-selinux &&
  make -f  /usr/share/selinux/devel/Makefile vsomeip.pp &&
  bzip2 -9 vsomeip.pp
  )

%install
%cmake_install
# Install samples
DESTDIR="%{buildroot}" %__cmake --install "%{__cmake_builddir}/tools/vsomeip_ctrl"
DESTDIR="%{buildroot}" %__cmake --install "%{__cmake_builddir}/examples"
DESTDIR="%{buildroot}" %__cmake --install "%{__cmake_builddir}/examples/hello_world"

mkdir -p %{buildroot}%{_datadir}/vsomeip
# Move sample config
mv %{buildroot}%{_prefix}%{_sysconfdir}/vsomeip %{buildroot}%{_datadir}/vsomeip/examples

for b in %{buildroot}%{_bindir}/*-sample %{buildroot}%{_bindir}/*hello_world*; do \
    mv $b $(dirname $b)/vsomeip-$(basename $b); \
done

# Home directory for the 'routingmanagerd' user
mkdir -p $RPM_BUILD_ROOT/var/lib/routingmanagerd

mkdir -p %{buildroot}%{_unitdir}
install %{SOURCE1} %{buildroot}%{_unitdir}/ # service

mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}.conf

mkdir -p %{buildroot}%{_sysconfdir}
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/vsomeip.json

mkdir -p %{buildroot}%{_datadir}/selinux/packages/ %{buildroot}%{_datadir}/selinux/devel/include/contrib/
install -m 0644 vsomeip-selinux/vsomeip.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/
install -m 0644 vsomeip-selinux/vsomeip.if %{buildroot}%{_datadir}/selinux/devel/include/contrib/

install -m0644 -D %{SOURCE8} %{buildroot}%{_sysusersdir}/vsomeip3.conf

%post selinux
. %{_sysconfdir}/selinux/config
%selinux_modules_install -s ${SELINUXTYPE} %{_datadir}/selinux/packages/vsomeip.pp.bz2
restorecon -R %{_bindir}/routingmanagerd &> /dev/null || :
restorecon -R %{_rundir}/vsomeip/ &> /dev/null || :
restorecon -R %{_localstatedir}/%{_rundir}/vsomeip/ &> /dev/null || :
restorecon -R /var/lib/routingmanagerd/ &> /dev/null || :

%postun selinux
if [ $1 -eq 0 ]; then
   . %{_sysconfdir}/selinux/config
   %selinux_modules_uninstall -s ${SELINUXTYPE} vsomeip
   restorecon -R %{_bindir}/routingmanagerd &> /dev/null || :
   restorecon -R %{_rundir}/vsomeip/ &> /dev/null || :
   restorecon -R %{_localstatedir}/%{_rundir}/vsomeip/ &> /dev/null || :
   restorecon -R /var/lib/routingmanagerd/ &> /dev/null || :
fi

%pre routingmanager
%sysusers_create_compat vsomeip3.conf

%post routingmanager
%systemd_post routingmanagerd.service

%preun routingmanager
%systemd_preun routingmanagerd.service

%postun routingmanager
%systemd_postun_with_restart routingmanagerd.service

%files
%doc AUTHORS CHANGES README.md
%license LICENSE
%{_libdir}/libvsomeip3.so.*
%{_libdir}/libvsomeip3-*.so.*
%{_tmpfilesdir}/%{name}.conf
%{_sysconfdir}/vsomeip.json

%files selinux
%{_datadir}/selinux/packages/vsomeip.pp.bz2
%{_datadir}/selinux/devel/include/contrib/vsomeip.if

%files compat
%doc AUTHORS CHANGES README.md
%license LICENSE
%{_libdir}/libvsomeip.so.*

%files routingmanager
%doc AUTHORS CHANGES README.md
%license LICENSE
%{_sysusersdir}/vsomeip3.conf
%attr(755,routingmanagerd,routingmanagerd) %dir /var/lib/routingmanagerd
%{_bindir}/routingmanagerd
%{_unitdir}/routingmanagerd.service

%files tools
%doc AUTHORS CHANGES README.md
%license LICENSE
%{_bindir}/vsomeip_ctrl

%files examples
%doc AUTHORS CHANGES README.md
%license LICENSE
%{_bindir}/vsomeip-*-sample
%{_bindir}/vsomeip-hello_world*
# Example configurations:
%{_datadir}/vsomeip

%files compat-devel
%doc AUTHORS CHANGES README.md
%license LICENSE
%{_includedir}/compat
%{_libdir}/libvsomeip.so
%{_libdir}/cmake/vsomeip
%{_libdir}/pkgconfig/vsomeip.pc

%files devel
%doc AUTHORS CHANGES README.md
%license LICENSE
%{_includedir}/vsomeip
%{_libdir}/libvsomeip3.so
%{_libdir}/libvsomeip3-*.so
%{_libdir}/cmake/vsomeip3
%{_libdir}/pkgconfig/vsomeip3.pc

%changelog
%autochangelog
