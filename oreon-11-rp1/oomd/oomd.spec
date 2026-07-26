%global source0_hash 89efe256c42223c7688cacdbc51605da1104de666ed27d32e38f60e311fd1356

%bcond_without tests

Name:		oomd
Summary:	Userspace Out-Of-Memory (OOM) killer
Version:	0.5.0
Release:	16%{dist}
License:	GPL-2.0-only
URL:		https://github.com/facebookincubator/oomd/
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Check return value for mkstemp()
Patch0:         %{url}/commit/076af42b270388f38055fdf60dccbb3001de723a.patch
# Fix ODR violation in tests
Patch1:         %{url}/commit/3989e169fc0da9c29da8dd692427d4f4c1ace413.patch
# Resolved a compiler error due to lacking include
Patch2:         %{url}/commit/83a6742f08349fbc93f459228dcc3d1f56eac411.patch
# Disable a test that seems to fail on kernel 6.6.9-100.fc38
Patch3:         oomd-disable-datalifecycle-children-test.patch

ExcludeArch:	i686 armv7hl

BuildRequires:	gcc-c++
BuildRequires:	meson >= 0.45
BuildRequires:	pkgconfig(jsoncpp)
BuildRequires:	pkgconfig(libsystemd)
%if %{with tests}
BuildRequires:	gmock-devel
BuildRequires:	gtest-devel
%endif
BuildRequires:	systemd-rpm-macros
%{?systemd_requires}

%description
Out of memory killing has historically happened inside kernel space. On a
memory overcommitted linux system, malloc(2) and friends usually never fail.
However, if an application dereferences the returned pointer and the system has
run out of physical memory, the linux kernel is forced take extreme measures,
up to and including killing processes. This is sometimes a slow and painful
process because the kernel can spend an unbounded amount of time swapping in
and out pages and evicting the page cache. Furthermore, configuring policy is
not very flexible while being somewhat complicated.

oomd aims to solve this problem in userspace. oomd leverages PSI and cgroupv2
to monitor a system holistically. oomd then takes corrective action in
userspace before an OOM occurs in kernel space. Corrective action is configured
via a flexible plugin system, in which custom code can be written. By default,
this involves killing offending processes. This enables an unparalleled level
of flexibility where each workload can have custom protection rules.
Furthermore, time spent livedlocked in kernelspace is minimized.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%if %{with tests}
%check
%meson_test -v
%endif

%install
%meson_install

%files
%license LICENSE
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md docs/
%{_bindir}/oomd
%{_unitdir}/oomd.service
%{_mandir}/man1/oomd.*
%config(noreplace) %{_sysconfdir}/oomd/

%post
%systemd_post oomd.service

%preun
%systemd_preun oomd.service

%postun
%systemd_postun_with_restart oomd.service

%changelog
%autochangelog
