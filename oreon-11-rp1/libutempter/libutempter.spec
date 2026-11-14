# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 52809c75af9b0e13249521177def85787f457888cbcee5511bf96fe06e146711

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libutempter
Version:        1.2.3
Release:        1%{?dist}
Summary:        A privileged helper for utmp/wtmp updates
License:        LGPL-2.1-or-later
URL:            https://github.com/altlinux/libutempter
Source0:        https://github.com/altlinux/libutempter/archive/%{version}-alt1/libutempter-%{version}-alt1.tar.gz

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  binutils

Requires(pre):  shadow-utils

%description
This library provides interface for terminal emulators such as
screen and xterm to record user sessions to utmp and wtmp files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the files needed to compile programs that use
the %{name} library.

%prep
%oreon_sha256
%autosetup -n libutempter-%{version}-alt1

%build
%make_build -C libutempter libdir=%{_libdir} libexecdir=%{_libexecdir} CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"

%install
make -C libutempter install DESTDIR=%{buildroot} libdir=%{_libdir} libexecdir=%{_libexecdir} includedir=%{_includedir} mandir=%{_mandir}

%check
nm -D --defined-only libutempter/libutempter.so | grep -q ' T utempter_add_record@@'
nm -D --defined-only libutempter/libutempter.so | grep -q ' T utempter_remove_record@@'
nm -D --defined-only libutempter/libutempter.so | grep -q ' T utempter_remove_added_record@@'
nm -D --defined-only libutempter/libutempter.so | grep -q ' T utempter_set_helper@@'
readelf -d libutempter/libutempter.so | grep -q 'SONAME.*libutempter.so.0'
readelf -d libutempter/utempter | grep -q 'BIND_NOW\|FLAGS.*NOW'

%pre
getent group utempter >/dev/null || groupadd -r -g 35 utempter

%ldconfig_scriptlets

%files
%license libutempter/COPYING
%doc libutempter/README
%dir %attr(0755,root,root) %{_libexecdir}/utempter
%attr(2711,root,utempter) %{_libexecdir}/utempter/utempter
%{_libdir}/libutempter.so.0
%{_libdir}/libutempter.so.%{version}

%files devel
%{_includedir}/utempter.h
%{_libdir}/libutempter.so
%{_mandir}/man3/libutempter.3*
%{_mandir}/man3/utempter.3*
%{_mandir}/man3/utempter_add_record.3*
%{_mandir}/man3/utempter_remove_record.3*
%{_mandir}/man3/utempter_remove_added_record.3*
%{_mandir}/man3/utempter_set_helper.3*

%changelog
%autochangelog
