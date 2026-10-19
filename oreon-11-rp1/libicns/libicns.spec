%global source0_hash 335f10782fc79855cf02beac4926c4bf9f800a742445afbbf7729dab384555c2
Name:           libicns
Version:        0.8.1
Release:        35%{?dist}
Summary:        Library for manipulating Macintosh icns files
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL:            http://icns.sourceforge.net/
Source0:        http://downloads.sourceforge.net/icns/%{name}-%{version}.tar.gz
Patch0:         %{name}-0.8.1-gcc6.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  jasper-devel
BuildRequires:  libpng-devel
BuildRequires:  make
# /oreon:deps
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
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libicns-devel -f %{oreon_filedir}/libicns-devel.list
%files -n libicns-utils -f %{oreon_filedir}/libicns-utils.list

%changelog

%autochangelog
