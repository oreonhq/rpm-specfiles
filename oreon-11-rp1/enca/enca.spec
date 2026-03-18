Name: enca
Summary: Character set analyzer and detector
Version: 1.19
Release: 19%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
Source: http://dl.cihar.com/enca/enca-%{version}.tar.xz
URL: http://cihar.com/software/enca

BuildRequires: gcc
BuildRequires: make


%description
Enca is an Extremely Naive Charset Analyser. It detects character set and
encoding of text files and can also convert them to other encodings using
either a built-in converter or external libraries and tools like libiconv,
librecode, or cstocs.

Currently, it has support for Belarussian, Bulgarian, Croatian, Czech,
Estonian, Latvian, Lithuanian, Polish, Russian, Slovak, Slovene, Ukrainian,
Chinese and some multibyte encodings (mostly variants of Unicode)
independent on the language.

This package also contains shared Enca library other programs can make use of.

Install %{name} if you need to cope with text files of dubious origin
and unknown encoding and convert them to some reasonable encoding.


%package devel
Summary: Header files and libraries for %{name} charset analyzer
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
The %{name}-devel package contains the header files for writing
programs using the Extremely Naive Charset Analyser library,
and its API documentation.

Install %{name}-devel if you are going to create applications using the Enca
library.


%prep
%setup -q


%build

%configure \
	--disable-dependency-tracking \
	--disable-rpath \
	--without-librecode \
	--disable-external \
	--disable-static \
	--disable-gtk-doc

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install

make install DESTDIR=$RPM_BUILD_ROOT HTML_DIR=/tmp/html

rm -rf $RPM_BUILD_ROOT/tmp/html
rm -rf $RPM_BUILD_ROOT/%{_libexecdir}
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la


%check
make check LD_LIBRARY_PATH=$RPM_BUILD_ROOT/%{_libdir}


%ldconfig_scriptlets


%files
%{_bindir}/*
%{_libdir}/libenca.so.*
%{_mandir}/*/*
%doc AUTHORS COPYING FAQ README THANKS TODO

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%doc DEVELOP.md


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.19-19
- Prepare for Oreon 11 (RP1)
