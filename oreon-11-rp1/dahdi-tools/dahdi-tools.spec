%global source3_hash 94271f7c3b421729ef7eb66f9fef224db61fa1453a9be9792ab3a5e6706c850b
%global source2_hash fccd6f147b58cbc8f9afb2235bd2eb2140b99d06eec572cf9860ef8d4bf370d1
%global source1_hash 5ef956cb07ff8b0bfeb207476b377dce829f143f2c6ff9b3407f078d4debfff9
%global source0_hash 9b9cd53ba51f4a03baf58bbcecda6d7bd7024e3ea3f7e0b864f666bdd794fcc5
%global tools_version 3.4.0
%global linux_version 3.4.0
Name:           dahdi-tools
Version:        %{tools_version}
Release:        1%{?dist}
Summary:        Userspace tools to configure the DAHDI kernel modules
License:        GPL-2.0-only AND LicenseRef-Callaway-LGPLv2
URL:            http://www.asterisk.org/
Source0:        http://downloads.asterisk.org/pub/telephony/%{name}/releases/%{name}-%{version}.tar.gz
Source1:        http://downloads.asterisk.org/pub/telephony/dahdi-tools/releases/dahdi-tools-%{tools_version}.tar.gz.asc
Source2:        http://downloads.asterisk.org/pub/telephony/dahdi-linux/releases/dahdi-linux-%{linux_version}.tar.gz
Source3:        http://downloads.asterisk.org/pub/telephony/dahdi-linux/releases/dahdi-linux-%{linux_version}.tar.gz.asc
Source4:        dahdi.service
Patch0:         dahdi-tools-blacklist-wcopenpci.patch
Patch3:		https://issues.asterisk.org/jira/secure/attachment/58976/dahdi-tools-3.1.0-fno-common.patch
Patch4:		gcc-lto.patch
Patch5:         dahdi-tools-2.11.1-Respect-CFLAGS.patch
Patch6:         dahdi-tools_fix-legacy-make.patch
%{?systemd_requires}
Requires:        dahdi-tools-libs%{?_isa} = %{version}-%{release}
Conflicts:       zaptel-utils
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  make
BuildRequires:  newt-devel
BuildRequires:  patch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-podlators
BuildRequires:  udev
# /oreon:deps
%description
DAHDI stands for Digium Asterisk Hardware Device Interface. This
package contains the userspace tools to configure the DAHDI kernel
modules.  DAHDI is the replacement for Zaptel, which must be renamed
due to trademark issues.

%package        libs
Summary:        Library files for DAHDI
Conflicts:      zaptel-lib
%description    libs
The dahdi-tools-libs package contains libraries for accessing DAHDI hardware.

%package        devel
Summary:        Development files for DAHDI
Requires:       dahdi-tools-libs%{?_isa} = %{version}-%{release}
BuildRequires:  chrpath
BuildRequires: make
%description    devel
The dahdi-devel package contains libraries and header files for
developing applications that use DAHDI hardware.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n dahdi-tools-%{tools_version} -a 2
ln -s dahdi-linux-%{linux_version}/include include

%patch -P0 -p1 -b .blacklist
# Fix for GCC 10
%patch -P3 -p1 -b .gcc10
%patch -P4 -p1 -b .gcc-lto
%patch -P5 -p1 -b .cflags
%patch -P6 -p1 -b .legacy-fix

# Copy SystemD service file
cp -pa %{SOURCE4} dahdi.service

# Fix incorrect FSF addresses
sed -i -e \
   's/675 Mass Ave, Cambridge, MA 02139/51 Franklin St, Boston, MA 02110/' \
   xpp/*.c xpp/*.h xpp/xtalk/*.c xpp/xtalk/*.h xpp/xtalk/include/xtalk/*.h \
   xpp/waitfor_xpds xpp/xpp_fxloader

sed -i -e \
   's/59 Temple Place, Suite 330, Boston, MA  02111-1307/51 Franklin St, Boston, MA 02110/' \
   LICENSE

# Create a sysusers.d config file
cat >dahdi-tools.sysusers.conf <<EOF
u dahdi - 'DAHDI User' /usr/share/dahdi -
EOF

%build

autoreconf -fi
%configure --with-dahdi=`pwd` --enable-shared --with-pic --with-perllib=%{perl_vendorlib}
%{make_build}
%install
%make_install config PERLLIBDIR=%{perl_vendorlib} perllibdir=%{perl_vendorlib} UDEVRULES_DIR=%{_udevrulesdir} udevrulesdir=%{_udevrulesdir}
install -D -p -m 0644 include/dahdi/user.h %{buildroot}%{_includedir}/dahdi/user.h
install -D -p -m 0644 include/dahdi/user.h %{buildroot}%{_includedir}/dahdi/dahdi_config.h
find %{buildroot} -name '*.a' -delete
rm -f %{buildroot}%{_sbindir}/sethdlc
rm -f %{buildroot}%{_libdir}/libtonezone.la
chrpath --delete %{buildroot}%{_sbindir}/dahdi_cfg
mkdir -p %{buildroot}%{_unitdir}
install -D -p -m 0644 dahdi.service %{buildroot}%{_unitdir}/dahdi.service
install -m0644 -D dahdi-tools.sysusers.conf %{buildroot}%{_sysusersdir}/dahdi-tools.conf
%oreon_autofiles dahdi-tools-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dahdi-tools-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_post dahdi.service
%preun

%systemd_preun dahdi.service
%postun

%systemd_postun_with_restart dahdi.service
%files -f %{oreon_filedir}/main.list
%files -n dahdi-tools-libs -f %{oreon_filedir}/dahdi-tools-libs.list
%files -n dahdi-tools-devel -f %{oreon_filedir}/dahdi-tools-devel.list

%changelog

%autochangelog
