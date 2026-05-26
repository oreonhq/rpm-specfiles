# RHEL 10 is dropping Qt5
%bcond gui %[%{undefined rhel} || 0%{?rhel} < 10]

Name:           ttfautohint
Version:        1.8.4
Release:        12%{?dist}
Summary:        Automated hinting utility for TrueType fonts
License:        FTL or GPL-2.0-only
URL:            http://www.freetype.org/ttfautohint
Source0:        http://download.savannah.gnu.org/releases/freetype/%{name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 8a876117fa6ebfd2ffe1b3682a9a98c802c0f47189f57d3db4b99774206832e1
%global source0_file ttfautohint-1.8.4.tar.gz
# oreon url source checksums end

BuildRequires:  autoconf automake libtool
BuildRequires:  make
BuildRequires:  gcc gcc-c++
BuildRequires:  freetype-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  pkgconfig
%if %{with gui}
BuildRequires:  qt5-qtbase-devel
%endif
Provides:       bundled(gnulib)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
This is a utility which takes a TrueType font as the input, removes its 
bytecode instructions (if any), and returns a new font where all glyphs 
are bytecode hinted using the information given by FreeType's autohinting 
module. The idea is to provide the excellent quality of the autohinter on 
platforms which don't use FreeType.

%if %{with gui}
%package        gui
Summary:        GUI for %{name} based on Qt
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    gui
%{name} is a utility which takes a TrueType font as the input, removes its 
bytecode instructions (if any), and returns a new font where all glyphs 
are bytecode hinted using the information given by FreeType's autohinting 
module. The idea is to provide the excellent quality of the autohinter on 
platforms which don't use FreeType.

This is a GUI of %{name} based on Qt.
%endif

%package        libs
Summary:        Library for %{name}

%description    libs
lib%{name} is a library which takes a TrueType font as the input, removes its 
bytecode instructions (if any), and returns a new font where all glyphs 
are bytecode hinted using the information given by FreeType's autohinting 
module. The idea is to provide the excellent quality of the autohinter on 
platforms which don't use FreeType.

%package        devel
Summary:        Development files for %{name}-libs
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
lib%{name} is a library which takes a TrueType font as the input, removes its 
bytecode instructions (if any), and returns a new font where all glyphs 
are bytecode hinted using the information given by FreeType's autohinting 
module. The idea is to provide the excellent quality of the autohinter on 
platforms which don't use FreeType.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/ttfautohint-1.8.4.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8a876117fa6ebfd2ffe1b3682a9a98c802c0f47189f57d3db4b99774206832e1" || { echo "oreon: Source0 SHA256 mismatch for ttfautohint-1.8.4.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup
# drop this hack if --with-doc is enabled
echo %{version} > VERSION
sed -i -e '/dist_man_MANS/d' -e 's/manpages/dist_man_MANS/' frontend/local.mk
autoreconf -fiv

%build
# doc: requires help2man, ImageMagick, inkscape, pandoc, xelatex, xvfb-run
%configure \
  --disable-silent-rules --disable-static --without-doc \
  %{!?with_gui:--without-qt}
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%ldconfig_scriptlets libs

%files
%doc AUTHORS NEWS README THANKS TODO *.TXT
%doc doc/img doc/ttfautohint.{html,pdf,txt}
%license COPYING
%{_bindir}/ttfautohint
%{_mandir}/man1/ttfautohint.1*

%if %{with gui}
%files gui
%license COPYING
%{_pkgdocdir}/
%{_bindir}/ttfautohintGUI
%{_mandir}/man1/ttfautohintGUI.1*
%endif

%files libs
%license COPYING
%{_libdir}/libttfautohint.so.1*

%files devel
%license COPYING
%{_includedir}/ttfautohint*.h
%{_libdir}/libttfautohint.so
%{_libdir}/pkgconfig/ttfautohint.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.4-12
- Prepare for Oreon 11 (RP1)
