%global source0_hash 700b76b97695b2fab4ef8c79619c68ae57d09e0c130724791cafbd39e0eb4aef
Name:           exiv2
Version:        0.28.9
Release:        1%{?dist}
Summary:        Exif, IPTC and XMP metadata manipulation library
License:        GPL-2.0-or-later AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL:            http://www.exiv2.org/
VCS:            https://github.com/Exiv2/exiv2/
%if 0%{?beta:1}
Source0:        https://github.com/Exiv2/%{name}//archive/v%{version}/%{name}-%{version}.tar.gz
%else
%endif
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  graphviz
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(INIReader)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
A command line utility to access image metadata, allowing one to:
* print the Exif metadata of Jpeg images as summary info, interpreted values,
  or the plain data for each tag
* print the Iptc metadata of Jpeg images
* print the Jpeg comment of Jpeg images
* set, add and delete Exif and Iptc metadata of Jpeg images
* adjust the Exif timestamp (that's how it all started...)
* rename Exif image files according to the Exif timestamp
* extract, insert and delete Exif metadata (including thumbnails),
  Iptc metadata and Jpeg comments

%package      devel
Summary:      Header files, libraries and development documentation for %{name}
Requires:     %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description  devel
%{summary}.

%package      libs
Summary:      Exif, IPTC and XMP metadata manipulation library
Recommends:   %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description  libs
A C++ library to access image metadata, supporting full read and write access
to the Exif and Iptc metadata, Exif MakerNote support, extract and delete
methods for Exif thumbnails, classes to access Ifd and so on.

%package      doc
Summary:      API documentation for %{name}
License:      MIT AND GPL-2.0-only
BuildArch:    noarch
%description  doc
%{summary}.

API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version}%{?beta:-%{beta}} -p1

%build

%cmake \
  -DCMAKE_INSTALL_DOCDIR="%{_pkgdocdir}" \
  -DEXIV2_BUILD_DOC:BOOL=ON \
  -DEXIV2_BUILD_SAMPLES:BOOL=OFF \
  -DEXIV2_ENABLE_NLS:BOOL=ON
%cmake_build
%cmake_build --target doc
%install
%cmake_install
%find_lang exiv2 --with-man
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export PKG_CONFIG_PATH="%{buildroot}%{_libdir}/pkgconfig${PKG_CONFIG_PATH:+:}${PKG_CONFIG_PATH}"
test "$(pkg-config --modversion exiv2)" = "%{version}"
test "$(pkg-config --variable=libdir exiv2)" = "%{_libdir}"
test -x %{buildroot}%{_libdir}/libexiv2.so
%files -f %{oreon_filedir}/main.list
%files -n exiv2-devel -f %{oreon_filedir}/exiv2-devel.list
%files -n exiv2-libs -f %{oreon_filedir}/exiv2-libs.list
%files -n exiv2-doc -f %{oreon_filedir}/exiv2-doc.list

%changelog

%autochangelog
