%global source0_hash none

%define		mainver		0.996
#%%define		betaver		pre3
%define		baserelease	11

# Note:
# mecab dictionary requires mecab-devel to rebuild it,
# and mecab requires mecab dictionary

Name:		mecab
Version:	%{mainver}
%if %{?betaver:0}%{!?betaver:1}
Release:	%{baserelease}%{?dist}
%else
Release:	0.%{baserelease}.%{betaver}%{?dist}
%endif
Summary:	Yet Another Part-of-Speech and Morphological Analyzer

# SPDX confirmed
License:	BSD-3-Clause OR LGPL-2.1-or-later OR GPL-2.0-or-later
URL:		http://mecab.sourceforge.net/
Source0:        http://mecab.googlecode.com/files/mecab-.tar.gz

BuildRequires:	make
BuildRequires:	gcc-c++

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}-%{mainver}%{?betaver}


mv doc/doxygen .
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
%configure
# remove rpath from libtool
%{__sed} -i.rpath \
	-e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
	-e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
	libtool

%make_build

%install
%make_install

%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/lib*.{a,la}
%{__rm} -f doc/Makefile*

# create directory
%{__mkdir} -p $RPM_BUILD_ROOT%{_libdir}/mecab/dic/

%check
# here enable rpath
export LD_LIBRARY_PATH=$(pwd)/src/.libs
cd tests
%{__make} check || :
cd ..

%ldconfig_scriptlets

%files
%doc AUTHORS
%license BSD COPYING GPL LGPL
%doc doc/ example/
%{_mandir}/man1/%{name}.1*

%config(noreplace) %{_sysconfdir}/mecabrc
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%{_libdir}/lib%{name}.so.2*
# several dictionaries can install data files
# into the following directory.
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/dic/

%files devel
%doc doxygen/
%{_bindir}/%{name}-config
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.996-11
- Import
