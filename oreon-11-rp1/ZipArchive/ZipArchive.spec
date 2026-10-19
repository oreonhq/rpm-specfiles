%global source0_hash b3e7bc9234c272b250e598b629ff66332eabf624d92ac05cbb77a62667774db8
Name:           ZipArchive
Version:        4.1.2
Release:        31%{?dist}
Summary:        Library for accessing zip files
License:        GPL-2.0-or-later
URL:            http://www.artpol-software.com/ZipArchive/
Source0:        http://www.artpol-software.com/Downloads/ziparchive_src.zip
Patch0:         %{name}-linux-enable.patch
Patch1:         %{name}-autotools.patch
Patch2:         %{name}-system-zlib.patch
Patch3:         %{name}-gcc-4.7.patch 
Patch4:         %{name}-4.1.1-file-attr-fix.patch
Patch5:         %{name}-4.1.1-new-zlib.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
The ZipArchive Library can be used to add compression functionality to your
software. It is written in C++ and offers the following features:
* Compression, decompression and modification of zip archives.
* Segmented archives support (splitting and spanning).
* Unicode support in archives compatible with WinZip.
* Standard zip encryption.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -p1

for i in ZipArchive/*.txt; do
    sed -i.old 's/\r//' "$i"
    touch -r "$i.old" "$i"
done

cd ZipArchive
rm -rf zlib bzip2
sh ./autogen.sh

%build

cd ZipArchive
%configure --disable-static
make %{?_smp_mflags}
%install
cd ZipArchive
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig
install -p -m 644 %{name}.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig
%oreon_autofiles ZipArchive-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ZipArchive-devel -f %{oreon_filedir}/ZipArchive-devel.list

%changelog

%autochangelog
