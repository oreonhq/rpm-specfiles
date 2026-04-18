%define utempter_compat_ver 0.5.2

Summary: A privileged helper for utmp/wtmp updates
Name: libutempter
Version: 1.2.1
Release: 20%{?dist}
License: LGPL-2.1-or-later AND LGPL-2.1-only AND BSD-2-Clause
URL: https://ftp.altlinux.org/pub/people/ldv/utempter

# spectool uses HTTP clients that do not speak FTP; same tree is on HTTPS.
Source0: https://ftp.altlinux.org/pub/people/ldv/utempter/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

Requires(pre): shadow-utils

Provides: utempter = %{utempter_compat_ver}

%description
This library provides interface for terminal emulators such as
screen and xterm to record user sessions to utmp and wtmp files.

%package devel
Summary: Development environment for utempter
Requires: %{name} = %{version}-%{release}

%description devel
This package contains development files required to build
utempter-based software.

%prep
%setup -q

cat > %{name}.sysusers.conf <<_EOF
g utmp 22
g utempter 35
_EOF

%build
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" \
    libdir="%{_libdir}" libexecdir="%{_libexecdir}"

%install
%make_install libdir="%{_libdir}" libexecdir="%{_libexecdir}"

rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

install -D -m0644 %{name}.sysusers.conf %{buildroot}%{_sysusersdir}/%{name}.conf

%files
%license COPYING
%doc README
%{_libdir}/libutempter.so.0
%{_libdir}/libutempter.so.1.*
%dir %attr(755,root,utempter) %{_libexecdir}/utempter
%attr(2711,root,utmp) %{_libexecdir}/utempter/utempter
%{_sysusersdir}/%{name}.conf

%files devel
%{_includedir}/utempter.h
%{_libdir}/libutempter.so
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.1-20
- Prepare for Oreon 11 (RP1)
