%global source0_hash 1bfa998110b351c0b5252ba5bf821b1e93e88a7152708a05c5b5a7adb320066e

# define these if using CVS version
%global cvs_date 2007.04.28
%global cvs_ver +cvs.%cvs_date

Name:           zipios++
Version:        0.1.5.9
Release:        37%{dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
Summary:        C++ library for reading and writing Zip files
Summary(pl.UTF-8): Biblioteka C++ do odczytu i zapisu plików Zip
URL:            http://zipios.sourceforge.net/
# Upstream is dead. Using updated Debian source as they are fixing FTBFS issues.
Source0:        ftp://ftp.debian.org/debian/pool/main/z/%{name}/%{name}_%{version}%{cvs_ver}.orig.tar.gz

# Patches extracted from debian diff
# ftp://ftp.debian.org/debian/pool/main/z/zipios++
Patch0:         zipios++-cstdlib.patch
Patch1:         zipios++-amd64_fix.patch
Patch2:         zipios++-fc16-ptrdiff_t.patch
Patch3:         zipios++-zipinputstreambuff.patch
Patch4:         0001-cppunit-config-no-longer-exists-use-pkg-config.patch
Patch10:        zipios++-zipheadio-size0.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  graphviz
BuildRequires:  ImageMagick
BuildRequires:  doxygen

%description
Zipios++ is a java.util.zip-like C++ library for reading and writing
Zip files. Access to individual entries is provided through standard
C++ iostreams. A simple read-only virtual file system that mounts
regular directories and zip files is also provided.

%description -l pl.UTF-8
Zipios++ jest jak java.util.zip biblioteką C++ do odczytywania oraz
zapisywania plików Zip. Dostęp do pojedyńczych wpisów jest możliwy
poprzez standardowe strumienie we/wy C++. Prosty wirtualny system
plików (tylko do odczytu) montujący regularne katalogi oraz pliki zip
również jest dostarczany.

%package devel
Summary:        Header files for zipios++
Summary(pl.UTF-8): Pliki nagłówkowe zipios++
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libstdc++-devel
Requires:       zlib-devel

%description devel
The header files are only needed for development of programs using the
zipios++.

%description devel -l pl.UTF-8
W pakiecie tym znajdują się pliki nagłówkowe, przeznaczone dla
programistów używających bibliotek zipios++.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}%{cvs_ver}

chmod 0644 COPYING

%build
autoreconf -if
%configure
%make_build
make V=1 doc

%install
%make_install

# Remove static libs
rm -f %{buildroot}%{_libdir}/*.{a,la}

%{ldconfig_scriptlets}

%files
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc doc/html
%{_libdir}/*.so
%{_includedir}/zipios++

%changelog
%autochangelog
