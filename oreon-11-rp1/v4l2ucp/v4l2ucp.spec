%global source0_hash 4c488bd804e8272da28857da27ebd37b17770160d31ceaccfe719e0a912a13b9

Name:           v4l2ucp
Version:        2.0.1
Release:        37%{?dist}
Summary:        Video4linux universal control panel
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://v4l2ucp.sourceforge.net/
Source0:        http://downloads.sourceforge.net/v4l2ucp/v4l2ucp-%{version}.tar.gz
Patch0:         v4l2ucp-1.3-libv4l.patch
Patch1:         v4l2ucp-2.0.1-desktop.patch
Patch2:         v4l2ucp-2.0.1-better-textinput.patch
Patch3:         v4l2ucp-2.0.1-no-more-v4l1.patch
Patch4:         v4l2ucp-2.0.1-flags.patch
BuildRequires:  qt-devel libXi-devel libXmu-devel libv4l-devel cmake
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
v4l2 is a control panel for video4linux2 devices, it reads a description of the
controls that the V4L2 device supports from the device, and presents the user
with a graphical means for adjusting those controls. It allows for controlling
multiple devices. Controls can be updated with the device status either
manually, or periodically and there is an easy way to reset one or all the
controls to their default state.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

# below is the desktop file and icon stuff.
desktop-file-install --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mv $RPM_BUILD_ROOT%{_datadir}/icons/%{name}.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps

%files
%license COPYING
%doc README
%{_bindir}/%{name}
%{_bindir}/v4l2ctrl
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%changelog
%autochangelog
