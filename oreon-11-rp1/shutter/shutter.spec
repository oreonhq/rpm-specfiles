%global source0_hash c3dba8cc26bbd90d6b7cb60c2d9b1898053869ce8df322b13da92fca8a6586e5
%global usesnapshot 0
%if 0%{?usesnapshot}
%global commit0 66c21b2b4750b2bb354887454a9977296d2d844e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global snapshottag .git%{shortcommit0}
%endif
Name:       shutter
%if 0%{?usesnapshot}
Version:    0.99.7
Release:        1%{?dist}
%else
Version:    0.99.7
Release:        1%{?dist}
%endif
Summary:        GTK+3-based screenshot application written in Perl
License:    GPL-3.0-or-later AND GPL-2.0-or-later AND GPL-2.0-only AND LicenseRef-Callaway-CC-BY-SA AND LicenseRef-Callaway-MIT AND CC0-1.0 AND LicenseRef-Callaway-Public-Domain
URL:        https://shutter-project.org/
%if 0%{?usesnapshot}
Source0:        https://github.com/%{name}-project/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
%endif
BuildArch:  noarch
Requires:       ImageMagick
Requires:       tango-icon-theme
Requires:       perl(X11::Protocol::Ext::XFIXES)
Requires:       hicolor-icon-theme
Requires:       libwnck3
Requires:       perl(Image::ExifTool)
Requires:       perl(Goo::Canvas)
%global __provides_exclude_from %{_datadir}/%{name}/resources/system/upload_plugins
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Gtk3::IconSize\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  perl-generators
BuildRequires:  sed
# /oreon:deps
%description
Shutter is a feature-rich screenshot program for Linux based operating systems
such as Ubuntu. You can take a screenshot of a specific area, window, your whole
screen, or even of a website – apply different effects to it, draw on it to
highlight points, and then upload to an image hosting site, all within one
window. Shutter is free, open-source, and licensed under GPL v3.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?usesnapshot}
  %autosetup -n %{name}-%{commit0}
%else
  %autosetup -p0 -n %{name}-%{version}
%endif
# Remove the bundled perl(X11::Protocol::Ext::XFIXES)
rm -vr share/%{name}/resources/modules/X11

%build

./po2mo.sh
%install
install -d -m 0755 -p %{buildroot}%{_bindir}
install -d -m 0755 -p %{buildroot}%{_datadir}
install -d -m 0755 -p %{buildroot}%{perl_vendorlib}
cp -pfr bin/* %{buildroot}%{_bindir}/
cp -pfr share/* %{buildroot}%{_datadir}/
mv %{buildroot}%{_datadir}/%{name}/resources/modules/* \
   %{buildroot}%{perl_vendorlib}
rmdir %{buildroot}%{_datadir}/%{name}/resources/modules/
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
chmod 0644 %{buildroot}%{_datadir}/%{name}/resources/system/upload_plugins/upload/*.pm
%find_lang %{name} --all-name
rm %{buildroot}%{_datadir}/icons/HighContrast/scalable/apps/shutter-panel.svg
ln -s %{_datadir}/icons/HighContrast/scalable/apps/shutter.svg %{buildroot}%{_datadir}/icons/HighContrast/scalable/apps/shutter-panel.svg
rm %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/shutter-panel.png
ln -s %{_datadir}/icons/hicolor/16x16/apps/shutter.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/shutter-panel.png
rm %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/shutter-panel.png
ln -s %{_datadir}/icons/hicolor/22x22/apps/shutter.png %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/shutter-panel.png
rm %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/shutter.png
ln -s %{_datadir}/icons/hicolor/32x32/apps/shutter.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/shutter-panel.png
rm %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/shutter-panel.svg 
ln -s %{_datadir}/icons/hicolor/scalable/apps/shutter.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/shutter-panel.svg
rm %{buildroot}%{_datadir}/shutter/resources/icons/Image.svg
ln -s %{_datadir}/shutter/resources/icons/drawing_tool/draw-image.svg %{buildroot}%{_datadir}/shutter/resources/icons/Image.svg
rm %{buildroot}%{_datadir}/shutter/resources/icons/Normal.cur
ln -s %{_datadir}/shutter/resources/icons/drawing_tool/objects/Cursors/Normal.cur %{buildroot}%{_datadir}/shutter/resources/icons/Normal.cur
rm %{buildroot}%{_datadir}/shutter/resources/icons/drawing_tool/cursor/backtext
ln -s %{_datadir}/shutter/resources/icons/drawing_tool/cursor/text %{buildroot}%{_datadir}/shutter/resources/icons/drawing_tool/cursor/backtext
ln -s %{_datadir}/icons/Tango/scalable %{buildroot}/%{_datadir}/shutter/resources/icons/drawing_tool/objects/Tango
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
