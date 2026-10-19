%global source1_hash e28e1ee5d29f88bd88bedf64bbbf033106eb28eb2efc9ffc4a0c3c92a80ac353
%global source0_hash a480198559733e9b3da999e90543ac6f888a2caa544d8d664c5a1f17e528e210
%global source2_key_fpr 6C37DC12121A5006BC1DB804DF6FD971306037D9
Summary:        A set of basic GNU tools commonly used in shell scripts
Name:    coreutils
Version: 9.12
Release:        1%{?dist}
License: GPL-3.0-or-later AND GFDL-1.3-no-invariants-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Url:     https://www.gnu.org/software/coreutils/
Source0:        https://mirrors.kernel.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        https://mirrors.kernel.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source2: coreutils-keyring.gpg
Source50:   supported_utils
Source105:  coreutils-colorls.sh
Source106:  coreutils-colorls.csh
%global __requires_exclude ^%{_bindir}/coreutils$
Patch100: coreutils-8.26-test-lock.patch
Patch101: coreutils-8.26-selinuxenable.patch
Patch102: coreutils-8.32-DIR_COLORS.patch
Patch103: coreutils-python3.patch
Patch104: coreutils-df-direct.patch
Patch800: coreutils-i18n.patch
Conflicts: filesystem < 3
Conflicts: coreutils-single
%ifarch %valgrind_arches
%endif
Requires: %{name}-common = %{version}-%{release}
Provides: coreutils-full = %{version}-%{release}
Provides: bundled(gnulib)
Obsoletes: %{name} < 8.24-100
# oreon:deps
BuildRequires:  acl
BuildRequires:  attr
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  diffutils
BuildRequires:  gcc
BuildRequires:  gdb
BuildRequires:  gettext-devel
BuildRequires:  glibc-all-langpacks
BuildRequires:  gmp-devel
BuildRequires:  gnupg2
BuildRequires:  hostname
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libcap-devel
BuildRequires:  libselinux-devel
BuildRequires:  libselinux-utils
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl(Expect)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Thread::Queue)
BuildRequires:  perl-interpreter
BuildRequires:  python3
BuildRequires:  python3-inotify
BuildRequires:  strace
BuildRequires:  systemd-devel
BuildRequires:  texinfo
BuildRequires:  tzdata
# /oreon:deps
%description
These are the GNU core utilities.  This package is the combination of
the old GNU fileutils, sh-utils, and textutils packages.

%package single
Summary:  coreutils multicall binary
Suggests: coreutils-common
Provides: coreutils = %{version}-%{release}
Provides: coreutils%{?_isa} = %{version}-%{release}
Provides: bundled(gnulib)
Conflicts: coreutils < 8.24-100
RemovePathPostfixes: .single
%description single
These are the GNU core utilities,
packaged as a single multicall binary.

%package common
Obsoletes: %{name} < 8.24-100
Requires: gnulib-l10n
Suggests: glibc-doc
Summary:  coreutils common optional components
%description common
Optional though recommended components,
including documentation and translations.

%prep

test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" 2>/dev/null | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; }
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

autoreconf -fiv

%build

export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fpic"
CFLAGS="$CFLAGS -Dlint"
export ac_cv_func_lchmod="no"
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
  ln -fv ../lib/parse-datetime.{c,y} .
  )
done
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
  mkdir -p $RPM_BUILD_ROOT/$subdir/%_sbindir
  mv $RPM_BUILD_ROOT/$subdir/{%_bindir,%_sbindir}/chroot
%endif
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
grep LC_TIME %name.lang | cut -d'/' -f1-6 | sed -e 's/) /) %%dir /g' >>%name.lang
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
%oreon_autofiles coreutils-single usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles coreutils-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n coreutils-single -f %{oreon_filedir}/coreutils-single.list
%files -n coreutils-common -f %{oreon_filedir}/coreutils-common.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.10-3
- Prepare for Oreon 11 (RP1)
