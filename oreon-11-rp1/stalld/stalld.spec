Name:		stalld
Version:	1.27.1
Release:	2%{?dist}
Summary:	Daemon that finds starving tasks and gives them a temporary boost

License:	GPL-2.0-or-later AND GPL-2.0-only
URL:		https://gitlab.com/rt-linux-tools/%{name}/%{name}.git
Source0:	https://gitlab.com/rt-linux-tools/%{name}/-/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 6aaedfa18f150e7898a633fbde60ec3a9bd583111f6791d7e0adda018f47957b
%global source0_file stalld-1.27.1.tar.gz
# oreon url source checksums end

BuildRequires:	glibc-devel
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	systemd-rpm-macros

Requires:	systemd

%ifnarch i686
BuildRequires:	bpftool
BuildRequires:	clang
BuildRequires:	llvm
BuildRequires:	libbpf-devel

Requires:	libbpf
%endif

%define _hardened_build 1

%description
The stalld program monitors the set of system threads,
looking for threads that are ready-to-run but have not
been given processor time for some threshold period.
When a starving thread is found, it is given a temporary
boost using the SCHED_DEADLINE policy. The default is to
allow 10 microseconds of runtime for 1 second of clock time.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/stalld-1.27.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6aaedfa18f150e7898a633fbde60ec3a9bd583111f6791d7e0adda018f47957b" || { echo "oreon: Source0 SHA256 mismatch for stalld-1.27.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build
%make_build CFLAGS="%{optflags} %{build_cflags} -DVERSION="\\\"%{version}\\\"""  LDFLAGS="%{build_ldflags}"

%install
%make_install DOCDIR=%{_docdir} MANDIR=%{_mandir} BINDIR=%{_bindir} DATADIR=%{_datadir} VERSION=%{version}
%make_install -C systemd UNITDIR=%{_unitdir}

%files
%{_bindir}/%{name}
%{_bindir}/throttlectl
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/sysconfig/stalld
%doc %{_docdir}/README.md
%doc %{_mandir}/man8/stalld.8*
%license gpl-2.0.txt

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.27.1-2
- Import
