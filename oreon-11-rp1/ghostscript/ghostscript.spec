%global source0_hash none

#
# Important notes regarding the package:
# ======================================
# 1) This package has GUI versions (*-x11, *-gtk), but we are not shipping the
#    desktop files, because the GUI versions are used for displaying of files
#    invoked from command line. The displaying GUI does not contain any buttons
#    or other means for user interaction. It can't even open a different file
#    from the GUI version. Therefore it does not make sense to ship desktop
#    files...

# === GLOBAL MACROS ===========================================================

# According to Fedora Package Guidelines, it is advised that packages that can
# process untrusted input are build with position-independent code (PIC).
#
# Koji should override the compilation flags and add the -fPIC or -fPIE flags by
# default. This is here just in case this wouldn't happen for some reason.
# For more info: https://fedoraproject.org/wiki/Packaging:Guidelines#PIE
%global _hardened_build 1

# By redefining the '_docdir_fmt' macro we override the default location of
# documentation or license files. Instead of them being located in 'libgs'
# folder, they are now located in 'ghostscript'.
%global _docdir_fmt     %{name}

# NOTE: Artifex is using Github only as a mirror for providing the source
#       tarballs, and their release tags/branches do not use the dot in version
#       tag. This makes obtaining the current version harder, and might prevent
#       automatic builds of new releases...
%global version_short %(echo "%{version}" | tr -d '.')

# Starting version of new sup-package layout scheme for Ghostscript, which is
# conflicting with the previous sup-package layout scheme.
#
# Obtain the location of Google Droid fonts directory:
%global google_droid_fontpath %%(dirname $(fc-list : file | grep "DroidSansFallback"))

# pdf2dsc is unmaintained in upstream, make its installation optional
%if 0%{?fedora} || 0%{?rhel} <= 10
  %bcond_without pdf2dsc
%else
  %bcond_with pdf2dsc
%endif

# =============================================================================

Name:             ghostscript
Summary:          Interpreter for PostScript language & PDF
Version:          10.06.0
Release:          2%{?dist}

License:          AGPL-3.0-or-later

URL:              https://ghostscript.com/
Source:        https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs%(echo/ghostscript-10.06.0.tar.xz

Requires:         libgs%{?_isa} = %{version}-%{release}
Requires:         %{name}-tools-fontutils = %{version}-%{release}
Requires:         %{name}-tools-printing = %{version}-%{release}

Provides:         ghostscript-core = %{version}-%{release}
Obsoletes:        ghostscript-core < 9.53.3-6
Provides:         ghostscript-x11 = %{version}-%{release}
Obsoletes:        ghostscript-x11 < 10.01.0-1

# Auxiliary build requirements:
BuildRequires:    automake
BuildRequires:    gcc
BuildRequires:    git

# Already packaged Resources -- needed to build package correctly:
BuildRequires:    adobe-mappings-cmap-devel
BuildRequires:    adobe-mappings-pdf-devel
BuildRequires:    google-droid-sans-fonts
BuildRequires:    urw-base35-fonts-devel

# Already packaged software -- needed for debundling of Ghostscript:
BuildRequires:    cups-devel
BuildRequires:    dbus-devel
# we use fc-list in generating macros at the top of SPEC file
BuildRequires:    fontconfig
BuildRequires:    fontconfig-devel
BuildRequires:    freetype-devel
# jbig2dec has no valid soname at the moment, they check jbig2dec version at runtime
# so any jbig2dec rebase means basically a soname bump - ghostscript has to be rebuilt
# with it and released at the same time to prevent issues
# 
# How does the check work:
# GS has jbig.h from jbig2dec-devel compiled in, which has the jbig2dec version
# as macro at the moment of gs build - if the jbig2dec is rebased, its shared library
# has the new version saved internally - when jbig2dec context is going to be initialized,
# the version from jbig.h in gs is compared with the version in the shared library, requiring
# the exact match.
BuildRequires:    jbig2dec-devel
BuildRequires:    lcms2-devel
BuildRequires:    libidn2-devel
BuildRequires:    libijs-devel
BuildRequires:    libjpeg-turbo-devel
BuildRequires:    libpng-devel
BuildRequires:    libpaper-devel
BuildRequires:    libtiff-devel
BuildRequires:    openjpeg2-devel
BuildRequires:    zlib-devel

# Enabling the GUI possibilities of Ghostscript:
BuildRequires:    gtk3-devel
BuildRequires:    libXt-devel
BuildRequires:    make

# =============================================================================

# NOTE: 'autosetup' macro (below) uses 'git' for applying the patches:
#       ->> All the patches should be provided in 'git format-patch' format.
#       ->> Auxiliary repository will be created during 'fedpkg prep', you
#           can see all the applied patches there via 'git log'.

# Upstream patches -- official upstream patches released by upstream since the
# ----------------    last rebase that are necessary for any reason:
#Patch000: example000.patch
# put pdf2dsc back for gv
Patch001: 0001-Reinstate-pdf2dsc.patch
# https://cgit.ghostscript.com/cgi-bin/cgit.cgi/ghostpdl.git/commit/?id=3c0be6e4fcffa6
Patch002: 0001-Fix-32-bit-build.patch


# Downstream patches -- these should be always included when doing rebase:
# ------------------
# Downstream patches for RHEL -- patches that we keep only in RHEL for various
# ---------------------------    reasons, but are not enabled in Fedora:
%if %{defined rhel} || %{defined centos}
#Patch200: example200.patch
%endif


# Patches to be removed -- deprecated functionality which shall be removed at
# ---------------------    some point in the future:


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

# This virtual provides is useful in case people get confused what *-devel
# subpackage they should actually use (i.e. ghostscript-devel vss libgs-devel?).
# By having this virtual provide both of the options above will work...
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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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
# code uses a custom-defined bool type, incompatible with C23
export CFLAGS="$CFLAGS -std=gnu17"
# --enable-dynamic
#     ... enables dynamically loaded drivers
#
# --disable-compile-inits
#     ... disables compiling of init files (PS code, fonts, etc.) into resulting
#         binaries, so they are loaded dynamically
#
# --without-versioned-path
#     ... tells configure to not use version string in the resulting paths after
#         'make_install' macro - this is safe, because only one version of
#         package can be installed at a given time on Fedora distribution,
#         so we won't end up with conflicting folders when doing rebase
#
# --with-fonthpath
#     ... searches for necessary fonts in these column-separated directories,
#         not just default ones
#
# --without-x
#     ... builds gs library  without X functionality (previously provided by ghostscript-x11)
#
# NOTE:   In RHEL we need to keep the /usr/share/ghostscript/conf.d/ folder
#         for China's GB18030 official certification:

%if %{defined rhel} || %{defined centos}
%configure --without-x --disable-compile-inits --without-versioned-path \
           --with-fontpath="%{urw_base35_fontpath}:%{google_droid_fontpath}:%{_datadir}/%{name}/conf.d/"
%else
%configure --disable-compile-inits --without-versioned-path \
           --with-fontpath="%{urw_base35_fontpath}:%{google_droid_fontpath}"
%endif
%make_build so %{?flatpak:XCFLAGS=-I%{_includedir} XTRALIBS=-L%{_libdir}}

# ---------------

%install
# Using the 'make_install' macro with 'soinstall' target would result in some
# files being installed unnecessary, so we are using traditional way:
make DESTDIR=%{buildroot} soinstall

# Remove files that we do not want ship / support:
# ------------------------------------------------
# LPR-related scripts:
rm -f %{buildroot}%{_bindir}/{lprsetup.sh,unix-lpr.sh}

# Rename the dynamic binary to be used by default as 'gs' binary.
mv -f %{buildroot}%{_bindir}/{gsc,gs}

# Remove useless files from doc/ directory and doc/ symlink:
rm -f %{buildroot}%{_docdir}/%{name}/{AUTHORS,COPYING,*.tex,*.hlp,*.txt}
rm -f %{buildroot}%{_datadir}/%{name}/doc

# pdf2dsc is unsupported upstream, but some packages (gv, emacs-auctex) use it in Fedora.
# Remove it for Centos, keep it in Fedora, but unsupported
%if %{without pdf2dsc}
rm -f %{buildroot}%{_bindir}/pdf2dsc
%endif

# ---------------

# Move html documentation into html/ subdir:
install -m 0755 -d %{buildroot}%{_docdir}/%{name}/html
mv -f %{buildroot}%{_docdir}/%{name}/{*.htm*,html}

# ---------------

# Create 'ghostscript' symlink for its binary:
ln -s %{_bindir}/gs %{buildroot}%{_bindir}/ghostscript

# Create a man page symlink for 'ghostscript':
ln -s %{_mandir}/man1/gs.1 %{buildroot}%{_mandir}/man1/ghostscript.1

# ---------------

# According to upstream, using fontconfig for fonts lookup is quite a slow
# process for Ghostscript startup, and they advise using the symlinks where
# possible. The fontconfig (Ghostscript's search path) should be used preferably
# as a fallback only.
ln -fs %{google_droid_fontpath}/DroidSansFallbackFull.ttf %{buildroot}%{_datadir}/%{name}/Resource/CIDFSubst/DroidSansFallback.ttf

for font in $(basename --multiple %{buildroot}%{_datadir}/%{name}/Resource/Font/*); do
  ln -fs %{urw_base35_fontpath}/${font}.t1 %{buildroot}%{_datadir}/%{name}/Resource/Font/${font}
done

# Using the system-wide available CMap files from Adobe via Ghostscript's search
# path is not safe (nor was ever intended to be supported) way of doing so
# according to upstream. Their preferred solution is to just create symlink for
# each of the CMap files in Ghostscript's Resources/CMap folder.
for file in $(basename --multiple %{buildroot}%{_datadir}/%{name}/Resource/CMap/*); do
  find %{adobe_mappings_rootpath} -type f -name ${file} -exec ln -fs {} %{buildroot}%{_datadir}/%{name}/Resource/CMap/${file} \;
done

# Create the configuration folder fo RHEL:
%if %{defined rhel} || %{defined centos}
  install -m 0755 -d %{buildroot}%{_datadir}/%{name}/conf.d/
%endif

# === INSTALLATION INSTRUCTIONS ===============================================

%ldconfig_scriptlets -n libgs

# === PACKAGING INSTRUCTIONS ==================================================

%files -n libgs
%license LICENSE doc/COPYING

%{_libdir}/libgs.so.10
%{_libdir}/libgs.so.10.*
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/Resource
%{_datadir}/%{name}/Resource/CIDFSubst/
%{_datadir}/%{name}/Resource/CIDFont/
%{_datadir}/%{name}/Resource/CMap/
%{_datadir}/%{name}/Resource/ColorSpace/
%{_datadir}/%{name}/Resource/Decoding/
%{_datadir}/%{name}/Resource/Encoding/
%{_datadir}/%{name}/Resource/Font/
%{_datadir}/%{name}/Resource/IdiomSet/
%{_datadir}/%{name}/Resource/Init/
%{_datadir}/%{name}/Resource/SubstCID/
%{_datadir}/%{name}/iccprofiles/
%{_datadir}/%{name}/lib/

# Include the configuration folder for RHEL:
%if %{defined rhel} || %{defined centos}
  %dir %{_datadir}/%{name}/conf.d/
%endif

# ---------------

%files -n libgs-devel
%{_libdir}/libgs.so
%{_includedir}/%{name}/

# ---------------

%files
%{_bindir}/gs
%{_bindir}/gsnd
%{_bindir}/ghostscript

# Useful conversion scripts:
%{_bindir}/eps2eps
%{_bindir}/pdf2ps
%{_bindir}/ps2ascii
%{_bindir}/ps2epsi
%{_bindir}/ps2pdf
%{_bindir}/ps2pdf12
%{_bindir}/ps2pdf13
%{_bindir}/ps2pdf14
%{_bindir}/ps2pdfwr
%{_bindir}/ps2ps
%{_bindir}/ps2ps2

%{_mandir}/man1/gs.1.gz
%{_mandir}/man1/gsnd.1.gz
%{_mandir}/man1/ghostscript.1.gz
%{_mandir}/man1/eps2eps.1.gz
%{_mandir}/man1/pdf2ps.1.gz
%{_mandir}/man1/ps2ascii.1.gz
%{_mandir}/man1/ps2epsi.1.gz
%{_mandir}/man1/ps2pdf.1.gz
%{_mandir}/man1/ps2pdf12.1.gz
%{_mandir}/man1/ps2pdf13.1.gz
%{_mandir}/man1/ps2pdf14.1.gz
%{_mandir}/man1/ps2pdfwr.1.gz
%{_mandir}/man1/ps2ps.1.gz

%if %{with pdf2dsc}
%{_bindir}/pdf2dsc
%{_mandir}/man1/pdf2dsc.1.gz
%endif

# ---------------

%files tools-dvipdf
%{_bindir}/dvipdf

%{_mandir}/man1/dvipdf.1.gz

# ---------------

%files tools-fontutils
%{_bindir}/pf2afm
%{_bindir}/pfbtopfa
%{_bindir}/printafm

%{_mandir}/man1/pf2afm.1.gz
%{_mandir}/man1/pfbtopfa.1.gz
%{_mandir}/man1/printafm.1.gz

# ---------------

%files tools-printing
%{_bindir}/gsbj
%{_bindir}/gsdj
%{_bindir}/gsdj500
%{_bindir}/gslj
%{_bindir}/gslp
%{_bindir}/pphs

%{_mandir}/man1/gsbj.1.gz
%{_mandir}/man1/gsdj.1.gz
%{_mandir}/man1/gsdj500.1.gz
%{_mandir}/man1/gslj.1.gz
%{_mandir}/man1/gslp.1.gz

# ---------------

%files gtk
%{_bindir}/gsx

# ---------------

%files doc
%doc %{_docdir}/%{name}/

# =============================================================================

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 10.06.0-2
- Prepare for Oreon 11 (RP1)
