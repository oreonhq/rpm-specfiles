%global source0_hash faf38add90ccfed34917506894a4dfe6faab58abdf5ca44a4d48e2040cebcd36
%global source4_hash 91a63540d0c5eeed36f91752a109b021a8318f648f04d4b40c2c572bad60919b
%global sblim_testsuite_version 1.2.4
%global provider_dir %{_libdir}/cmpi
%global with_test_subpackage 1
Name:           sblim-gather
Version:        2.2.9
Release:        42%{?dist}
Summary:        SBLIM Gatherer
License:        EPL-1.0
URL:            http://sourceforge.net/projects/sblim/
Source0:        https://downloads.sourceforge.net/project/sblim/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source1:        gather-config.h.prepend
Source2:        gather-config.h
Source3:        sblim-gather.tmpfiles
Source4:        missing-providers.tgz
Source5:        gatherer.service
Source6:        reposd.service
Patch1:         sblim-gather-2.2.7-missing_providers.patch
Patch2:         sblim-gather-2.2.7-typos.patch
Patch8:         sblim-gather-2.2.9-remove-cxx-check.patch
Patch15:        sblim-gather-2.2.9-cmake-minimum.patch
Patch3:         sblim-gather-2.2.8-docdir.patch
Patch4:         sblim-gather-2.2.8-multilib.patch
Patch5:         sblim-gather-2.2.9-pegasus-interop.patch
Patch6:         sblim-gather-2.2.9-prov-reg-sfcb-systemd.patch
Patch7:         sblim-gather-2.2.9-remove-assoc-conflict.patch
Patch9:         sblim-gather-2.2.9-inline.patch
Patch10:        sblim-gather-2.2.9-fix-multiple-definition.patch
Patch11:        sblim-gather-2.2.9-covscan-fixes.patch
Patch12:        sblim-gather-2.2.9-fix-use-of-temp-paths.patch
Patch13:        sblim-gather-2.2.9-gcc15-fix.patch
Patch14:        sblim-gather-2.2.9-suppress-repeated-value-msg.patch
Requires:       cim-server
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libsysfs-devel
BuildRequires:  libvirt-devel
BuildRequires:  make
BuildRequires:  sblim-cmpi-base-devel
BuildRequires:  sblim-cmpi-devel
BuildRequires:  systemd-units
BuildRequires:  xmlto
# /oreon:deps
%description
Standards Based Linux Instrumentation for Manageability
Performance Data Gatherer Base.
This package contains the agents and control programs for gathering
and providing performance data.

%package        provider
Summary:        SBLIM Gatherer Provider
Requires:       %{name} = %{version}-%{release}
Requires:       sblim-cmpi-base
Requires:       cim-server
%description    provider
The CIM (Common Information Model) Providers for the
SBLIM (Standards Based Linux Instrumentation for Manageability)
Gatherer.

%package        devel
Summary:        SBLIM Gatherer Development Support
Requires:       %{name} = %{version}-%{release}
Requires:       cim-server
%description    devel
This package is needed to develop new plugins for the
SBLIM (Standards Based Linux Instrumentation for Manageability)
Gatherer.

%if 0%{?with_test_subpackage}
%package        test
Summary:        SBLIM Gatherer Testcase Files
Requires:       %{name}-provider = %{version}-%{release}
Requires:       sblim-testsuite
Requires:       cim-server
%description    test
Gatherer Testcase Files for the
SBLIM (Standards Based Linux Instrumentation for Manageability)
Testsuite
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source4_hash}" = "none" || { f="%{SOURCE4}"; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source4_hash}" || { echo "oreon: Source4 hash mismatch" >&2; exit 1; }; }
%setup -q
# for missing providers
tar xfvz %{SOURCE4}
%autopatch -p1

%build

%ifarch s390 s390x ppc ppc64
export CFLAGS="$RPM_OPT_FLAGS -fsigned-char -fno-strict-aliasing"
%else
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%endif
%configure \
%if 0%{?with_test_subpackage}
        TESTSUITEDIR=%{_datadir}/sblim-testsuite \
%endif
%ifarch s390 s390x
        --enable-z \
%endif
        PROVIDERDIR=%{provider_dir}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
%global _cmake_generator "Unix Makefiles"
pushd missing-providers
  %{cmake}
  pushd redhat-linux-build
    make %{?_smp_mflags}
  popd
popd
%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/*a
rm -f $RPM_BUILD_ROOT/%{provider_dir}/*a
rm -f $RPM_BUILD_ROOT/%{_libdir}/gather/*plug/*a
cat %{SOURCE1} \
        $RPM_BUILD_ROOT/%{_includedir}/gather/gather-config.h > \
        $RPM_BUILD_ROOT/%{_includedir}/gather/gather-config-%{_arch}.h
chmod 644 $RPM_BUILD_ROOT/%{_includedir}/gather/gather-config.h
install -m644 %{SOURCE2} $RPM_BUILD_ROOT/%{_includedir}/gather/
mkdir -p $RPM_BUILD_ROOT/%{_tmpfilesdir}
install -p -D -m 644 %{SOURCE3} $RPM_BUILD_ROOT/%{_tmpfilesdir}/sblim-gather.conf
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/cmpi" > $RPM_BUILD_ROOT/%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
make install/fast DESTDIR=$RPM_BUILD_ROOT -C missing-providers/redhat-linux-build
mkdir -p $RPM_BUILD_ROOT/var/lib/gather
rm $RPM_BUILD_ROOT/%{_sysconfdir}/init.d/gatherer
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_unitdir}/gatherer.service
install -p -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_unitdir}/reposd.service
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

install -d -m 0755 -o root -g root /var/run/gather
%{?ldconfig}
%systemd_post gatherer.service
%systemd_post reposd.service
%preun

%systemd_preun gatherer.service
%systemd_preun reposd.service
if [ $1 -eq 0 ]; then
  rm -rf /var/run/gather
  rm -rf /var/lib/gather
fi
%postun

%{?ldconfig}
%systemd_postun_with_restart gatherer.service
%systemd_postun_with_restart reposd.service
%pre provider

function unregister()
{
  GLOBIGNORE=%{G_GLOB_IGNORE}
  %{_datadir}/%{name}/provider-register.sh -v -d $1 -m %{SCHEMA} -r %{REGISTRATION} #> /dev/null 2>&1 || :;
  %{_datadir}/%{name}/provider-register.sh -v -d $1 -m %{GATHER_1ST_SCHEMA} -r %{GATHER_1ST_REGISTRATION} #> /dev/null 2>&1 || :;
}
if [ $1 -gt 1 ]; then
  unregistered=no
  if [ -e /usr/sbin/cimserver ]; then
    unregister "-t pegasus";
    unregistered=yes
  fi
  if [ -e /usr/sbin/sfcbd ]; then
    unregister "-t sfcb";
    unregistered=yes
  fi
  if [ "$unregistered" != yes ]; then
    unregister
  fi
fi
%post provider

function register()
{
  %{_datadir}/%{name}/provider-register.sh -v $1 -m %{GATHER_1ST_SCHEMA} -r %{GATHER_1ST_REGISTRATION} > /dev/null 2>&1 || :;
  GLOBIGNORE=%{G_GLOB_IGNORE}
  %{_datadir}/%{name}/provider-register.sh -v $1 -m %{SCHEMA} -r %{REGISTRATION} > /dev/null 2>&1 || :;
}
%{?ldconfig}
if [ $1 -ge 1 ]; then
  registered=no
  if [ -e /usr/sbin/cimserver ]; then
    register "-t pegasus";
    registered=yes
  fi
  if [ -e /usr/sbin/sfcbd ]; then
    register "-t sfcb";
    registered=yes
  fi
  if [ "$registered" != yes ]; then
    register
  fi
fi
%preun provider

function unregister()
{
  GLOBIGNORE=%{G_GLOB_IGNORE}
  %{_datadir}/%{name}/provider-register.sh -v -d $1 -m %{SCHEMA} -r %{REGISTRATION} > /dev/null 2>&1 || :;
  %{_datadir}/%{name}/provider-register.sh -v -d $1 -m %{GATHER_1ST_SCHEMA} -r %{GATHER_1ST_REGISTRATION} > /dev/null 2>&1 || :;
}
if [ $1 -eq 0 ]; then
  unregistered=no
  if [ -e /usr/sbin/cimserver ]; then
    unregister "-t pegasus";
    unregistered=yes
  fi
  if [ -e /usr/sbin/sfcbd ]; then
    unregister "-t sfcb";
    unregistered=yes
  fi
  if [ "$unregistered" != yes ]; then
    unregister
  fi
fi
%ldconfig_postun provider
%files -f %{oreon_filedir}/main.list
%files -n sblim-gather-provider -f %{oreon_filedir}/sblim-gather-provider.list
%files -n sblim-gather-devel -f %{oreon_filedir}/sblim-gather-devel.list
%files -n sblim-gather-test -f %{oreon_filedir}/sblim-gather-test.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.9-42
- Import
