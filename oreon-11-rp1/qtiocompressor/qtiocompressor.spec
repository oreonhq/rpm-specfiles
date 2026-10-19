%global source0_hash 76adedd641b6d5fd03ae44abdefb0a7f5f092029f3bf84cb5daa412ca7a371d8
%global upstreamver 2.3_1-opensource
Summary:        QIODevice that compresses data streams
Name:       qtiocompressor
Version:    2.3.1
Release:        1%{?dist}
License:    GPL-3.0-only OR LGPL-2.1-only WITH Digia-Qt-LGPL-exception-1.1
URL:        http://qt.nokia.com/products/appdev/add-on-products/catalog/4/Utilities/qtiocompressor/
Source0:        https://fale.fedorapeople.org/%{name}/%{name}-%{upstreamver}.tar.gz
Source1:    qtiocompressor.prf
Patch0:     qtiocompressor-qt6.patch
# oreon:deps
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The class works on top of a QIODevice subclass, compressing data before it is
written and decompressing it when it is read. Since QtIOCompressor works on
streams, it does not have to see the entire data set before compressing or
decompressing it. This can reduce the memory requirements when working on large
data sets.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   qt6-qtbase-devel
%description devel
This package contains libraries and header files for developing applications
that use QtIOCompressor.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{upstreamver}

# Drop 'examples' from SUBDIRS to avoid build errors due to missing -lz
sed -i '/SUBDIRS.*examples/d' qtiocompressor.pro

%build

touch .licenseAccepted
./configure -library
%{qmake_qt6}
%make_build
%install
mkdir -p %{buildroot}%{_qt6_libdir}
cp -a lib/* %{buildroot}%{_qt6_libdir}
chmod 755 %{buildroot}%{_qt6_libdir}/*.so.*.*.*
mkdir -p %{buildroot}%{_qt6_headerdir}/QtSolutions
cp -a \
    src/qtiocompressor.h \
    src/QtIOCompressor \
    %{buildroot}%{_qt6_headerdir}/QtSolutions
mkdir -p %{buildroot}%{_qt6_libdir}/qt6/mkspecs/features/
cp -a %{SOURCE1} %{buildroot}%{_qt6_libdir}/qt6/mkspecs/features/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n qtiocompressor-devel -f %{oreon_filedir}/qtiocompressor-devel.list

%changelog

%autochangelog
