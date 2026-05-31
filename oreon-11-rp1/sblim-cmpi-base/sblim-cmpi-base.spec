%global source0_hash 0e9cb016ac3103b3f564cb5d0cb5dd5609cd32084fafac08b0b42250f5dcda7f

%global with_test_subpackage 1

Name:           sblim-cmpi-base
Version:        1.6.4
Release:        32%{?dist}
Summary:        SBLIM CMPI Base Providers

License:        EPL-1.0
URL:            https://sourceforge.net/projects/sblim/
Source0:        http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
Patch0:         sblim-cmpi-base-1.6.0-missing-fclose.patch
Patch1:         sblim-cmpi-base-1.6.0-methods-enable.patch
Patch2:         sblim-cmpi-base-1.6.1-double-fclose.patch
# Patch3: removes version from docdir
Patch3:         sblim-cmpi-base-1.6.2-docdir.patch
# Patch4: use Pegasus root/interop instead of root/PG_Interop
Patch4:         sblim-cmpi-base-1.6.2-pegasus-interop.patch
# Patch5: call systemctl in provider registration
Patch5:         sblim-cmpi-base-1.6.4-prov-reg-sfcb-systemd.patch
# Patch6: explicitly list library dependencies in Makefile.am, rhbz#1606302
Patch6:         sblim-cmpi-base-1.6.4-list-lib-dependencies.patch
# Patch7: don't install COPYING with license, included through %%license
Patch7:         sblim-cmpi-base-1.6.4-dont-install-license.patch
# Patch8: fixes getting of InstallDate property, improves it to work
#   on non en_US locales and updates support for Fedora
Patch8:         sblim-cmpi-base-1.6.4-fix-get-os-install-date.patch
# Patch9: fixes possible null pointer dereferences after strstr calls
Patch9:         sblim-cmpi-base-1.6.4-fix-possible-null-dereference.patch
# Patch10: fixes issues that causes FTBFS with GCC15
Patch10:        sblim-cmpi-base-1.6.4-gcc15-fixes.patch
# Patch11: adds support for Image Mode
Patch11:        sblim-cmpi-base-1.6.4-image-mode.patch
Requires:       cim-server sblim-indication_helper
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  sblim-cmpi-devel sblim-indication_helper-devel
BuildRequires:  autoconf automake libtool pkgconfig


%description
SBLIM (Standards Based Linux Instrumentation for Manageability)
CMPI (Common Manageability Programming Interface) Base Providers
for System-Related CIM (Common Information Model) classes.

%package devel
Summary:        SBLIM CMPI Base Providers Development Header Files
Requires:       %{name} = %{version}-%{release}

%description devel
SBLIM (Standards Based Linux Instrumentation for Manageability)
CMPI (Common Manageability Programming Interface) Base Provider
development header files and link libraries.

%if 0%{?with_test_subpackage}
%package test
Summary:        SBLIM CMPI Base Providers Test Cases
Requires:       %{name} = %{version}-%{release}
Requires:       sblim-testsuite

%description test
SBLIM (Standards Based Linux Instrumentation for Manageability)
CMPI (Common Manageability Programming Interface) Base Provider
Testcase Files for the SBLIM Testsuite.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
autoreconf --install --force
%patch -P0 -p0 -b .missing-fclose
%patch -P1 -p0 -b .methods-enable
%patch -P2 -p1 -b .double-fclose
%patch -P3 -p1 -b .docdir
%patch -P4 -p1 -b .pegasus-interop
%patch -P5 -p1 -b .prov-reg-sfcb-systemd
%patch -P6 -p1 -b .list-lib-dependencies
%patch -P7 -p1 -b .dont-install-license
%patch -P8 -p1 -b .fix-get-os-install-date
%patch -P9 -p1 -b .fix-possible-null-dereference
%patch -P10 -p1 -b .gcc15-fixes
%patch -P11 -p1 -b .image-mode

%build
%configure \
%if 0%{?with_test_subpackage}
        TESTSUITEDIR=%{_datadir}/sblim-testsuite \
%endif
        --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
cp -fp *OSBase_UnixProcess.h $RPM_BUILD_ROOT/%{_includedir}/sblim
chmod 644 $RPM_BUILD_ROOT/%{_includedir}/sblim/*OSBase_UnixProcess.h
# remove unused libtool files
rm -f $RPM_BUILD_ROOT/%{_libdir}/*a
rm -f $RPM_BUILD_ROOT/%{_libdir}/cmpi/*a

%files
%license COPYING
%doc AUTHORS DEBUG README README.INDICATION README.TEST README.tog-pegasus
%{_datadir}/%{name}
%{_libdir}/*.so.*
%{_libdir}/cmpi/*.so*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%if 0%{?with_test_subpackage}
%files test
%dir %{_datadir}/sblim-testsuite/cim
%dir %{_datadir}/sblim-testsuite/system
%dir %{_datadir}/sblim-testsuite/system/linux
%{_datadir}/sblim-testsuite/test-cmpi-base.sh
%{_datadir}/sblim-testsuite/cim/*.cim
%{_datadir}/sblim-testsuite/system/linux/*.system
%{_datadir}/sblim-testsuite/system/linux/*.sh
%{_datadir}/sblim-testsuite/system/linux/*.pl
%endif

%global SCHEMA %{_datadir}/%{name}/Linux_Base.mof %{_datadir}/%{name}/Linux_BaseIndication.mof

%global REGISTRATION %{_datadir}/%{name}/Linux_BaseIndication.registration

%pre
%sblim_pre

%post
%sblim_post

%preun
%sblim_preun

%postun -p /sbin/ldconfig

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.4-32
- Prepare for Oreon 11 (RP1)
