%global source0_hash 43c3c124a44be60b70cd288d8f55fc32ce7f5a02f16f762bd4858da780a85882
Name:           stellarium
Version:        26.2
Release:        1%{?dist}
Summary:        Photo-realistic nightsky renderer
License:        GPL-2.0-or-later
URL:            http://www.stellarium.org
Source0:        https://github.com/Stellarium/stellarium/archive/v%{version}/stellarium-%{version}.tar.gz
Patch0:         stellarium-fix-build-against-qt-6-10.patch
Requires:       %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  CalcMySky-devel
BuildRequires:  ImageMagick
BuildRequires:  NLopt-devel
BuildRequires:  QXlsx-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  exiv2-devel
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  libappstream-glib
BuildRequires:  libnova-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  make
BuildRequires:  md4c-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  perl-podlators
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtcharts-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtlocation-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qtserialport-devel
BuildRequires:  qt6-qttools-devel
# /oreon:deps
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
%oreon_prep
%build

%{cmake} -DCMAKE_BUILD_TYPE=Release -DQT6_LIBS=%{_libdir}/qt6 -DCPM_USE_LOCAL_PACKAGES=yes -DENABLE_SHOWMYSKY=yes \
   %{nil}
%cmake_build
%install
%cmake_install
sed -i /url/d $RPM_BUILD_ROOT%{_datadir}/metainfo/org.stellarium.Stellarium.appdata.xml
sed -i -e 's/<icon/<generic-icon/' $RPM_BUILD_ROOT%{_datadir}/mime/packages/stellarium.xml
rm -f $RPM_BUILD_ROOT%{_datadir}/stellarium/data/*.ttf
rm -f $RPM_BUILD_ROOT%{_datadir}/pixmaps/stellarium.xpm
rm -f $RPM_BUILD_ROOT%{_datadir}/stellarium/data/stellarium.ico
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.stellarium.Stellarium.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.stellarium.Stellarium.desktop
%files -f %{oreon_filedir}/main.list
%files -n stellarium-data -f %{oreon_filedir}/stellarium-data.list

%changelog

%autochangelog
