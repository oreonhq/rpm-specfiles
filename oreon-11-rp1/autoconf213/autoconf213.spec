%global source0_hash none

Summary:    A GNU tool for automatically configuring source code
Name:       autoconf213
Version:    2.13
Release:    60%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
URL:        http://www.gnu.org/software/autoconf/
Source:        https://ftp.gnu.org/gnu/autoconf/autoconf-%{version}.tar.gz
Patch0:     autoconf-2.12-race.patch
Patch1:     autoconf-2.13-mawk.patch
Patch2:     autoconf-2.13-notmp.patch
Patch3:     autoconf-2.13-c++exit.patch
Patch4:     autoconf-2.13-headers.patch
Patch6:     autoconf-2.13-exit.patch
Patch7:     autoconf-2.13-wait3test.patch
Patch8:     autoconf-2.13-make-defs-62361.patch
Patch9:     autoconf-2.13-versioning.patch
Patch10:    autoconf213-destdir.patch
Patch11:    autoconf213-info.patch
Patch12:    autoconf213-testsuite.patch
Requires:   gawk, m4 >= 1.1, coreutils
Buildrequires:   texinfo, m4 >= 1.1, perl, gawk, dejagnu, flex
BuildRequires: make
BuildArch:  noarch

%description
GNU's Autoconf is a tool for configuring source code and Makefiles.
Using Autoconf, programmers can create portable and configurable
packages, since the person building the package is allowed to specify
various configuration options.

You should install Autoconf if you are developing software and you
would like to use it to create shell scripts that will configure your
source code packages. If you are installing Autoconf, you will also
need to install the GNU m4 package.

Note that the Autoconf package is not required for the end-user who
may be configuring software with an Autoconf-generated script;
Autoconf is only required for the generation of the scripts, not their
use.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n autoconf-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
mv autoconf.texi autoconf213.texi
rm -f autoconf.info

%build
%configure --program-suffix=-%{version}
make

%install
rm -rf ${RPM_BUILD_ROOT}
#makeinstall
make install DESTDIR=$RPM_BUILD_ROOT

rm ${RPM_BUILD_ROOT}/%{_bindir}/autoscan-%{version}

# We don't want to include the standards.info stuff in the package,
# because it comes from binutils...
rm -f ${RPM_BUILD_ROOT}%{_infodir}/standards*

%check
# autoconf expects a compiler that supports C89-only features.  The
# test suite necessarily ignores the CC variable, so put wrapper
# scripts in front of PATH.  Rewrite the c89 wrapper script so that it
# invokes /usr/bin/gcc, to avoid an infinite loop.
mkdir compiler-overrides
PATH="`pwd`/compiler-overrides:$PATH"
sed 's,^exec gcc,exec %{_bindir}/gcc,' < %{_bindir}/c89 \
  > compiler-overrides/c89
chmod 755 compiler-overrides/c89
ln -s c89 compiler-overrides/cc
ln -s c89 compiler-overrides/gcc
ls -l compiler-overrides/
make check

%files
%{_bindir}/*
%{_infodir}/*.info*
%{_datadir}/autoconf-%{version}/
%doc AUTHORS COPYING NEWS README TODO

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.13-60
- Import
