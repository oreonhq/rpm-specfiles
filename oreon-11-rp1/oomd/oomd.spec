%global source0_hash 89efe256c42223c7688cacdbc51605da1104de666ed27d32e38f60e311fd1356
%bcond_without tests
Name:		oomd
Summary:        Userspace Out-Of-Memory (OOM) killer
Version:	0.5.0
Release:        1%{?dist}
License:	GPL-2.0-only
URL:		https://github.com/facebookincubator/oomd/
Source0:        https://github.com/facebookincubator/%{name}//archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{url}/commit/076af42b270388f38055fdf60dccbb3001de723a.patch
Patch1:         %{url}/commit/3989e169fc0da9c29da8dd692427d4f4c1ace413.patch
Patch2:         %{url}/commit/83a6742f08349fbc93f459228dcc3d1f56eac411.patch
Patch3:         oomd-disable-datalifecycle-children-test.patch
ExcludeArch:	i686 armv7hl
%if %{with tests}
%endif
%{?systemd_requires}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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
%oreon_prep
%build

%meson
%meson_build
%if %{with tests}
%check

%meson_test -v
%endif
%install
%meson_install
%oreon_autofiles main

%post

%systemd_post oomd.service
%preun

%systemd_preun oomd.service
%postun

%systemd_postun_with_restart oomd.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
