%global source0_hash 788b29f256502b83536116c90795383961b26338a04d32c8ed35e53da4284aad

Summary:       Serial terminal for the gnome desktop
Name:          moserial
Version:       3.0.21
Release:       14%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
URL:           https://wiki.gnome.org/moserial/
Source0:       http://ftp.gnome.org/pub/GNOME/sources/moserial/3.0/moserial-%{version}.tar.xz
BuildRequires: GConf2-devel
BuildRequires: desktop-file-utils
BuildRequires: gnome-doc-utils
BuildRequires: gtk3-devel
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: make
BuildRequires: perl(XML::Parser)
BuildRequires: rarian-compat
BuildRequires: sed
BuildRequires: vala
Requires:      yelp
Requires:      lrzsz
Requires:      hicolor-icon-theme
%description
Moserial is a clean, friendly gtk-based serial terminal for the gnome
desktop. It is written in Vala for extra goodness.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
find -name *.c -delete
find -name moserial.vala.stamp -delete
chmod 0644 AUTHORS ChangeLog* NEWS COPYING README

%build
%configure
%make_build

%install
%make_install
desktop-file-install --delete-original         \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/moserial.desktop

for book in %{buildroot}%{_datadir}/help/[a-z]*/moserial/index.docbook ; do
    sed -i -e 's|fileref="figures|fileref="../../C/moserial/figures|' $book
done
for dir in %{buildroot}%{_datadir}/help/[a-z]*/moserial/figures ; do
    rm -rf $dir
done

%find_lang moserial

%files -f moserial.lang
%license COPYING
%doc AUTHORS ChangeLog ChangeLog.pre-git NEWS README
%{_bindir}/moserial
%{_datadir}/applications/moserial.desktop
%{_datadir}/metainfo/moserial.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/moserial.svg
%{_datadir}/help/*/moserial
%{_mandir}/man1/moserial.1*

%changelog
%autochangelog
