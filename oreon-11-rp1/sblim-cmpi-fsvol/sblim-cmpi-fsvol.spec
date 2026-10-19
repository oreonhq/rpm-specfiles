%global source0_hash 19882ebe9c3079a50ec98f38b27b1679ddfcbe7b5bbab29561d223e9fb8bb859
%global provider_dir %{_libdir}/cmpi
%global with_test_subpackage 1
Summary:        SBLIM fsvol instrumentation
Name:           sblim-cmpi-fsvol
Version:        1.5.1
Release:        1%{?dist}
License:        EPL-1.0
URL:            http://sourceforge.net/projects/sblim/
Source0:        http://downloads.sourceforge.net/project/sblim/providers/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0:         sblim-cmpi-fsvol-1.5.0-ext4-support.patch
Patch1:         sblim-cmpi-fsvol-1.5.1-mounted-fs-shown-as-disabled.patch
Patch2:         sblim-cmpi-fsvol-1.5.1-docdir.patch
Patch3:         sblim-cmpi-fsvol-1.5.1-pegasus-interop.patch
Patch4:         sblim-cmpi-fsvol-1.5.1-prov-reg-sfcb-systemd.patch
Patch5:         sblim-cmpi-fsvol-1.5.1-mounted-dm-fs-shown-as-disabled.patch
Requires:       sblim-cmpi-base cim-server
Requires:       /etc/ld.so.conf.d
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  sblim-cmpi-base-devel
BuildRequires:  sblim-cmpi-devel
# /oreon:deps
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
rm -f $RPM_BUILD_ROOT/%{_libdir}/*a
rm -f $RPM_BUILD_ROOT/%{provider_dir}/*a
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/cmpi" > $RPM_BUILD_ROOT/%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

%sblim_pre
%post

%sblim_post
%preun

%sblim_preun
%postun -p /sbin/ldconfig

%files -f %{oreon_filedir}/main.list
%files -n sblim-cmpi-fsvol-devel -f %{oreon_filedir}/sblim-cmpi-fsvol-devel.list
%files -n sblim-cmpi-fsvol-test -f %{oreon_filedir}/sblim-cmpi-fsvol-test.list

%changelog

%autochangelog
