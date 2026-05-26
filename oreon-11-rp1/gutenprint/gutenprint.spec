#%%global prever pre1
#%%global ver %{version}-%{prever}

# change with every change of major or minor version number
#%%global majminver 5.3
%global majminver $(echo %{version} | sed -E 's/\.[0-9]+$//')

%if 0%{?rhel} <= 8 && 0%{?fedora} < 41
%bcond_without plugin
%else
%bcond_with plugin
%endif

%if 0%{?rhel} <= 9 || 0%{?fedora}
%bcond_without gtk2
%else
%bcond_with gtk2
%endif

# added in cups-1:2.4.7-3 - remove once F40 is EOL and C10S is released
# (that's the safe bet for versions where macros will be always available)
%{!?_cups_datadir:%global _cups_datadir %(/usr/bin/pkg-config --variable=cups_datadir cups)}
%{!?_cups_serverroot:%global _cups_serverroot %(/usr/bin/pkg-config --variable=cups_serverroot cups)}

Name: gutenprint
Summary: Printer Drivers Package
Version: 5.3.5
Release: 7%{?dist}
URL: http://gimp-print.sourceforge.net/
Source0: http://downloads.sourceforge.net/gimp-print/%{name}-%{version}.tar.xz
# Post-install script to update CUPS native PPDs.
Source1: cups-genppdupdate.py.in
# ported from old gimp-print package - fix for a menu in gimp gutenprint plugin
Patch0: gutenprint-menu.patch
Patch1: gutenprint-postscriptdriver.patch
Patch2: gutenprint-yyin.patch
Patch3: gutenprint-manpage.patch
Patch4: gutenprint-python36syntax.patch
# fix utf-8 support in translations
# https://sourceforge.net/p/gimp-print/source/ci/96819fadd5ee6d0
Patch5: 0001-genppd-Ensure-we-don-t-improperly-truncate-utf-8-enc.patch
# oreon url source checksums begin
%global source0_sha256 f5a9f47de28530b1ae2069cfbc647a9a641baeeabe809bb0ef2b3ec5b9668d70
%global source0_file gutenprint-5.3.5.tar.xz
# oreon url source checksums end
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND MIT AND GPL-3.0-or-later WITH Bison-exception-2.2


Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# autoreconf
BuildRequires: autoconf
BuildRequires: automake
# we remove rpath during %%install
BuildRequires: chrpath
# we use CUPS functions in CUPS driver
BuildRequires: cups
BuildRequires: cups-devel
BuildRequires: cups-libs
# gcc is no longer in buildroot by default
BuildRequires: gcc
# for language support
BuildRequires: gettext-devel
# glib-mkenums required for autogen.sh regardless of plugin
BuildRequires: glib2-devel
# for JPEG, PNG and TIFF file format support
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
# for autoreconf
BuildRequires: libtool
# uses make
BuildRequires: make
# we use pkgconfig in spec file to get correct devel packages
BuildRequires: pkgconfig
# for gutenprint usb backend gutenprintMAJMIN+usb
BuildRequires: pkgconfig(libusb-1.0)
# Make sure we get postscriptdriver tags - for automatic driver installation
# via PackageKit.
BuildRequires:  python3-cups
# needed for defining %%{__python3} macro for prep phase
BuildRequires: python3-devel
# we use sed in spec file to get majorver.minver string, which is used in directory
# structure
BuildRequires: sed

# the plugin is built only in Fedora, so
# no need gimp devel files for its ui
%if %{with plugin}
BuildRequires: gimp-devel
%endif

%if %{with gtk2}
# gutenprint library uses functions from GTK2 for gutenprint UI library
BuildRequires: pkgconfig(gtk+-2.0)
%endif

# escputil uses lp for sending raw print commands to the printer...
Requires:      cups-client%{?_isa}

## NOTE ##
# The README file in this package contains suggestions from upstream
# on how to package this software. I'd be inclined to follow those
# suggestions unless there's a good reason not to do so.

%description
Gutenprint is a package of high quality printer drivers for Linux, BSD,
Solaris, IRIX, and other UNIX-alike operating systems.
Gutenprint was formerly called Gimp-Print.

%package doc
Summary:        Documentation for gutenprint

%description doc
Documentation for gutenprint.

%package libs
Summary:       libgutenprint library

%description libs
This package includes libgutenprint library, necessary to run gutenprint.

%if %{with gtk2}
%package libs-ui
Summary:       libgutenprintui2 library
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
# function in the library tries to figure out local printing system by checking for lp binary
Requires:      cups-client%{?_isa}

%description libs-ui
This package includes libgutenprintui2 library, which contains
GTK+ widgets, which may be used for print dialogs etc.
%endif

%package devel
Summary:        Library development files for gutenprint
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if %{with gtk2}
Requires:       gtk2-devel
Requires:       %{name}-libs-ui%{?_isa} = %{version}-%{release}
%endif

%description devel
This package contains headers and libraries required to build applications that
uses gutenprint package.

%if %{with plugin}
%package plugin
Summary:        GIMP plug-in for gutenprint
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs-ui%{?_isa} = %{version}-%{release}
Requires:       gimp

%description plugin
This package contains the gutenprint GIMP plug-in.

%package extras
Summary:        Sample test pattern generator for gutenprint-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description extras
This package contains test pattern generator and the sample test pattern
that is used by gutenprint-devel package.
%endif

%package cups
Summary:        CUPS drivers for Canon, Epson, HP and compatible printers
Requires:       cups
Requires:       %{name}%{?_isa} = %{version}-%{release}
# for cups-genppdupdate python script
Requires:       python3
Requires:       python3-charset-normalizer

%description cups
This package contains native CUPS support for a wide range of Canon,
Epson, HP and compatible printers.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/gutenprint-5.3.5.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f5a9f47de28530b1ae2069cfbc647a9a641baeeabe809bb0ef2b3ec5b9668d70" || { echo "oreon: Source0 SHA256 mismatch for gutenprint-5.3.5.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{name}-%{version}
# Fix menu placement of GIMP plugin.
%patch -P 0 -p1 -b .menu
# Allow the CUPS dynamic driver to run inside a build root.
%patch -P 1 -p1 -b .postscriptdriver
# Don't export yy* symbols (bug #882194).
%patch -P 2 -p1 -b .yyin
# Added some escputil options to the manpage (bug #979064).
%patch -P 3 -p1 -b .manpage

cp %{SOURCE1} src/cups/cups-genppdupdate.in

#shebang can change between releases - use %%{__python3} macro
sed -i -e 's,^#!/usr/bin/python3,#!%{__python3},' src/cups/cups-genppdupdate.in

# Python 3.6 invalid escape sequence deprecation fixes, COPYING as license (bug #1448303)
%patch -P 4 -p1 -b .python36syntax
# fix utf-8 support
%patch -P 5 -p1 -b .utf8-ka

# sbin is hardcoded in stp_cups.m4 - root it out (idea taken from Arch Linux)
%if 0%{?fedora} > 41 || 0%{?rhel} > 10
  sed -i 's,cups_sbindir="${cups_exec_prefix}/sbin",cups_sbindir="${cups_exec_prefix}/bin",g' m4local/stp_cups.m4
%endif


%build
# run after patch for configure.ac
./autogen.sh

# Don't run the weave test as it takes a very long time.
sed -i -e 's,^\(TESTS *=.*\) run-weavetest,\1,' test/Makefile.in

%configure --disable-dependency-tracking \
    --disable-static \
    --enable-samples \
    --enable-escputil \
    --enable-test \
    --disable-rpath \
    --enable-cups-1_2-enhancements \
    --disable-cups-ppds \
%if %{without gtk2}
    --disable-libgutenprintui2 \
%endif
    --enable-simplified-cups-ppds

%make_build

# Test suite disabled due to bug #1069274.
#%check
#make check
 
%install
%make_install

rm -rf %{buildroot}%{_datadir}/gutenprint/doc
rm -f %{buildroot}%{_datadir}/foomatic/kitload.log

rm -rf %{buildroot}%{_libdir}/gutenprint/%{majminver}/modules/*.la
rm -f %{buildroot}%{_cups_serverroot}/command.types

%find_lang %{name}
sed 's!%{_datadir}/locale/\([^/]*\)/LC_MESSAGES/gutenprint.mo!%{_datadir}/locale/\1/gutenprint_\1.po!g' %{name}.lang >%{name}-po.lang
rm -f %{name}.lang
%find_lang %{name} --all-name
cat %{name}-po.lang >>%{name}.lang

#echo .so man8/cups-genppd.8 > %{buildroot}%{_mandir}/man8/cups-genppd.5.3.3

# Fix up rpath.  If you can find a way to do this without resorting
# to chrpath, please let me know!
for file in \
  %{buildroot}%{_sbindir}/cups-genppd.%{majminver} \
  %{buildroot}%{_libdir}/*.so.* \
  %{buildroot}%{_cups_serverbin}/driver/* \
  %{buildroot}%{_cups_serverbin}/filter/* \
  %{buildroot}%{_bindir}/escputil \
  %{buildroot}%{_bindir}/testpattern \
  %{buildroot}%{_bindir}/cups-calibrate
do
  chrpath --delete ${file}
done

%if %{with plugin}
  for file in %{buildroot}%{_libdir}/gimp/*/plug-ins/*
  do
    chrpath --delete ${file}
  done
%else
  %{_bindir}/rm -f %{buildroot}%{_bindir}/testpattern \
%endif

%ldconfig_scriptlets libs
%ldconfig_scriptlets libs-ui

%post cups
%{_sbindir}/cups-genppdupdate >/dev/null 2>&1 || :
%{_sbindir}/restorecon -vRF /etc/cups/printers.conf 2>&1 || :
%{_bindir}/systemctl restart cups >/dev/null 2>&1 || :
exit 0


%files -f %{name}.lang
%license COPYING
%{_bindir}/escputil
%{_mandir}/man1/escputil.1*
%{_datadir}/%{name}
%{_libdir}/%{name}

%files doc
%doc AUTHORS NEWS README doc/FAQ.html doc/gutenprint-users-manual.odt doc/gutenprint-users-manual.pdf
%license COPYING

%files libs
%{_libdir}/libgutenprint.so.9
%{_libdir}/libgutenprint.so.9.*

%if %{with gtk2}
%files libs-ui
%{_libdir}/libgutenprintui2.so.2
%{_libdir}/libgutenprintui2.so.2.*
%endif

%files devel
%doc ChangeLog doc/developer/reference-html doc/developer/gutenprint.pdf
%doc doc/gutenprint
%{_includedir}/gutenprint/
%{_libdir}/*.so
%{_libdir}/pkgconfig/gutenprint.pc
%exclude %{_libdir}/*.la
%if %{with gtk2}
%doc doc/gutenprintui2
%{_includedir}/gutenprintui2/
%{_libdir}/pkgconfig/gutenprintui2.pc
%endif

%if %{with plugin}
%files plugin
%{_libdir}/gimp/*/plug-ins/gutenprint

%files extras
%doc
%{_bindir}/testpattern
%{_datadir}/gutenprint/samples/*
%endif

%files cups
%doc
%{_cups_datadir}/calibrate.ppm
%{_cups_datadir}/usb/net.sf.gimp-print.usb-quirks
%{_cups_serverbin}/filter/commandtocanon
%{_cups_serverbin}/filter/commandtodyesub
%{_cups_serverbin}/filter/commandtoepson
%{_cups_serverbin}/filter/rastertogutenprint.5.3
%{_cups_serverbin}/driver/gutenprint.5.3
%{_cups_serverbin}/backend/gutenprint53+usb
%{_bindir}/cups-calibrate
%{_sbindir}/cups-genppd.5.3
%{_sbindir}/cups-genppdupdate
%{_mandir}/man8/cups-calibrate.8*
%{_mandir}/man8/cups-genppd*8*.gz

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.3.5-7
- Prepare for Oreon 11 (RP1)
