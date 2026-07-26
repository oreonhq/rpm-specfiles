%global source0_hash d3f99ec04016b38995fb370265200254710318105c792c017d3aaccfb97a84b2

%bcond perl %{undefined flatpak}
%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)

Summary: File transfer utilities between Linux and PalmPilots
Name: pilot-link
Version: 0.12.5
Release: 67%{?dist}
Epoch: 2
# libpisock/md5.c       Public Domain
# libpisock/blob.c      LGPLv2+
# libpisock/contact.c   GPLv2
# kittykiller.c         GPLv2+
# Automatically converted from old format: GPLv2 and GPLv2+ and LGPLv2+ and Public Domain - review is highly recommended.
License: GPL-2.0-only AND GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-Public-Domain
URL: http://www.pilot-link.org/
Source0: http://downloads.pilot-link.org/%{name}-%{version}.tar.bz2
Source1: blacklist-visor
Source2: README.fedora
Source3: 60-pilot.perms
Source4: 69-pilot-link.rules

Patch0: pilot-link-0.12.1-var.patch
Patch1: pilot-link-0.12.2-open.patch
Patch2: pilot-link-0.12.3-clio.patch
Patch3: pilot-link-0.12.5-mp.patch
Patch4: pilot-link-0.12.5-redefinePerlsymbols.patch
Patch5: pilot-link-0.12.5-compiler_warnings.patch
Patch6: pilot-link-0.12.5-ftbfs-f19.patch
Patch7: pilot-link-0.12.5-aarch64.patch
Patch8: pilot-link-0.12.5-ftbfs-f21.patch
Patch9: pilot-link-configure-c99.patch
Patch10: pilot-link-c99.patch

ExcludeArch: s390 s390x
BuildRequires: make
BuildRequires: gcc
BuildRequires: libpng-devel, readline-devel
BuildRequires: libusb1-devel, bluez-libs-devel
%if %{with perl}
BuildRequires: perl(ExtUtils::MakeMaker), perl-devel, perl-generators, perl(Devel::PPPort)
%endif
Requires: pilot-link-libs = %{epoch}:%{version}-%{release}

%description
This suite of tools allows you to upload and download programs and
data files between a Linux/UNIX machine and the PalmPilot. It has a
few extra utilities that will allow for things like syncing the
PalmPilot's calendar app with Ical. Note that you might still need to
consult the sources for pilot-link if you would like the Python, Tcl,
or Perl bindings.

Install pilot-link if you want to synchronize your Palm with your Red
Hat Linux system.

%package devel
Summary: PalmPilot development header files
Requires: pilot-link-libs = %{epoch}:%{version}-%{release}
Requires: libpng-devel, readline-devel

%description devel
This package contains the development headers that are used to build
the pilot-link package. It also includes the static libraries
necessary to build static pilot applications.

If you want to develop PalmPilot synchronizing applications, you'll
need to install pilot-link-devel.

%if %{with perl}
%package perl
Summary: PalmPilot utilies written in perl
Requires: %{name} = %{epoch}:%{version}-%{release}

%description perl
This package contains utilities that depend on perl
%endif

%package libs
Summary: PalmPilot libraries

%description libs
Libraries for applications communicating with PalmPilot

%{perl_default_filter}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .var
%patch -P1 -p1 -b .open
%patch -P2 -p1 -b .clio
%patch -P3 -p1 -b .mp
%patch -P4 -p1 -b .symbol
%patch -P5 -p1 -b .compiler
%patch -P6 -p1 -b .ftbfs-f19
%patch -P7 -p1 -b .aarch64
%patch -P8 -p1 -b .ftbfs-f21
%patch -P9 -p1
%patch -P10 -p1
iconv -f windows-1252 -t UTF8 doc/README.usb > doc/README.usb.aux
mv doc/README.usb.aux doc/README.usb
iconv -f windows-1252 -t UTF8 ChangeLog > ChangeLog.aux
mv ChangeLog.aux ChangeLog
iconv -f windows-1252 -t UTF8 NEWS > NEWS.aux
mv NEWS.aux NEWS

%build
%set_build_flags
CFLAGS="$CFLAGS -std=gnu99"
%configure \
    --with-python=no \
    --with-itcl=no \
    --with-tk=no \
    --with-tcl=no \
    --with-java=no \
    --with-cpp=yes \
%if %{with perl}
    --with-perl=yes \
%else
    --with-perl=no \
%endif
    --enable-conduits \
    --enable-libusb
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} libdir=%{_libdir}
make install -C doc/man DESTDIR=%{buildroot} libdir=%{_libdir}

%if %{with perl}
if test -f bindings/Perl/Makefile.PL ; then
    cd bindings/Perl
    perl -pi -e 's|^\$libdir =.*|\$libdir = "%{buildroot}%{_libdir}";|g' Makefile.PL
    CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS=vendor
    make -B || :
    make
    cd ../..
fi

cd bindings/Perl
make pure_install PERL_INSTALL_ROOT=%{buildroot} %{?_smp_mflags}
cd ../..
# remove files and fix perms
find %{buildroot}%{_libdir}/perl5/ -type f -name '.packlist' -exec rm -f {} \;
find %{buildroot}%{_libdir}/perl5/ -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot}%{_libdir}/perl5/ -type f -name '*.so' -exec chmod 0755 {} \;
find %{buildroot}%{_libdir}/perl5/ -type f -name '*.pod' -exec rm -f {} \;
rm -f %{buildroot}%{_libdir}/perl5/perllocal.pod
rm -f %{buildroot}%{_libdir}/perl5/*/*/*/PDA/dump.pl
%endif

# remove files we don't want to include
rm -f %{buildroot}%{_libdir}/*.la

# remove static libraries
rm -f %{buildroot}%{_libdir}/*.a

# remove broken prog
rm -f %{buildroot}%{_bindir}/pilot-prc

# Put visor to blacklist
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d/
install -p -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/modprobe.d/blacklist-visor.conf

# put README.fedora into tree
cp %{SOURCE2} README.fedora

# install visor configs to share/udev
install -p -m644 %{SOURCE3} %{buildroot}%{_datadir}/pilot-link/udev

# now that rules are moved out HAL, install to /lib/udev/
install -d %{buildroot}/lib/udev/rules.d/
install -p -m644 %{SOURCE4} %{buildroot}/lib/udev/rules.d/

%files
%doc COPYING ChangeLog README NEWS doc/README.usb doc/README.debugging doc/README.libusb README.fedora
%{_bindir}/*
%exclude %{_bindir}/pilot-ietf2datebook
%exclude %{_bindir}/pilot-sync-plan
%exclude %{_bindir}/pilot-undelete
%{_datadir}/pilot-link
%{_mandir}/man?/*
%exclude %{_mandir}/man1/ietf2datebook*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/aclocal/*.m4

%if %{with perl}
%files perl
%{_bindir}/pilot-ietf2datebook
%{_bindir}/pilot-sync-plan
%{_bindir}/pilot-undelete
%{_mandir}/man1/ietf2datebook*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/PDA*
%endif

%files libs
%doc COPYING
%{_libdir}/*.so.*
%config(noreplace) %{_sysconfdir}/modprobe.d/blacklist-visor.conf
/lib/udev/rules.d/69-pilot-link.rules

%changelog
%autochangelog
