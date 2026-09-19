%global source0_hash 06dd004d735b728575b6c06535ba37de52a62318d8938ed73bf43187ed95ab56

%global provider_dir %{_libdir}/cmpi
%global with_test_subpackage 1

Name:           sblim-cmpi-network
Version:        1.4.0
Release:        39%{?dist}
Summary:        SBLIM Network Instrumentation

License:        EPL-1.0
URL:            http://sblim.wiki.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2

Patch0:         sblim-cmpi-network-1.4.0-network-devices-arbitrary-names-support.patch
# Patch1: remove version from docdir
Patch1:         sblim-cmpi-network-1.4.0-docdir.patch
# Patch2: use Pegasus root/interop instead of root/PG_Interop
Patch2:         sblim-cmpi-network-1.4.0-pegasus-interop.patch
# Patch3: call systemctl in provider registration
Patch3:         sblim-cmpi-network-1.4.0-prov-reg-sfcb-systemd.patch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  sblim-cmpi-base-devel >= 1.5 sblim-cmpi-devel
BuildRequires:  gcc
Requires:       sblim-cmpi-base >= 1.5 cim-server cim-schema

%description
Standards Based Linux Instrumentation Network Providers

%package        devel
Summary:        SBLIM Network Instrumentation Header Development Files
Requires:       %{name} = %{version}-%{release}

%description    devel
SBLIM Base Network Development Package

%if 0%{?with_test_subpackage}
%package        test
Summary:        SBLIM Network Instrumentation Testcases
Requires:       sblim-cmpi-network = %{version}-%{release}

%description    test
SBLIM Base Network Testcase Files for SBLIM Testsuite
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
        --disable-static \
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
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT/%{provider_dir}/*.la
# shared libraries
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/cmpi" > $RPM_BUILD_ROOT/%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

%files
%doc AUTHORS COPYING DEBUG README README.TEST README.tog-pegasus
%{_datadir}/%{name}
%{_libdir}/*.so.*
%{provider_dir}/*.so
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

%files devel
%{_includedir}/*
%{_libdir}/*.so

%if 0%{?with_test_subpackage}
%files test
%{_datadir}/sblim-testsuite
%endif

%global SCHEMA %{_datadir}/%{name}/Linux_Network.mof

%global REGISTRATION %{_datadir}/%{name}/Linux_Network.registration

%pre
%sblim_pre

%post
%sblim_post

%preun
%sblim_preun

%postun -p /sbin/ldconfig

%changelog
%autochangelog
