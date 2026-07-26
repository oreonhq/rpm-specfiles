%global source0_hash none

Name:           plee-the-bear
Version:        0.7.1
Release:        23%{?dist}
Summary:        2D platform game
# Code and artwork respectively
# Automatically converted from old format: GPLv3 and CC-BY-SA - review is highly recommended.
License:        GPL-3.0-only AND LicenseRef-Callaway-CC-BY-SA
URL:            https://github.com/j-jorge/plee-the-bear/
Source0:        https://github.com/j-jorge/plee-the-bear/archive/%{version}.tar.gz
Patch3:         ptb-docbook2man.patch
BuildRequires:  gcc-c++
BuildRequires:  bear-factory-devel
BuildRequires:  docbook-utils
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libclaw-devel >= 1.7.0
BuildRequires:  SDL2_mixer-devel SDL2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  gettext
BuildRequires:  cmake
BuildRequires:  chrpath
# Build is totally broken on ppc64
ExcludeArch:    %{power64}

%description
Plee the Bear is a 2D platform game in the spirit of 1990s console games.

%prep
%setup -q -n %{name}-%{version}
%autopatch -p1

%build
# plee the bear uses some private libs which it builds as unversioned .so files
# we put them in a private-libdir, and use a wrapper to set LD_LIBRARY_PATH
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

# Translations
%find_lang %{name}

# Move binary to libexec, install wrapper to set LD_LIBRARY_PATH
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
mv $RPM_BUILD_ROOT%{_bindir}/%{name} $RPM_BUILD_ROOT%{_libexecdir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/sh
# export LD_LIBRARY_PATH=%{_libdir}/%{name}
exec %{_libexecdir}/%{name} "$@"
EOF
chmod +x $RPM_BUILD_ROOT%{_bindir}/%{name}

# conflicts with bear
rm -rf $RPM_BUILD_ROOT%{_datadir}/bear-factory/item-description
rm -rf $RPM_BUILD_ROOT%{_datadir}/bear-factory/images
rm `find $RPM_BUILD_ROOT%{_datadir}/%{name} -name "*.sh"`
rm -rf $RPM_BUILD_ROOT%{_datadir}/pixmaps

# Menu entries
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# Nuke the rpaths.
for i in $RPM_BUILD_ROOT%{_libdir}/*.so \
         $RPM_BUILD_ROOT%{_libexecdir}/%{name}; do
         chrpath --delete $i
done

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
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

%files -f %{name}.lang
%license LICENSE license/GPL license/CCPL
%doc README.md
%{_bindir}/%{name}
%{_libdir}/lib*.so
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/bear-factory/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/ptb.png
%{_mandir}/man6/%{name}.6*

%changelog
%autochangelog
