%global source2_hash 458355936509c94e575720b326efdac985c7a4dc2a78c16207afea94643bd9eb
%global source1_hash a75bbae0309bc843e1ca258d644bc59b1270b71b117fa0107b9288be69b6814c
%global source0_hash 395edc32d94bffa442fb3b222893a4eff9e3b613b7285e2d377724dddf73db51
%global commit 4a3650d88725e8fda6387fbdbaa0ed98cdca76ce
%global githead %(printf %%.7s %commit)
%global gitdate 20260302
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global module1 git-merge-changelog
%global common_desc \
The GNU portability library is a macro system and C declarations and \
definitions for commonly-used API elements and abstracted system behaviors. \
It can be used to improve portability and other functionality in your programs.
%global debug_package %{nil}
Name:     gnulib
Version:  0
Release:        1%{?dist}
Summary:        GNU Portability Library
License:  LicenseRef-Fedora-Public-Domain AND BSD-3-Clause AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-or-later
URL:      https://www.gnu.org/software/gnulib
Source0:        https://git.savannah.gnu.org/gitweb/?p=%{name}.git;a=snapshot;h=4a365%{version}d;sf=tgz;name=%{name}-4a365%{version}d.tar.gz#/%{name}-4a365%{version}d.tar.gz
Source1:  https://salsa.debian.org/debian/gnulib/-/raw/debian/latest/debian/manpages/check-module.1
Source2:  https://salsa.debian.org/debian/gnulib/-/raw/debian/latest/debian/manpages/gnulib-tool.1
%ifnarch %{ix86}
Requires:           %{name}-javaversion
%endif
# oreon:deps
BuildRequires:  bison
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  gperf
BuildRequires:  help2man
BuildRequires:  java-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl-generators
BuildRequires:  python3-devel
BuildRequires:  texinfo
# /oreon:deps
%description
%common_desc

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{githead} -p1 -Sgit

#modules not to be tested by direct import
toRemove="lib-symbol-visibility havelib .*-obsolete localcharset gettext-h gettext alloca-opt alloca "

list="$(./gnulib-tool --list)"
for item in $toRemove
do
   list="$(echo $list| sed "s:\b$item\b::g")"
done

#is necessary to avoid some modules to test prep pass
./gnulib-tool --create-testdir --with-tests --with-obsolete --avoid=alloca --avoid=lib-symbol-visibility --avoid=havelib --dir=build-tests $list

rm lib/javaversion.class
# MODULE #1 - git-merge-changelog

# The 'gnulib' source package has built and shipped the binary package
# 'git-merge-changelog' but now upstream split this off into a proper
# package and there is a release of it:
# https://lists.gnu.org/archive/html/info-gnu/2025-12/msg00009.html
# https://linux.debian.devel.narkive.com/LawcvirC/bug-1124418-itp-git-merge-changelog-git-merge-driver-for-gnu-changelog-files
# https://tracker.debian.org/pkg/git-merge-changelog

#gnulib-tool --create-testdir --dir=build-%{module1} %{module1}

%build

pushd build-tests
mkdir m4
autoreconf -vfi
%configure --prefix=%_prefix
%make_build
popd
%ifnarch %{ix86}
javac -d lib lib/javaversion.java
%endif
%make_build MODULES.html
sed -i -r 's#HREF="(lib|m4|modules)#HREF="%{_datadir}/%{name}/\1#g' MODULES.html
sed -i "/^[ ]*gnulib_dir=/s#\`[^\`]*\`#%{_datadir}/%{name}#" gnulib-tool
sed -i "/^[ ]*gnulib_dir=/s#\`[^\`]*\`#%{_datadir}/%{name}#" gnulib-tool.sh
sed -i "/^[ ]*gnulib_dir=/s#\`[^\`]*\`#%{_datadir}/%{name}#" gnulib-tool.py
%make_build info
%make_build html
rm -f */.cvsignore
rm -f */.gitignore
rm -f */.gitattributes
rm -f lib/.cppi-disable
rm -f lib/uniname/gen-uninames.lisp
%check

make -C build-tests check VERBOSE=1
%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/info
mkdir -p %{buildroot}%{_pkgdocdir}
mkdir -p %{buildroot}%{_mandir}/man1
cp -p check-module %{buildroot}%{_bindir}
cp -p gnulib-tool gnulib-tool.sh gnulib-tool.py %{buildroot}%{_datadir}/%{name}/
ln -sr %{buildroot}%{_datadir}/%{name}/gnulib-tool %{buildroot}%{_bindir}
cp -rp build-aux lib m4 modules config tests %{buildroot}%{_datadir}/%{name}/
cp -p .gnulib-tool.py %{buildroot}%{_datadir}/%{name}/
mkdir -p %{buildroot}%{_datadir}/%{name}/doc
cp -arv doc/relocatable.texi %{buildroot}%{_datadir}/%{name}/doc
cp -p doc/gnulib.info %{buildroot}%{_datadir}/info/
cp -p doc/gnulib.html MODULES.html NEWS COPYING ChangeLog HACKING users.txt doc/COPYING* %{buildroot}%{_pkgdocdir}/
cp -p %{SOURCE1} %{SOURCE2} %{buildroot}%{_mandir}/man1
cp -rp top %{buildroot}%{_datadir}/%{name}/
mkdir -p %{buildroot}%{python3_sitelib}
cp -rp py%{name} %{buildroot}%{python3_sitelib}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%package docs
Summary: Documentation for %{name} modules
License: GFDL-1.3-or-later
Requires:			%{name}-devel = %{version}-%{release}
BuildArch: noarch
%description docs
%common_desc

This package contains documentation for %{name}.

%package javaversion
Summary: javaversion built unit
License: GPL-3.0-or-later
Requires:			%{name}-devel = %{version}-%{release}
%description javaversion
This package contains javaversion built unit of %{name}.

%package devel
Summary: Devel files of %{name}
BuildArch: noarch
Provides: gnulib = %{version}-%{release}
Requires: gettext-devel
Requires: bison
Requires: coreutils
Requires: gperf
Requires: libtool
Requires: make
Requires: texinfo
Requires: diffutils
Requires: patch
Requires: m4
Requires: grep
Requires: autoconf
Requires: automake
Requires: gawk
Requires: gcc
Requires: gnulib-python
%description devel
%common_desc

This package contains devel files of %{name}.

%package -n python3-%{name}
Summary: Python Implement of Gnulib
BuildArch: noarch
Requires: gnulib = %{version}-%{release}
Provides: gnulib-python = %{version}-%{release}
Requires: python3
%description -n python3-%{name}
Python Implement of Gnulib

%package -n %{module1}
Summary: Git merge driver for ChangeLog files
License: GPL-2.0-or-later
%description -n %{module1}
Git Merge Changelog is a git merge driver for changelogs that combines
parallel additions to the changelog without generating merge conflicts.
It can be enabled for specific files by setting appropriate git attributes.

#%%files -n %%{module1}
#%%{_bindir}/%%{module1}
#%%{_mandir}/*/%%{module1}.*
#%%license doc/COPYINGv2

#-------------------------------------------------------------------------
%files -f %{oreon_filedir}/main.list
%files -n gnulib-docs -f %{oreon_filedir}/gnulib-docs.list
%files -n gnulib-javaversion -f %{oreon_filedir}/gnulib-javaversion.list
%files -n gnulib-devel -f %{oreon_filedir}/gnulib-devel.list
%files -n python3-gnulib -f %{oreon_filedir}/python3-gnulib.list
%files -n git-merge-changelog -f %{oreon_filedir}/git-merge-changelog.list

%changelog

%autochangelog
