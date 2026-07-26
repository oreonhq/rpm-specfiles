%global source0_hash a22e4fb0df70dbc8224edeebaf5402b69a8eca1e658da7573b1331f124a63396

%global svn_rev 1200

Name:           lcd4linux
Version:        0.11
# We package an svn snapshot of what will become 0.11 since upstream has
# neglected to do a new release for ages
Release:        0.38.svn%{svn_rev}%{?dist}
Summary:        Display system state on an external LCD display
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://ssl.bulix.org/projects/lcd4linux/
# This is the non rpmbuild parsable url:
# http://ssl.bulix.org/projects/lcd4linux/changeset/1200/trunk?old_path=%2F&format=zip
# Note replace 1200 with svn_rev!
Source0:        lcd4linux-trunk-1200.zip
# Courtesey of Debain
Source1:        lcd4linux.8
Source2:        lcd4X11.sh
Source3:        lcd4X11.desktop
Source4:        README.fedora
Patch0:         lcd4linux-XWindow-conf.patch
BuildRequires:  gd-devel ncurses-devel libX11-devel libICE-devel sqlite-devel
BuildRequires:  serdisplib-devel libftdi-devel libjpeg-devel libst2205-devel
BuildRequires:  libvncserver-devel gettext-devel dbus-devel
BuildRequires:  libtool desktop-file-utils make
# Most drivers require the old libusb-0.1 API; and
# the MDM166A driver requires the new libusb-1.0
BuildRequires:  libusb-compat-0.1-devel libusb1-devel
ExcludeArch:    s390 s390x

%description
LCD4Linux is a small program that grabs information from the kernel
and some subsystems and displays it on an external liquid crystal display.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n trunk
chmod +x bootstrap configure
export ACLOCAL_PATH=/usr/share/gettext/m4/
./bootstrap
cp -a %{SOURCE4} .

%build
# The AddFunction() function which is part of the eval/parser code gets called
# with a function callback with many different prototypes. So this cannot work
# with the strict prototype matching -std=gnu23 enables.
export CFLAGS="%{optflags} -std=gnu17"
%configure
make %{?_smp_mflags}
sed -e "s@#Display 'XWindow'@Display 'XWindow'@" \
    -e "s@Display 'ACool'@#Display 'ACool'@" \
    -e "s@Layout 'TestLayer'@#Layout 'TestLayer'@" \
    -e "s@#Layout 'Default'@Layout 'Default'@" \
    lcd4linux.conf.sample > lcd4X11.conf
touch -r lcd4linux.conf.sample lcd4X11.conf

%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 644 lcd4X11.conf $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m 644 lcd4linux.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/lcd4X11
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE3}

%files
%doc COPYING ChangeLog README.fedora lcd4linux.conf.sample
%config(noreplace) %{_sysconfdir}/lcd4X11.conf
%{_bindir}/%{name}
%{_bindir}/lcd4X11
%{_mandir}/man8/%{name}.8*
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/lcd4X11.desktop

%changelog
%autochangelog
