%global source0_hash 1f1a63767bc36e4758b06db0daae556733530fec543775082bbe477655c20db1
%define		mainver		0.996
%define		baserelease	11
Name:		mecab
Version:	%{mainver}
%if %{?betaver:0}%{!?betaver:1}
Release:        1%{?dist}
%else
Release:        1%{?dist}
%endif
Summary:        Yet Another Part-of-Speech and Morphological Analyzer
License:	BSD-3-Clause OR LGPL-2.1-or-later OR GPL-2.0-or-later
URL:		http://mecab.sourceforge.net/
Source0:        https://github.com/taku910/%{name}/archive/master/%{name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
MeCab is a open source morphological analyzer which uses 
CRF (Conditional Random Fields) as the estimation of parameters.

NOTE:
You have to install MeCab dictionary rpm to make use
of MeCab.

%package devel
Summary:	Libraries and Header files for Mecab
Requires:	%{name}%{?isa} = %{version}-%{release}
%description devel
This is the development package that provides header files and libraries
for MeCab.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n mecab-master
cd mecab

find . -name \*.cpp -print0 | xargs -0 %{__chmod} 0644

# compiler flags fix
%{__sed} -i.flags \
	-e '/-O3/s|CFLAGS=\"\(.*\)\"|CFLAGS=\${CFLAGS:-\1}|' \
	-e '/-O3/s|CXXFLAGS=\"\(.*\)\"|CXXFLAGS=\${CFLAGS:-\1}|' \
	-e '/MECAB_LIBS/s|-lstdc++||' \
	configure

# multilib change
%{__sed} -i.multilib \
	-e 's|@prefix@/lib/mecab|%{_libdir}/mecab|' \
	mecab-config.in mecabrc.in

%build

cd mecab
%configure
%{__sed} -i.rpath \
	-e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
	-e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
	libtool
%make_build
%install
cd mecab
%make_install
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/lib*.{a,la}
%{__rm} -f doc/Makefile*
%{__mkdir} -p $RPM_BUILD_ROOT%{_libdir}/mecab/dic/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LD_LIBRARY_PATH=$(pwd)/mecab/src/.libs
cd mecab/tests
%{__make} check || :
cd ..
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n mecab-devel -f %{oreon_filedir}/mecab-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.996-11
- Import
