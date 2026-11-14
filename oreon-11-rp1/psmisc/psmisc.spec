# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 58c55d9c1402474065adae669511c191de374b0871eec781239ab400b907c327

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           psmisc
Version:        23.7
Release:        1%{?dist}
Summary:        Utilities for managing processes on your system
License:        GPL-2.0-or-later
URL:            https://gitlab.com/psmisc/psmisc
Source0:        https://sourceforge.net/projects/%{name}/files/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}-%{version}.tar.xz.asc
Source2:        gpgkey-5D3DF0F538B327C0AA7A77A2022166C0FF3C84E3.gpg

BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  gettext
BuildRequires:  libselinux-devel
BuildRequires:  ncurses-devel

%if "%{_sbindir}" == "%{_bindir}"
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/fuser
%endif

%description
The psmisc package contains utilities for managing processes on your
system: pstree, killall, fuser and pslog. The pstree command displays
a tree structure of all of the running processes on your system. The
killall command sends a specified signal (SIGTERM if nothing is specified)
to processes identified by name. The fuser command identifies the PIDs
of processes that are using specified files or filesystems. The pslog
command shows the path of log files owned by a given process.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}

%autosetup -p1

%build
%configure --prefix=%{_prefix} --enable-selinux
%make_build

%install
%make_install

%if "%{_sbindir}" != "%{_bindir}"
mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/fuser %{buildroot}%{_sbindir}
%endif

%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README
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
%ifarch %{ix86} x86_64 ppc %{power64} %{arm} aarch64 mipsel loongarch64
%{_bindir}/peekfd
%{_mandir}/man1/peekfd.1*
%else
%exclude %{_mandir}/man1/peekfd.1*
%endif

%changelog
%autochangelog
