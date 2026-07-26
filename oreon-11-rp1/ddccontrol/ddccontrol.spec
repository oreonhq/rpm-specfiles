%global source0_hash 4f3a3d9a00e09b07423d2aed308b21dccfe57642f5d9bbf79802a0656dd11d1e

%ifarch x86_64 i686
%bcond_without ddcpci
%else
%bcond_with ddcpci
%endif

#%%global git_commit 811d34d95f5740ae8310dba3521155ad0f70fc0c
#%%global git_date 20170623

#%%global git_short_commit %%(c=%%{git_commit}; echo ${c:0:8})
#%%global git_suffix %%{git_date}git%%{git_short_commit}

Name:             ddccontrol
URL:              https://github.com/ddccontrol/ddccontrol
Version:          1.0.3
Release:          7%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
BuildRequires:    gtk2-devel
BuildRequires:    pkgconfig
BuildRequires:    pciutils-devel
BuildRequires:    desktop-file-utils
BuildRequires:    perl(XML::Parser)
BuildRequires:    gettext
BuildRequires:    libtool
BuildRequires:    libxml2-devel
BuildRequires:    tidy
BuildRequires:    libX11-devel
BuildRequires:    xml-common
BuildRequires:    libxslt
BuildRequires:    libXt-devel
BuildRequires:    docbook-style-xsl
BuildRequires:    gettext-devel
BuildRequires:    intltool
BuildRequires:    make
BuildRequires:    systemd
BuildRequires:    systemd-rpm-macros
Requires:         ddccontrol-db
Requires:         dbus-common
Requires:         /sbin/modprobe
Requires(post):   /sbin/modprobe
Summary:          Control your monitor by software using the DDC/CI protocol
Source0:          https://github.com/ddccontrol/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# no monitors on s390(x)
ExcludeArch:      s390 s390x

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

%autosetup -p1

%build
./autogen.sh

# applet is not supported on Gnome 3
%configure --enable-doc --disable-gnome-applet --prefix=%{_prefix} \
  --exec-prefix=%{_exec_prefix} --disable-rpath %{!?with_ddcpci:--disable-ddcpci}

# kill rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# use as-needed to remove unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} libdir=%{_libdir}

desktop-file-validate %{buildroot}%{_datadir}/applications/gddccontrol.desktop

# move i2c-dev module configuration to the correct place
# https://github.com/ddccontrol/ddccontrol/issues/146
A="%{buildroot}%{_libdir}/modules-load.d"
B="%{buildroot}%{_prefix}/lib/modules-load.d"
[ "$A" = "$B" ] || mv "$A" "$B"

# move html to subdir
mkdir %{buildroot}%{_docdir}/%{name}/html
mv %{buildroot}%{_docdir}/%{name}/*.html %{buildroot}%{_docdir}/%{name}/html

# remove static and *.la files
rm -f %{buildroot}%{_libdir}/{*.a,*.la}

# remove Bluecurve icon (duplicate of the hicolor one)
rm -rf %{buildroot}%{_datadir}/icons/Bluecurve

%find_lang %{name}

%post
# autoload i2c-dev module
/sbin/modprobe i2c-dev &>/dev/null || :
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md TODO
%exclude %{_docdir}/%{name}/html
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/ddccontrol.DDCControl.conf
%{_bindir}/ddccontrol
%dir %{_libexecdir}/%{name}
%if 0%{?with_ddcpci}
%{_libexecdir}/%{name}/ddcpci
%endif
%{_libexecdir}/%{name}/ddccontrol_service
%{_prefix}/lib/modules-load.d/%{name}-i2c-dev.conf
%{_libdir}/lib*.so.*
%{_datadir}/dbus-1/interfaces/ddccontrol.DDCControl.xml
%{_datadir}/dbus-1/system-services/ddccontrol.DDCControl.service
%{_mandir}/man1/ddccontrol.1*
%{_unitdir}/%{name}.service

%files gtk
%{_bindir}/gddccontrol
%{_mandir}/man1/gddccontrol.1*
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/applications/*

%files doc
%doc %{_docdir}/%{name}/html

%files devel
%{_includedir}/%{name}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
