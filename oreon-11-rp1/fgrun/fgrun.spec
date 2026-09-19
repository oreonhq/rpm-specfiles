%global source0_hash f3aa03190becdcb878635d7765f4219fe540711c367fbacbc05945ed26371653

Name:           fgrun
Summary:        Graphical front-end for launching FlightGear flight simulator
Version:        2016.3.1
Release:        69%{?dist}
# Automatically converted from old format: GPLv2+ and CC-BY-SA - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            https://gitlab.com/flightgear/fgrun
Source0:        https://gitlab.com/flightgear/fgrun/-/archive/version/%{version}/fgrun-version-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        README.Fedora
# The icon is licensed under the CC Attribution-Share Alike 3.0 license
# http://commons.wikimedia.org/wiki/File:Bt_plane.svg
Source10:       http://upload.wikimedia.org/wikipedia/commons/9/9c/Bt_plane.svg
Source11:       Bt_plane-16.png
Source12:       Bt_plane-32.png
Source13:       Bt_plane-48.png
Source14:       Bt_plane-64.png
Source15:       Bt_plane-128.png
Patch:          0001-Build-fgrun-with-static-ui-libs.patch
Patch:          0002-Fix-a-crash-when-setting-defaults.patch
Patch:          0003-Default-settings-for-Fedora.patch
Patch:          0004-Fix-reloadPath-logic.patch
Patch:          0005-Fix-build-with-newer-simgear.patch
Requires:       FlightGear, opengl-games-utils, hicolor-icon-theme
BuildRequires:  gcc-c++
BuildRequires:  SimGear-devel >= 2.6.0
%if 0%{?fedora} >= 44
BuildRequires:  fltk1.3-devel fltk1.3-fluid
%else
BuildRequires:  fltk-devel fltk-fluid
%endif
BuildRequires:  plib-devel
BuildRequires:  sg3_utils-devel OpenSceneGraph-devel mesa-libEGL-devel
BuildRequires:  gettext boost-devel desktop-file-utils
BuildRequires:  cmake

%description 
FlightGear Launch Control is a graphical front-end for launching
FlightGear flight simulator

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n fgrun-version-%{version}
cp -a %{SOURCE2} .

%build 
CXXFLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64"
%cmake \
    -DSIMGEAR_SHARED=ON \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5

%cmake_build

%install 
%cmake_install
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/fgrun-wrapper
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/fltk/flightgear.org
install -m 0644 fgrun.prefs \
        $RPM_BUILD_ROOT%{_sysconfdir}/fltk/flightgear.org/fgrun.prefs
%find_lang %{name}

desktop-file-install                                    \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications   \
        %{SOURCE1}

# install icons
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps

install -m 0644 %{SOURCE10} \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -m 0644 %{SOURCE11} \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -m 0644 %{SOURCE12} \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -m 0644 %{SOURCE13} \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -m 0644 %{SOURCE14} \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -m 0644 %{SOURCE15} \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%files  -f %{name}.lang
%doc NEWS AUTHORS README README.Fedora
%license COPYING
%dir %{_sysconfdir}/fltk
%dir %{_sysconfdir}/fltk/flightgear.org
%{_sysconfdir}/fltk/flightgear.org/fgrun.prefs
%{_bindir}/* 
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*

%changelog
%autochangelog
