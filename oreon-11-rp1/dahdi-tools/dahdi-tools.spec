%global source0_hash 53ffeb333f3e44b0c88e5b17475cdbf87d3f652eb81a6422de76250c061e2909

%global tools_version 2.11.1
%global linux_version 2.11.1

Name:           dahdi-tools
Version:        %{tools_version}
Release:        39%{?dist}
Summary:        Userspace tools to configure the DAHDI kernel modules

# Automatically converted from old format: GPLv2 and LGPLv2 - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-LGPLv2
URL:            http://www.asterisk.org/

Source0:        http://downloads.asterisk.org/pub/telephony/dahdi-tools/releases/dahdi-tools-%{tools_version}.tar.gz
Source1:        http://downloads.asterisk.org/pub/telephony/dahdi-tools/releases/dahdi-tools-%{tools_version}.tar.gz.asc
Source2:        http://downloads.asterisk.org/pub/telephony/dahdi-linux/releases/dahdi-linux-%{linux_version}.tar.gz
Source3:        http://downloads.asterisk.org/pub/telephony/dahdi-linux/releases/dahdi-linux-%{linux_version}.tar.gz.asc
# Add SystemD service file
Source4:        dahdi.service

# Add wcopenpci to initial blacklist
Patch0:         dahdi-tools-blacklist-wcopenpci.patch
# Fix gcc warning (upgraded to error) for what was almost certainly
# an incorrect use of the logical negation operator
#Patch1:         mpptalk-oper-fix.patch
# Fix GCC warning for unused variables, bug #1306634,
# fixed in upstream after 2.11.0
#Patch2:         dahdi-tools-2.10.0-Remove-unused-rcsid.patch
# Fix for GCC 10
Patch3:		https://issues.asterisk.org/jira/secure/attachment/58976/dahdi-tools-3.1.0-fno-common.patch
Patch4:		gcc-lto.patch
# Fixes building PIE executables
Patch5:         dahdi-tools-2.11.1-Respect-CFLAGS.patch
# Fix Makefile.legacy so that it adds compiler and linker flags
Patch6:         dahdi-tools_fix-legacy-make.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  newt-devel
BuildRequires:  patch
BuildRequires:  perl-interpreter
BuildRequires:  perl-podlators
BuildRequires:  perl-generators
BuildRequires:  udev
%{?systemd_requires}

Requires:        dahdi-tools-libs%{?_isa} = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires:        systemd-udev
%endif

Conflicts:       zaptel-utils

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

# allow overrding the variable in Makefile
#sed -i s/UDEVRULES_DIR:=/UDEVRULES_DIR=/ Makefile

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

%post
%systemd_post dahdi.service

%preun
%systemd_preun dahdi.service

%postun
%systemd_postun_with_restart dahdi.service

%files
%license LICENSE LICENSE.LGPL
%doc README
%dir %{_sysconfdir}/dahdi
%config(noreplace) %{_sysconfdir}/bash_completion.d/dahdi
%config(noreplace) %{_sysconfdir}/dahdi/assigned-spans.conf.sample
%config(noreplace) %{_sysconfdir}/dahdi/modules.sample
%config(noreplace) %{_sysconfdir}/dahdi/span-types.conf.sample
%config(noreplace) %{_sysconfdir}/dahdi/system.conf.sample
%{_udevrulesdir}/dahdi.rules
%{_udevrulesdir}/xpp.rules
%{_sbindir}/astribank_allow
%{_sbindir}/astribank_hexload
%{_sbindir}/astribank_is_starting
%{_sbindir}/astribank_tool
%{_sbindir}/dahdi_cfg
%{_sbindir}/dahdi_genconf
%{_sbindir}/dahdi_hardware
%{_sbindir}/dahdi_maint
%{_sbindir}/dahdi_monitor
%{_sbindir}/dahdi_registration
%{_sbindir}/dahdi_scan
%{_sbindir}/dahdi_span_assignments
%{_sbindir}/dahdi_span_types
%{_sbindir}/dahdi_speed
%{_sbindir}/dahdi_test
%{_sbindir}/dahdi_tool
%{_sbindir}/dahdi_waitfor_span_assignments
%{_sbindir}/fxotune
%{_sbindir}/lsdahdi
%{_sbindir}/twinstar
%{_sbindir}/xpp_blink
%{_sbindir}/xpp_sync
%dir %{_datadir}/dahdi
%{_datadir}/dahdi/astribank_hook
%{_datadir}/dahdi/xpp_fxloader
%{_datadir}/dahdi/waitfor_xpds
%{_datadir}/dahdi/dahdi_auto_assign_compat
%{_datadir}/dahdi/dahdi_handle_device
%{_datadir}/dahdi/dahdi_span_config
%dir %{_datadir}/dahdi/handle_device.d
%{_datadir}/dahdi/handle_device.d/10-span-types
%{_datadir}/dahdi/handle_device.d/20-span-assignments
%dir %{_datadir}/dahdi/span_config.d
%{_datadir}/dahdi/span_config.d/10-dahdi-cfg
%{_datadir}/dahdi/span_config.d/20-fxotune
%{_datadir}/dahdi/span_config.d/50-asterisk
%{_mandir}/man8/astribank_allow.8.gz
%{_mandir}/man8/astribank_hexload.8.gz
%{_mandir}/man8/astribank_is_starting.8.gz
%{_mandir}/man8/astribank_tool.8.gz
%{_mandir}/man8/dahdi_cfg.8.gz
%{_mandir}/man8/dahdi_genconf.8.gz
%{_mandir}/man8/dahdi_hardware.8.gz
%{_mandir}/man8/dahdi_maint.8.gz
%{_mandir}/man8/dahdi_monitor.8.gz
%{_mandir}/man8/dahdi_registration.8.gz
%{_mandir}/man8/dahdi_scan.8.gz
%{_mandir}/man8/dahdi_span_assignments.8.gz
%{_mandir}/man8/dahdi_span_types.8.gz
%{_mandir}/man8/dahdi_test.8.gz
%{_mandir}/man8/dahdi_tool.8.gz
%{_mandir}/man8/dahdi_waitfor_span_assignments.8.gz
%{_mandir}/man8/fxotune.8.gz
%{_mandir}/man8/lsdahdi.8.gz
%{_mandir}/man8/twinstar.8.gz
%{_mandir}/man8/xpp_blink.8.gz
%{_mandir}/man8/xpp_sync.8.gz
%{perl_vendorlib}/Dahdi.pm
%{perl_vendorlib}/Dahdi
%{_sbindir}/xtalk_send
%{_mandir}/man8/xtalk_send.8.gz
%{_unitdir}/dahdi.service
%{_sysusersdir}/dahdi-tools.conf

%files libs
%license LICENSE LICENSE.LGPL
%{_libdir}/*.so.*

%files devel
%license LICENSE LICENSE.LGPL
%{_includedir}/*
%{_libdir}/*.so

%changelog
%autochangelog
