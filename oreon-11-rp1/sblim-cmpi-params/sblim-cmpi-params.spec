%global source0_hash a75df3e17316954a9c544375b773199bbbc8a89ef8e1623032ee177b3ed7db98
%global provider_dir %{_libdir}/cmpi
%global with_test_subpackage 1
Name:           sblim-cmpi-params
Version:        1.3.0
Release:        37%{?dist}
Summary:        SBLIM params instrumentation
License:        EPL-1.0
URL:            http://sblim.wiki.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
Patch0:         sblim-cmpi-params-1.2.4-no-abi-params.patch
Patch1:         sblim-cmpi-params-1.3.0-docdir.patch
Patch2:         sblim-cmpi-params-1.3.0-pegasus-interop.patch
Patch3:         sblim-cmpi-params-1.3.0-prov-reg-sfcb-systemd.patch
Requires:       sblim-cmpi-base cim-server cim-schema
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sblim-cmpi-base-devel
BuildRequires:  sblim-cmpi-devel
# /oreon:deps
%description
Standards Based Linux Instrumentation Params Providers

%if 0%{?with_test_subpackage}
%package        test
Summary:        SBLIM Params Instrumentation Testcases
Requires:       sblim-cmpi-params = %{version}-%{release}
Requires:       sblim-testsuite
%description -n sblim-cmpi-params-test
SBLIM Base Params Testcase Files for SBLIM Testsuite
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%autopatch -p1

%build

%configure \
        --disable-static \
%if 0%{?with_test_subpackage}
        TESTSUITEDIR=%{_datadir}/sblim-testsuite \
%endif
        PROVIDERDIR=%{provider_dir}
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT/%{provider_dir}/*.la
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

%sblim_pre
%post

%sblim_post
%preun

%sblim_preun
%files -f %{oreon_filedir}/main.list
%files -n sblim-cmpi-params-test -f %{oreon_filedir}/sblim-cmpi-params-test.list

%changelog

%autochangelog
