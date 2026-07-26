%global source0_hash af70bc2bcd7af7468495774fed9e3a2de434650119fbc3d3388c2bcf7e0acb01

# TODO: fixes scons to generate debug information
%global debug_package %{nil}

%define _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/xsunpinyin.conf
%define gitdate 20190805

Name:		sunpinyin
Version:	3.0.0
Release:	0.16.%{gitdate}git%{?dist}
Summary:	A statistical language model based Chinese input method engine
License:	LGPL-2.1-only OR CDDL-1.0
URL:		http://code.google.com/p/sunpinyin/
Source0:	%{name}-%{gitdate}.tar.xz
Source2:	http://downloads.sourceforge.net/project/open-gram/lm_sc.3gm.arpa-20140820.tar.bz2
Source3:	http://downloads.sourceforge.net/project/open-gram/dict.utf8-20131214.tar.bz2
Patch0: 	sunpinyin-use-python3.patch
Patch1: 	sunpinyin-fixes-scons.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:	sqlite-devel
BuildRequires:	gettext	
BuildRequires:	python3-scons
BuildRequires:	perl(Pod::Man)
BuildRequires:	python3-devel

%description
Sunpinyin is an input method engine for Simplified Chinese. It is an SLM based
IM engine, and features full sentence input.

SunPinyin has been ported to various input method platforms and operating 
systems. The 2.0 release currently supports iBus, XIM, and Mac OS X. 

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files that allows user
to write their own front-end for sunpinyin.

%package data
Summary:	Little-endian data files for %{name}
License:	CC-BY-SA-3.0
Obsoletes:	%{name}-data-le
Obsoletes:	%{name}-data-be

%description data
The %{name}-data package contains necessary lexicon data and its index data
files needed by the sunpinyin input methods.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{gitdate}

mkdir -p raw
cp %SOURCE2 raw
cp %SOURCE3 raw
pushd raw
tar xvf lm_sc.3gm.arpa-20140820.tar.bz2
tar xvf dict.utf8-20131214.tar.bz2
popd

%build
# export CFLAGS, CXXFLAGS, LDFLAGS, ...
%configure || :

scons %{?_smp_mflags} --prefix=%{_prefix} --libdir=%{_libdir} --datadir=%{_datadir}
export PATH=`pwd`/src:$PATH
pushd raw
ln -sf ../doc/SLM-inst.mk Makefile
make %{?_smp_mflags} VERBOSE=1
popd

%install
scons %{?_smp_mflags} --prefix=%{_prefix} --libdir=%{_libdir} --datadir=%{_datadir} install --install-sandbox=%{buildroot}
pushd raw
make install DESTDIR=%{buildroot} INSTALL="install -p"
popd

# additional %%doc files to include by path to avoid duplicates/conflicts
# see https://bugzilla.redhat.com/1001266
install -m0644 AUTHORS TODO %{buildroot}%{_docdir}/%{name}

%files
%license COPYING *.LICENSE
%{_libdir}/libsunpinyin*.so.*
%{_docdir}/%{name}/README
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/TODO

%files devel
%{_libdir}/libsunpinyin*.so
%{_libdir}/pkgconfig/sunpinyin*.pc
%{_includedir}/sunpinyin*

%files data
%{_datadir}/%{name}
%{_bindir}/*
%{_mandir}/man1/*.1.gz
%{_docdir}/%{name}/SLM-*.mk

%changelog
%autochangelog
