%global source0_hash 96a9ecce87caa5495e3d5c37f2d4ce6bf993ca7de7281a57383be085456eca0f
Name:		lgogdownloader
Version:	3.19
Release:        1%{?dist}
Summary:        GOG.com download client
License:	WTFPL
URL:		https://github.com/Sude-/lgogdownloader
Source0:        https://github.com/Sude-/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%ifarch %{qt5_qtwebengine_arches}
%endif
# oreon:deps
BuildRequires:  binutils
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  pkgconfig(htmlcxx)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(tidy)
BuildRequires:  pkgconfig(tinyxml2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  rhash-devel
# /oreon:deps
%description
LGOGDownloader is an unofficial GOG.com downloader for Linux users. It uses the
same API as the official GOG Galaxy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%ifarch %{qt5_qtwebengine_arches}
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DUSE_QT_GUI=ON
%else
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DUSE_QT_GUI=OFF
%endif
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
