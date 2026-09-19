%global source0_hash 400bc7d84dcfb3265a7a1ce51819679dc3adaeda231514bd89b0f932b78ff5c4

Name:		xloadimage
Summary: 	Image viewer and processor
Version:	4.1
Release:	42%{?dist}
License:	MIT
Source0:	ftp://ftp.x.org/R5contrib/%{name}.%{version}.tar.gz
# Patches with number prefix come from Debian
# Many thanks to all those who have done work on this package over the years
Patch0:		01_libjpeg-support.dpatch
Patch1:		02_png-support.dpatch
Patch2:		03_security-strfoo.dpatch
Patch3:		04_previous-image.dpatch
Patch4:		05_idelay-manpage.dpatch
Patch5:		06_-Wall-cleanup.dpatch
Patch6:		07_SYSPATHFILE.dpatch
Patch7:		08_manpage-config-path.dpatch
Patch8:		09_xloadimagerc-path.dpatch
Patch9:		10_config.c-HOME-fix.dpatch
Patch10:	11_fork-implies-quiet.dpatch
Patch11:	12_fix-tile.dpatch
Patch12:	13_varargs-is-obsolete.dpatch
Patch13:	14_errno-not-extern.dpatch
Patch14:	15_CAN-2005-0638.dpatch
Patch15:	16_CAN-2005-0639.dpatch
Patch16:	17_security-sprintf.dpatch
Patch17:	18_manpage_fixes.dpatch
Patch18:	19_fix_root_c_resource_leak.dpatch
Patch19:	xloadimage-4.1-ignore-dummy-copyright-variables.patch
Patch20:	xloadimage-4.1-bracketfix.patch
Patch21:	xloadimage-4.1-png-pkg-config.patch
Patch22:	xloadimage-4.1-libtiff4.patch
Patch23:	xloadimage-4.1-png-1.5.patch
Patch24:	xloadimage-4.1-fix-mem-leak.patch
Patch25:	xloadimage-4.1-sub-second-delay.patch
Patch26:	xloadimage-c99.patch
Patch27:	22-include.patch
Patch28:	27_shrink-should-not-zoom-upwards.patch
Patch29:	28_correct-scaling-fullscreen.patch
Patch30:	29_fix-manpage-hyphens.patch
Patch31:	32_fix-spelling.patch
# There is no real upstream for xloadimage anymore, so this work probably stays here forever.
Patch32:	xloadimage-4.1-c23.patch
URL:		http://www.frostbytes.com/~jimf/xloadimage.html
%if 0%{?fedora} >= 18
BuildRequires:  gcc
BuildRequires:	libtiff-devel >= 4.0
%else
BuildRequires:	libtiff-devel
%endif
BuildRequires:	make
BuildRequires:	libX11-devel, libpng-devel, libjpeg-devel
BuildRequires:	libICE-devel

%description
Xloadimage is a utility which will view many different types of images 
under X11, load images onto the root window, or dump processed images 
into one of several image file formats. The current version can read 
many different image file types.

A variety of options are available to modify images prior to viewing. 
These options include clipping, dithering, depth reduction, zoom (either 
X or Y axis independently or both at once), brightening or darkening, 
and image merging. When applicable, these options are done automatically 
(eg a color image to be displayed on a monochrome screen will be 
dithered automatically). 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}.%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1
%patch -P14 -p1
%patch -P15 -p1
%patch -P16 -p1
%patch -P17 -p1
%patch -P18 -p1
%patch -P19 -p1
%patch -P20 -p1
%patch -P21 -p1 -b .png-pkg-config
%if 0%{?fedora} >= 18
%patch -P22 -p1 -b .tiff4
%endif
%patch -P23 -p1 -b .png15
%patch -P24 -p1 -b .fix-mem-leak
%patch -P25 -p1 -b .sub-second-delay
%patch -P26 -p1
%patch -P27 -p1
%patch -P28 -p1
%patch -P29 -p1
%patch -P30 -p1
%patch -P31 -p1
%patch -P32 -p1 -b .c23

chmod +x configure

%build
%configure
make %{?_smp_mflags}

%install
# First, the binaries:
mkdir -p %{buildroot}%{_bindir}
install -m 0755 uufilter %{buildroot}%{_bindir}
install -m 0755 xloadimage %{buildroot}%{_bindir}
# Next, the symlinks
pushd %{buildroot}%{_bindir}
ln -s xloadimage xsetbg
ln -s xloadimage xview
popd
# The configuration file
mkdir -p %{buildroot}%{_sysconfdir}/X11/
install -m 0644 xloadimagerc %{buildroot}%{_sysconfdir}/X11/Xloadimage
# Now, the man pages
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 0644 xloadimage.man %{buildroot}%{_mandir}/man1/xloadimage.1x
install	-m 0644 uufilter.man %{buildroot}%{_mandir}/man1/uufilter.1x
# And some copies for the symlinks (we can't really make symlinks here because of how rpm 
# compresses man pages)
cp -a %{buildroot}%{_mandir}/man1/xloadimage.1x %{buildroot}%{_mandir}/man1/xsetbg.1x
cp -a %{buildroot}%{_mandir}/man1/xloadimage.1x %{buildroot}%{_mandir}/man1/xview.1x

%files
%doc README mit.cpyrght
%{_bindir}/uufilter
%{_bindir}/xloadimage
%{_bindir}/xsetbg
%{_bindir}/xview
%config(noreplace) %{_sysconfdir}/X11/Xloadimage
%{_mandir}/man1/*

%changelog
%autochangelog
