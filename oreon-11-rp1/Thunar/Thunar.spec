%global source0_hash a5a32b51028dc821155e44cdec025fe70398bae193c619ae6ba8b1babf6f49f1
%global _hardened_build 1
%global xfceversion 4.20
Name:           Thunar
Version:        4.20.10
Release:        1%{?dist}
Summary:        Thunar File Manager
License:        GPL-2.0-or-later
URL:            http://thunar.xfce.org/
Source0:        http://archive.xfce.org/src/xfce/thunar/%{xfceversion}/thunar-%{version}.tar.bz2
Source1:        thunar-sendto-gnome-bluetooth.desktop
Source2:        thunar-sendto-audacious-playlist.desktop
Source3:        thunar-sendto-quodlibet-playlist.desktop
Source4:        thunar-sendto-blueman.desktop
Patch:          https://gitlab.xfce.org/xfce/thunar/-/merge_requests/620.patch
Requires:       shared-mime-info
Requires:       dbus
Requires:       gvfs
Requires:       tumbler
Obsoletes:     thunar-vcs-plugin <= 0.2.0-24
Provides:       thunar = %{version}-%{release}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libappstream-glib
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(exo-2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libxfce4panel-2.0)
BuildRequires:  pkgconfig(libxfce4ui-2)
# /oreon:deps
%description
Thunar is a new modern file manager for the Xfce Desktop Environment. It has 
been designed from the ground up to be fast and easy-to-use. Its user interface 
is clean and intuitive, and does not include any confusing or useless options. 
Thunar is fast and responsive with a good start up time and directory load time.

%package devel
Summary: Development tools for Thunar file manager
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: exo-devel
%description devel
libraries and header files for the Thunar file manager.

%package docs
Summary: GTK docs for Thunar file manager
Requires: %{name} = %{version}-%{release}
%description docs
Thunarx GTK documentation files for the Thunar file manager.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n thunar-%{version} -p1

# fix icon in thunar-sendto-email.desktop
sed -i 's!internet-mail!mail-message-new!' \
        plugins/thunar-sendto-email/thunar-sendto-email.desktop.in.in

%build

%configure --enable-dbus
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
export LD_LIBRARY_PATH="`pwd`/thunarx/.libs"
%make_build
%install
%make_install
chmod 755 %{buildroot}/%{_libdir}/*.so
make -C examples distclean
chmod 644 examples/thunar-file-manager.py
chmod 644 examples/xfce-file-manager.py
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%find_lang thunar
desktop-file-install --delete-original          \
        --dir %{buildroot}/%{_datadir}/applications         \
        %{buildroot}/%{_datadir}/applications/thunar-settings.desktop
desktop-file-install --delete-original          \
        --dir %{buildroot}/%{_datadir}/applications          \
        %{buildroot}/%{_datadir}/applications/thunar-bulk-rename.desktop
desktop-file-install --delete-original          \
        --dir %{buildroot}/%{_datadir}/applications         \
        %{buildroot}/%{_datadir}/applications/thunar.desktop
for source in %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} ; do
    desktop-file-install --vendor "" \
            --dir %{buildroot}%{_datadir}/Thunar/sendto \
            $source
done
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%oreon_autofiles Thunar-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles Thunar-docs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

for target in %{_defaultdocdir}/Thunar/html/*/images
do
       if [ -d $target ]
       then
               rm -rf $target
       fi
done
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n Thunar-devel -f %{oreon_filedir}/Thunar-devel.list
%files -n Thunar-docs -f %{oreon_filedir}/Thunar-docs.list

%changelog

%autochangelog
