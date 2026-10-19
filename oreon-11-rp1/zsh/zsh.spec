%global source0_hash 36fa734374b44783582cec09bcd67822e2f992c779ec1624ab5596df078d2f81
Summary:        Powerful interactive shell
Name: zsh
Version: 5.9.2
Release:        1%{?dist}
License: MIT-Modern-Variant AND ISC AND GPL-2.0-only
URL: http://zsh.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1: zlogin.rhs
Source2: zlogout.rhs
Source3: zprofile.rhs
Source4: zshrc.rhs
Source5: zshenv.rhs
Source6: dotzshrc
Source7: dotzprofile
Requires(post): grep
Requires(postun): coreutils grep
%define _bindir /bin
Provides: /bin/zsh
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  coreutils
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gdbm-devel
BuildRequires:  glibc-langpack-ja
BuildRequires:  libcap-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pcre2-devel
BuildRequires:  sed
BuildRequires:  texi2html
BuildRequires:  texinfo
# /oreon:deps
%description
The zsh shell is a command interpreter usable as an interactive login
shell and as a shell script command processor.  Zsh resembles the ksh
shell (the Korn shell), but includes many enhancements.  Zsh supports
command line editing, built-in spelling correction, programmable
command completion, shell functions (with autoloading), a history
mechanism, and more.

%package html
Summary: Zsh shell manual in html format
BuildArch:	noarch
%description html
The zsh shell is a command interpreter usable as an interactive login
shell and as a shell script command processor.  Zsh resembles the ksh
shell (the Korn shell), but includes many enhancements.  Zsh supports
command line editing, built-in spelling correction, programmable
command completion, shell functions (with autoloading), a history
mechanism, and more.

This package contains the Zsh manual in html format.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
autoreconf -fiv

# enable parallel build
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
for i in %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5}; do
    install -m 644 $i $RPM_BUILD_ROOT%{_sysconfdir}/"$(basename $i .rhs)"
done
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/skel
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/skel/.zshrc
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/skel/.zprofile
for i in checkmail harden run-help test-repo-git-rebase-{apply,merge} zcalc zkbd; do
    sed -i -e 's!/usr/local/bin/zsh!%{_bindir}/zsh!' \
    $RPM_BUILD_ROOT%{_datadir}/zsh/%{version}/functions/$i
    chmod +x $RPM_BUILD_ROOT%{_datadir}/zsh/%{version}/functions/$i
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n zsh-html -f %{oreon_filedir}/zsh-html.list

%changelog

%autochangelog
