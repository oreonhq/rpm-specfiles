%global source0_hash 186892539dedd661276014d71318c8c8f97ecb1250a86625256abd4defbf0d0c

Name: libcdio-paranoia
Version: 10.2+2.0.2
Release: 6%{?dist}
Summary: CD paranoia on top of libcdio
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: http://www.gnu.org/software/libcdio/
Source0: https://github.com/libcdio/libcdio-paranoia/releases/download/release-%{version}/libcdio-paranoia-%{version}.tar.bz2
# Fix for https://bugzilla.redhat.com/show_bug.cgi?id=2334834
# Based on https://github.com/libcdio/libcdio-paranoia/pull/52.patch
Patch0: 2334834.patch
BuildRequires: gcc
BuildRequires: pkgconfig
BuildRequires: gettext-devel
BuildRequires: chrpath
BuildRequires: libcdio-devel
BuildRequires: make

Requires:       libcdio%{?_isa}

%description
This CDDA reader distribution ('libcdio-cdparanoia') reads audio from the
CDROM directly as data, with no analog step between, and writes the
data to a file or pipe as .wav, .aifc or as raw 16 bit linear PCM.

Split off from libcdio to allow more flexible licensing and to be compatible
with cdparanoia-III-10.2's license. And also, libcdio is just too large.

%package devel
Summary: Header files and libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains header files and libraries for %{name}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%patch -P 0 -p 1

# fix pkgconfig files
sed -i -e 's,-I${includedir},-I${includedir}/cdio,g' libcdio_paranoia.pc.in
sed -i -e 's,-I${includedir},-I${includedir}/cdio,g' libcdio_cdda.pc.in

f=doc/ja/cd-paranoia.1.in
iconv -f euc-jp -t utf-8 -o $f.utf8 $f && mv $f.utf8 $f
iconv -f ISO88591 -t utf-8 -o THANKS.utf8 THANKS && mv THANKS.utf8 THANKS

%build
%configure \
	--disable-dependency-tracking \
	--disable-static \
	--disable-rpath
%make_build

%install
%make_install

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

# copy include files to an additional directory for backward compatibility
# this is where most software still expects those files
cp -a $RPM_BUILD_ROOT%{_includedir}/cdio/paranoia/*.h $RPM_BUILD_ROOT%{_includedir}/cdio/

# remove rpath
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/*
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/*.so.*

%check
%make_build check

%files
%license COPYING
%doc AUTHORS NEWS.md README.md THANKS
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1/*


%files devel
%doc doc/overlapdef.txt
%{_includedir}/cdio/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 10.2+2.0.2-6
- Prepare for Oreon 11 (RP1)
