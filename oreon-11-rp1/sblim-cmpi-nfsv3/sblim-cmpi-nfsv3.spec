%global source0_hash ea73a7da0020b9f9baa0801e96d952f6a2f695d90ffe883ba0ded9469205d1a3

%global provider_dir %{_libdir}/cmpi
%global with_test_subpackage 1

Summary:        SBLIM nfsv3 instrumentation
Name:           sblim-cmpi-nfsv3
Version:        1.1.1
Release:        37%{?dist}
License:        EPL-1.0
URL:            http://sourceforge.net/projects/sblim/
Source0:        http://downloads.sourceforge.net/project/sblim/providers/%{name}/%{version}/%{name}-%{version}.tar.bz2

#Patch0: remove version from docdir
Patch0:         sblim-cmpi-nfsv3-1.1.1-docdir.patch
#Patch1: use Pegasus root/interop instead of root/PG_Interop
Patch1:         sblim-cmpi-nfsv3-1.1.1-pegasus-interop.patch
# Patch2: call systemctl in provider registration
Patch2:         sblim-cmpi-nfsv3-1.1.1-prov-reg-sfcb-systemd.patch
Patch3: sblim-cmpi-nfsv3-c99.patch

BuildRequires: make
BuildRequires:  sblim-cmpi-base-devel sblim-cmpi-devel
BuildRequires:  gcc
Requires:       sblim-cmpi-base cim-server cim-schema
Requires:       /etc/ld.so.conf.d
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Standards Based Linux Instrumentation Nfsv3 Providers

%package devel
Summary:        SBLIM Nfsv3 Instrumentation Header Development Files
Requires:       %{name} = %{version}-%{release}

%description devel
SBLIM Base Nfsv3 Development Package

%if 0%{?with_test_subpackage}
%package test
Summary:        SBLIM Nfsv3 Instrumentation Testcases
Requires:       %{name} = %{version}-%{release}
Requires:       sblim-testsuite

%description test
SBLIM Base Fsvol Testcase Files for SBLIM Testsuite
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%autopatch -p1

# Prevent regenerating the lexers/parsers.
touch -r util/parser/lexer.l \
  util/parser/parser.y parser.c lexer.c
touch -r util/xmlparser/xmllexer.l \
  util/xmlparser/xmlparser.y xmllexer.c xmlparser.c

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
mv $RPM_BUILD_ROOT/%{_libdir}/libLinux_NFSv3SystemConfigurationUtil.so $RPM_BUILD_ROOT/%{_libdir}/cmpi/
# remove unused libtool files
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT/%{provider_dir}/*.la
# shared libraries
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/cmpi" > $RPM_BUILD_ROOT/%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

%files
%doc AUTHORS COPYING DEBUG README README.TEST README.tog-pegasus
%{provider_dir}/*.so
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

%if 0%{?with_test_subpackage}
%files test
%{_datadir}/sblim-testsuite
%endif

%global SCHEMA %{_datadir}/%{name}/Linux_NFSv3SystemSetting.mof %{_datadir}/%{name}/Linux_NFSv3SystemConfiguration.mof

%global REGISTRATION %{_datadir}/%{name}/Linux_NFSv3SystemSetting.registration %{_datadir}/%{name}/Linux_NFSv3SystemConfiguration.registration

%pre
%sblim_pre

%post
%sblim_post

%preun
%sblim_preun

%postun -p /sbin/ldconfig

%changelog
%autochangelog
