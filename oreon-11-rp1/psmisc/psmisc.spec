%global source0_hash 58c55d9c1402474065adae669511c191de374b0871eec781239ab400b907c327

Summary: Utilities for managing processes on your system
Name: psmisc
Version: 23.7
Release: 7%{?dist}
License: GPL-2.0-or-later
URL: https://gitlab.com/psmisc/psmisc

Source:        https://sourceforge.net/projects/%{name}/files/%{name}/%{name}-%{version}.tar.xz

#The following has been reworked by upstream in a different way ... we'll see
#Patch1: psmisc-22.13-fuser-silent.patch

BuildRequires: make
BuildRequires: libselinux-devel
BuildRequires: gettext
BuildRequires: ncurses-devel
BuildRequires: autoconf automake
BuildRequires: gcc
BuildRequires: git

%if "%{_sbindir}" == "%{_bindir}"
# Compat symlinks for Requires in other packages.
# We rely on filesystem to create the symlinks for us.
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/fuser
%endif

%description
The psmisc package contains utilities for managing processes on your
system: pstree, killall, fuser and pslog.  The pstree command displays
a tree structure of all of the running processes on your system.  The
killall command sends a specified signal (SIGTERM if nothing is specified)
to processes identified by name.  The fuser command identifies the PIDs
of processes that are using specified files or filesystems. The pslog
command shows the path of log files owned by a given process.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -S git

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


%files -f %{name}.lang
%{_sbindir}/fuser
%{_bindir}/killall
%{_bindir}/pstree
%{_bindir}/pstree.x11
%{_bindir}/prtstat
%{_bindir}/pslog
%{_mandir}/man1/fuser.1*
%{_mandir}/man1/killall.1*
%{_mandir}/man1/pstree.1*
%{_mandir}/man1/prtstat.1*
%{_mandir}/man1/pslog.1*
%ifarch %{ix86} x86_64 ppc %{power64} %{arm} aarch64 mipsel
%{_bindir}/peekfd
%{_mandir}/man1/peekfd.1*
%else
%exclude %{_mandir}/man1/peekfd.1*
%endif
%license COPYING
%doc AUTHORS ChangeLog README


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.7-7
- Prepare for Oreon 11 (RP1)
