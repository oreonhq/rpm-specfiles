%global source0_hash ae852f46af84aba7f51d813fb916fc7fcdbeea43f7134f150507024e1743fb5e
%global         pcbver    4.3.0
Name:           pcb
Version:        %{pcbver}
Release:        1%{?dist}
Summary:        An interactive printed circuit board editor
License:        GPL-2.0-or-later
URL:            http://pcb.geda-project.org/index.html
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Requires:       m4
Requires:       electronics-menu
Source0:        http://downloads.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch1:		pcb-fedora-c99.patch
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  bison
BuildRequires:  cups
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  fontconfig-devel
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  gd-devel
BuildRequires:  gettext-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtkglext-devel
BuildRequires:  intltool
BuildRequires:  libICE-devel
BuildRequires:  make
BuildRequires:  mesa-libGLU-devel
BuildRequires:  perl-generators
BuildRequires:  tcl
BuildRequires:  tetex-latex
BuildRequires:  tk
# /oreon:deps
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
desktop-file-install --vendor ""               \
    --dir %{buildroot}%{_datadir}/applications \
    --delete-original                          \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
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
unzip tools/apctools.zip
install -p -m 755 apc*.pl  %{buildroot}%{_datadir}/%{name}/tools
%{__rm} -f %{buildroot}%{_datadir}/%{name}/tools/apctools.zip
%{__rm} -f %{buildroot}%{_datadir}/%{name}/tools/pcb2ncap.tgz
chmod 755 %{buildroot}%{_datadir}/%{name}/tools/{PCB2HPGL,tgo2pcb.tcl,Merge*}
%{__rm} -f %{buildroot}%{_datadir}/%{name}/tools/gerbertotk.c
%{__rm} -rf %{buildroot}%{_datadir}/info/dir
mv %{buildroot}%{_pkgdocdir}/refcard.pdf %{buildroot}%{_pkgdocdir}/pcb-reference-card.pdf
%{__rm} -f %{buildroot}%{_bindir}/Merge*
%{__rm} -f %{buildroot}%{_libdir}/libgts.a %{buildroot}%{_includedir}/gts.h
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n pcb-doc -f %{oreon_filedir}/pcb-doc.list

%changelog

%autochangelog
