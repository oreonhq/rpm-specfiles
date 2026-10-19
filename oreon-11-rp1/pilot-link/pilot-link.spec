%global source0_hash d3f99ec04016b38995fb370265200254710318105c792c017d3aaccfb97a84b2
%bcond perl %{undefined flatpak}
%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)
Summary:        File transfer utilities between Linux and PalmPilots
Name: pilot-link
Version: 0.15.0
Release:        1%{?dist}
Epoch: 2
License: GPL-2.0-only AND GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-Public-Domain
URL: http://www.pilot-link.org/
Source0:        http://downloads.pilot-link.org/%{name}-%{version}.tar.bz2
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
%if %{with perl}
%endif
Requires: pilot-link-libs = %{epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  bluez-libs-devel
BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  libusb1-devel
BuildRequires:  make
BuildRequires:  perl(Devel::PPPort)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  readline-devel
# /oreon:deps
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
find %{buildroot}%{_libdir}/perl5/ -type f -name '.packlist' -exec rm -f {} \;
find %{buildroot}%{_libdir}/perl5/ -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot}%{_libdir}/perl5/ -type f -name '*.so' -exec chmod 0755 {} \;
find %{buildroot}%{_libdir}/perl5/ -type f -name '*.pod' -exec rm -f {} \;
rm -f %{buildroot}%{_libdir}/perl5/perllocal.pod
rm -f %{buildroot}%{_libdir}/perl5/*/*/*/PDA/dump.pl
%endif
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_bindir}/pilot-prc
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d/
install -p -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/modprobe.d/blacklist-visor.conf
cp %{SOURCE2} README.fedora
install -p -m644 %{SOURCE3} %{buildroot}%{_datadir}/pilot-link/udev
install -d %{buildroot}/lib/udev/rules.d/
install -p -m644 %{SOURCE4} %{buildroot}/lib/udev/rules.d/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n pilot-link-devel -f %{oreon_filedir}/pilot-link-devel.list
%files -n pilot-link-perl -f %{oreon_filedir}/pilot-link-perl.list
%files -n pilot-link-libs -f %{oreon_filedir}/pilot-link-libs.list

%changelog

%autochangelog
