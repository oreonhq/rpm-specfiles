# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 36fa734374b44783582cec09bcd67822e2f992c779ec1624ab5596df078d2f81
%global source1_hash 34cf9126224befeacf9cbd654f75362bd2c0afd5c4e08672b7eafee81173592d
%global source2_hash b6333e75a019034d2869333adb56387a56bbec8ffb2056f7f3b721b2fc7acc2e
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary: Powerful interactive shell
Name: zsh
Version: 5.9.2
Release: %{autorelease}
License: MIT-Modern-Variant AND ISC AND GPL-2.0-only
URL: http://zsh.sourceforge.net/

Source0: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz.asc
Source2: zsh-keyring.asc

Source3: zlogin.rhs
Source4: zlogout.rhs
Source5: zprofile.rhs
Source6: zshrc.rhs
Source7: zshenv.rhs
Source8: dotzshrc
Source9: dotzprofile

Patch: zsh-memcpy-sigsegv-bracketed-paste.patch

BuildRequires: oreon-rpm-macros
BuildRequires: coreutils
BuildRequires: gawk
BuildRequires: clang
BuildRequires: gcc
BuildRequires: glibc-langpack-ja
BuildRequires: gnupg2
BuildRequires: groff
BuildRequires: hostname
BuildRequires: libcap-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: pcre2-devel
BuildRequires: sed
BuildRequires: texi2html
BuildRequires: texinfo
Requires(post): grep
Requires(postun): coreutils grep

Provides: /bin/zsh

%description
The zsh shell is a command interpreter usable as an interactive login
shell and as a shell script command processor.  Zsh resembles the ksh
shell (the Korn shell), but includes many enhancements.  Zsh supports
command line editing, built-in spelling correction, programmable
command completion, shell functions (with autoloading), a history
mechanism, and more.

%package html
Summary: Zsh shell manual in html format
BuildArch: noarch

%description html
The zsh shell is a command interpreter usable as an interactive login
shell and as a shell script command processor.  Zsh resembles the ksh
shell (the Korn shell), but includes many enhancements.  Zsh supports
command line editing, built-in spelling correction, programmable
command completion, shell functions (with autoloading), a history
mechanism, and more.

This package contains the Zsh manual in html format.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

sed -e 's|^\.NOTPARALLEL|#.NOTPARALLEL|' -i 'Config/defs.mk.in'

%build
%undefine _strict_symbol_defs_build

export zsh_cv_sys_nis='no'

%configure \
    --enable-etcdir=%{_sysconfdir} \
    --with-tcsetpgrp \
    --enable-maildir-support \
    --enable-pcre

make -C Src headers
make -C Src -f Makemod zsh{path,xmod}s.h version.h

%make_build all html

%check
unset RPS1

make check

%install
%make_install install.info \
  fndir=%{_datadir}/%{name}/%{version}/functions \
  sitefndir=%{_datadir}/%{name}/site-functions \
  scriptdir=%{_datadir}/%{name}/%{version}/scripts \
  sitescriptdir=%{_datadir}/%{name}/scripts \
  runhelpdir=%{_datadir}/%{name}/%{version}/help

rm -f $RPM_BUILD_ROOT%{_bindir}/zsh-%{version}
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}
for i in %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7}; do
    install -m 644 $i $RPM_BUILD_ROOT%{_sysconfdir}/"$(basename $i .rhs)"
done

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/skel
install -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/skel/.zshrc
install -m 644 %{SOURCE9} $RPM_BUILD_ROOT%{_sysconfdir}/skel/.zprofile

for i in checkmail harden run-help test-repo-git-rebase-{apply,merge} zcalc zkbd; do
    sed -i -e 's!/usr/local/bin/zsh!%{_bindir}/zsh!' \
    $RPM_BUILD_ROOT%{_datadir}/zsh/%{version}/functions/$i
    chmod +x $RPM_BUILD_ROOT%{_datadir}/zsh/%{version}/functions/$i
done

%post
if [ "$1" = 1 ]; then
  if [ ! -f %{_sysconfdir}/shells ] ; then
    echo "%{_bindir}/%{name}" > %{_sysconfdir}/shells
    echo "/bin/%{name}" >> %{_sysconfdir}/shells
  else
    grep -q "^%{_bindir}/%{name}$" %{_sysconfdir}/shells || echo "%{_bindir}/%{name}" >> %{_sysconfdir}/shells
    grep -q "^/bin/%{name}$" %{_sysconfdir}/shells || echo "/bin/%{name}" >> %{_sysconfdir}/shells
  fi
fi

%postun
if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ] ; then
  sed -i '\!^%{_bindir}/%{name}$!d' %{_sysconfdir}/shells
  sed -i '\!^/bin/%{name}$!d' %{_sysconfdir}/shells
fi

%files
%doc README LICENCE Etc/BUGS Etc/CONTRIBUTORS Etc/FAQ FEATURES MACHINES
%doc NEWS Etc/zsh-development-guide Etc/completion-style-guide
%attr(755,root,root) %{_bindir}/zsh
%{_mandir}/*/*
%{_infodir}/*
%{_datadir}/zsh
%{_libdir}/zsh
%config(noreplace) %{_sysconfdir}/skel/.z*
%config(noreplace) %{_sysconfdir}/z*

%files html
%doc Doc/*.html

%changelog
%autochangelog
