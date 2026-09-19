%global source0_hash aa7528c9c1d3982ebc50289b1c4287363c01b2f0c888d8650d1a993275bcf39d

%global commit d73a25c61fa6b7f41000b38b4b4c8b32ed4e2fd1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global buildbin 1

Name:		libdxfrw
Version:	1.1.0
Release:	0.11.rc1%{?dist}
Summary:	Library to read/write DXF files
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/LibreCAD/libdxfrw
Source0:	https://github.com/LibreCAD/libdxfrw/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildRequires:	gcc-c++
%if 0%{?epel} == 7
BuildRequires:	cmake3
%else
BuildRequires:	cmake
%endif
# Upstream development has only happened in the LibreCAD fork since 2022.
# Bring those changes here so we still have a viable library.

# Treat infinity bulge as zero angle for tangential polylines
# https://github.com/LibreCAD/LibreCAD/commit/aec7b7161087a7783f77369c77c6807b32b5bd2f
Patch1:		aec7b7161087a7783f77369c77c6807b32b5bd2f.patch
# Save closed splines with wrapped control points
# https://github.com/LibreCAD/LibreCAD/commit/25c2e472b0cd83e2b7ae28e523b89fe094fbd246
Patch2:		25c2e472b0cd83e2b7ae28e523b89fe094fbd246.patch
# drw_entities: coding style: initialize class members
# https://github.com/LibreCAD/LibreCAD/commit/6fd84ff6a952ab8a35e6e701ddac23a4c39d9fae
Patch3:		6fd84ff6a952ab8a35e6e701ddac23a4c39d9fae.patch
# avoid risky c style string functions
# https://github.com/LibreCAD/LibreCAD/commit/4fa20f7db90705ef30705857d404756e6ae48ad0
Patch4:		4fa20f7db90705ef30705857d404756e6ae48ad0.patch
# parseDWG specified override
# https://github.com/LibreCAD/LibreCAD/commit/0778a64d9535dc1b04495cf6b8b206ee68509004
Patch5:		0778a64d9535dc1b04495cf6b8b206ee68509004.patch
# Change DXF Export to use ext Style handle ID for 340 Dimstyle
# https://github.com/LibreCAD/LibreCAD/commit/cb7043c7c44a10dc4a89813faee9357ae21ffac7
Patch6:		cb7043c7c44a10dc4a89813faee9357ae21ffac7.patch
# more override fixes
# https://github.com/LibreCAD/LibreCAD/commit/3e6dbf7eb43ae3f5141ac7a74a75f93105d206ea
Patch7:		3e6dbf7eb43ae3f5141ac7a74a75f93105d206ea.patch
# Fixes for CodeQL scan (issue #1646)
# https://github.com/LibreCAD/LibreCAD/commit/d7b5b0a30bc096ec7a6802a2806258f9e6e39fea
Patch8:		d7b5b0a30bc096ec7a6802a2806258f9e6e39fea.patch
# Fix compiler warning
# https://github.com/LibreCAD/LibreCAD/commit/4dc3d5fa4b328873af07be05d7b67e5846628eb7
Patch9:		4dc3d5fa4b328873af07be05d7b67e5846628eb7.patch
# Header cleanup
# https://github.com/LibreCAD/LibreCAD/commit/1603a1ac5ef804b50b8fb583662c0bdcbf9ec72c
Patch10:	1603a1ac5ef804b50b8fb583662c0bdcbf9ec72c.patch

# All of these patches are committed but not in the LibreCAD 2.2 branch, 3.0 work?

# Merging qt6
# https://github.com/LibreCAD/LibreCAD/commit/ab3e44e28b282e3c4d304db37264d0c6e2142ad8
Patch11:	ab3e44e28b282e3c4d304db37264d0c6e2142ad8.patch
# Compiler warnings
# https://github.com/LibreCAD/LibreCAD/commit/7cf1408247e1c03aba86ddebd951d1e413c26fa3
Patch12:	7cf1408247e1c03aba86ddebd951d1e413c26fa3.patch
# Improved preview on actions, copy/paste, shortcuts etc.
# https://github.com/LibreCAD/LibreCAD/commit/05c0f3bd865aae21f453965a504d215a63a02782
Patch13:	05c0f3bd865aae21f453965a504d215a63a02782.patch
# Rendering performance (#1922)
# https://github.com/LibreCAD/LibreCAD/commit/8b3cf9caf984dff07df2c83f685c9bd7a175df67
Patch14:	8b3cf9caf984dff07df2c83f685c9bd7a175df67.patch
# Views and actions (#1958)
# https://github.com/LibreCAD/LibreCAD/commit/a46f1967474e7a39cf82e45464000373503fabbe
Patch15:	a46f1967474e7a39cf82e45464000373503fabbe.patch
# Arcs and splines (#1967)
# https://github.com/LibreCAD/LibreCAD/commit/7838da61f71baf93c722c05f7c4c80f802cd06a1
Patch16:	7838da61f71baf93c722c05f7c4c80f802cd06a1.patch
# fixed a compiler warning
# https://github.com/LibreCAD/LibreCAD/commit/3c55e604ea9622bfaac33bbd83ebab3b26293e27
Patch17:	3c55e604ea9622bfaac33bbd83ebab3b26293e27.patch
# User Coordinates, Angles Basis, Angles format for input, etc.
# https://github.com/LibreCAD/LibreCAD/commit/c42f4f644f22a90a7e5d8cc0892f4e630737abc6
Patch18:	c42f4f644f22a90a7e5d8cc0892f4e630737abc6.patch
# Ordinate Dimensions (#2131)
# https://github.com/LibreCAD/LibreCAD/commit/944e6340fe5a1e17a4e44d9de25c78131bfb4cb5
Patch19:	944e6340fe5a1e17a4e44d9de25c78131bfb4cb5.patch
# MText: fixed a division by zero (for libdxfrw this is just a newline cleanup)
# https://github.com/LibreCAD/LibreCAD/commit/5abf92a84416d82978a1bff94736ec7cdc709ad4
Patch20:	5abf92a84416d82978a1bff94736ec7cdc709ad4.patch
# static-analysis warnings
# https://github.com/LibreCAD/LibreCAD/commit/3f16299c1c7a6fec9ff8fc85ce989cbe3bcb9659
Patch21:	3f16299c1c7a6fec9ff8fc85ce989cbe3bcb9659.patch

%description
libdxfrw is a free C++ library to read and write DXF files in both formats,
ASCII and binary form.

%package devel
Summary:	Development files for libdxfrw
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libdxfrw.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
%patch -P1 -p1 -b .aec7b7161087a7783f77369c77c6807b32b5bd2f
%patch -P2 -p1 -b .25c2e472b0cd83e2b7ae28e523b89fe094fbd246
%patch -P3 -p1 -b .6fd84ff6a952ab8a35e6e701ddac23a4c39d9fae
%patch -P4 -p1 -b .4fa20f7db90705ef30705857d404756e6ae48ad0
%patch -P5 -p1 -b .0778a64d9535dc1b04495cf6b8b206ee68509004
%patch -P6 -p1 -b .cb7043c7c44a10dc4a89813faee9357ae21ffac7
%patch -P7 -p1 -b .3e6dbf7eb43ae3f5141ac7a74a75f93105d206ea
%patch -P8 -p1 -b .d7b5b0a30bc096ec7a6802a2806258f9e6e39fea
%patch -P9 -p1 -b .4dc3d5fa4b328873af07be05d7b67e5846628eb7
%patch -P10 -p1 -b .1603a1ac5ef804b50b8fb583662c0bdcbf9ec72c
# LibreCAD 3?
%if 0
%patch -P11 -p1 -b .ab3e44e28b282e3c4d304db37264d0c6e2142ad8
%patch -P12 -p1 -b .7cf1408247e1c03aba86ddebd951d1e413c26fa3
%patch -P13 -p1 -b .05c0f3bd865aae21f453965a504d215a63a02782
%patch -P14 -p1 -b .8b3cf9caf984dff07df2c83f685c9bd7a175df67
%patch -P15 -p1 -b .a46f1967474e7a39cf82e45464000373503fabbe
%patch -P16 -p1 -b .7838da61f71baf93c722c05f7c4c80f802cd06a1
%patch -P17 -p1 -b .3c55e604ea9622bfaac33bbd83ebab3b26293e27
%patch -P18 -p1 -b .c42f4f644f22a90a7e5d8cc0892f4e630737abc6
%patch -P19 -p1 -b .944e6340fe5a1e17a4e44d9de25c78131bfb4cb5
%patch -P20 -p1 -b .5abf92a84416d82978a1bff94736ec7cdc709ad4
%patch -P21 -p1 -b .3f16299c1c7a6fec9ff8fc85ce989cbe3bcb9659
%endif

%build
export CXXFLAGS="%{optflags} -Wno-error=unused-parameter -Wno-error=return-type"
%if 0%{?epel} == 7
%cmake3
%cmake3_build
%else
%if 0%{?buildbin}
%cmake -DLIBDXFRW_BUILD_DWG2DXF=1 -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%else
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DLIBDXFRW_BUILD_DWG2DXF=0
%endif
%cmake_build
%endif

%install
%if 0%{?epel} == 7
%cmake3_install
%else
%cmake_install
%endif

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS ChangeLog README
%if 0%{?buildbin}
%{_bindir}/dwg2dxf
%{_mandir}/man1/dwg2dxf.*
%endif
%{_libdir}/*.so.*

%files devel
%{_includedir}/libdxfrw
%{_libdir}/cmake/libdxfrw
%{_libdir}/*.so
%{_libdir}/pkgconfig/libdxfrw.pc

%changelog
%autochangelog
