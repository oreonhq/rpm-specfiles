%global source0_hash cd4b36df6747789775812fb433f246d6bd5a27f3a16357d78d9c4c9b59c59a43

# Features in Fedora/Free Electronic Lab

%global         pcbver    4.2.0

Name:           pcb
Version:        %{pcbver}
Release:        20%{?dist}

Summary:        An interactive printed circuit board editor
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://pcb.geda-project.org/index.html

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  perl-generators
BuildRequires:  tcl, tk, bison, flex, gawk, ImageMagick, gtk2-devel, gd-devel, fontconfig-devel
BuildRequires:  cups, tetex-latex, libICE-devel, desktop-file-utils, intltool, gettext-devel
BuildRequires:  dbus-devel
BuildRequires:  mesa-libGLU-devel gtkglext-devel
# Testsuite
# 2011-11-29 Disabling testsuite as rawhide has a broken libgmp.so.3
# BuildRequires:  gerbv geda-gaf

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Requires:       m4
Requires:       electronics-menu

Source0:        http://downloads.sourceforge.net/sourceforge/%{name}/%{name}-%{pcbver}.tar.gz

# sent upstream
#Patch0:         0001-Fix-the-AppData-and-update-to-the-latest-spec-versio.patch

# Upstream http://git.geda-project.org/pcb/commit/?id=9dea9f5a3801d612f78c738fe7efccefa5745000
Patch1:		pcb-fedora-c99.patch

%description
PCB is an interactive printed circuit board editor.
PCB includes a rats nest feature, design rule checking, and can provide
industry standard RS-274-X (Gerber), NC drill, and centroid data (X-Y data)
output for use in the board fabrication and assembly process. PCB offers
high end features such as an auto-router and trace optimizer which can
tremendously reduce layout time.

%package doc
Summary:         Documentation for PCB, an interactive printed circuit board editor
Requires:        %{name}%{?_isa} = %{version}-%{release}

%description doc
This package contains the documentation of PCB, an interactive printed circuit
board editor.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{pcbver}

%{__sed} -i \
   's|examplesdir = $(pkgdatadir)/examples|examplesdir = @docdir@/examples|' \
   example/libraries/Makefile.*

%{__sed} -i \
   's|tutdir = $(pkgdatadir)/tutorial|tutdir = @docdir@/tutorial|' \
   tutorial/Makefile.*

#%%patch0 -p1 -b fix-appdata-file
%patch -P1 -p1 -b fedora-c99
touch aclocal.m4 Makefile.in

%build
export WISH=%{_bindir}/wish

# Fixes failed build on EPEL-5
%if 0%{?rhel}
export CFLAGS=`echo %optflags | sed "s/-D_FORTIFY_SOURCE=2 // g" -`
%endif

# Bug 472618 : disable-update-desktop-database
# Bug 544657 : --enable-dbus
%configure \
    --enable-dbus \
    --enable-toporouter \
    --disable-update-mime-database \
    --disable-update-desktop-database \
    --docdir=%{_pkgdocdir}

%{__make} %{?_smp_mflags}
pushd doc
%{__make} -t pcb.pdf pcb.info pcb.html
popd

%install
%{__make} DESTDIR=%{buildroot} INSTALL="%{_bindir}/install -p" install

# in /usr/share/pcb/newlib/ folder, sockets is an empty folder

desktop-file-install --vendor ""               \
    --dir %{buildroot}%{_datadir}/applications \
    --delete-original                          \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

#
# Additional Examples
#
set +x
dest=%{buildroot}%{_pkgdocdir}/examples
for d in thermal pad puller ; do
   echo -n -e "... Fixing path of $d  \t"
   mkdir -p $dest/$d
   mv $dest/../$d.* $dest/$d
   install -pm 0644 doc/$d.{pcb,pdf} $dest/$d
   sed -i "s|$d.png|examples/$d/$d.png|" $dest/../%{name}.html
   echo "done"
done
set -x

## --- pcb supports for acpcircuits
# http://www.apcircuits.com/resources/links/pcb_unix.html
unzip tools/apctools.zip
install -p -m 755 apc*.pl  %{buildroot}%{_datadir}/%{name}/tools

# Removes duplicates
%{__rm} -f %{buildroot}%{_datadir}/%{name}/tools/apctools.zip

## ---

# Old versions of PCB don't support auto-route, pcb2ncap convert
# pcb format to ncap format used for mucspcb to auto-route the circuit.
# In newer versions of PCB, auto-route is included and pcb2ncap and mucspcb
# are no more needed.
%{__rm} -f %{buildroot}%{_datadir}/%{name}/tools/pcb2ncap.tgz

chmod 755 %{buildroot}%{_datadir}/%{name}/tools/{PCB2HPGL,tgo2pcb.tcl,Merge*}

# remove unnecessary file
%{__rm} -f %{buildroot}%{_datadir}/%{name}/tools/gerbertotk.c

%{__rm} -rf %{buildroot}%{_datadir}/info/dir

mv %{buildroot}%{_pkgdocdir}/refcard.pdf %{buildroot}%{_pkgdocdir}/pcb-reference-card.pdf

# remove duplicates
%{__rm} -f %{buildroot}%{_bindir}/Merge*

# L#854396 0.20110918 needlessly installs gts static library & header file
%{__rm} -f %{buildroot}%{_libdir}/libgts.a %{buildroot}%{_includedir}/gts.h

# locale's
%find_lang %{name}

# Documentation sub-package
%files doc
%{_infodir}/%{name}*
%doc %{_pkgdocdir}/

# Main package
%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README
#%%doc README_FILES/CHANGES README_FILES/Whats_new_in_2.0 README_FILES/Tools

%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-*
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/mime/packages/pcb.xml
#%%{_datadir}/mimelnk/application/x-*.desktop
%{_datadir}/gEDA/scheme/gnet-pcbfwd.scm

%changelog
%autochangelog
