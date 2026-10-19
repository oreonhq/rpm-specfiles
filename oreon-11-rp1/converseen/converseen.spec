%global source0_hash 2dba5ecbc896f90a997d12504db2540be90c36c49a9ca462fb9c84a14fb368e9
Name:		converseen
Version:	0.15.2.7
Release:        1%{?dist}
Summary:        A batch image conversion tool written in C++ with Qt5 and Magick++
License:	GPL-3.0-only
URL:		https://converseen.fasterland.net/
Source0:        https://downloads.sourceforge.net/converseen/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Magick++)
BuildRequires:  pkgconfig(MagickCore)
BuildRequires:  pkgconfig(MagickWand)
# /oreon:deps
%description
Converseen is a batch image conversion tool and resizer written in C++ with Qt5
and Magick++.  Converseen allows you to convert images in more than 100
different formats!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DUSE_QT6:BOOL=ON
%cmake_build
%install
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/net.fasterland.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
