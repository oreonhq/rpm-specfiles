# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 8e6a305f81e45a78b41ce696d34497cc208d97075469d7304c11a6d44bf006ac
%global source2_hash 09b8cec866f439f326dfb058ce8a1efcbab6ebf5a9699828a5f291edd86e0989
%global source3_hash e4997d5f11882ffe1901724cb1617f0c2e8ac7df8295cd12c85fd4d5244f0984
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libcdio
Version: 2.4.0
Release:        %{autorelease}
Summary: CD-ROM input and control library
License: GPL-3.0-or-later AND BSD-2-Clause AND LGPL-2.1-or-later
URL: http://www.gnu.org/software/libcdio/
Source0: https://github.com/libcdio/libcdio/releases/download/%{version}/libcdio-%{version}.tar.bz2
Source2: libcdio-no_date_footer.hml
Source3: cdio_config.h

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: pkgconfig
BuildRequires: doxygen
BuildRequires: ncurses-devel
BuildRequires: help2man
BuildRequires: gettext-devel
BuildRequires: chrpath
BuildRequires: make

%description
This library provides an interface for CD-ROM access. It can be used
by applications that need OS- and device-independent access to CD-ROM
devices.

%package devel
Summary: Header files and libraries for %{name}
License: GPL-3.0-or-later AND BSD-2-Clause AND LGPL-2.1-or-later AND GFDL-1.2-or-later
Requires: %{name} = %{version}-%{release}

%description devel
This package contains header files and libraries for %{name}.

%prep
%oreon_sha256
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
%autosetup

iconv -f ISO88591 -t utf-8 -o THANKS.utf8 THANKS && mv THANKS.utf8 THANKS

%build
%ifarch %{ix86}
export CPPFLAGS="$CPPFLAGS -D_LARGEFILE64_SOURCE"
%endif
%configure \
	--disable-vcd-info \
	--disable-dependency-tracking \
	--disable-cddb \
	--disable-static \
	--disable-rpath
%make_build

sed -i -e "s,%{version} .*$,%{version}\\\",g" include/cdio/version.h

cd doc/doxygen
sed -i -e "s,HTML_FOOTER.*$,HTML_FOOTER = libcdio-no_date_footer.hml,g; \
		s,EXCLUDE .*$,EXCLUDE = ../../include/cdio/cdio_config.h,g;" Doxyfile
cp %{SOURCE2} .
./run_doxygen

%install
%make_install

case %{_arch} in
	i386 | x86_64 | ppc | ppc64 | s390 | s390x | sparc | sparc64 )
		mv $RPM_BUILD_ROOT%{_includedir}/cdio/cdio_config.h $RPM_BUILD_ROOT%{_includedir}/cdio/cdio_config_%{_arch}.h
		install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_includedir}/cdio
		;;
	*)
		;;
esac

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

rm -rf examples
mkdir -p examples/C++
cp -a example/{*.c,README} examples
cp -a example/C++/{*.cpp,README} examples/C++

for i in cd-info iso-read iso-info cd-read cd-drive; do
	sed -i -e 's, version.*linux-gnu,,g' $RPM_BUILD_ROOT%{_mandir}/man1/$i.1
	sed -i -e 's,lt-,,g;s,LT-,,g' $RPM_BUILD_ROOT%{_mandir}/man1/$i.1
	touch -r src/$i.help2man $RPM_BUILD_ROOT%{_mandir}/man1/$i.1
done

chrpath --delete $RPM_BUILD_ROOT%{_bindir}/*
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/*.so.*

%check
%{__sed} -i -e "s,testiso9660\$(EXEEXT),,g" \
	    -e "s,testisocd\$(EXEEXT),,g" \
	    -e "s,check_paranoia.sh check_opts.sh, check_opts.sh,g" \
	    test/Makefile
make check

%files
%license COPYING
%doc AUTHORS NEWS.md README.md README-libcdio.md THANKS TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_infodir}/*
%{_mandir}/man1/*

%files devel
%doc doc/doxygen/html examples
%{_includedir}/cdio
%{_includedir}/cdio++
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
