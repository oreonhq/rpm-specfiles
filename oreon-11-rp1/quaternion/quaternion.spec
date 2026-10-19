%global source0_hash 1d19374124a3a266390f0d1519b970ece4c2efb6921b31de747852a57f34c1ca
%global appid       io.github.quotient_im.Quaternion
%global forgeurl    https://github.com/quotient-im/Quaternion
%global tag         %{version}
Name:       quaternion
Version:    0.0.97.1
Release:        1%{?dist}
%forgemeta
Summary:        A Qt-based IM client for Matrix
License:    GPL-3.0-or-later
URL:        %{forgeurl}
Source0:        %{forgeurl}/archive/%{version}/Quaternion-%{version}.tar.gz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Olm)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(QuotientQt6)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
# /oreon:deps
%description
Quaternion is a cross-platform desktop IM client for the Matrix protocol.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
#%%autosetup -n Quaternion-0.0.97-beta1

%build

%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DUSE_INTREE_LIBQMC=NO
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-qt
cp -p linux/%{appid}.appdata.xml %{buildroot}%{_metainfodir}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{appid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appid}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
