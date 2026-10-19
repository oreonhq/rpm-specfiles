%global source1_hash 6f017c31cf5d42f194a16d4f291f7f2937be1687dbd47e46bd9b76ab89ff0d88
%global source0_hash afa064f70433008ec9837fb601c8d73e73db07856e4566f8bee010758c5304ac
Name:           SILLY
Version:        0.1.0
Release:        44%{?dist}
Summary:        Simple and easy to use library for image loading
License:        MIT
URL:            http://www.cegui.org.uk
Source0:        http://downloads.sourceforge.net/crayzedsgui/%{name}-%{version}.tar.gz
Source1:        http://downloads.sourceforge.net/crayzedsgui/%{name}-DOCS-%{version}.tar.gz
Patch0:         SILLY-0.1.0-libpng15.patch
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  make
# /oreon:deps
%description
The Simple Image Loading LibrarY is a companion library of the CEGUI project.
It provides a simple and easy to use library for image loading.

It currently supports the following formats:
TGA (Targa)
JPEG (Joint Photographic Experts Group)
PNG (Portable Network Graphics)

%package devel
Summary:        Development files for SILLY
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for SILLY

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a1
%patch -P0 -p1

# Don't use full path, otherwise it shows buildroot as part of the path
sed -i 's|\(FULL_PATH_NAMES[ \t][ \t]*= \)YES|\1NO|' Doxyfile

# Get rid of some useless noise
sed -i 's|\(WARNINGS[ \t][ \t]*= \)YES|\1NO|' Doxyfile
sed -i 's|\(WARN_IF_UNDOCUMENTED[ \t][ \t]*= \)YES|\1NO|' Doxyfile
sed -i 's|\(WARN_IF_DOC_ERROR[ \t][ \t]*= \)YES|\1NO|' Doxyfile

# Generate developer man pages
sed -i 's|\(GENERATE_MAN[ \t][ \t]*= \)NO|\1YES|' Doxyfile

# Multiarch hack, we are now using prebuilt HTML
sed -i 's|\(GENERATE_HTML[ \t][ \t]*= \)YES|\1NO|' Doxyfile

#Fix encoding on AUTHORS
iconv -f iso8859-1 AUTHORS -t utf8 > AUTHORS.conv && /bin/mv -f AUTHORS.conv AUTHORS

%build

%configure --disable-static --with-pic
make %{?_smp_mflags}
doxygen
%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
mkdir -p %{buildroot}%{_mandir}/man3
cp -a doc/man/man3/* %{buildroot}%{_mandir}/man3
chmod 0755 %{buildroot}%{_libdir}/*.so.*
%ldconfig_scriptlets
%oreon_autofiles SILLY-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n SILLY-devel -f %{oreon_filedir}/SILLY-devel.list

%changelog

%autochangelog
