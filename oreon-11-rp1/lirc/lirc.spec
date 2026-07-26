%global source0_hash a44a26caf9ba55c2343e065f0a9451425c136572b279ea1e011ad012b36b607e

# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2

%global _hardened_build 1
%global __python %{__python3}

%global released 1
#define tag     devel

Name:           lirc
Version:        0.10.2
Release:        5%{?tag:.}%{?tag}%{?dist}
Summary:        The Linux Infrared Remote Control package

%global repo    http://downloads.sourceforge.net/lirc/LIRC/%{version}
%global tarball %{name}-%{version}%{?tag:-}%{?tag}.tar.gz

                # lib/ciniparser* and lib/dictionary* are BSD, others GPLv2
# Automatically converted from old format: GPLv2 and BSD - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-BSD
URL:            http://www.lirc.org/
Source0:        %{?released:%{repo}%{?tag:-}%{?tag}/}%{tarball}
Source1:        README.fedora
Source2:        99-remote-control-lirc.rules
Patch1:         0001-build-install-media-lirc.h-BTS-872074.patch
Patch2:         0002-Revert-build-Fix-missing-media-lirc.h-BTS-872074.patch
Patch3:         0003-asyncio.get_event_loop-can-return-an-error-in-python.patch

BuildRequires:  gcc-c++
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  alsa-lib-devel
Buildrequires:  autoconf
BuildRequires:  automake
BuildRequires:  checkpolicy
BuildRequires:  doxygen
BuildRequires:  expect
BuildRequires:  kernel-headers
BuildRequires:  man2html-core
BuildRequires:  libftdi-devel
BuildRequires:  libtool
%if (0%{?fedora} && 0%{?fedora} < 37) || (0%{?rhel} && 0%{?rhel} < 10)
BuildRequires:  libusb-devel
%else
BuildRequires:  libusb-compat-0.1-devel
%endif
BuildRequires:  libusb1-devel

BuildRequires:  libxslt
BuildRequires:  libXt-devel
BuildRequires:  portaudio-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-PyYAML
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  socat
BuildRequires:  systemd-devel
BuildRequires: make

Requires:       %{name}-libs = %{version}-%{release}
Requires:       lockdev
Suggests:       xorg-x11-misc-fonts

Requires(post):    systemd
                   #for triggerun
Requires(post):    systemd-sysv
Requires(post):    policycoreutils
Requires(postun):  systemd
Requires(postun):  policycoreutils
Requires(preun):   systemd

%description
LIRC is a package that allows you to decode and send infra-red and
other signals of many (but not all) commonly used remote controls.
Included applications include daemons which decode the received
signals as well as user space applications which allow controlling a
computer with a remote control.

Installing this package will install most of the LIRC sub-packages.
You might want to install lirc-core, possibly adding some other
packages to get a smaller installation.

%package        core
Summary:        LIRC core, always needed to run LIRC
Requires:       lirc-libs%{?_isa} = %{version}-%{release}
%{?systemd_requires}

%description    core
Part of the LIRC package suite which handles IR remotes. See
the package lirc for more.

The lirc core contains the lircd daemons, the devinput and
default driver and most of the applications.

%package        compat
Summary:        Compatibility package installing all lirc packages
Obsoletes:      lirc <=  0.9.1a
Provides:       lirc = %{version}-%{release}
Requires:       lirc-core%{?_isa} = %{version}-%{release}
Requires:       lirc-config = %{version}-%{release}
Requires:       lirc-tools-gui%{?_isa} = %{version}-%{release}
Requires:       lirc-drv-portaudio%{?_isa} = %{version}-%{release}
Requires:       lirc-drv-ftdi%{?_isa} = %{version}-%{release}

%description    compat
Part of the LIRC package suite which handles IR remotes. See
the package lirc for more.

Installing this package will install most lirc sub-packages, roughly
the same as installing previous versions of the lirc package.

%package        libs
Summary:        LIRC libraries

%description    libs
Part of the LIRC package suite which handles IR remotes. See
the package lirc for more.

This package includes shared libraries that applications use to
interface with LIRC.

%package        config
Summary:        LIRC Configuration Tools and Data
Requires:       lirc-core = %{version}-%{release}
Requires:       lirc-doc = %{version}-%{release}
Requires:       gnome-icon-theme
Requires:       python%{python3_pkgversion}-PyYAML
BuildArch:      noarch

%description    config
Part of the LIRC package suite which handles IR remotes. See
the package lirc for more.

The  config package contains tools and data to support the
LIRC configuration process.

%package        devel
Summary:        Development files for LIRC
Requires:       lirc-core%{?_isa} = %{version}-%{release}

%description    devel
Part of the LIRC package suite which handles IR remotes. See
the package lirc for more.

This package includes files for developing applications that use lirc
including headers and pkg-config files.

%package        doc
Summary:        LIRC documentation
BuildArch:      noarch

%description    doc
Part of the LIRC package suite which handles IR remotes. See
the package lirc for more.

This package contains lirc documentation.

%package        disable-kernel-rc
Summary:        Disable kernel ir device handling in favor of lirc
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description  disable-kernel-rc
Part of the LIRC package suite which handles IR remotes. See
the package lirc for more.

This package contains an udev rule which disables the kernel built-in
handling of infrared devices (i. e., rc* ones) by making lirc the only
used protocol.

%package        tools-gui
Summary:        LIRC GUI tools
Requires:       lirc-core%{?_isa} = %{version}-%{release}

%description   tools-gui
Part of the LIRC package suite which handles IR remotes. See
the package lirc for more.

This package contains some seldom used X11-based tools for debugging
lirc configurations.

%package        drv-portaudio
Summary:        Portaudio LIRC User-Space Driver
Requires:       lirc-core%{?_isa} = %{version}-%{release}
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2

%description    drv-portaudio
Part of the LIRC package suite which handles IR remotes. See
the package lirc for more.

This package contains a lirc user space driver which supports
an IR receiver in microphone input using the portaudio library.

%package        drv-ftdi
Summary:        Ftdi LIRC User-Space Driver
Requires:       lirc-core%{?_isa} = %{version}-%{release}

%description    drv-ftdi
Part of the LIRC package suite which handles IR remotes. See
the package lirc for more.

This package contains a user-space driver which works together
with the kernel, providing full support for the ftdi device.
See http://www.ftdichip.com.

# Don't provide or require anything from _docdir, per policy.
%global __provides_exclude_from ^%{_docdir}/.*$
%global __requires_exclude_from ^%{_docdir}/.*$

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}%{?tag:-}%{?tag}
sed -i -e 's/#effective-user/effective-user /' lirc_options.conf
sed -i -e '/^effective-user/s/=$/= lirc/' lirc_options.conf
sed -i '/User=/s/; *//' systemd/lircd.service
sed -i '/Group=/s/; *//' systemd/lircd.service
sed -i 's/; *user=/User=/' systemd/irexec.service
sed -i 's/; *group=/Group=/' systemd/irexec.service

sed -i -e "s|/usr/local/etc/|%{_sysconfdir}/|" contrib/irman2lirc

# Create a sysusers.d config file
cat >lirc.sysusers.conf <<EOF
u lirc - 'LIRC daemon user, runs lircd.' /var/log/lirc -
m lirc dialout
m lirc lock
m lirc input
EOF

%build
autoreconf -fi
export PYTHON=/usr/bin/python3

%configure \
        --docdir="%{_pkgdocdir}" \
        --enable-uinput \
        --enable-devinput \
        --with-lockdir=/var/lock/lockdev
make LANG=C.utf8 V=0 %{?_smp_mflags}

%check
if test -d python-pkg/tests; then
    cd python-pkg/tests; python3 -m unittest discover || exit 1
    cd $OLDPWD
fi

echo "Plugins: 40" > summary.ok
echo "Drivers: 51" >> summary.ok
echo "Errors: 0"   >> summary.ok
tools/lirc-lsplugins -U plugins/.libs -s > summary
diff -w summary summary.ok || exit 1

%install
make -s V=0 LIBTOOLFLAGS="--silent %{?Wnone}" DESTDIR=$RPM_BUILD_ROOT install

chmod 755 $RPM_BUILD_ROOT%{_datadir}/lirc/contrib/irman2lirc
find $RPM_BUILD_ROOT%{_libdir}/ -name \*.la -delete

install -pm 755 contrib/irman2lirc $RPM_BUILD_ROOT%{_bindir}
install -Dpm 644 contrib/60-lirc.rules \
    $RPM_BUILD_ROOT%{_udevrulesdir}/60-lirc.rules
install -Dpm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_udevrulesdir}/99-remote-control-lirc.rules
cp -a %{SOURCE1} README.fedora

mkdir -p $RPM_BUILD_ROOT/%{_tmpfilesdir}
echo "d %{_rundir}/lirc  0755  lirc  lirc  -" \
    > $RPM_BUILD_ROOT%{_tmpfilesdir}/lirc.conf

install -m0644 -D lirc.sysusers.conf %{buildroot}%{_sysusersdir}/lirc.conf

%post core
%systemd_post lircd.service lircmd.service
systemd-tmpfiles --create %{_tmpfilesdir}/lirc.conf

%preun core
%systemd_preun lircd.service lircmd.service

%postun core
%systemd_postun_with_restart lircd.service lircmd.service

%ldconfig_scriptlets libs

%files compat

%files drv-portaudio
%{_libdir}/lirc/plugins/audio.so
%{_datadir}/lirc/configs/audio.conf

%files drv-ftdi
%{_libdir}/lirc/plugins/ftdi.so
%{_datadir}/lirc/configs/ftdi.conf

%files tools-gui
%{_bindir}/xmode2
%{_bindir}/irxevent
%{_mandir}/man1/irxevent*
%{_mandir}/man1/xmode2*

%files config
%{_bindir}/irdb-get
%{_bindir}/lirc-config-tool
%{_bindir}/lirc-setup
%{_mandir}/man1/irdb-get*
%{_mandir}/man1/lirc-config-tool*
%{_mandir}/man1/lirc-setup*
%{_datadir}/lirc/configs/*
%exclude %{_datadir}/lirc/configs/ftdi.conf
%exclude %{_datadir}/lirc/configs/audio.conf

%files core
%doc README AUTHORS NEWS README.fedora
%dir  %{_sysconfdir}/lirc
%{_sysconfdir}/lirc/lircd.conf.d
%config(noreplace) %{_sysconfdir}/lirc/lirc*.conf
%config(noreplace) %{_sysconfdir}/lirc/irexec.lircrc
%{_tmpfilesdir}/lirc.conf
%{_unitdir}/lirc*
%{_unitdir}/irexec.service
%{_udevrulesdir}/60-lirc.rules
%{_bindir}/ircat
%{_bindir}/irexec
%{_bindir}/irman2lirc
%{_bindir}/irpipe
%{_bindir}/irpty
%{_bindir}/irrecord
%{_bindir}/irsend
%{_bindir}/irsimreceive
%{_bindir}/irsimsend
%{_bindir}/irtestcase
%{_bindir}/irtext2udp
%{_bindir}/irw
%{_bindir}/lirc-init-db
%{_bindir}/lirc-lsremotes
%{_bindir}/lirc-make-devinput
%{_bindir}/lircrcd
%{_bindir}/mode2
%{_bindir}/pronto2lirc
%{_sbindir}/lirc-lsplugins
%{_sbindir}/lircd
%{_sbindir}/lircd-setup
%{_sbindir}/lircd-uinput
%{_sbindir}/lircmd
%{_libdir}/lirc/plugins
%exclude %{_libdir}/lirc/plugins/ftdi.so
%exclude %{_libdir}/lirc/plugins/audio.so
%{_libdir}/python%{python3_version}/site-packages/lirc
%{_libdir}/python%{python3_version}/site-packages/lirc-setup
%{_datadir}/lirc/
%{_localstatedir}/lib/lirc/images
%{_localstatedir}/lib/lirc/plugins
%exclude %{_datadir}/lirc/configs/*
%{_mandir}/man1/ircat.1*
%{_mandir}/man1/irexec.1*
%{_mandir}/man1/irpipe.1*
%{_mandir}/man1/irpty.1*
%{_mandir}/man1/irrecord.1*
%{_mandir}/man1/irsend.1*
%{_mandir}/man1/irsimreceive.1*
%{_mandir}/man1/irsimsend.1*
%{_mandir}/man1/irtestcase.1*
%{_mandir}/man1/irtext2udp.1*
%{_mandir}/man1/irw.1*
%{_mandir}/man1/lirc-lsplugins.1*
%{_mandir}/man1/lirc-lsremotes.1*
%{_mandir}/man1/lirc-make-devinput.1*
%{_mandir}/man1/mode2.1*
%{_mandir}/man1/pronto2lirc.1*
%{_mandir}/man5/lircd.conf.5*
%{_mandir}/man5/lircrc.5*
%{_mandir}/man8/lircd-setup.8*
%{_mandir}/man8/lircd-uinput.8*
%{_mandir}/man8/lircd.8*
%{_mandir}/man8/lircmd.8*
%{_mandir}/man8/lircrcd.8*
%{_sysusersdir}/lirc.conf
%exclude %{_bindir}/lirc-data2table
%exclude %{_bindir}/lirc-postinstall
%exclude %{_mandir}/man1/lirc-postinstall.1.gz

%files libs
%license COPYING COPYING.ciniparser COPYING.curl
%{_libdir}/libirrecord.so.*
%{_libdir}/liblirc_client.so.*
%{_libdir}/liblirc_driver.so.*
%{_libdir}/liblirc.so.*

%files devel
%{_includedir}/lirc/
%{_includedir}/lirc_private.h
%{_includedir}/lirc_driver.h
%{_includedir}/lirc_client.h
%{_libdir}/libirrecord.so
%{_libdir}/liblirc_client.so
%{_libdir}/liblirc_driver.so
%{_libdir}/liblirc.so
%{_libdir}/pkgconfig/lirc-driver.pc
%{_libdir}/pkgconfig/lirc.pc

%files doc
%license COPYING COPYING.ciniparser COPYING.curl
%doc ChangeLog
%{_pkgdocdir}

%files disable-kernel-rc
%{_udevrulesdir}/99-remote-control-lirc.rules

%changelog
%autochangelog
