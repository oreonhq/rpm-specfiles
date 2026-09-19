%global source0_hash cf112a1fb02f5b1c0fce5cab11ea8243852c139e669c44014125874b14b7dfaa

%{?mingw_package_header}

%global pkgname libmng

Name:          mingw-%{pkgname}
Version:       2.0.3
Release:       24%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       Zlib
BuildArch:     noarch
URL:           http://www.libmng.com/
Source0:       http://download.sourceforge.net/sourceforge/%{pkgname}/%{pkgname}-%{version}.tar.gz
# Add -no-undefined to linker flags
Patch0:        libmng_no-undefined.patch
# Replace deprecated configure.ac macro
Patch1:        libmng_deprecated-macro.patch

BuildRequires: make
BuildRequires: libtool autoconf automake

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-libjpeg-turbo
BuildRequires: mingw32-lcms2
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-libjpeg-turbo
BuildRequires: mingw64-lcms2
BuildRequires: mingw64-zlib

%description
MinGW Windows %{pkgname} library

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
%{summary}.

%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
%{summary}.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
%{summary}.

%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-static
%{summary}.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkgname}-%{version}
%patch -P0 -p1
%patch -P1 -p1

# Delete pre-built library
rm -f bcb/win32dll/libmng.dll

%build
# Hack to stop configure complaining about already configured source tree
rm -f config.status
./bootstrap.sh
# Hack for rhbz#1214506
sed -i 's|-specs=/usr/lib/rpm/redhat/redhat-hardened-ld||g' ltmain.sh

%mingw_configure
%mingw_make_build

%install
%mingw_make_install

# Delete *.la files
find %{buildroot} -name '*.la' -delete

# Delete man pages
rm -rf %{buildroot}%{mingw32_datadir}
rm -rf %{buildroot}%{mingw64_datadir}

%files -n mingw32-%{pkgname}
%license LICENSE
%{mingw32_bindir}/libmng-2.dll
%{mingw32_includedir}/libmng*.h
%{mingw32_libdir}/libmng.dll.a
%{mingw32_libdir}/pkgconfig/libmng.pc

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libmng.a

%files -n mingw64-%{pkgname}
%license LICENSE
%{mingw64_bindir}/libmng-2.dll
%{mingw64_includedir}/libmng*.h
%{mingw64_libdir}/libmng.dll.a
%{mingw64_libdir}/pkgconfig/libmng.pc

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libmng.a

%changelog
%autochangelog
