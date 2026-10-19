%global source0_hash a44a26caf9ba55c2343e065f0a9451425c136572b279ea1e011ad012b36b607e
%global _hardened_build 1
%global __python %{__python3}
%global released 1
Name:           lirc
Version:        0.10.2
Release:        1%{?dist}
Summary:        The Linux Infrared Remote Control package
%global repo    http://downloads.sourceforge.net/lirc/LIRC/%{version}
%global tarball %{name}-%{version}%{?tag:-}%{?tag}.tar.gz
License:        GPL-2.0-only AND LicenseRef-Callaway-BSD
URL:            http://www.lirc.org/
Source0:        %{repo}/%{name}-%{version}.tar.gz
Source1:        README.fedora
Source2:        99-remote-control-lirc.rules
Patch1:         0001-build-install-media-lirc.h-BTS-872074.patch
Patch2:         0002-Revert-build-Fix-missing-media-lirc.h-BTS-872074.patch
Patch3:         0003-asyncio.get_event_loop-can-return-an-error-in-python.patch
Requires:       %{name}-libs = %{version}-%{release}
Requires:       lockdev
Suggests:       xorg-x11-misc-fonts
Requires(post):    systemd
Requires(post):    systemd-sysv
Requires(post):    policycoreutils
Requires(postun):  systemd
Requires(postun):  policycoreutils
Requires(preun):   systemd
# oreon:deps
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  checkpolicy
BuildRequires:  doxygen
BuildRequires:  expect
BuildRequires:  gcc-c++
BuildRequires:  kernel-headers
BuildRequires:  libXt-devel
BuildRequires:  libftdi-devel
BuildRequires:  libtool
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  libusb1-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  man2html-core
BuildRequires:  portaudio-devel
BuildRequires:  python3-PyYAML
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  socat
BuildRequires:  systemd-devel
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post core

%systemd_post lircd.service lircmd.service
systemd-tmpfiles --create %{_tmpfilesdir}/lirc.conf
%preun core

%systemd_preun lircd.service lircmd.service
%postun core

%systemd_postun_with_restart lircd.service lircmd.service
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n lirc-core -f %{oreon_filedir}/lirc-core.list
%files -n lirc-compat -f %{oreon_filedir}/lirc-compat.list
%files -n lirc-libs -f %{oreon_filedir}/lirc-libs.list
%files -n lirc-config -f %{oreon_filedir}/lirc-config.list
%files -n lirc-devel -f %{oreon_filedir}/lirc-devel.list
%files -n lirc-doc -f %{oreon_filedir}/lirc-doc.list
%files -n lirc-disable-kernel-rc -f %{oreon_filedir}/lirc-disable-kernel-rc.list
%files -n lirc-tools-gui -f %{oreon_filedir}/lirc-tools-gui.list
%files -n lirc-drv-portaudio -f %{oreon_filedir}/lirc-drv-portaudio.list
%files -n lirc-drv-ftdi -f %{oreon_filedir}/lirc-drv-ftdi.list

%changelog

%autochangelog
