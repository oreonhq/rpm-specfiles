%global source3_hash af70bc2bcd7af7468495774fed9e3a2de434650119fbc3d3388c2bcf7e0acb01
%global source2_hash 751bab7c55ea93a2cedfb0fbb7eb09f67d4da9c2c55496e5f31eb8580f1d1e2f
%global source0_hash af70bc2bcd7af7468495774fed9e3a2de434650119fbc3d3388c2bcf7e0acb01
%global debug_package %{nil}
%define _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/xsunpinyin.conf
%define gitdate 20190805
Name:		sunpinyin
Version:	3.0.0
Release:        1%{?dist}
Summary:        A statistical language model based Chinese input method engine
License:	LGPL-2.1-only OR CDDL-1.0
URL:		http://code.google.com/p/sunpinyin/
Source0:        %{name}-%{gitdate}.tar.xz
Source2:	http://downloads.sourceforge.net/project/open-gram/lm_sc.3gm.arpa-20140820.tar.bz2
Source3:	http://downloads.sourceforge.net/project/open-gram/dict.utf8-20131214.tar.bz2
Patch0: 	sunpinyin-use-python3.patch
Patch1: 	sunpinyin-fixes-scons.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  perl(Pod::Man)
BuildRequires:  python3-devel
BuildRequires:  python3-scons
BuildRequires:  sqlite-devel
# /oreon:deps
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
install -m0644 AUTHORS TODO %{buildroot}%{_docdir}/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n sunpinyin-devel -f %{oreon_filedir}/sunpinyin-devel.list
%files -n sunpinyin-data -f %{oreon_filedir}/sunpinyin-data.list

%changelog

%autochangelog
