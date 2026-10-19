%global source0_hash 2e18c2a976db50da58788c742fccddfcb41029a00399c03f747733025442673f
Summary:        Tracks runtime library calls from dynamically linked executables
Name: ltrace
Version: 0.8.1
Release:        2%{?dist}
URL: https://gitlab.com/cespedes/ltrace
License: GPL-2.0-or-later
Source0:        https://gitlab.com/cespedes/ltrace/-/archive/%{version}/ltrace-%{version}.tar.bz2
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dejagnu
BuildRequires:  elfutils-devel
BuildRequires:  gcc-c++
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Ltrace is a debugging program which runs a specified command until the
command exits.  While the command is executing, ltrace intercepts and
records both the dynamic library calls called by the executed process
and the signals received by the executed process.  Ltrace can also
intercept and print system calls executed by the process.

You should install ltrace if you need a sysadmin tool for tracking the
execution of processes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -i
%configure --docdir=%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
%make_build
%install
%make_install bindir=%{_bindir}
%oreon_autofiles main

%check

echo ====================TESTING=========================
%ifnarch ppc64le
timeout 180 make check ||:
%endif
echo ====================TESTING END=====================
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.1-2
- Import
