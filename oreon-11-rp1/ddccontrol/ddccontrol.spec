%global source0_hash ca518f53920aef90e20c86d8497b9d66fdb24808c11131d3cda0b167b65c703e
%ifarch x86_64 i686
%bcond_without ddcpci
%else
%bcond_with ddcpci
%endif
Name:             ddccontrol
URL:              https://github.com/ddccontrol/ddccontrol
Version:          3.4.0
Release:        1%{?dist}
License:          GPL-2.0-or-later
Requires:         ddccontrol-db
Requires:         dbus-common
Requires:         /sbin/modprobe
Requires(post):   /sbin/modprobe
Summary:        Control your monitor by software using the DDC/CI protocol
Source0:        https://github.com/ddccontrol/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch:      s390 s390x
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pciutils-devel
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  tidy
BuildRequires:  xml-common
# /oreon:deps
%description
DDCcontrol is a program to control monitor parameters, like brightness and
contrast, by software, i.e. without using the OSD (On Screen Display) and
the monitor HW controls.

%package gtk
Summary:        GTK GUI for ddccontrol
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
%description gtk
This package provides the GTK graphical user interface for ddccontrol.

%package doc
Summary:        Documentation files for ddccontrol
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description doc
Documentation files for ddccontrol.

%package devel
Summary:        Development files for ddccontrol
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for ddccontrol.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure --enable-doc --disable-gnome-applet --prefix=%{_prefix} \
  --exec-prefix=%{_exec_prefix} --disable-rpath %{!?with_ddcpci:--disable-ddcpci}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot} libdir=%{_libdir}
desktop-file-validate %{buildroot}%{_datadir}/applications/gddccontrol.desktop
A="%{buildroot}%{_libdir}/modules-load.d"
B="%{buildroot}%{_prefix}/lib/modules-load.d"
[ "$A" = "$B" ] || mv "$A" "$B"
mkdir %{buildroot}%{_docdir}/%{name}/html
mv %{buildroot}%{_docdir}/%{name}/*.html %{buildroot}%{_docdir}/%{name}/html
rm -f %{buildroot}%{_libdir}/{*.a,*.la}
rm -rf %{buildroot}%{_datadir}/icons/Bluecurve
%find_lang %{name}
%oreon_autofiles ddccontrol-gtk usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ddccontrol-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ddccontrol-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

/sbin/modprobe i2c-dev &>/dev/null || :
%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n ddccontrol-gtk -f %{oreon_filedir}/ddccontrol-gtk.list
%files -n ddccontrol-doc -f %{oreon_filedir}/ddccontrol-doc.list
%files -n ddccontrol-devel -f %{oreon_filedir}/ddccontrol-devel.list

%changelog

%autochangelog
