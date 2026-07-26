%global source0_hash 335f10782fc79855cf02beac4926c4bf9f800a742445afbbf7729dab384555c2

Name:           libicns
Version:        0.8.1
Release:        35%{?dist}
Summary:        Library for manipulating Macintosh icns files

# libicns, icns2png and icontainer2icns are under LGPLv2+
# png2icns is under GPLv2+
# Automatically converted from old format: LGPLv2+ and GPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL:            http://icns.sourceforge.net/
Source0:        http://downloads.sourceforge.net/icns/%{name}-%{version}.tar.gz
# Fix compiling with gcc6
# Patch is already in upstream git
Patch0:         %{name}-0.8.1-gcc6.patch

BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  jasper-devel
BuildRequires: make

%description
libicns is a library providing functionality for easily reading and 
writing Macintosh icns files

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        utils
Summary:        Utilities for %{name}
Requires:       %{name} = %{version}-%{release}

%description    utils
icns2png - convert Mac OS icns files to png images
png2icns - convert png images to Mac OS icns files
icontainer2icns - extract icns files from icontainers 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build
%configure --disable-static
# disable rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README TODO
%license COPYING COPYING.LGPL-2 COPYING.LGPL-2.1
%{_libdir}/*.so.*

%files devel
%doc src/apidocs.*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%files utils
%{_bindir}/*
%{_mandir}/man1/*
%doc README

%changelog
%autochangelog
