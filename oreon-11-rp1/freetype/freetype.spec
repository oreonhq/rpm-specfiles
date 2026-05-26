# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 32427e8c471ac095853212a37aef816c60b42052d4d9e48230bab3bdf2936ccc
%global source1_sha256 719142a897aef4e5b47689ba4394934285045f45f6aade07c65160e1813839f2
%global source2_sha256 06aaf46e1cabca75856193e83f01f260a0d3dfc9954081db5b4ed1467b4385a0
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })} \
%{?source1_sha256:%(test -z "%{source1_sha256}" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_sha256}" || { echo "oreon: Source1 sha256 mismatch" >&2; exit 1; }; })} \
%{?source2_sha256:%(test -z "%{source2_sha256}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_sha256}" || { echo "oreon: Source2 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%{!?with_xfree86:%define with_xfree86 1}
%bcond_with bootstrap

Name: freetype
Version: 2.14.1
Release: 3%{?dist}
Summary: A free and portable font rendering engine
License: (FTL OR GPL-2.0-or-later) AND BSD-3-Clause AND MIT AND MIT-Modern-Variant AND LicenseRef-Fedora-Public-Domain AND Zlib
URL: http://www.freetype.org
Source:  http://download.savannah.gnu.org/releases/freetype/freetype-%{version}.tar.xz
Source1: http://download.savannah.gnu.org/releases/freetype/freetype-doc-%{version}.tar.xz
Source2: http://download.savannah.gnu.org/releases/freetype/ft2demos-%{version}.tar.xz
Source3: ftconfig.h

# Enable subpixel rendering (ClearType)
Patch0:  freetype-2.3.0-enable-spr.patch
# Enable otvalid and gxvalid modules
Patch1:  freetype-2.2.1-enable-valid.patch

Patch3:  freetype-2.6.5-libtool.patch

Patch4:  freetype-2.8-multilib.patch

Patch5:  freetype-2.10.0-internal-outline.patch

BuildRequires: gcc
BuildRequires: libX11-devel
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: brotli-devel
BuildRequires: make
%if %{without bootstrap}
BuildRequires: harfbuzz-devel
%endif

Provides: %{name}-bytecode
Provides: %{name}-subpixel
Obsoletes: freetype-freeworld < 2.9.1-2

%description
The FreeType engine is a free and portable font rendering
engine, developed to provide advanced font support for a variety of
platforms and environments. FreeType is a library which can open and
manages font files as well as efficiently load, hint and render
individual glyphs. FreeType is not a font server or a complete
text-rendering library.


%package demos
Summary: A collection of FreeType demos
Requires: %{name} = %{version}-%{release}

%description demos
The FreeType engine is a free and portable font rendering
engine, developed to provide advanced font support for a variety of
platforms and environments.  The demos package includes a set of useful
small utilities showing various capabilities of the FreeType library.


%package devel
Summary: FreeType development libraries and header files
Requires: %{name} = %{version}-%{release}
Requires: pkgconf%{?_isa}

%description devel
The freetype-devel package includes the static libraries and header files
for the FreeType font rendering engine.

Install freetype-devel if you want to develop programs which will use
FreeType.


%prep
%oreon_verify_sources
%setup -q -b 1 -a 2

%patch 0  -p1 -b .enable-spr
%patch 1  -p1 -b .enable-valid

%patch 3 -p1 -b .libtool
%patch 4 -p1 -b .multilib
%patch 5 -p1 -b .internal-outline

%build

%configure --disable-static \
           --with-zlib=yes \
           --with-bzip2=yes \
           --with-png=yes \
           --enable-freetype-config \
%if %{without bootstrap}
           --with-harfbuzz=yes \
%else
           --with-harfbuzz=no \
%endif
           --with-brotli=yes
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' builds/unix/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' builds/unix/libtool
%make_build

%if %{with_xfree86}
# Build demos
pushd ft2demos-%{version}
make TOP_DIR=".."
popd
%endif

%install

%make_install gnulocaledir=$RPM_BUILD_ROOT%{_datadir}/locale

{
  for ftdemo in ftbench ftdump ftlint ftvalid ttdebug ; do
      builds/unix/libtool --mode=install install -m 755 ft2demos-%{version}/bin/$ftdemo $RPM_BUILD_ROOT/%{_bindir}
  done
}
%if %{with_xfree86}
{
  for ftdemo in ftdiff ftgamma ftgrid ftmulti ftsdf ftstring ftview ; do
      builds/unix/libtool --mode=install install -m 755 ft2demos-%{version}/bin/$ftdemo $RPM_BUILD_ROOT/%{_bindir}
  done
}
%endif

# man pages for freetype-demos
{
  for ftdemo in ftbench ftdump ftlint ftvalid ttdebug ; do
      builds/unix/libtool --mode=install install -m 644 ft2demos-%{version}/man/${ftdemo}.1 $RPM_BUILD_ROOT/%{_mandir}/man1
  done
}
%if %{with_xfree86}
{
  for ftdemo in ftdiff ftgamma ftgrid ftmulti ftsdf ftstring ftview ; do
      builds/unix/libtool --mode=install install -m 644 ft2demos-%{version}/man/${ftdemo}.1 $RPM_BUILD_ROOT/%{_mandir}/man1
  done
}
%endif

# fix multilib issues
%define wordsize %{__isa_bits}

mv $RPM_BUILD_ROOT%{_includedir}/freetype2/freetype/config/ftconfig.h \
   $RPM_BUILD_ROOT%{_includedir}/freetype2/freetype/config/ftconfig-%{wordsize}.h
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_includedir}/freetype2/freetype/config/ftconfig.h

# Don't package static .a or .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.{a,la}


%triggerpostun -- freetype < 2.0.5-3
{
  # ttmkfdir updated - as of 2.0.5-3, on upgrades we need xfs to regenerate
  # things to get the iso10646-1 encoding listed.
  for I in %{_datadir}/fonts/*/TrueType /usr/share/X11/fonts/TTF; do
      [ -d $I ] && [ -f $I/fonts.scale ] && [ -f $I/fonts.dir ] && touch $I/fonts.scale
  done
  exit 0
}

%ldconfig_scriptlets

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.TXT docs/FTL.TXT docs/GPLv2.TXT
%{_libdir}/libfreetype.so.*
%doc README

%files demos
%{_bindir}/ftbench
%{_bindir}/ftdump
%{_bindir}/ftlint
%{_bindir}/ftvalid
%{_bindir}/ttdebug
%{_mandir}/man1/ftbench.1.gz
%{_mandir}/man1/ftdump.1.gz
%{_mandir}/man1/ftlint.1.gz
%{_mandir}/man1/ftvalid.1.gz
%{_mandir}/man1/ttdebug.1.gz
%if %{with_xfree86}
%{_bindir}/ftdiff
%{_bindir}/ftgamma
%{_bindir}/ftgrid
%{_bindir}/ftmulti
%{_bindir}/ftsdf
%{_bindir}/ftstring
%{_bindir}/ftview
%{_mandir}/man1/ftdiff.1.gz
%{_mandir}/man1/ftgamma.1.gz
%{_mandir}/man1/ftgrid.1.gz
%{_mandir}/man1/ftmulti.1.gz
%{_mandir}/man1/ftsdf.1.gz
%{_mandir}/man1/ftstring.1.gz
%{_mandir}/man1/ftview.1.gz
%endif
%doc ChangeLog README

%files devel
%doc docs/CHANGES docs/formats.txt docs/ft2faq.html
%dir %{_includedir}/freetype2
%{_datadir}/aclocal/freetype2.m4
%{_includedir}/freetype2/*
%{_libdir}/libfreetype.so
%{_bindir}/freetype-config
%{_libdir}/pkgconfig/freetype2.pc
%doc docs/design
%doc docs/glyphs
%doc docs/reference
%doc docs/tutorial
%{_mandir}/man1/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.14.1-3
- Prepare for Oreon 11 (RP1)
