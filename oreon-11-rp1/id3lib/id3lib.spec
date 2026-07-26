%global source0_hash 2749cc3c0cd7280b299518b1ddf5a5bcfe2d1100614519b68702230e26c7d079

Summary:        Library for manipulating ID3v1 and ID3v2 tags
Name:           id3lib
Version:        3.8.3
Release:        62%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://id3lib.sourceforge.net/

Source0:        http://downloads.sourceforge.net/id3lib/%{name}-%{version}.tar.gz
Source1:        id3lib-no_date_footer.hml

Patch0:         id3lib-dox.patch
Patch1:         id3lib-3.8.3-autoreconf.patch
Patch2:         id3lib-3.8.3-io_helpers-163101.patch
Patch3:         https://patches.osdyson.org/patch/series/dl/id3lib3.8.3/3.8.3-15+dyson1/10-fix-compilation-with-cpp-headers.patch
Patch4:         https://patches.osdyson.org/patch/series/dl/id3lib3.8.3/3.8.3-15+dyson1/15-fix-headers-of-main-functions.patch
Patch5:         https://patches.osdyson.org/patch/series/dl/id3lib3.8.3/3.8.3-15+dyson1/40-deal-with-mkstemp.patch
Patch6:         https://patches.osdyson.org/patch/series/dl/id3lib3.8.3/3.8.3-15+dyson1/50-remove-outdated-check.patch
Patch7:         https://patches.osdyson.org/patch/series/dl/id3lib3.8.3/3.8.3-15+dyson1/20-create-manpages.patch
Patch8:         https://patches.osdyson.org/patch/series/dl/id3lib3.8.3/3.8.3-15+dyson1/60-id3lib-missing-nullpointer-check.patch
Patch9:         https://patches.osdyson.org/patch/series/dl/id3lib3.8.3/3.8.3-15+dyson1/60-fix_make_check.patch
Patch10:        https://patches.osdyson.org/patch/series/dl/id3lib3.8.3/3.8.3-15+dyson1/61-fix_vbr_stack_smash.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  zlib-devel
BuildRequires: make

%description
This package provides a software library for manipulating ID3v1 and ID3v2 tags.
It provides a convenient interface for software developers to include
standards-compliant ID3v1/2 tagging capabilities in their applications.
Features include identification of valid tags, automatic size conversions,
(re)synchronisation of tag frames, seamless tag (de)compression, and optional
padding facilities. Additionally, it can tell mp3 header info, like bitrate etc.

%package devel
Summary:        Development tools for the id3lib library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zlib-devel

%description devel
This package provides files needed to develop with the id3lib library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
for i in doc/id3v2.3.0.txt doc/id3v2.3.0.html ChangeLog THANKS; do
  iconv --from-code=ISO-8859-1 --to-code=UTF8 $i --output=tmp
  sed -i -e 's/\r//' tmp
  touch --reference=$i tmp
  mv tmp $i
done
sed -i -e 's|@DOX_DIR_HTML@|%{_docdir}/%{name}-devel/api|' doc/index.html.in
sed -i -e "s,HTML_FOOTER.*$,HTML_FOOTER = id3lib-no_date_footer.hml,g" doc/Doxyfile.in
cp %{SOURCE1} doc

%build
autoreconf --force --install
%configure --disable-dependency-tracking --disable-static
%make_build libid3_la_LIBADD=-lz

%install
%make_install
make docs
mkdir -p __doc/doc ; cp -p doc/*.{gif,jpg,png,html,txt,ico,css}  __doc/doc
rm -f $RPM_BUILD_ROOT%{_libdir}/libid3.la
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -pm 644 doc/man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%check
make check

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog HISTORY NEWS README THANKS TODO __doc/doc/
%license COPYING
%{_libdir}/libid3-3.8.so.*
%{_bindir}/id3convert
%{_bindir}/id3cp
%{_bindir}/id3info
%{_bindir}/id3tag
%{_mandir}/man1/id3convert.1*
%{_mandir}/man1/id3cp.1*
%{_mandir}/man1/id3info.1*
%{_mandir}/man1/id3tag.1*

%files devel
%doc doc/id3lib.css doc/api/
%{_includedir}/id3.h
%{_includedir}/id3/
%{_libdir}/libid3.so

%changelog
%autochangelog
