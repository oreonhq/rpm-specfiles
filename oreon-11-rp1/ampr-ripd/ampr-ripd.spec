%global source0_hash e4635bd0f88c1f2b0777e948a00d0470aa97254ec4b0b8fd75c79d109995a350

# hardened build if not overriden
%{!?_hardened_build:%global _hardened_build 1}

%if %{?_hardened_build}%{!?_hardened_build:0}
%global cflags_harden -fpie
%global ldflags_harden -pie -z relro -z now
%endif

Summary: Routing daemon for the ampr network
Name: ampr-ripd
Version: 2.4.2
Release: 4%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.yo2loj.ro/hamprojects/
BuildRequires: gcc
BuildRequires: dos2unix
BuildRequires: systemd
BuildRequires: make
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Source0: http://www.yo2loj.ro/hamprojects/%{name}-%{version}.tgz
Source1: ampr-ripd.service
# upstream notified
Source2: COPYING
Patch: ampr-ripd-2.4.2-install-fix.patch
Patch: ampr-ripd-2.1.1-examples-noshebang.patch
Patch: ampr-ripd-2.4.1-pidfile.patch

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

# Systemd
install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

# Examples
install -Dd %{buildroot}%{_datadir}/%{name}/examples
install -Dpm 644 -t %{buildroot}%{_datadir}/%{name}/examples examples/ampr-run.sh examples/find_pass.sh \
  examples/interfaces

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc COPYING manual.txt

%{_sbindir}/ampr-ripd
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_unitdir}/%{name}.service

%changelog
%autochangelog
