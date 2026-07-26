%global source0_hash none

Name:           stellarium
Version:        25.4
Release:        1%{?dist}
Summary:        Photo-realistic nightsky renderer

License:        GPL-2.0-or-later
URL:            http://www.stellarium.org
Source0:        https://github.com/Stellarium/stellarium/archive/v%{version}/stellarium-%{version}.tar.gz

Patch0:         stellarium-fix-build-against-qt-6-10.patch

# Disabled due to lconvert segfaulting on armv7hl and i686
# https://bugzilla.redhat.com/show_bug.cgi?id=1884681
%if 0%{?fedora} > 32
ExcludeArch:    armv7hl i686
%endif

BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  mesa-libGLU-devel
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtlocation-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtserialport-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qtcharts-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  gettext-devel
BuildRequires:  boost-devel
BuildRequires:  glib2-devel
BuildRequires:  perl-podlators
BuildRequires:  libappstream-glib
BuildRequires:  CalcMySky-devel >= 0.2.1
%if 0%{?fedora} && 0%{?fedora} < 38
BuildRequires:  libindi-devel
%endif
BuildRequires:  QXlsx-devel
BuildRequires:  libnova-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  exiv2-devel
BuildRequires:  NLopt-devel
BuildRequires:  md4c-devel

Requires:       %{name}-data = %{version}-%{release}

%description
Stellarium is a real-time 3D photo-realistic nightsky renderer. It can
generate images of the sky as seen through the Earth's atmosphere with
more than one hundred thousand stars from the Hipparcos Catalogue,
constellations, planets, major satellites and nebulas.

%package        data
Summary:        Data files for Stellarium
BuildArch:      noarch

%description    data
Data files for the stellarium package.

%prep
%autosetup -p1

%build
# Kill USE_PLUGIN_TELESCOPECONTROL support due to libindi 2 incompatibility
%{cmake} -DCMAKE_BUILD_TYPE=Release -DQT6_LIBS=%{_libdir}/qt6 -DCPM_USE_LOCAL_PACKAGES=yes -DENABLE_SHOWMYSKY=yes \
%if 0%{?fedora} >= 38
   -DUSE_PLUGIN_TELESCOPECONTROL=no \
%endif
   %{nil}
%cmake_build

%install
%cmake_install

#Fix appdata
sed -i /url/d $RPM_BUILD_ROOT%{_datadir}/metainfo/org.stellarium.Stellarium.appdata.xml

# Fix mimetype icon: https://github.com/Stellarium/stellarium/pull/3011
sed -i -e 's/<icon/<generic-icon/' $RPM_BUILD_ROOT%{_datadir}/mime/packages/stellarium.xml

# Remove unwanted files
rm -f $RPM_BUILD_ROOT%{_datadir}/stellarium/data/*.ttf
rm -f $RPM_BUILD_ROOT%{_datadir}/pixmaps/stellarium.xpm
rm -f $RPM_BUILD_ROOT%{_datadir}/stellarium/data/stellarium.ico

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.stellarium.Stellarium.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.stellarium.Stellarium.desktop

%files
%license COPYING
%doc ChangeLog CREDITS.md README.md
%{_bindir}/stellarium
%{_datadir}/applications/org.stellarium.Stellarium.desktop
%{_datadir}/icons/hicolor/*/apps/stellarium.png
%{_datadir}/metainfo/org.stellarium.Stellarium.appdata.xml
%{_mandir}/man1/stellarium.1*
%{_datadir}/mime/packages/stellarium.xml

%files data
%license COPYING
%{_datadir}/stellarium

%changelog
%autochangelog
