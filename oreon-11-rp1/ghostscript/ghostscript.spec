%global source0_hash c20492bc8ebb96c87fa2e52a0926e1cda8cde95d66145e018ac713fed5da38cf
%global _hardened_build 1
%global _docdir_fmt     %{name}
%global google_droid_fontpath %%(fc=$(fc-list : file 2>/dev/null | grep -m1 "DroidSansFallback"); if [ -n "$fc" ]; then dirname "$fc"; else echo %{_datadir}/fonts/google-droid-sans-fonts; fi)
  %bcond_with pdf2dsc
Name:             ghostscript
Summary:        Interpreter for PostScript language & PDF
Version:          10.08.0
Release:        1%{?dist}
%global version_short %(echo %{version} | tr -d '.')
License:          AGPL-3.0-or-later
URL:              https://ghostscript.com/
Source0:        https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs%{version_short}/%{name}-%{version}.tar.xz
Requires:         libgs%{?_isa} = %{version}-%{release}
Requires:         %{name}-tools-fontutils = %{version}-%{release}
Requires:         %{name}-tools-printing = %{version}-%{release}
Provides:         ghostscript-core = %{version}-%{release}
Obsoletes:        ghostscript-core < 9.53.3-6
Provides:         ghostscript-x11 = %{version}-%{release}
Obsoletes:        ghostscript-x11 < 10.01.0-1
Patch001: 0001-Reinstate-pdf2dsc.patch
# oreon:deps
BuildRequires:  adobe-mappings-cmap-devel
BuildRequires:  adobe-mappings-pdf-devel
BuildRequires:  automake
BuildRequires:  cups-devel
BuildRequires:  dbus-devel
BuildRequires:  fontconfig
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  google-droid-sans-fonts
BuildRequires:  gtk3-devel
BuildRequires:  jbig2dec-devel
BuildRequires:  lcms2-devel
BuildRequires:  libXt-devel
BuildRequires:  libidn2-devel
BuildRequires:  libijs-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpaper-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  openjpeg2-devel
BuildRequires:  urw-base35-fonts-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
This package provides useful conversion utilities based on Ghostscript software,
for converting PS, PDF and other document formats between each other.

Ghostscript is a suite of software providing an interpreter for Adobe Systems'
PostScript (PS) and Portable Document Format (PDF) page description languages.
Its primary purpose includes displaying (rasterization & rendering) and printing
of document pages, as well as conversions between different document formats.

# === SUBPACKAGES =============================================================

# Below requirements are resources, which are not detected by RPM automatically:
%package -n libgs
Summary:          Library providing Ghostcript's core functionality
Requires:         adobe-mappings-cmap
Requires:         adobe-mappings-cmap-deprecated
Requires:         adobe-mappings-pdf
Requires:         google-droid-sans-fonts
Requires:         urw-base35-fonts
Requires:         libijs%{?_isa}
Requires:         jbig2dec-libs%{?_isa}
Requires:         libpaper%{?_isa}
%description -n libgs
This library provides Ghostscript's core functionality, based on Ghostscript's
API, which is useful for many packages that are build on top of Ghostscript.

It also provides an X11-based driver for Ghostscript, which enables displaying
of various document files (including PS and PDF).

# ---------------

%package -n libgs-devel
Summary:          Development files for Ghostscript's library
Requires:         libgs%{?_isa} = %{version}-%{release}
Provides:         %{name}-devel         = %{version}-%{release}
Provides:         %{name}-devel%{?_isa} = %{version}-%{release}
%description -n libgs-devel
This package contains development files that are useful for building packages
against Ghostscript's library, which provides Ghostscript's core functionality.

# ---------------

# NOTE: The 'dvipdf' utility invokes 'dvips', which is part of 'texlive-dvips'.
#       This requirement pulls in a lot of texlive subpackages. Not all users
#       need to use this utility, nor they wish to have a lot of disk space to
#       be used by 'texlive'. Therefore the specific subpackage is necessary.
#
#       Previously, the 'dvips' was moving between packages before, so it's
#       more convenient (even for users) to have a direct requiremnt for the
#       executable instead of package.
%package tools-dvipdf
Summary:          Ghostscript's 'dvipdf' utility
BuildArch:        noarch
Requires:         %{name} = %{version}-%{release}
Requires:         %{_bindir}/dvips
%description tools-dvipdf
This package provides the utility 'dvipdf' for converting of TeX DVI files into
PDF files using Ghostscript and dvips.

# ---------------

%package tools-fontutils
Summary:          Ghostscript's font utilities
BuildArch:        noarch
Obsoletes:        %{name}-tools-fonts < 10.05.1-4
Requires:         %{name} = %{version}-%{release}
%description tools-fontutils
This package provides utilities which are useful when you are working with AFM,
PFB or PFA files, mostly for conversion purposes.

# ---------------

%package tools-printing
Summary:          Ghostscript's printing utilities
BuildArch:        noarch
Requires:         %{name} = %{version}-%{release}
%description tools-printing
This package provides utilities for formatting and printing text files using
either Ghostscript, or BubbleJet, DeskJet, DeskJet 500, and LaserJet printers.

It also provides the utility 'pphs', which is useful for printing of Primary
Hint Stream of a linearized PDF file.

# ---------------

%package gtk
Summary:          Ghostscript's GTK-based document renderer
Requires:         libgs%{?_isa} = %{version}-%{release}
%description gtk
This package provides GTK-based utility 'gsx', which can be used for displaying
of various document files (including PS and PDF).

# ---------------

%package doc
Summary:          Documentation files for Ghostscript
Requires:         %{name} = %{version}-%{release}
BuildArch:        noarch
%description doc
This package provides detailed documentation files for Ghostscript software.

# === BUILD INSTRUCTIONS ======================================================

# Call the 'autosetup' macro to prepare the environment, but do not patch the
# source code yet -- we need to remove bundled software before the build first:
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -N -S git

# Libraries that we already have packaged in Fedora (see Build Requirements):
rm -rf cups/libs freetype ijs jbig2dec jpeg lcms2* leptonica libpng openjpeg tesseract tiff windows zlib
# Add the remaining source code to the initial commit, patch the source code:
git add --all --force .
git commit --all --amend --no-edit > /dev/null

%if %{with pdf2dsc}
%autopatch
%else
%autopatch -m 2
%endif
# ---------------

%build

%set_build_flags
export CFLAGS="$CFLAGS -std=gnu17"
%configure --disable-compile-inits --without-versioned-path \
           --with-fontpath="%{urw_base35_fontpath}:%{google_droid_fontpath}"
%make_build so %{?flatpak:XCFLAGS=-I%{_includedir} XTRALIBS=-L%{_libdir}}
%install
make DESTDIR=%{buildroot} soinstall
rm -f %{buildroot}%{_bindir}/{lprsetup.sh,unix-lpr.sh}
mv -f %{buildroot}%{_bindir}/{gsc,gs}
rm -f %{buildroot}%{_docdir}/%{name}/{AUTHORS,COPYING,*.tex,*.hlp,*.txt}
rm -f %{buildroot}%{_datadir}/%{name}/doc
%if %{without pdf2dsc}
rm -f %{buildroot}%{_bindir}/pdf2dsc
%endif
install -m 0755 -d %{buildroot}%{_docdir}/%{name}/html
mv -f %{buildroot}%{_docdir}/%{name}/{*.htm*,html}
ln -s %{_bindir}/gs %{buildroot}%{_bindir}/ghostscript
ln -s %{_mandir}/man1/gs.1 %{buildroot}%{_mandir}/man1/ghostscript.1
ln -fs %{google_droid_fontpath}/DroidSansFallbackFull.ttf %{buildroot}%{_datadir}/%{name}/Resource/CIDFSubst/DroidSansFallback.ttf
for font in $(basename --multiple %{buildroot}%{_datadir}/%{name}/Resource/Font/*); do
  ln -fs %{urw_base35_fontpath}/${font}.t1 %{buildroot}%{_datadir}/%{name}/Resource/Font/${font}
done
for file in $(basename --multiple %{buildroot}%{_datadir}/%{name}/Resource/CMap/*); do
  find %{adobe_mappings_rootpath} -type f -name ${file} -exec ln -fs {} %{buildroot}%{_datadir}/%{name}/Resource/CMap/${file} \;
done
%ldconfig_scriptlets -n libgs
%oreon_autofiles libgs usr/*/lib*.so.*
%oreon_autofiles libgs-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libgs -f %{oreon_filedir}/libgs.list
%files -n libgs-devel -f %{oreon_filedir}/libgs-devel.list
%files -n ghostscript-tools-dvipdf -f %{oreon_filedir}/ghostscript-tools-dvipdf.list
%files -n ghostscript-tools-fontutils -f %{oreon_filedir}/ghostscript-tools-fontutils.list
%files -n ghostscript-tools-printing -f %{oreon_filedir}/ghostscript-tools-printing.list
%files -n ghostscript-gtk -f %{oreon_filedir}/ghostscript-gtk.list
%files -n ghostscript-doc -f %{oreon_filedir}/ghostscript-doc.list

%changelog

%autochangelog
