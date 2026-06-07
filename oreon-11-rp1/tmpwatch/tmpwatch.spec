%global source0_hash none

Summary: A utility for removing files based on when they were last accessed
Name: tmpwatch
Version: 2.11
Release: 30%{?dist}
URL: https://pagure.io/%{name}
Source0:        https://github.com/pete4abw/tmpwatch/archive/44a0f5f3fbc4414cf12e06ccc09565852ba859ba.tar.gz#/tmpwatch-%{version}.tar.bz2
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n tmpwatch-44a0f5f3fbc4414cf12e06ccc09565852ba859ba

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
