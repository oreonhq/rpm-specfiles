%global source0_hash e4635bd0f88c1f2b0777e948a00d0470aa97254ec4b0b8fd75c79d109995a350
%{!?_hardened_build:%global _hardened_build 1}
%if %{?_hardened_build}%{!?_hardened_build:0}
%global cflags_harden -fpie
%global ldflags_harden -pie -z relro -z now
%endif
Summary:        Routing daemon for the ampr network
Name: ampr-ripd
Version: 2.4.2
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://www.yo2loj.ro/hamprojects/
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Source0:        http://www.yo2loj.ro/hamprojects/%{name}-%{version}.tgz
Source1: ampr-ripd.service
Source2: COPYING
Patch: ampr-ripd-2.4.2-install-fix.patch
Patch: ampr-ripd-2.1.1-examples-noshebang.patch
Patch: ampr-ripd-2.4.1-pidfile.patch
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
Routing daemon written in C similar to Hessu's rip44d including optional
resending of RIPv2 broadcasts for router injection.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
cp %{SOURCE2} .

%build

make %{?_smp_mflags} CFLAGS="%{optflags} %{?cflags_harden}" LDFLAGS="%{?__global_ldflags} %{?ldflags_harden}"
%install
make %{?_smp_mflags} DESTDIR=%{buildroot} SBINDIR=%{buildroot}/%{_sbindir} install
install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -Dd %{buildroot}%{_datadir}/%{name}/examples
install -Dpm 644 -t %{buildroot}%{_datadir}/%{name}/examples examples/ampr-run.sh examples/find_pass.sh \
  examples/interfaces
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
