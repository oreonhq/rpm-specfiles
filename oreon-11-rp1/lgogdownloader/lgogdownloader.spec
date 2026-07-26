%global source0_hash 7e35739e1de947ebd2de342875ccf16b0044c3c0ad16adb2e06109aa902f414a

Name:		lgogdownloader
Version:	3.16
Release:	7%{?dist}
Summary:	GOG.com download client

License:	WTFPL
URL:		https://github.com/Sude-/lgogdownloader
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	help2man
BuildRequires:	binutils
BuildRequires:	pkgconfig(tidy)
BuildRequires:	pkgconfig(htmlcxx)
BuildRequires:	pkgconfig(jsoncpp)
BuildRequires:	pkgconfig(libcrypto)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(tinyxml2)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	boost-devel
BuildRequires:	rhash-devel
%ifarch %{qt5_qtwebengine_arches}
BuildRequires:	pkgconfig(Qt5WebEngine)
%endif

%description
LGOGDownloader is an unofficial GOG.com downloader for Linux users. It uses the
same API as the official GOG Galaxy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%ifarch %{qt5_qtwebengine_arches}
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DUSE_QT_GUI=ON
%else
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DUSE_QT_GUI=OFF
%endif
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_bindir}/lgogdownloader
%{_mandir}/man1/lgogdownloader.1.*

%changelog
%autochangelog
