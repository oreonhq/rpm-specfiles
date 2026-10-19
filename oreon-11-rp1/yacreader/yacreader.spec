%global source0_hash fd47b0c8845371899c71fc5ae1a15498fc75d37bab96816437b5cdb68266eaae
%global appname YACReader
%global versuf %{nil}
Name:           yacreader
Version:        10.3.0
Release:        1%{?dist}
Summary:        Cross platform comic reader and library manager
License:        GPL-3.0-or-later AND BSD-3-Clause AND MIT
URL:            https://www.yacreader.com
Source0:        https://github.com/%{appname}/%{name}/releases/download/%{version}/%{name}-%{version}-src.tar.xz
Requires:       hicolor-icon-theme
Requires:       qt5-qtgraphicaleffects%{?_isa}
Requires:       qt5-qtquickcontrols%{?_isa}
Requires:       qt5-qtsvg
# oreon:deps
BuildRequires:  cmake(Qt5)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5ScriptTools)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake3
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  mesa-libGLU-devel
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(libunarr)
BuildRequires:  pkgconfig(poppler-qt5)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
"Yet another comic reader".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}%{versuf}

# wrong-file-end-of-line-encoding fix
sed -i 's/\r$//' INSTALL.md
# file-not-utf8 fix
iconv -f iso8859-1 -t utf-8 README.md > README.md.conv && mv -f README.md.conv README.md

%build

lrelease-qt5 %{appname}/%{appname}.pro
lrelease-qt5 %{appname}Library/%{appname}Library.pro
%qmake_qt5
%make_build
%install
%make_install \
    INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{name}/languages
find . -name \*.qm -exec cp {} %{buildroot}%{_datadir}/%{name}/languages/ \;
%find_lang %{name} --with-qt
%find_lang %{name}library --with-qt
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
