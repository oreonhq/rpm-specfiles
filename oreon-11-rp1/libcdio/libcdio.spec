%global source0_hash 8e6a305f81e45a78b41ce696d34497cc208d97075469d7304c11a6d44bf006ac
Name: libcdio
Version: 2.4.0
Release:        1%{?dist}
Summary:        CD-ROM input and control library
License: GPL-3.0-or-later AND BSD-2-Clause AND LGPL-2.1-or-later
URL: http://www.gnu.org/software/libcdio/
Source0:        https://github.com/libcdio/libcdio/releases/download/%{version}/libcdio-%{version}.tar.bz2
Source2: libcdio-no_date_footer.hml
Source3: cdio_config.h
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
case `uname -i` in
	i386 | x86_64 | ppc | ppc64 | s390 | s390x | sparc | sparc64 )
		mv $RPM_BUILD_ROOT%{_includedir}/cdio/cdio_config.h $RPM_BUILD_ROOT%{_includedir}/cdio/cdio_config_`uname -i`.h
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{__sed} -i -e "s,testiso9660\$(EXEEXT),,g" \
	    -e "s,testisocd\$(EXEEXT),,g" \
	    -e "s,check_paranoia.sh check_opts.sh, check_opts.sh,g" \
	    test/Makefile
make check
%files -f %{oreon_filedir}/main.list
%files -n libcdio-devel -f %{oreon_filedir}/libcdio-devel.list

%changelog

%autochangelog
