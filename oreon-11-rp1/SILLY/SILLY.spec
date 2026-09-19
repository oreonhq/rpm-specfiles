%global source0_hash 6f017c31cf5d42f194a16d4f291f7f2937be1687dbd47e46bd9b76ab89ff0d88

Name:           SILLY
Version:        0.1.0
Release:        44%{?dist}
Summary:        Simple and easy to use library for image loading
License:        MIT
URL:            http://www.cegui.org.uk
Source0:        http://downloads.sourceforge.net/crayzedsgui/%{name}-%{version}.tar.gz
Source1:        http://downloads.sourceforge.net/crayzedsgui/%{name}-DOCS-%{version}.tar.gz
Patch0:         SILLY-0.1.0-libpng15.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  doxygen
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel

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

#Build developer documentation
doxygen

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

#Install man pages
mkdir -p %{buildroot}%{_mandir}/man3
cp -a doc/man/man3/* %{buildroot}%{_mandir}/man3

#Fix so that RPM's strip works (only strips files marked executable)
chmod 0755 %{buildroot}%{_libdir}/*.so.*

%ldconfig_scriptlets

%files
%{_libdir}/*.so.*
%exclude %{_libdir}/*.la
%doc AUTHORS ChangeLog COPYING

%files devel
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*
%doc %{name}-%{version}/doc/html

%changelog
%autochangelog
