%global source0_hash 58c55d9c1402474065adae669511c191de374b0871eec781239ab400b907c327
Summary:        Utilities for managing processes on your system
Name: psmisc
Version: 23.7
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: https://gitlab.com/psmisc/psmisc
Source0:        https://sourceforge.net/projects/%{name}/files/%{name}/%{name}-%{version}.tar.xz
%if "%{_sbindir}" == "%{_bindir}"
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/fuser
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  libselinux-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
The psmisc package contains utilities for managing processes on your
system: pstree, killall, fuser and pslog.  The pstree command displays
a tree structure of all of the running processes on your system.  The
killall command sends a specified signal (SIGTERM if nothing is specified)
to processes identified by name.  The fuser command identifies the PIDs
of processes that are using specified files or filesystems. The pslog
command shows the path of log files owned by a given process.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --prefix=%{_prefix} --enable-selinux
make %{?_smp_mflags}
%install
make install DESTDIR="$RPM_BUILD_ROOT"
%if "%{_sbindir}" != "%{_bindir}"
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
mv $RPM_BUILD_ROOT%{_bindir}/fuser $RPM_BUILD_ROOT%{_sbindir}
%endif
%find_lang %name --all-name --with-man
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.7-7
- Prepare for Oreon 11 (RP1)
