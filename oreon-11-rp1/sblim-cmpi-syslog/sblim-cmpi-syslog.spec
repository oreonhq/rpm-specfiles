%global source0_hash 4d6004acf07159d763605230703da8247f7109ae19e0c33f454dca6d29b3b96a

%global provider_dir %{_libdir}/cmpi
%global with_test_subpackage 1

Summary:        SBLIM syslog instrumentation
Name:           sblim-cmpi-syslog
Version:        0.9.0
Release:        32%{?dist}
License:        EPL-1.0
URL:            http://sourceforge.net/projects/sblim/
Source0:        http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2

# use Pegasus' root/interop instead of root/PG_Interop
Patch0:         sblim-cmpi-syslog-0.9.0-pegasus-interop.patch
Patch1:         sblim-cmpi-syslog-0.9.0-docdir.patch
# Patch2: call systemctl in provider registration
Patch2:         sblim-cmpi-syslog-0.9.0-prov-reg-sfcb-systemd.patch
# Patch3: fixes -Wformat-security build error when debug is enabled
Patch3:         sblim-cmpi-syslog-0.9.0-format-security.patch
# Patch4: fix possible buffer overflow, remove usage of obsolete tmpnam()
Patch4:         sblim-cmpi-syslog-0.9.0-buffer-overflow-remove-tmpnam.patch
Patch5: sblim-cmpi-syslog-c99.patch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  sblim-cmpi-devel
BuildRequires:  sblim-cmpi-base-devel >= 1.5.4
BuildRequires:  libtool
Requires:       sblim-cmpi-base >= 1.5.4 cim-server
Requires:       /etc/ld.so.conf.d
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Standards Based Linux Instrumentation Syslog Providers

%package devel
# ^- currently a placeholder - no devel files shipped
Summary:        SBLIM Syslog Instrumentation Header Development Files
Requires:       %{name} = %{version}-%{release}

%description devel
SBLIM Base Syslog Development Package

%if 0%{?with_test_subpackage}
%package test
Summary:        SBLIM Syslog Instrumentation Testcases
Requires:       %{name} = %{version}-%{release}
Requires:       sblim-testsuite

%description test
SBLIM Base Syslog Testcase Files for SBLIM Testsuite
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%autopatch -p1
# removing COPYING, because it's misleading
rm -f COPYING
# ./autoconfiscate.sh

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
        PROVIDERDIR=%{provider_dir} \
        SYSLOG=rsyslog
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
# move libraries to provider dir
mv $RPM_BUILD_ROOT/%{_libdir}/lib[Ss]yslog*.so* $RPM_BUILD_ROOT/%{provider_dir}
# add shebang to the scripts
sed -i -e '1i#!/bin/sh' $RPM_BUILD_ROOT/%{_bindir}/syslog-service.sh \
%if 0%{?with_test_subpackage}
$RPM_BUILD_ROOT/%{_datadir}/sblim-testsuite/runtest_pegasus.sh \
$RPM_BUILD_ROOT/%{_datadir}/sblim-testsuite/runtest_wbemcli.sh \
$RPM_BUILD_ROOT/%{_datadir}/sblim-testsuite/system/linux/logrecord.sh \
$RPM_BUILD_ROOT/%{_datadir}/sblim-testsuite/system/linux/msglogtest.sh \
$RPM_BUILD_ROOT/%{_datadir}/sblim-testsuite/system/linux/messagelog.sh
%endif

%files
%{_bindir}/syslog-service.sh
%{provider_dir}/lib[Ss]yslog*.so*
%{_datadir}/%{name}
%docdir %{_datadir}/doc/%{name}
%{_datadir}/doc/%{name}
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

%if 0%{?with_test_subpackage}
%files test
%{_datadir}/sblim-testsuite/runtest*
%{_datadir}/sblim-testsuite/test-cmpi-syslog*
%{_datadir}/sblim-testsuite/cim/Syslog*
%{_datadir}/sblim-testsuite/system/linux/Syslog*
%{_datadir}/sblim-testsuite/system/linux/logrecord.sh
%{_datadir}/sblim-testsuite/system/linux/messagelog.sh
%{_datadir}/sblim-testsuite/system/linux/msglogtest.sh
%{_datadir}/sblim-testsuite/system/linux/setting
%endif

%global SCHEMA %{_datadir}/sblim-cmpi-syslog/Syslog_Log.mof %{_datadir}/sblim-cmpi-syslog/Syslog_Service.mof  %{_datadir}/sblim-cmpi-syslog/Syslog_Configuration.mof
%global REGISTRATION %{_datadir}/sblim-cmpi-syslog/Syslog_Configuration.registration  %{_datadir}/sblim-cmpi-syslog/Syslog_Log.registration %{_datadir}/sblim-cmpi-syslog/Syslog_Service.registration

%pre
%sblim_pre

%post
%sblim_post

%preun
%sblim_preun

%postun -p /sbin/ldconfig

%changelog
%autochangelog
