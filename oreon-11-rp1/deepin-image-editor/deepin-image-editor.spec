%global source0_hash 64975b187e8bc71f05ef68d566bd812e7344d424234e5b5505dc31bf53123f05
%global gitdate       20260129
%global commit        3e96cfe21771d282b9caba2959145fc2835bd9da
%global short_commit  %(c="%{commit}"; echo ${c:0:7})
Name:           deepin-image-editor
Version:        6.5.2^%{gitdate}git%{short_commit}
Release:        1%{?dist}
Summary:        Public library for deepin-image-viewer and deepin-album
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/image-editor
Source0:        https://github.com/linuxdeepin/image-editor/archive/%{commit}/%{name}-%{short_commit}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  ffmpegthumbnailer-devel
BuildRequires:  gcc-c++
BuildRequires:  libtiff-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(dfm6-io)
BuildRequires:  pkgconfig(dtk6core)
BuildRequires:  pkgconfig(dtk6gui)
BuildRequires:  pkgconfig(dtk6widget)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libmediainfo)
# /oreon:deps
%description
%{summary}.

%package -n     libimageviewer6
Summary:        The libimageviewer6 library
%description -n libimageviewer6
This package contains the libraries for Deepin Image editor.

%package -n     libimageviewer6-devel
Summary:        Development files for libimageviewer6
Requires:       libimageviewer6%{?_isa} = %{version}-%{release}
%description -n libimageviewer6-devel
This package contains development files for libimageviewer6.

%package -n     libimagevisualresult6
Summary:        The libimagevisualresult6 library
Requires:       libimagevisualresult6-data%{?_isa} = %{version}-%{release}
%description -n libimagevisualresult6
This package contains the libraries for Deepin Image editor.

%package -n     libimagevisualresult6-devel
Summary:        Development files for libimagevisualresult6
Requires:       libimagevisualresult6%{?_isa} = %{version}-%{release}
%description -n libimagevisualresult6-devel
This package contains development files for libimagevisualresult6.

%package -n     libimagevisualresult6-data
Summary:        Data files for libimagevisualresult6
Requires:       libimagevisualresult6%{?_isa} = %{version}-%{release}
%description -n libimagevisualresult6-data
This package provides data files for libimagevisualresult6.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -GNinja -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build
%install
%cmake_install
%find_lang libimageviewer6 --with-qt --all-name
%oreon_autofiles libimageviewer6 usr/*/lib*.so.*
%oreon_autofiles libimageviewer6-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libimagevisualresult6 usr/*/lib*.so.*
%oreon_autofiles libimagevisualresult6-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libimagevisualresult6-data usr/*/lib*.so.*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libimageviewer6 -f %{oreon_filedir}/libimageviewer6.list
%files -n libimageviewer6-devel -f %{oreon_filedir}/libimageviewer6-devel.list
%files -n libimagevisualresult6 -f %{oreon_filedir}/libimagevisualresult6.list
%files -n libimagevisualresult6-devel -f %{oreon_filedir}/libimagevisualresult6-devel.list
%files -n libimagevisualresult6-data -f %{oreon_filedir}/libimagevisualresult6-data.list

%changelog

%autochangelog
