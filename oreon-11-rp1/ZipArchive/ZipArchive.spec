%global source0_hash dd41c74090332a70e711e7a680bda22d1e3d33c3defb6b30d775fd0501859a8a

Name:           ZipArchive
Version:        4.1.2
Release:        31%{?dist}
Summary:        Library for accessing zip files

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.artpol-software.com/ZipArchive/
Source0:        http://www.artpol-software.com/Downloads/ziparchive_src.zip
# switch to Linux version
Patch0:         %{name}-linux-enable.patch
# add autotooled build system
Patch1:         %{name}-autotools.patch
# use system zlib
Patch2:         %{name}-system-zlib.patch
# Fix building with gcc-4.7
Patch3:         %{name}-gcc-4.7.patch 
# Fix ZipArchive not recognising dirs as such in some zips
Patch4:         %{name}-4.1.1-file-attr-fix.patch
# Fix ZipArchive not building with latest version of zlib
Patch5:         %{name}-4.1.1-new-zlib.patch

BuildRequires: make
BuildRequires:  libtool
BuildRequires:  zlib-devel
BuildRequires:  gcc-c++

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

%files
%doc ZipArchive/License.txt
%{_libdir}/libziparch-%{version}.so

%files devel
%doc ZipArchive/{Appnote.txt,_readme.txt}
%{_includedir}/ZipArchive/
%{_libdir}/libziparch.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
