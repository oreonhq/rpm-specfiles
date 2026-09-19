%global source0_hash 4aa759b2e055ef3c3fbeb9e92f7f0aacc1fd1f8602fdd2f122719793ee14414c

%define		mainver	1.3
%define		tarballver	20110227
%define		minorver	date%{tarballver}
%define		prerelease	1

%define		baserelease	22

%define		uprel		%(echo %{?minorver} | %{__sed} -e 's|^--*||' | %{__sed} -e 's|-|_|g' )
%define		rel		%{?prerelease:0.}%{baserelease}%{?minorver:.%uprel}

%define		skkdicdir	%{_datadir}/skk
%define		skkcoding	EUC-JP

Name:		cmigemo
Version:	%{mainver}
Release:	%{rel}%{?dist}
Summary:	C interface of Ruby/Migemo Japanese incremental search tool

# doc/LICENSE_MIT.txt	MIT
# SKK-JISYO.L (from skkdic)	GPL-2.0-or-later
# SPDX confirmed
License:	MIT AND GPL-2.0-or-later
URL:		http://www.kaoriya.net/software/cmigemo
#Source0:	http://www.kaoriya.net/dist/var/%{name}-%{mainver}%{?minorver}.tar.bz2
Source0:	http://cmigemo.googlecode.com/files/cmigemo-default-src-%{tarballver}.zip
Patch0:		cmigemo-20110227-ignore-random-string.patch
Patch1:		cmigemo-1.3c-MIT-dont-escape.patch
Patch2:		cmigemo-20110227-compile.patch
Patch3:		cmigemo-20110227-keep-regex-with-brackets.patch

BuildRequires:  gcc
BuildRequires:  skkdic
BuildRequires:  /usr/bin/perl
BuildRequires:  make

%description
C/Migemo is a C interface of Ruby/Migemo, a Japanese incremental search tool
by Romaji.

%package	devel
Summary:	Development files for cmigemo

Requires:	%{name}%{?isa} = %{version}-%{release}

%description	devel
This package  contains libraries and header files for
developing applications that use cmigemo.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T %{name}-%{version} -a 0
cd cmigemo-default-src/
%patch -P0 -p1 -b .random
%patch -P1 -p1 -b .escape
%patch -P2 -p1 -b .build
%patch -P3 -p1 -b .regex

# Change default command for configure
%{__sed} -i.command \
	-e 's|curl|true|' \
	-e 's|nkf|true|' \
	-e 's|install\"|install -p"|' \
	configure

# use iconv instead of nkf
%{__sed} -i.nkf \
	-e 's|^\(FILTER_CP932[ \t][ \t]*=\).*|\1 iconv -f %{skkcoding} -t SJIS|' \
	-e 's|^\(FILTER_EUCJP[ \t][ \t]*=\).*|\1 iconv -f SJIS -t EUC-JP|' \
	compile/config.mk.in

# make cmigemo original data dir
%{__sed} -i.dir \
	-e 's|/share/migemo|/share/cmigemo|' \
	compile/config.mk.in config.mk

# ( don't create unnecessary backup file for document...)
%{__sed} -i \
	-e 's|/usr/local/share/migemo|%{_datadir}/cmigemo|' \
	doc/README_j.txt tools/migemo.vim

# remove unneeded rpath
%{__sed} -i.rpath \
	-e 's|^\(LDFLAGS_MIGEMO[ \t][ \t]*=\).*|\1 |' \
	compile/Make_gcc.mak

# 64 bits libdir
%{__sed} -i.bits \
	-e 's|\$(prefix)/lib|$(prefix)/%{_lib}|' \
	config.mk compile/config.mk.in compile/config_default.mk

# Also install zen2han
%{__sed} -i.han \
	-e 's|^\(.*\)\(han2zen\)\(.*\)$|\1\2\3\n\1zen2han\3|' \
	compile/unix.mak

%{__chmod} 0644 tools/*

%build
cd cmigemo-default-src/
%{__chmod} u+x configure
%configure

# parallel make unsafe
%{__make} gcc CC="gcc $RPM_OPT_FLAGS"

# This is under GPL-2.0-or-later
%{__cat} %{skkdicdir}/SKK-JISYO.L | gzip > dict/SKK-JISYO.L.gz
%{__make} gcc-dict
( cd dict ; %{__make} utf-8 )

%install
pushd cmigemo-default-src/

%{__make} gcc-install prefix=$RPM_BUILD_ROOT%{_prefix}

# remove unneeded document
%{__rm} -rf $RPM_BUILD_ROOT%{_prefix}/doc/

popd

# make documentation directory
%{__rm} -rf doc_install
%{__rm} -rf licenses
%{__rm} -rf tools

pushd cmigemo-default-src/
cp -a tools ..

%{__rm} -rf doc_install
%{__mkdir} doc_install
%{__mkdir} licenses
cd doc
for f in *txt ; do \
	iconv -f SJIS -t UTF-8 $f > ../doc_install/$f && \
		touch -r $f ../doc_install/$f || \
		%{__cp} -p $f ../doc_install/$f
done
cp -p LICENSE_MIT.txt ../licenses/
cd ..

mv doc_install ..
mv licenses ..
popd

%ldconfig_scriptlets

%files
%defattr(-,root,root,-)
%license licenses/*
%doc doc_install/*
%doc tools/

%{_bindir}/%{name}
%{_libdir}/libmigemo.so.1{,.*}

%{_datadir}/cmigemo/

%files	devel
%defattr(-,root,root,-)
%{_includedir}/migemo.h
%{_libdir}/libmigemo.so

%changelog
%autochangelog
