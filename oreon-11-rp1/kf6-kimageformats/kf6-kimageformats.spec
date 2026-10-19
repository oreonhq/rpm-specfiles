%global source1_hash b0dc7dca867cf904f8c134e1516eb9ccd92abf3026597021ececb86903dbfbcf
%global source0_hash f74ea9ede7877afb66f4d7dea567f074bf63d806a824c87a9d9067d05848a316
%undefine __cmake_in_source_build
%global framework kimageformats
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:           kf6-%{framework}
Version:        6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon with additional image plugins for QtGui
License:        LGPLv2+
URL:            https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:       kf6-filesystem
Requires:       openexr-libs%{?_isa}
Requires:       LibRaw%{?_isa}
Recommends:     poppler-utils
Recommends:     ghostscript
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(OpenEXR)
BuildRequires:  cmake(OpenJPEG)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(libavif)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  jxrlib-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  openexr-devel
BuildRequires:  openjpeg-tools
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libraw_r)
# /oreon:deps
%description
This framework provides additional image format plugins for QtGui.  As
such it is not required for the compilation of any other software, but
may be a runtime requirement for Qt-based software to support certain
image formats.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf6 \
  -DKIMAGEFORMATS_HEIF:BOOL=ON \
  -DKIMAGEFORMATS_JXR:BOOL=ON
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-kimageformats-devel -f %{oreon_filedir}/kf6-kimageformats-devel.list

%changelog

%autochangelog
