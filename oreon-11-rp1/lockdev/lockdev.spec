%global source0_hash 2507f0e3e3ff5c9cc829b0e1c47af8b88324f0030eeccc8244b1f4b1ad40af32

%global _lockdir /run/lock/lockdev

%global checkout 20111007git
%global co_date  2011-10-07

%global _hardened_build 1

Summary: A library for locking devices
Name: lockdev
Version: 1.0.4
Release: %autorelease -p -e %{checkout}
License: LGPL-2.1-or-later
URL: https://github.com/definesat/lockdev

Source0:        https://codeload.github.com/definesat/lockdev/tar.gz/master#/lockdev-%{version}.%{checkout}.tar.gz

Patch1:        lockdev-euidaccess.patch
Patch2:        0001-major-and-minor-functions-moved-to-sysmacros.h.patch

Requires(post): glibc
Requires(postun): glibc
Requires: systemd

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: perl-interpreter
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: systemd
BuildRequires: make
BuildRequires: git
%description
Lockdev provides a reliable way to put an exclusive lock to devices
using both FSSTND and SVr4 methods.

%package devel
Summary: The header files for the lockdev library
Requires: lockdev = %{version}-%{release}

%description devel
The lockdev library provides a reliable way to put an exclusive lock
on devices using both FSSTND and SVr4 methods. The lockdev-devel
package contains the development headers.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n lockdev-master

%patch -P1 -p1 -b .access
%patch -P2 -p1

cat >lockdev.sysusers.conf <<EOF
g lock 54
EOF

%build
./scripts/git-version > VERSION

touch ChangeLog

autoreconf --verbose --force --install

CFLAGS="%{optflags} -D_PATH_LOCK=\\\"%{_lockdir}\\\"" \
%configure --disable-static --enable-helper --disable-silent-rules

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/*.la

mkdir -p %{buildroot}%{_lockdir}

mkdir -p ${RPM_BUILD_ROOT}%{_tmpfilesdir}
cat > ${RPM_BUILD_ROOT}%{_tmpfilesdir}/lockdev.conf <<EOF
d %{_lockdir} 0775 root lock -
EOF

install -m0644 -D lockdev.sysusers.conf %{buildroot}%{_sysusersdir}/lockdev.conf


%post
if [ $1 -eq 1 ] ; then
%tmpfiles_create lockdev.conf
fi

%files
%{license} COPYING
%doc AUTHORS
%ghost %dir %attr(0775,root,lock) %{_lockdir}
%attr(2711,root,lock)  %{_sbindir}/lockdev
%{_tmpfilesdir}/lockdev.conf
%{_libdir}/*.so.*
%{_mandir}/man8/*
%{_sysusersdir}/lockdev.conf

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/lockdev.pc
%{_mandir}/man3/*
%{_includedir}/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.4-0.1.20111007git
- Import
