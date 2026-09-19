%global source0_hash 8a78b9235e4acc977e950af7648a2f434bde68fb46d407dbc84bfbd1e9a9626e

%global provider_dir %{_libdir}/cmpi
%global with_test_subpackage 1

Name:           sblim-cmpi-sysfs
Version:        1.2.0
Release:        38%{?dist}
Summary:        SBLIM sysfs instrumentation

License:        EPL-1.0
URL:            http://sblim.wiki.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2

# Patch0: already upstream,
#         see http://sourceforge.net/tracker/index.php?func=detail&aid=2818227&group_id=128809&atid=712784
Patch0:         sblim-cmpi-sysfs-1.2.0-provider-segfault.patch
# Patch1: issue reported upstream, patch not accepted yet,
#         see http://sourceforge.net/tracker/index.php?func=detail&aid=2818223&group_id=128809&atid=712784
Patch1:         sblim-cmpi-sysfs-1.2.0-sysfs-links.patch
# Patch2: remove version from docdir
Patch2:         sblim-cmpi-sysfs-1.2.0-docdir.patch
# Patch3: use Pegasus root/interop instead of root/PG_Interop
Patch3:         sblim-cmpi-sysfs-1.2.0-pegasus-interop.patch
# Patch4: call systemctl in provider registration
Patch4:         sblim-cmpi-sysfs-1.2.0-prov-reg-sfcb-systemd.patch
Patch5:         sblim-cmpi-sysfs-c99.patch

BuildRequires: make
BuildRequires:  sblim-cmpi-devel sblim-cmpi-base-devel
BuildRequires:  gcc
Requires:       sblim-cmpi-base cim-server

%description
Standards Based Linux Instrumentation Sysfs Providers

%if 0%{?with_test_subpackage}
%package        test
Summary:        SBLIM Sysfs Instrumentation Testcases
Requires:       sblim-cmpi-sysfs = %{version}-%{release}
Requires:       sblim-testsuite

%description test
SBLIM Base Params Testcase Files for SBLIM Testsuite
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%autopatch -p1
sed -ri 's,-type d -maxdepth 1 -mindepth 1,-maxdepth 1 -mindepth 1 -type d,g' \
        ./test/system/linux/*.{sh,system}

%build
%ifarch s390 s390x ppc ppc64
export CFLAGS="$RPM_OPT_FLAGS -fsigned-char"
%else
export CFLAGS="$RPM_OPT_FLAGS"
%endif

%configure \
%if 0%{?with_test_subpackage}
        TESTSUITEDIR=%{_datadir}/sblim-testsuite \
%endif
        PROVIDERDIR=%{provider_dir}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
# remove unused libtool files
rm -f $RPM_BUILD_ROOT/%{_libdir}/*a
rm -f $RPM_BUILD_ROOT/%{provider_dir}/*a
# shared libraries
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/cmpi" > $RPM_BUILD_ROOT/%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
mv $RPM_BUILD_ROOT/%{_libdir}/libLinux_SysfsAttributeUtil.so $RPM_BUILD_ROOT/%{provider_dir}
mv $RPM_BUILD_ROOT/%{_libdir}/libLinux_SysfsDeviceUtil.so $RPM_BUILD_ROOT/%{provider_dir}

%files
%doc AUTHORS COPYING DEBUG README README.TEST README.tog-pegasus sysfs.txt
%dir %{provider_dir}
%{provider_dir}/libLinux_Sysfs*
%{_datadir}/sblim-cmpi-sysfs
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

%if 0%{?with_test_subpackage}
%files test
%{_datadir}/sblim-testsuite/sblim-cmpi-sysfs-test.sh
%{_datadir}/sblim-testsuite/cim/Linux_Sysfs*
%{_datadir}/sblim-testsuite/system/linux/Linux_Sysfs*
%endif

%global SCHEMA %{_datadir}/%{name}/Linux_SysfsAttribute.mof %{_datadir}/%{name}/Linux_SysfsBlockDevice.mof %{_datadir}/%{name}/Linux_SysfsBusDevice.mof %{_datadir}/%{name}/Linux_SysfsInputDevice.mof %{_datadir}/%{name}/Linux_SysfsNetworkDevice.mof %{_datadir}/%{name}/Linux_SysfsSCSIDevice.mof %{_datadir}/%{name}/Linux_SysfsSCSIHostDevice.mof %{_datadir}/%{name}/Linux_SysfsTTYDevice.mof

%global REGISTRATION %{_datadir}/%{name}/Linux_SysfsAttribute.registration %{_datadir}/%{name}/Linux_SysfsBlockDevice.registration %{_datadir}/%{name}/Linux_SysfsBusDevice.registration %{_datadir}/%{name}/Linux_SysfsInputDevice.registration %{_datadir}/%{name}/Linux_SysfsNetworkDevice.registration %{_datadir}/%{name}/Linux_SysfsSCSIDevice.registration %{_datadir}/%{name}/Linux_SysfsSCSIHostDevice.registration %{_datadir}/%{name}/Linux_SysfsTTYDevice.registration

%pre
%sblim_pre

%post
%sblim_post

%preun
%sblim_preun
 
%postun -p /sbin/ldconfig

%changelog
%autochangelog
