%global source0_hash fe7e1e68c259e69454a43d7415991a6f4b86775d25f22806fcd076a21b9e9c3f

%global commit 4a3650d88725e8fda6387fbdbaa0ed98cdca76ce
# %%global tag 11 #disabled due to unarragment release line after mass rebuild.
%global githead %(printf %%.7s %commit)
%global gitdate 20260302

# epel7 compatibility mode
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

# Module Sample: (Alpha Version)
# %% global moduleX %%name-of-module
#
# %% package -n %%{moduleX}
# Summary: %%{summary_of_moduleX}
# License: %%{license_of_moduleX}
#
# %% description -n %%{moduleX}
# %%description-of-module
#
# %% prep
# ./gnulib-tool --create-testdir --dir=build-%%{moduleX} %%{moduleX}
#
# %% build
# pushd build-%%{moduleX}
# %% configure --prefix=%%_prefix
# make %%{?_smp_mflags}
# popd
#
# %% install
# pushd build-%%{moduleX}
# %%make_install
# popd
# help2man -N --no-discard-stderr %%{buildroot}%%{_bindir}/%%{moduleX} | gzip -9c > %%{buildroot}%%{_mandir}/man1/%%{moduleX}.1.gz
#
# %% files -n %%{moduleX}
# %%{_bindir}/%%{moduleX}
# %%{_mandir}/*/%%{moduleX}.*

##################################
# LIST OF SINGLE MODULE PACKAGES :
# 1.git-merge-changelog
##################################

%global module1 git-merge-changelog
%global common_desc \
The GNU portability library is a macro system and C declarations and \
definitions for commonly-used API elements and abstracted system behaviors. \
It can be used to improve portability and other functionality in your programs.

# without modules1
%global debug_package %{nil}

Name:     gnulib
Version:  0
Release:  57.%{gitdate}git%{githead}%{?dist}
Summary:  GNU Portability Library
License:  LicenseRef-Fedora-Public-Domain AND BSD-3-Clause AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-or-later
URL:      https://www.gnu.org/software/gnulib
Source0:  https://git.savannah.gnu.org/gitweb/?p=gnulib.git;a=snapshot;h=%{githead};sf=tgz;name=gnulib-%{githead}.tar.gz#/gnulib-%{githead}.tar.gz
Source1:  https://salsa.debian.org/debian/gnulib/-/raw/debian/latest/debian/manpages/check-module.1
Source2:  https://salsa.debian.org/debian/gnulib/-/raw/debian/latest/debian/manpages/gnulib-tool.1

#Patch0:   test-u8-strstr-alarm.diff

BuildRequires:		perl-generators
BuildRequires:		texinfo

# Java JDK dropped in i686
# https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs
%ifnarch %{ix86}
BuildRequires:		java-devel
Requires:           %{name}-javaversion
%endif

# For building Modules, all gnulib requires must be found, Modules BRs:
BuildRequires:		gettext-devel
BuildRequires:		bison
BuildRequires:		gperf
BuildRequires:		libtool
BuildRequires:		help2man
BuildRequires:		git
BuildRequires:      make
BuildRequires:      ncurses-devel
BuildRequires:      python3-devel >= 3.7

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
# MODULE #1 - git-merge-changelog
#pushd build-%{module1}
#configure --prefix=%_prefix
#make_build
#popd
#tests build
#cp -p lib/timevar.def build-tests/gllib #Fix timevar.def not found
pushd build-tests

# FIX ERROR CAN'T DETECT AC_LIB_PREPARE_PREFIX
mkdir m4
autoreconf -vfi

%configure --prefix=%_prefix
%make_build
popd

# Java JDK dropped in i686
# https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs
%ifnarch %{ix86}
# Rebuild removed java class
javac -d lib lib/javaversion.java
%endif

# This part is done with the original path

%make_build MODULES.html

sed -i -r 's#HREF="(lib|m4|modules)#HREF="%{_datadir}/%{name}/\1#g' MODULES.html
sed -i "/^[ ]*gnulib_dir=/s#\`[^\`]*\`#%{_datadir}/%{name}#" gnulib-tool
sed -i "/^[ ]*gnulib_dir=/s#\`[^\`]*\`#%{_datadir}/%{name}#" gnulib-tool.sh
sed -i "/^[ ]*gnulib_dir=/s#\`[^\`]*\`#%{_datadir}/%{name}#" gnulib-tool.py

# This part is done with the target path
%make_build info
%make_build html
# Removing unused files
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

# Python Gnulib installing
mkdir -p %{buildroot}%{python3_sitelib}
cp -rp py%{name} %{buildroot}%{python3_sitelib}

# Module installing
#make_install -C build-%{module1}
#help2man -N --no-discard-stderr %{buildroot}%{_bindir}/%{module1} | gzip -9c > %{buildroot}%{_mandir}/man1/%{module1}.1.gz

#-------------------------------------------------------------------------

%package docs
Summary: Documentation for %{name} modules
License: GFDL-1.3-or-later
Requires:			%{name}-devel = %{version}-%{release}
BuildArch: noarch

%description docs
%common_desc

This package contains documentation for %{name}.

%files docs
%{_datadir}/info/gnulib.info.gz
%{_pkgdocdir}/gnulib.html
%{_pkgdocdir}/MODULES.html
# license text is included directly in info and html files.

#-------------------------------------------------------------------------

# Java JDK dropped in i686
# https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs
%ifnarch %{ix86}
%package javaversion
Summary: javaversion built unit
License: GPL-3.0-or-later
Requires:			%{name}-devel = %{version}-%{release}
%description javaversion
This package contains javaversion built unit of %{name}.

%files javaversion
%{_datadir}/%{name}/lib/javaversion.class
%endif

#-------------------------------------------------------------------------

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

%files devel
%{_datadir}/%{name}/
%{_bindir}/gnulib-tool
%{_bindir}/check-module
%{_mandir}/*/check-module.*
%{_mandir}/*/gnulib-tool.*
%{_pkgdocdir}/
%exclude %{_pkgdocdir}/MODULES.html
%exclude %{_pkgdocdir}/gnulib.html
# Java JDK dropped in i686
# https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs
%ifnarch %{ix86}
# Remove built java class, goes to javaversion sub-package
%exclude %{_datadir}/%{name}/lib/javaversion.class
%endif

#-------------------------------------------------------------------------
%package -n python3-%{name}
Summary: Python Implement of Gnulib
BuildArch: noarch
Requires: gnulib = %{version}-%{release}
Provides: gnulib-python = %{version}-%{release}
Requires: python3

%description -n python3-%{name}
Python Implement of Gnulib

%files -n python3-%{name}
%{python3_sitelib}/py%{name}

#-------------------------------------------------------------------------

# MODULE #1 - git-merge-changelog
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
%changelog
%autochangelog
