%global source0_hash a802f3f4e7983f33c47f0548fb82111bbfde97fa722ae78b4d8c0c58ac8ecdcf

# disable offensive fortunes by default
%bcond_with offensive
# there are no actual tests
%bcond_with tests

%global CookieDir %{_datadir}/games/fortune
%global _cmake_generator "Unix Makefiles"

# needed to support out-of-source builds on EPEL8
%undefine __cmake_in_source_build

Name:		fortune-mod
Version:	3.26.0
Release:	1%{?dist}
Summary:	A program which will display a fortune

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/shlomif/fortune-mod
Source0:	https://www.shlomifish.org/open-source/projects/fortune-mod/arcs/fortune-mod-%{version}.tar.xz
Source1:	kernelnewbies-fortunes.tar.gz
Source2:	bofh-excuses.tar.bz2
# originally at http://www.aboleo.net/software/misc/fortune-tao.tar.gz
Source3:	fortune-tao.tar.gz
Source4:	http://www.splitbrain.org/Fortunes/hitchhiker/fortune-hitchhiker.tgz
# originally at http://www.dibona.com/opensources/osfortune.tar.gz
Source5:	osfortune.tar.gz
Source6:	http://humorix.org/downloads/humorixfortunes-1.4.tar.gz
Patch1:     fortune-mod-3.26.0--fix-build.patch

BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Find::Object)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Path::Tiny)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::RunValgrind)
BuildRequires:	perl(Test::Trap)
BuildRequires:	perl(autodie)
BuildRequires:	perl(lib)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl-Test-Harness
BuildRequires:	perl-interpreter
BuildRequires:	perl-libs
BuildRequires:	pkgconfig(librinutils)
BuildRequires:	recode-devel
BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	valgrind
BuildRequires:	valgrind-devel
BuildRequires:	chrpath

%description
Fortune-mod contains the ever-popular fortune program, which will
display quotes or witticisms. Fun-loving system administrators can add
fortune to users' .login files, so that the users get their dose of
wisdom each time they log in.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%patch -P 1 -p 1

%build
%cmake -DCOOKIEDIR=%{CookieDir} -DLOCALDIR=%{CookieDir} -DNO_OFFENSIVE=TRUE
%cmake_build

%install
%cmake_install

tar zxvf %{SOURCE1} -C $RPM_BUILD_ROOT%{CookieDir}
%if %{without offensive}
rm -f $RPM_BUILD_ROOT%{CookieDir}/men-women*
%endif

mv $RPM_BUILD_ROOT/usr/games/fortune $RPM_BUILD_ROOT%{_bindir}
rm -f $RPM_BUILD_ROOT%{_bindir}/rot
# this isn't debian
rm -f $RPM_BUILD_ROOT%{CookieDir}/debian*
rm -f $RPM_BUILD_ROOT%{CookieDir}/off/debian*

# Using bzcat for portability because tar keeps changing the switch
bzcat %{SOURCE2} | tar xvf - -C $RPM_BUILD_ROOT%{CookieDir}

# Non-standard source files, need to move things around
tar zxvf %{SOURCE3} -C $RPM_BUILD_ROOT%{CookieDir}/ fortune-tao/tao*
mv $RPM_BUILD_ROOT%{CookieDir}/fortune-tao/* $RPM_BUILD_ROOT%{CookieDir}/
rmdir $RPM_BUILD_ROOT%{CookieDir}/fortune-tao

tar zxvf %{SOURCE4} -C $RPM_BUILD_ROOT%{CookieDir}/ fortune-hitchhiker/hitch*
mv $RPM_BUILD_ROOT%{CookieDir}/fortune-hitchhiker/* $RPM_BUILD_ROOT%{CookieDir}/
rmdir $RPM_BUILD_ROOT%{CookieDir}/fortune-hitchhiker

tar zxvf %{SOURCE5} -C $RPM_BUILD_ROOT%{CookieDir}/
chmod 644 $RPM_BUILD_ROOT%{CookieDir}/osfortune*

tar zxvf %{SOURCE6} -C $RPM_BUILD_ROOT%{CookieDir}/ humorixfortunes-1.4/*
mv $RPM_BUILD_ROOT%{CookieDir}/humorixfortunes-1.4/* $RPM_BUILD_ROOT%{CookieDir}/
rmdir $RPM_BUILD_ROOT%{CookieDir}/humorixfortunes-1.4

# Recreate random access files for the added fortune files.
strfile="`find . -type f -name strfile -executable -print | head -1`"
for i in \
    kernelnewbies bofh-excuses tao hitchhiker \
    osfortune humorix-misc humorix-stories \
; do "$strfile" $RPM_BUILD_ROOT%{CookieDir}/$i ; done

# Fix for https://fedoraproject.org/wiki/Changes/Broken_RPATH_will_fail_rpmbuild
#ERROR   0001: file '/usr/bin/strfile' contains a standard runpath '/usr/lib64' in [/usr/lib64]
#ERROR   0001: file '/usr/bin/unstr' contains a standard runpath '/usr/lib64' in [/usr/lib64]
#ERROR   0001: file '/usr/bin/fortune' contains a standard runpath '/usr/lib64' in [/usr/lib64]
chrpath -d %{buildroot}%{_bindir}/strfile
chrpath -d %{buildroot}%{_bindir}/unstr
chrpath -d %{buildroot}%{_bindir}/fortune

%check
%__rm -f tests/t/trailing-space*.t
%__rm -f tests/t/valgrind*.t
# The fortune-mod tests suite does not use CTest - only "[build-cmd] check"
# ctest
%cmake_build --target check

%files
%license COPYING.txt
%doc README ChangeLog TODO
%{_bindir}/fortune
%{_bindir}/strfile
%{_bindir}/unstr
%{CookieDir}
%{_mandir}/man*/*

%changelog
%autochangelog
