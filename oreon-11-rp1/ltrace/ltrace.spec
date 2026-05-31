%global source0_hash 2e18c2a976db50da58788c742fccddfcb41029a00399c03f747733025442673f

Summary: Tracks runtime library calls from dynamically linked executables
Name: ltrace
Version: 0.8.1
Release: 2%{?dist}
# In coordination with Juan Céspedes, upstream is now officially on gitlab.
# We are going to being sending all of our Fedora patches upstream to gitlab.
URL: https://gitlab.com/cespedes/ltrace
License: GPL-2.0-or-later

BuildRequires: elfutils-devel dejagnu
BuildRequires: libselinux-devel
BuildRequires: autoconf automake libtool
BuildRequires: gcc-c++
BuildRequires: make

#  https://gitlab.com/cespedes/ltrace/-/releases
Source0:        https://gitlab.com/cespedes/ltrace/-/archive/v0.8.1/ltrace-0.8.1.tar.bz2

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
%autosetup -p1

%build
autoreconf -i
%configure --docdir=%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
%make_build

%install
%make_install bindir=%{_bindir}

# The testsuite is useful for development in real world, but fails in
# koji for some reason.  Disable it, but have it handy.
%check
echo ====================TESTING=========================
# The ppc64 testsuite hangs rpmbuild hard in koji, disable until fixed.
%ifnarch ppc64le
timeout 180 make check ||:
%endif
echo ====================TESTING END=====================

%files
%doc NEWS COPYING CREDITS INSTALL README TODO
%{_bindir}/ltrace
%{_mandir}/man1/ltrace.1*
%{_mandir}/man5/ltrace.conf.5*
%{_datadir}/ltrace

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.1-2
- Import
