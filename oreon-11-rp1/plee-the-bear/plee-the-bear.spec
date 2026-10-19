%global source0_hash 1353f37d392966e58cb976ad031af4e4aecfd032d6994d22fb08af0a219417bc
Name:           plee-the-bear
Version:        0.7.1
Release:        23%{?dist}
Summary:        2D platform game
License:        GPL-3.0-only AND LicenseRef-Callaway-CC-BY-SA
URL:            https://github.com/j-jorge/plee-the-bear/
Source0:        https://github.com/j-jorge/plee-the-bear/archive/%{version}.tar.gz
Patch3:         ptb-docbook2man.patch
ExcludeArch:    %{power64}
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  bear-factory-devel
BuildRequires:  boost-devel
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libclaw-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
# /oreon:deps
%description
Plee the Bear is a 2D platform game in the spirit of 1990s console games.

%prep

%setup -q -n %{name}-%{version}
%autopatch -p1

%build

%cmake \
        -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
        -DCMAKE_BUILD_TYPE=release \
        -DPTB_LIBRARY_PATH=%{_libdir} \
        -DPTB_INSTALL_CUSTOM_LIBRARY_DIR=%{_lib} \
        -DPTB_LIBRARY_OUTPUT_PATH=%{_libdir} \
        -DPTB_DATA_DEBUG_DIRECTORY=%{_datadir}/%{name} \
        -DBEAR_ENGINE_LIBRARY_DIRECTORY=%{_libdir} \
        -DBEAR_ENGINE_INSTALL_LIBRARY_DIR=%{_lib} \
        -DBEAR_ROOT_DIRECTORY=%{_includedir}/bear-factory
%cmake_build
%install
%cmake_install
%find_lang %{name}
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
mv $RPM_BUILD_ROOT%{_bindir}/%{name} $RPM_BUILD_ROOT%{_libexecdir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
exec %{_libexecdir}/%{name} "$@"
EOF
chmod +x $RPM_BUILD_ROOT%{_bindir}/%{name}
rm -rf $RPM_BUILD_ROOT%{_datadir}/bear-factory/item-description
rm -rf $RPM_BUILD_ROOT%{_datadir}/bear-factory/images
rm `find $RPM_BUILD_ROOT%{_datadir}/%{name} -name "*.sh"`
rm -rf $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
for i in $RPM_BUILD_ROOT%{_libdir}/*.so \
         $RPM_BUILD_ROOT%{_libexecdir}/%{name}; do
         chrpath --delete $i
done
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://github.com/j-jorge/plee-the-bear/issues/2
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">plee-the-bear.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Rescue your kidnapped son in this side scrolling platform game</summary>
  <description>
    <p>
      Plee the bear is a side scrolling platform game where you have to rescue your kidnapped son.
      Progress through the levels and dodge all the obstacles to try to rescue your son.
    </p>
  </description>
  <url type="homepage">http://www.stuff-o-matic.com/plee-the-bear/</url>
  <screenshots>
    <screenshot type="default">http://www.stuff-o-matic.com/plee-the-bear/assets/screenshots/large/2.png</screenshot>
  </screenshots>
</application>
EOF
%ldconfig_scriptlets
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
