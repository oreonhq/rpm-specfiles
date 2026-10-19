%global source0_hash 33452c37b59f4aa983c1ae4a460412ddffc2906796ad613242c7ad1096201b14
%bcond_without  qt5
%global gitdate 20140202
%global commit0 6ada849baca7918078e53f7dece4d96b2a0e6210
Name:           lxqt-config-randr
Version:        0.1.2
%if 0%{?gitdate}
Release:        1%{?dist}
%else
Release:        1%{?dist}
%endif
Summary:        GUI interface to RandR extension
License:        GPLv2+
URL:            https://github.com/zballina/%{name}
%if 0%{?gitdate}
Source0:        https://github.com/zballina/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
%else
%endif
Patch0:         http://bazaar.launchpad.net/~lubuntu-dev/lxde/%{name}/diff/29#/%{name}-qt5.patch
%if %with qt5
%endif
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  qt4-devel
BuildRequires:  qt5-linguist
# /oreon:deps
%description
Qt-based tool to configure the X output using the RandR 1.3/1.2 extension,
based in KDE parts, intended to be a viable option for the LXQt desktop.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?gitdate}
%setup -qn%{name}-%{commit0}
# revert Virtual Modes: Fixing bug in Brightness setting (PR#6)
# commit/3aa7fa26fb61a7a521443ff3ef1d3abc574f609e
# prevents gcc error: 'sleep' was not declared in this scope
sed -i /sleep/d src/randrcrtc.cpp
%else
%setup -q
%endif
%if %with qt5
%patch -P0 -p0
# fixes for Fedora Qt5.6
sed -i -r -e 's,(find_package.lxqt)-qt5,\1,' -e /include/d CMakeLists.txt
# permessive gcc
sed -i s,None,0, src/randroutput.cpp
%endif

%build

%cmake_lxqt -DCMAKE_BUILD_TYPE:STRING=Debug \
%if %with qt5
 -DUSE_QT5:BOOL=ON
%endif
%cmake_build
%install
%cmake_install
desktop-file-edit --remove-category=LXQt --remove-only-show-in=LXQt \
 --add-only-show-in=X-LXQt %{buildroot}%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
