%global source0_hash 19882ebe9c3079a50ec98f38b27b1679ddfcbe7b5bbab29561d223e9fb8bb859

%global provider_dir %{_libdir}/cmpi
%global with_test_subpackage 1

Summary:        SBLIM fsvol instrumentation
Name:           sblim-cmpi-fsvol
Version:        1.5.1
Release:        41%{?dist}
License:        EPL-1.0
URL:            http://sourceforge.net/projects/sblim/
Source0:        http://downloads.sourceforge.net/project/sblim/providers/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0:         sblim-cmpi-fsvol-1.5.0-ext4-support.patch
# Patch1: bz921487, backported from upstream
Patch1:         sblim-cmpi-fsvol-1.5.1-mounted-fs-shown-as-disabled.patch
# Patch2: remove version from docdir
Patch2:         sblim-cmpi-fsvol-1.5.1-docdir.patch
# Patch3: use Pegasus root/interop instead of root/PG_Interop
Patch3:         sblim-cmpi-fsvol-1.5.1-pegasus-interop.patch
# Patch4: call systemctl in provider registration
Patch4:         sblim-cmpi-fsvol-1.5.1-prov-reg-sfcb-systemd.patch
# Patch5: fixes  mounted filesystem is shown as disabled when device mapper is used
Patch5:         sblim-cmpi-fsvol-1.5.1-mounted-dm-fs-shown-as-disabled.patch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  sblim-cmpi-base-devel sblim-cmpi-devel
BuildRequires:  gcc
Requires:       sblim-cmpi-base cim-server
Requires:       /etc/ld.so.conf.d
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Standards Based Linux Instrumentation Fsvol Providers

%package devel
Summary:        SBLIM Fsvol Instrumentation Header Development Files
Requires:       %{name} = %{version}-%{release}

%description devel
SBLIM Base Fsvol Development Package

%if 0%{?with_test_subpackage}
%package test
Summary:        SBLIM Fsvol Instrumentation Testcases
Requires:       %{name} = %{version}-%{release}
Requires:       sblim-testsuite

%description test
SBLIM Base Fsvol Testcase Files for SBLIM Testsuite
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%autopatch -p1

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

%files
%doc AUTHORS COPYING DEBUG README README.TEST README.tog-pegasus
%{_libdir}/libcmpiOSBase_CommonFsvol*.so.*
%{provider_dir}/libcmpiOSBase_LocalFileSystemProvider.so
%{provider_dir}/libcmpiOSBase_NFSProvider.so
%{provider_dir}/libcmpiOSBase_BlockStorageStatisticalDataProvider.so
%{provider_dir}/libcmpiOSBase_HostedFileSystemProvider.so
%{provider_dir}/libcmpiOSBase_BootOSFromFSProvider.so
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

%files devel
%{_libdir}/libcmpiOSBase_CommonFsvol*.so
%{_includedir}/sblim/*Fsvol.h

%if 0%{?with_test_subpackage}
%files test
%{_datadir}/sblim-testsuite/test-cmpi-fsvol.sh
%{_datadir}/sblim-testsuite/cim/*FileSystem.cim
%{_datadir}/sblim-testsuite/cim/*FS.cim
%{_datadir}/sblim-testsuite/cim/*BlockStorageStatisticalData.cim
%{_datadir}/sblim-testsuite/system/linux/*FileSystem.*
%{_datadir}/sblim-testsuite/system/linux/*FileSystemEntries.*
%endif

%global SCHEMA %{_datadir}/%{name}/Linux_Fsvol.mof

%global REGISTRATION %{_datadir}/%{name}/Linux_Fsvol.registration

%pre
%sblim_pre

%post
%sblim_post

%preun
%sblim_preun

%postun -p /sbin/ldconfig

%changelog
%autochangelog
