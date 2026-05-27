%global source0_hash d14929f910d060932e717e9382425d47c2e7144235a53713d55a94f7de535a4b

Summary: A utility for displaying and/or setting hard disk parameters
Name: hdparm
Version: 9.65
Release: 10%{?dist}
License: hdparm
URL:    https://sourceforge.net/projects/%{name}/
Source: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0: %{name}-9.60-ditch_dead_code.patch
Patch1: %{name}-9.43-close_fd.patch
Patch2: %{name}-9.43-get_geom.patch
Patch3: %{name}-9.54-resourceleak-fixes.patch
Patch4: %{name}-9.54-resourceleak-fixes-2.patch
Patch5: %{name}-9.60-sysfs-fclose.patch

BuildRequires: gcc
BuildRequires: make

Provides: /sbin/hdparm

%if "%{_sbindir}" == "%{_bindir}"
# We rely on filesystem to create the compat symlinks for us
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/hdparm
%endif

%description
Hdparm is a useful system utility for setting (E)IDE hard drive
parameters.  For example, hdparm can be used to tweak hard drive
performance and to spin down hard drives for power conservation.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
CFLAGS="$RPM_OPT_FLAGS" %make_build STRIP=/bin/true LDFLAGS="$RPM_LD_FLAGS"

%install
install -c -m 755 -Dt $RPM_BUILD_ROOT%{_sbindir}/ hdparm
install -c -m 644 -Dt $RPM_BUILD_ROOT%{_mandir}/man8/ hdparm.8

%files
%doc hdparm.lsm Changelog README.acoustic TODO
%license LICENSE.TXT
%{_sbindir}/hdparm
%{_mandir}/man8/hdparm.8*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.65-10
- Prepare for Oreon 11 (RP1)
