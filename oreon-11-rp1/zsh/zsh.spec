%global source0_hash 9b8d1ecedd5b5e81fbf1918e876752a7dd948e05c1a0dba10ab863842d45acd5

Summary: Powerful interactive shell
Name: zsh
Version: 5.9
Release: 19%{?dist}
License: MIT-Modern-Variant AND ISC AND GPL-2.0-only
URL: http://zsh.sourceforge.net/
Source0: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1: zlogin.rhs
Source2: zlogout.rhs
Source3: zprofile.rhs
Source4: zshrc.rhs
Source5: zshenv.rhs
Source6: dotzshrc
Source7: dotzprofile

# do not use egrep in tests to make them pass again
Patch1: 0001-zsh-5.9-do-not-use-egrep-in-tests.patch
# Upstream commit ab4d62eb975a4c4c51dd35822665050e2ddc6918
Patch2: 0002-zsh-Use-int-main-in-test-c-codes.patch
# upstream commit a84fdd7c8f77935ecce99ff2b0bdba738821ed79
Patch3: 0003-zsh-fix-module-loading-problem-with-full-RELRO.patch
# upstream commit 1b421e4978440234fb73117c8505dad1ccc68d46
Patch4: 0004-zsh-enable-PCRE-locale-switching.patch
# upstream commit b62e911341c8ec7446378b477c47da4256053dc0 and 10bdbd8b5b0b43445aff23dcd412f25cf6aa328a
Patch5: 0005-zsh-port-to-pcre2.patch
# upstream commit ecd3f9c9506c7720dc6c0833dc5d5eb00e4459c4
Patch6: 0006-zsh-support-texinfo-7.0.patch
# upstream commit 4c89849c98172c951a9def3690e8647dae76308f
Patch7: 0007-zsh-configure-c99.patch
# upstream commit d3edf318306e37d2d96c4e4ea442d10207722e94
Patch8: 0008-zsh-deletefilelist-segfault.patch
# upstream commit b70b241cc5ca88cc129ff9ba14f8af2e889b90e6
Patch9: 0009-zsh-support-dnf5.patch
# upstream commit 071e325c826a89b792056c3faf0c400b8c0c5738
Patch10: 0010-zsh-fix-dnf5-completion-with-rpm-files.patch

BuildRequires: autoconf
BuildRequires: coreutils
BuildRequires: gawk
BuildRequires: gcc
BuildRequires: gdbm-devel
BuildRequires: glibc-langpack-ja
BuildRequires: libcap-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: pcre2-devel
BuildRequires: sed
BuildRequires: texi2html
BuildRequires: texinfo
Requires(post): grep
Requires(postun): coreutils grep

# the hostname package is not available on RHEL-6
%if 12 < 0%{?fedora} || 6 < 0%{?rhel}
BuildRequires: hostname
%else
# /bin and /usr/bin are separate directories on RHEL-6
%define _bindir /bin
%endif

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1
autoreconf -fiv

# enable parallel build
sed -e 's|^\.NOTPARALLEL|#.NOTPARALLEL|' -i 'Config/defs.mk.in'

%build
# make build of run-time loadable modules work again (#1535422)
%undefine _strict_symbol_defs_build

# avoid build failure in case we have working ypcat (#1687574)
export zsh_cv_sys_nis='no'

%configure \
    --enable-etcdir=%{_sysconfdir} \
    --with-tcsetpgrp \
    --enable-maildir-support \
    --enable-pcre

# prevent the build from failing while running in parallel
make -C Src headers
make -C Src -f Makemod zsh{path,xmod}s.h version.h

%make_build all html

%check
# avoid unnecessary failure of the test-suite in case ${RPS1} is set
unset RPS1

# run the test-suite
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

# This is just here to shut up rpmlint, and is very annoying.
# Note that we can't chmod everything as then rpmlint will complain about
# those without a she-bang line.
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.9-19
- Prepare for Oreon 11 (RP1)
