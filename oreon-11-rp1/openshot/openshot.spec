%global source0_hash none

%global distname %{name}-qt
%global distrdnn org.openshot.OpenShot

%global minlibver 0.4.0

Name:           openshot
Version:        3.4.0
Release:        2%{?dist}
Summary:        Create and edit videos and movies
License:        GPL-3.0-or-later and Apache-2.0 and MIT and CC-BY-SA-4.0
URL:            http://www.openshot.org

Source0:        https://github.com/OpenShot/%{distname}/archive/v%{version}/%{distname}-%{version}.tar.gz

BuildArch:      noarch
# libopenshot is unavailable on ppc64le, see rfbz #5528
ExcludeArch:    ppc64le

# For appdata
BuildRequires:  libappstream-glib

BuildRequires:  python3-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-setuptools
BuildRequires:  libopenshot >= %{minlibver}
BuildRequires:  libopenshot-audio >= %{minlibver}
BuildRequires:  desktop-file-utils

Requires:       python%{python3_pkgversion}-httplib2
Requires:       python%{python3_pkgversion}-qt5
Requires:       (python%{python3_pkgversion}-qt5-webengine or python%{python3_pkgversion}-qt5-webkit)
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-zmq
Requires:       python%{python3_pkgversion}-libopenshot >= %{minlibver}
# Use to indicate we need ffmpeg at runtime
Requires:       /usr/bin/ffmpeg

Recommends:     openshot-lang
Recommends:     font(bitstreamverasans)
Recommends:     blender >= 2.80
Recommends:     python%{python3_pkgversion}-defusedxml
Recommends:     python%{python3_pkgversion}-distro
Recommends:     python%{python3_pkgversion}-sentry-sdk

# Support the actual name of this tool
Provides:       %{distname} = %{version}-%{release}

%generate_buildrequires
%pyproject_buildrequires 

%description
OpenShot Video Editor is a free, open-source, non-linear video editor. It
can create and edit videos and movies using many popular video, audio,
image formats.  Create videos for YouTube, Flickr, Vimeo, Metacafe, iPod,
Xbox, and many more common formats!

Features include:
* Multiple tracks (layers)
* Compositing, image overlays, and watermarks
* Audio mixing and editing
* Support for image sequences (rotoscoping)
* Key-frame animation
* Video effects (chroma-key)
* Transitions (lumas and masks)
* Titles with integrated editor and templates
* 3D animation (titles and effects)

%package lang
Summary:        Additional languages for OpenShot
Requires:       %{name} = %{version}-%{release}

%description lang
%{summary}.

%prep
%autosetup -p1 -n %{distname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

# We strip bad shebangs (/usr/bin/env) instead of fixing them
# since these files are not executable anyways
find %{buildroot}/%{python3_sitelib} -name '*.py' \
  -exec grep -q '^#!' '{}' \; -print | while read F
do
  awk '/^#!/ {if (FNR == 1) next;} {print}' $F >chopped
  touch -r $F chopped
  mv chopped $F
done

# Remove an outdated file installed into /usr/lib/mime/
rm -v %{buildroot}%{_prefix}/lib/mime/packages/openshot-qt
rmdir -p --ignore-fail-on-non-empty %{buildroot}%{_prefix}/lib/mime/packages

%find_lang OpenShot --with-qt

%check
# Validate desktop file
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop

# Validate appdata file
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files
%license COPYING
%doc AUTHORS.md README.md
%{_bindir}/%{distname}
%{_datadir}/applications/%{distrdnn}.desktop
%{_datadir}/icons/hicolor/*/apps/%{distname}.png
%{_datadir}/icons/hicolor/scalable/apps/%{distname}.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/%{distname}-doc.svg
%{_datadir}/pixmaps/%{distname}.svg
%{_datadir}/mime/packages/%{distrdnn}.xml
%{_metainfodir}/%{distrdnn}.appdata.xml
%{python3_sitelib}/%{name}_qt/
%{python3_sitelib}/%{name}_qt-%{version}.dist-info/
%exclude %{python3_sitelib}/%{name}_qt/language/*
#{python3_sitelib}/*egg-info/

%files lang -f OpenShot.lang
%dir %{python3_sitelib}/%{name}_qt/language
%{python3_sitelib}/%{name}_qt/language/%{name}_lang.py
%{python3_sitelib}/%{name}_qt/language/%{name}_lang.qrc

%changelog
%autochangelog
