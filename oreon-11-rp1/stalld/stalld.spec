%global source0_hash b2d2c4f610e1a66d1a2df964f98840215ca1e23f933ec890611aea597b596fe2
Name:		stalld
Version:	1.28.1
Release:        1%{?dist}
Summary:        Daemon that finds starving tasks and gives them a temporary boost
License:	GPL-2.0-or-later AND GPL-2.0-only
URL:		https://gitlab.com/rt-linux-tools/%{name}/%{name}.git
Source0:        https://gitlab.com/rt-linux-tools/%{name}/-/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:	systemd
%ifnarch i686
Requires:	libbpf
%endif
%define _hardened_build 1
# oreon:deps
BuildRequires:  bpftool
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libbpf-devel
BuildRequires:  llvm
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
The stalld program monitors the set of system threads,
looking for threads that are ready-to-run but have not
been given processor time for some threshold period.
When a starving thread is found, it is given a temporary
boost using the SCHED_DEADLINE policy. The default is to
allow 10 microseconds of runtime for 1 second of clock time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir stalld-v%{version}-3639a0579c3edfc6626559c902d0bf31daf33f8b
%oreon_prep
%build

%make_build CFLAGS="%{optflags} %{build_cflags} -DVERSION="\\\"%{version}\\\"""  LDFLAGS="%{build_ldflags}"
%install
%make_install DOCDIR=%{_docdir} MANDIR=%{_mandir} BINDIR=%{_bindir} DATADIR=%{_datadir} VERSION=%{version}
%make_install -C systemd UNITDIR=%{_unitdir}
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
