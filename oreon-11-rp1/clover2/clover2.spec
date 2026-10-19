%global source0_hash 645d54b0da3a30eb3b463226da7de339dff8d4ab47e17ede6845aac083df363b
%global	mainver	11.0.0
%global	gitdate	20211017
%global	gitcommit	1e6a0256612c8f8b6b1d42bd75778b15c8c5ff67
%global	shortcommit	%(c=%{gitcommit}; echo ${c:0:7})
%global	tarballdate	20221008
%global	tarballtime	2308
%global	toolchain	clang
Name:			clover2
Version:		%{mainver}
Release:        15%{?dist}
Summary:        Yet another compiler language
License:		GPL-2.0-only
URL:			https://github.com/ab25cq/clover2/wiki
Source0:        %{name}-%{tarballdate}T%{tarballtime}.tar.gz
Source1:		create-clover-git-bare-tarball.sh
Patch1:		clover2-11.0.0-0001-port-to-pcre2.patch
Patch2:		clover2-11.0.0-0002-block-TCGETA-usage-on-ppc64le.patch
Patch3:		clover2-11.0.0-0003-Fix-Wincompatible-pointer-types-warning.patch
Requires:		%{name}-libs%{?_isa} = %{version}-%{release}
ExcludeArch:	armv7hl
# oreon:deps
BuildRequires:  /usr/bin/time
BuildRequires:  clang
BuildRequires:  gc-devel
BuildRequires:  git
BuildRequires:  make
BuildRequires:  pcre2-devel
BuildRequires:  readline-devel
# /oreon:deps
%description
clover2 is a Ruby-like compiler language with static type like Java.
This language consists of compilers and virtual machines like Java and C#.
In order to compile, type checking can be done at compile time. In addition,
it is designed to be able to use an easy-to-use library like Ruby.
Regular expressions, lambda, closure etc are first class objects.

%package	libs
Summary:	Library package needed for %{name}
%description	libs
This package contains libraries needed for clover2.

%package	devel
Summary:	Development files for %{name}
Requires:		%{name}-libs%{?_isa} = %{version}-%{release}
%description	devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T -a 0
git clone ./clover2.git
cd clover2

git config user.name "%{name} Fedora maintainer"
git config user.email "%{name}-owner@fedoraproject.org"

git checkout -b %{version}-fedora %{gitcommit}

cp -a [A-Z]* ..

# honor cflags, toolchain
git rm --cached configure~
git commit -m "untrack configure~" -a

sed -i.cflags configure.in configure \
	-e '\@CFLAGS=.*-DPREFIX=@s|-DPREFIX=|%build_cflags -DPREFIX=|' \
	-e 's|-O3|-O2|' \
	-e's|^CC=gcc|CC=%{toolchain}|' \
	%{nil}
# honor libdir
sed -i.lib configure.in configure -e 's|/lib |/%{_lib} |'
sed -i.lib Makefile.in -e 's|/lib$|/%{_lib}|'

git commit -m "Apply Fedora specific configuration" -a
cat %PATCH1 | git am
cat %PATCH2 | git am
cat %PATCH3 | git am

%build

cd clover2
%configure \
	--with-interpreter \
	%{nil}
%make_build -j1
%install
cd clover2
make install \
	DESTDIR=%{buildroot}%{_prefix} \
	INSTALL="install -p" \
	%{nil}
chmod 0644 %{buildroot}%{_mandir}/man1/%{name}.1*
cd ..
rm -rf installed-doc
mv %{buildroot}%{_docdir}/%{name}/ installed-doc
%oreon_autofiles clover2-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles clover2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

LANG=C.utf8 make -C clover2 test
%files -f %{oreon_filedir}/main.list
%files -n clover2-libs -f %{oreon_filedir}/clover2-libs.list
%files -n clover2-devel -f %{oreon_filedir}/clover2-devel.list

%changelog

%autochangelog
