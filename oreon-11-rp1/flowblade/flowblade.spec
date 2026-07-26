%global source0_hash 8726b0e73b5316880f16bbc91469088fba700ecf1e944e49faed75e9441f31bd

#For git snapshots, set to 0 to use release instead:
%global usesnapshot 0
%if 0%{?usesnapshot}
%global commit0 21710f51e7f14e14bfed998ef2df8cc444d26776
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global snapshottag .git%{shortcommit0}
%endif
%global unique_name io.github.jliljebl.Flowblade

Name:           flowblade
%if 0%{?usesnapshot}
Version:        2.14.0.2
Release:        8%{?dist}
%else
Version:        2.24
Release:        4%{?dist}
%endif
License:        GPL-3.0-only
Summary:        Multitrack non-linear video editor for Linux
Url:            https://github.com/jliljebl/flowblade
%if 0%{?usesnapshot}
Source0:        %{url}/archive/%{commit0}/%{name}-%{version}-%{shortcommit0}.tar.gz
%else
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
%endif
Patch0:         %{name}_sys_path.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
Requires:       /usr/bin/ffmpeg
Requires:       python3-mlt
Requires:       frei0r-plugins >= 1.4
Requires:       gmic
Requires:       gtk3
# This dependency isn't available anymore since f30
Requires:       ladspa-swh-plugins
Requires:       librsvg2
Requires:       python3-numpy
Requires:       python3-pillow
Requires:       python3-dbus
Requires:       python3-gobject-base
Requires:       python3-libusb1
Requires:       shared-mime-info

BuildArch:      noarch

%description
Flowblade Movie Editor is a multitrack non-linear video editor for Linux
released under GPL 3 license.

Flowblade is designed to provide a fast, precise and robust editing 
experience.

In Flowblade clips are usually automatically placed tightly after or 
between clips when they are inserted on the timeline. Edits are fine 
tuned by trimming in and out points of clips, or by cutting and deleting 
parts of clips.

Flowblade provides powerful tools to mix and filter video and audio. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?usesnapshot}
%setup -qn %{name}-%{commit0}
%else
%autosetup -p1 -n %{name}-%{version}
%endif

# fix wrong-script-interpreter errors
sed -i -e 's|#!/usr/bin/env python|#!/usr/bin/python3|g' flowblade-trunk/Flowblade/launch/*
sed -i -e 's|#!/usr/bin/env python|#!/usr/bin/python3|g' flowblade-trunk/Flowblade/tools/clapperless.py

# fix to %%{_datadir}/locale
sed -i "s|respaths.LOCALE_PATH|'%{_datadir}/locale'|g" flowblade-trunk/Flowblade/translations.py

# flowblade is not a native Wayland application and needs to run using XWayland
sed -i -e 's|env GDK_BACKEND=x11 flowblade %f|env GDK_BACKEND=x11 SDL_VIDEODRIVER=x11 flowblade %f|' flowblade-trunk/installdata/io.github.jliljebl.Flowblade.desktop

%generate_buildrequires
   cd flowblade-trunk
   %pyproject_buildrequires

%build 
cd flowblade-trunk
%pyproject_wheel

%install 
cd flowblade-trunk
%pyproject_install

# fix permissions
chmod +x %{buildroot}%{python3_sitelib}/Flowblade/launch/*

# setup of mime is already done, so for what we need this file ?
rm %{buildroot}/usr/lib/mime/packages/flowblade

# move .mo files to /usr/share/locale the right place
for i in $(ls -d %{buildroot}%{python3_sitelib}/Flowblade/locale/*/LC_MESSAGES/ | sed 's/\(^.*locale\/\)\(.*\)\(\/LC_MESSAGES\/$\)/\2/') ; do
    mkdir -p %{buildroot}%{_datadir}/locale/$i/LC_MESSAGES/
    mv %{buildroot}%{python3_sitelib}/Flowblade/locale/$i/LC_MESSAGES/%{name}.mo \
        %{buildroot}%{_datadir}/locale/$i/LC_MESSAGES/
done

# E: non-executable-script
chmod a+x %{buildroot}%{python3_sitelib}/Flowblade/tools/clapperless.py
chmod a+x %{buildroot}%{python3_sitelib}/Flowblade/tools/exportardour.py

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{unique_name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files -f flowblade-trunk/%{name}.lang
%doc flowblade-trunk/README
%license flowblade-trunk/COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{unique_name}.desktop
%{_mandir}/man1/%{name}.1.*
%{_datadir}/mime/packages/%{unique_name}.xml
%{_datadir}/metainfo/%{unique_name}.appdata.xml
%{_datadir}/icons/hicolor/128x128/apps/%{unique_name}.png
%{python3_sitelib}/Flowblade/
%{python3_sitelib}/%{name}*

%changelog
%autochangelog
