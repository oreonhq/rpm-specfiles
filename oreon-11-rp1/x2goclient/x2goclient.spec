%global source0_hash ab8bb3c78d31625c749e42f15f810fe3d242927a15298308c13dea3b915aca3c

Name:           x2goclient
Version:        4.1.2.3
Release:        10%{?dist}
Summary:        X2Go Client application

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.x2go.org
Source0:        http://code.x2go.org/releases/source/%{name}/%{name}-%{version}.tar.gz
Source1:        org.x2go.X2GoClient.metainfo.xml
# Drop clumsy attempt at Kerberos delegation
# http://bugs.x2go.org/cgi-bin/bugreport.cgi?bug=731
Patch0:         x2goclient-krb5.patch
# ensure RPM_LD_FLAGS/RPM_OPT_FLAGS are used
# https://bugzilla.redhat.com/show_bug.cgi?id=1306463
Patch2:         x2goclient-optflags.patch
# Select X11 backend on wayland
# https://bugzilla.redhat.com/show_bug.cgi?id=1756430
# https://bugs.x2go.org/cgi-bin/bugreport.cgi?bug=1414
Patch4:         0001-Select-X11-backend-on-wayland.patch
# Also fix desktop files created by session manager
# https://bugzilla.redhat.com/show_bug.cgi?id=1820989
Patch5:         0002-Select-X11-backend-for-desktop-files-created-by-sess.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  libssh-devel
BuildRequires:  libXpm-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:  man2html-core
%else
BuildRequires:  man
%endif
BuildRequires:  openldap-devel
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-linguist
%else
BuildRequires:  qt-devel
%endif
Requires:       hicolor-icon-theme
Requires:       nxproxy
# For GSSAPI authenticated connections
Requires:       openssh-clients
# For local folder sharing and printing
Requires:       openssh-server
Obsoletes:      x2goplugin < 4.1.2.1
%if 0%{?rhel} == 7
# libssh is x86_64 only for EL7
ExclusiveArch:  x86_64
%endif

%description
X2Go is a server-based computing environment with
    - session resuming
    - low bandwidth support
    - session brokerage support
    - client-side mass storage mounting support
    - client-side printing support
    - audio support
    - authentication by smartcard and USB stick

X2Go Client is a graphical client for the X2Go system.
You can use it to connect to running sessions and start new sessions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Fix up install issues
sed -i -e 's/-o root -g root//' Makefile
sed -i -e '/^MOZPLUGDIR=/s/lib/%{_lib}/' Makefile
sed -i -e '/^MAKEOVERRIDES *=/d' Makefile
%if 0%{?fedora} || 0%{?rhel} >= 8
sed -i -e 's/qt4/qt5/' Makefile
%endif
sed -i -e '/^LIBS /s/$/ -ldl/' x2goclient.pro

%build
%if 0%{?fedora} || 0%{?rhel} >= 8
export PATH=%{_qt5_bindir}:$PATH
%else
export PATH=%{_qt4_bindir}:$PATH
%endif
%make_build

%install
%make_install PREFIX=%{_prefix}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

install -D -p -m644 %{SOURCE1} %{buildroot}%{_metainfodir}/org.x2go.X2GoClient.metainfo.xml
appstream-util validate-relax \
  --nonet %{buildroot}%{_metainfodir}/org.x2go.X2GoClient.metainfo.xml

mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d

%if 0%{?rhel} && 0%{?rhel} <= 7
%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/bin/touch --no-create %{_datadir}/mime/packages &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
  /usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :
%endif

%files
%license COPYING LICENSE 
%doc AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/mime/packages/x-x2go.xml
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1.gz
%{_metainfodir}/org.x2go.X2GoClient.metainfo.xml

%changelog
%autochangelog
