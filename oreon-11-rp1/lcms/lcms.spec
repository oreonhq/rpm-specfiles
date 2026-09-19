%global source0_hash 80ae32cb9f568af4dc7ee4d3c05a4c31fc513fc3e31730fed0ce7378237273a9

%global build_type_safety_c 2

Name:           lcms
Version:        1.19
Release:        43%{?dist}

Summary:        Color Management System
License:        MIT
URL:            http://www.littlecms.com/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

Patch0:         %{name}-1.19-rhbz675186.patch
# bug 992979 / CVE-2013-4276
# Stack-based buffer overflows in ColorSpace conversion calculator
# and TIFF compare utility
Patch1:         %{name}-1.19-rhbz991757.patch
# bug 1003950
Patch2:         %{name}-1.19-rhbz1003950.patch
Patch3: lcms-c99.patch

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  swig >= 1.3.12
BuildRequires:  zlib-devel

Provides:       littlecms%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

# This package is provided only for foo2zjs. No other packages should depend on it.
Provides:       deprecated()

%description
LittleCMS intends to be a small-footprint, speed optimized color management
engine in open source form.

%package        libs
Summary:        Library for %{name}
Provides:       littlecms-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       deprecated()

%description    libs
The %{name}-libs package contains library for %{name}.

%package        devel
Summary:        Development files for LittleCMS
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       littlecms-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       deprecated()

%description    devel
Development files for LittleCMS.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
find . -type f -name '*.[ch]' -exec chmod -x '{}' \;
chmod 0644 AUTHORS COPYING ChangeLog NEWS README.1ST doc/TUTORIAL.TXT doc/LCMSAPI.TXT

# Convert not UTF-8 files
pushd doc
mkdir -p __temp
for f in LCMSAPI.TXT TUTORIAL.TXT ;do
cp -p $f __temp/$f
iconv -f ISO-8859-1 -t UTF-8 __temp/$f > $f
touch -r __temp/$f $f
done
rm -rf __temp
popd

%build
%configure --without-python --disable-static
# remove rpath from libtool
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install
find %{buildroot} -type f -name '*.la' -delete

%files
%doc README.1ST ChangeLog doc/TUTORIAL.TXT
%license AUTHORS COPYING
%{_bindir}/*
%{_mandir}/man1/*.1*

%files libs
%doc NEWS
%license AUTHORS COPYING
%{_libdir}/lib%{name}.so.1*

%files devel
%doc doc/LCMSAPI.TXT
%{_includedir}/*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
