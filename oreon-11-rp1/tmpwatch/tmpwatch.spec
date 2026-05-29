%global source0_hash 93168112b2515bc4c7117e8113b8d91e06b79550d2194d62a0c174fe6c2aa8d4

Summary: A utility for removing files based on when they were last accessed
Name: tmpwatch
Version: 2.11
Release: 30%{?dist}
URL: https://pagure.io/%{name}
Source0:        https://releases.pagure.org/tmpwatch/tmpwatch-2.11.tar.bz2
License: GPL-2.0-only
Requires: psmisc
Provides: bundled(gnulib)
# configure is looking for /sbin/fuser
BuildRequires: make
BuildRequires:  gcc
BuildRequires: psmisc

%description
The tmpwatch utility recursively searches through specified
directories and removes files which have not been accessed in a
specified period of time.  Tmpwatch is normally used to clean up
directories which are used for temporarily holding files (for example,
/tmp).  Tmpwatch ignores symlinks, won't switch filesystems and only
removes empty directories and regular files.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} INSTALL='install -p' install

%if "%{_sbindir}" != "%{_bindir}"
mkdir -p %{buildroot}%{_bindir}
# The $(...) computes /usr/bin => ../../
ln -s $(echo %{_bindir} |sed 's,/[^/]\+,/..,g; s,^/,,')%{_sbindir}/tmpwatch \
   %{buildroot}%{_bindir}/tmpwatch
%endif

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%if "%{_sbindir}" != "%{_bindir}"
%{_bindir}/tmpwatch
%endif
%{_sbindir}/tmpwatch
%{_mandir}/man8/tmpwatch.8*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.11-30
- Prepare for Oreon 11 (RP1)
