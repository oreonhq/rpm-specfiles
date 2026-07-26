%global source0_hash 33cc0e25daa62e5ba7091caea3c83a8dc74dc5d7721c4501d349f210c4b3c6d3

%define _legacy_common_support 1

Name:           grsync
Version:        1.3.1
Release:        %autorelease
Summary:        A Gtk+ GUI for rsync
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.opbyte.it/grsync/
Source0:        http://www.opbyte.it/release/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gtk3-devel desktop-file-utils gettext perl(XML::Parser)
BuildRequires:  intltool
BuildRequires:  make
Requires:       polkit

%description
Grsync is a GUI (Graphical User Interface) for rsync, the commandline 
directory synchronization tool. It makes use of the GTK libraries and 
is released under the GPL license, so it is opensource. It is in beta 
stage and doesn't support all of rsync features, but can be effectively 
used to synchronize local directories. For example some people use 
grsync to synchronize their music collection with removable devices or 
to backup personal files to a networked drive. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# some minor corrections for rpmlint
sed -i 's/\r//' README AUTHORS NEWS
sed -i 's|@prefix@/bin/@PACKAGE@|@PACKAGE@|' grsync.desktop.in

%build
%configure --disable-unity
%make_build
sed -i 's|Icon=%{name}.png|Icon=%{name}|g' %{name}.desktop

%install
%make_install
desktop-file-install \
    --remove-category=Application \
    --add-category=FileTransfer \
    --add-category=GTK \
    --dir=%{buildroot}%{_datadir}/applications/ \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_bindir}/grsync*
%{_mandir}/man1/grsync*.1.*
%{_datadir}/pixmaps/grsync*.png
%{_datadir}/applications/grsync.desktop
%{_datadir}/grsync/
%{_datadir}/icons/hicolor/*/mimetypes/application-x-grsync-session.png
%{_datadir}/mime/packages/grsync.xml

%changelog
%autochangelog
