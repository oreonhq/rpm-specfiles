%global source0_hash a22e4fb0df70dbc8224edeebaf5402b69a8eca1e658da7573b1331f124a63396
%global svn_rev 1200
Name:           lcd4linux
Version:        0.11
Release:        1%{?dist}
Summary:        Display system state on an external LCD display
License:        GPL-2.0-or-later
URL:            http://ssl.bulix.org/projects/lcd4linux/
Source0:        lcd4linux-trunk-1200.zip
Source1:        lcd4linux.8
Source2:        lcd4X11.sh
Source3:        lcd4X11.desktop
Source4:        README.fedora
Patch0:         lcd4linux-XWindow-conf.patch
ExcludeArch:    s390 s390x
# oreon:deps
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gd-devel
BuildRequires:  gettext-devel
BuildRequires:  libICE-devel
BuildRequires:  libX11-devel
BuildRequires:  libftdi-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libst2205-devel
BuildRequires:  libtool
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  libusb1-devel
BuildRequires:  libvncserver-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  serdisplib-devel
BuildRequires:  sqlite-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
