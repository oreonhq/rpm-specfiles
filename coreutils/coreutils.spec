Summary: A set of basic GNU tools commonly used in shell scripts
Name:    coreutils
Version: 9.10
Release: 3%{?dist}
# some used parts of gnulib are under various variants of LGPL
License: GPL-3.0-or-later AND GFDL-1.3-no-invariants-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Url:     https://www.gnu.org/software/coreutils/
Source0: https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1: https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
# From https://savannah.gnu.org/project/release-gpgkeys.php?group=coreutils&download=1
# which is linked as project keyring on https://savannah.gnu.org/projects/coreutils
Source2: coreutils-keyring.gpg
Source50:   supported_utils
Source105:  coreutils-colorls.sh
Source106:  coreutils-colorls.csh

# do not make coreutils-single depend on /usr/bin/coreutils
%global __requires_exclude ^%{_bindir}/coreutils$

# disable the test-lock gnulib test prone to deadlock
Patch100: coreutils-8.26-test-lock.patch

# require_selinux_(): use selinuxenabled(8) if available
Patch101: coreutils-8.26-selinuxenable.patch

# downstream changes to default DIR_COLORS
Patch102: coreutils-8.32-DIR_COLORS.patch

# use python3 in tests
Patch103: coreutils-python3.patch

# df --direct
Patch104: coreutils-df-direct.patch

# tests: fix "Hangup" termination of non-interactive runs
# https://github.com/coreutils/coreutils/commit/8fab3c6d30d812cd681e51221bae27930f62615a
Patch200: coreutils-9.10-fix-tests-hangup.patch

# fold: fix output truncation with 0xFF bytes in input
# https://github.com/coreutils/coreutils/commit/a85e9182b1d173c26205dada54133cd9e9174fc1
Patch201: coreutils-9.10-fold-xFF-truncation.patch

# (sb) lin18nux/lsb compliance - multibyte functionality patch
Patch800: coreutils-i18n.patch

Conflicts: filesystem < 3

# To avoid clobbering installs
Conflicts: coreutils-single

BuildRequires: attr
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: gettext-devel
BuildRequires: gmp-devel
BuildRequires: hostname
BuildRequires: libacl-devel
BuildRequires: libattr-devel
BuildRequires: libcap-devel
BuildRequires: libselinux-devel
BuildRequires: libselinux-utils
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: strace
BuildRequires: systemd-devel
BuildRequires: texinfo

# For gpg verification of source tarball
BuildRequires: gnupg2

# test-only dependencies
BuildRequires: acl
BuildRequires: gdb
BuildRequires: perl-interpreter
BuildRequires: perl(FileHandle)
BuildRequires: python3
BuildRequires: tzdata
%ifarch %valgrind_arches
BuildRequires: valgrind
%endif

%if 0%{?fedora}
BuildRequires: perl(Expect)
BuildRequires: python3-inotify
%endif

%if 23 < 0%{?fedora} || 7 < 0%{?rhel}
# needed by i18n test-cases
BuildRequires: glibc-all-langpacks
%endif

Requires: %{name}-common = %{version}-%{release}

Provides: coreutils-full = %{version}-%{release}
Provides: bundled(gnulib)
Obsoletes: %{name} < 8.24-100

%description
These are the GNU core utilities.  This package is the combination of
the old GNU fileutils, sh-utils, and textutils packages.

%package single
Summary:  coreutils multicall binary
Suggests: coreutils-common
Provides: coreutils = %{version}-%{release}
Provides: coreutils%{?_isa} = %{version}-%{release}
Provides: bundled(gnulib)
# To avoid clobbering installs
Conflicts: coreutils < 8.24-100
# Note RPM doesn't support separate buildroots for %files
# http://rpm.org/ticket/874 so use RemovePathPostfixes
# (new in rpm 4.13) to support separate file sets.
RemovePathPostfixes: .single
%description single
These are the GNU core utilities,
packaged as a single multicall binary.


%package common
# yum obsoleting rules explained at:
# https://bugzilla.redhat.com/show_bug.cgi?id=1107973#c7
Obsoletes: %{name} < 8.24-100

# Gnulib translations are maintained seprately since coreutils 9.6 (#2393892)
Requires: gnulib-l10n

# info doc refers to "Specifying the Time Zone" from glibc-doc (#959597)
Suggests: glibc-doc

Summary:  coreutils common optional components
%description common
Optional though recommended components,
including documentation and translations.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -N

# will be regenerated in the build directories
rm -f src/fs.h

# will be further modified by coreutils-8.32-DIR_COLORS.patch
sed src/dircolors.hin \
        -e 's| 00;36$| 01;36|' \
        > DIR_COLORS
sed src/dircolors.hin \
        -e 's| 01;31$| 00;31|' \
        -e 's| 01;35$| 00;35|' \
        > DIR_COLORS.lightbgcolor

# git add DIR_COLORS{,.lightbgcolor}
# git commit -m "clone DIR_COLORS before patching"

# apply all patches
%autopatch -p1

(echo ">>> Fixing permissions on tests") 2>/dev/null
find tests -name '*.sh' -perm 0644 -print -exec chmod 0755 '{}' '+'
(echo "<<< done") 2>/dev/null

# FIXME: Force a newer gettext version to workaround `autoreconf -i` errors
# with coreutils 9.6 and bundled gettext 0.19.2 from gettext-common-devel.
sed -i "s/0.19.2/$(rpm -q --queryformat '%%{VERSION}\n' gettext-devel)/" bootstrap.conf configure.ac

%if 0%{?rhel}
# Temporarily disable test-getaddrinfo from gnulib because it malfunctions in
# the environment used to bootstrap RHEL.
sed -i 's/TESTS += test-getaddrinfo//' gnulib-tests/gnulib.mk
%endif

autoreconf -fiv

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fpic"

# Upstream suggests to build with -Dlint for static analyzers:
# https://lists.gnu.org/archive/html/coreutils/2018-06/msg00110.html
# ... and even for production binary RPMs:
# https://lists.gnu.org/archive/html/bug-gnulib/2020-05/msg00130.html
# There is currently no measurable performance drop or other known downside.
CFLAGS="$CFLAGS -Dlint"

# make mknod work again in chroot without /proc being mounted (#1811038)
export ac_cv_func_lchmod="no"

# needed for out-of-tree build
%global _configure ../configure

%{expand:%%global optflags %{optflags} -D_GNU_SOURCE=1}
for type in separate single; do
  mkdir -p $type && \
  (cd $type || exit $?
  if test $type = 'single'; then
    config_single='--enable-single-binary'
    config_single="$config_single --without-openssl"  # smaller/slower sha*sum
    config_single="$config_single --without-libgmp"   # expr/factor machine ints
  else
    config_single='--with-openssl'  # faster sha*sum
  fi
  %configure $config_single \
             --cache-file=../config.cache \
             --enable-install-program=arch \
             --enable-no-install-program=kill,uptime \
             --enable-systemd \
             --enable-manual-url \
             --with-tty-group \
             DEFAULT_POSIX2_VERSION=200112 alternative=199209 || :
  %make_build all V=1

  # make sure that parse-datetime.{c,y} ends up in debuginfo (#1555079)
  ln -fv ../lib/parse-datetime.{c,y} .
  )
done

# Get the list of supported utilities
cp %SOURCE50 .

%check
for type in separate single; do
  test $type = 'single' && subdirs='SUBDIRS=.' # Only check gnulib once
  (cd $type && make check %{?_smp_mflags} $subdirs)
done

%install
for type in separate single; do
  install=install
  if test $type = 'single'; then
    subdir=%{_libexecdir}/%{name}; install=install-exec
  fi
  (cd $type && make DESTDIR=$RPM_BUILD_ROOT/$subdir $install)

%if "%{_sbindir}" != "%{_bindir}"
  # chroot was in /usr/sbin :
  mkdir -p $RPM_BUILD_ROOT/$subdir/%_sbindir
  mv $RPM_BUILD_ROOT/$subdir/{%_bindir,%_sbindir}/chroot
%endif

  # Move multicall variants to *.single.
  # RemovePathPostfixes will strip that later.
  if test $type = 'single'; then
    for dir in %{_bindir} \
%if "%{_sbindir}" != "%{_bindir}"
%{_sbindir} \
%endif
%{_libexecdir}/%{name}; do
      for bin in $RPM_BUILD_ROOT/%{_libexecdir}/%{name}/$dir/*; do
        basebin=$(basename $bin)
        mv $bin $RPM_BUILD_ROOT/$dir/$basebin.single
      done
    done
  fi
done

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -p -c -m644 DIR_COLORS{,.lightbgcolor} $RPM_BUILD_ROOT%{_sysconfdir}
install -p -c -m644 %SOURCE105 $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/colorls.sh
install -p -c -m644 %SOURCE106 $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/colorls.csh

%find_lang %name
# Add the %%lang(xyz) ownership for the LC_TIME dirs as well...
grep LC_TIME %name.lang | cut -d'/' -f1-6 | sed -e 's/) /) %%dir /g' >>%name.lang

# (sb) Deal with Installed (but unpackaged) file(s) found
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%files -f supported_utils
%exclude %{_bindir}/*.single
%dir %{_libexecdir}/coreutils
%{_libexecdir}/coreutils/*.so

%files single
%{_bindir}/*.single
%if "%{_sbindir}" != "%{_bindir}"
%{_sbindir}/chroot.single
%endif
%dir %{_libexecdir}/coreutils
%{_libexecdir}/coreutils/*.so.single
# duplicate the license because coreutils-common does not need to be installed
%{!?_licensedir:%global license %%doc}
%license COPYING

%files common -f %{name}.lang
%config(noreplace) %{_sysconfdir}/DIR_COLORS*
%config(noreplace) %{_sysconfdir}/profile.d/*
%{_infodir}/coreutils*
%{_mandir}/man*/*
# The following go to /usr/share/doc/coreutils-common
%doc ABOUT-NLS NEWS README THANKS TODO
%license COPYING

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.10-3
- Prepare for Oreon 11 (RP1)
