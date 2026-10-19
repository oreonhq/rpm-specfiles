%global source0_hash 2a3665af8285354dd3315b0f4846d0854715736b3f791db0466c5bd758256720
%global repo util-dfm
Name:           deepin-util-dfm
Version:        1.4.5
Release:        1%{?dist}
Summary:        Utilities of deepin file manager
License:        GPL-3.0-or-later AND ClArtistic AND BSD-3-Clause AND BSD-4-Clause
URL:            https://github.com/linuxdeepin/util-dfm
Source0:        https://github.com/linuxdeepin/%{repo}/archive/%{version}/%{repo}-%{version}.tar.gz
Patch0:         https://github.com/linuxdeepin/util-dfm/pull/256.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libisoburn-1)
BuildRequires:  pkgconfig(liblucene++)
BuildRequires:  pkgconfig(liblucene++-contrib)
BuildRequires:  pkgconfig(libmediainfo)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(udisks2)
# /oreon:deps
%description
Deepin File Manager utilities (libdfm-io, libdfm-mount and libdfm-burn)
developed by UnionTech Software Technology Co., Ltd

%package -n     dfm6-burn
Summary:        The dfm6-burn libraries
%description -n dfm6-burn
A Toolkit of dfm6-burn.

%package -n     dfm6-burn-devel
Summary:        Development files for dfm6-burn
Requires:       dfm6-burn%{?_isa} = %{version}-%{release}
%description -n dfm6-burn-devel
This package contains development files for dfm6-burn.

%package -n     dfm6-io
Summary:        The dfm6-io libraries
%description -n dfm6-io
A Toolkit of dfm6-io.

%package -n     dfm6-io-devel
Summary:        Development files for dfm6-io
Requires:       dfm6-io%{?_isa} = %{version}-%{release}
%description -n dfm6-io-devel
This package contains development files for dfm6-io.

%package -n     dfm6-mount
Summary:        The dfm6-mount libraries
%description -n dfm6-mount
A Toolkit of dfm6-mount.

%package -n     dfm6-mount-devel
Summary:        Development files for dfm6-mount
Requires:       dfm6-mount%{?_isa} = %{version}-%{release}
%description -n dfm6-mount-devel
This package contains development files for dfm6-mount.

%package -n     dfm6-search
Summary:        The dfm6-search libraries
%description -n dfm6-search
A Toolkit of dfm6-search.

%package -n     dfm6-search-devel
Summary:        Development files for dfm6-search
Requires:       dfm6-search%{?_isa} = %{version}-%{release}
Requires:       boost-devel
Requires:       pkgconfig(liblucene++)
Requires:       pkgconfig(liblucene++-contrib)
%description -n dfm6-search-devel
This package contains development files for dfm6-search.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{repo}-%{version}

sed -i 's|Boostsystem Threads||' misc/dfm-search/dfm-search.pc.in

%build

%cmake -DVERSION=%{version}
%cmake_build
%install
%cmake_install
%oreon_autofiles dfm6-burn usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dfm6-burn-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles dfm6-io usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dfm6-io-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles dfm6-mount usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dfm6-mount-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles dfm6-search usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dfm6-search-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dfm6-burn -f %{oreon_filedir}/dfm6-burn.list
%files -n dfm6-burn-devel -f %{oreon_filedir}/dfm6-burn-devel.list
%files -n dfm6-io -f %{oreon_filedir}/dfm6-io.list
%files -n dfm6-io-devel -f %{oreon_filedir}/dfm6-io-devel.list
%files -n dfm6-mount -f %{oreon_filedir}/dfm6-mount.list
%files -n dfm6-mount-devel -f %{oreon_filedir}/dfm6-mount-devel.list
%files -n dfm6-search -f %{oreon_filedir}/dfm6-search.list
%files -n dfm6-search-devel -f %{oreon_filedir}/dfm6-search-devel.list

%changelog

%autochangelog
