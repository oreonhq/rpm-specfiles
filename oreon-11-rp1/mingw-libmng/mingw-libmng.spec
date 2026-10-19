%global source0_hash cf112a1fb02f5b1c0fce5cab11ea8243852c139e669c44014125874b14b7dfaa
%{?mingw_package_header}
%global pkgname libmng
Name:          mingw-%{pkgname}
Version:       2.0.3
Release:        1%{?dist}
Summary:        MinGW Windows libmng library
License:       Zlib
BuildArch:     noarch
URL:           http://www.libmng.com/
Source0:        http://download.sourceforge.net/sourceforge/%{pkgname}/%{pkgname}-%{version}.tar.gz
Patch0:        libmng_no-undefined.patch
Patch1:        libmng_deprecated-macro.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-lcms2
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-lcms2
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw64-zlib
# /oreon:deps
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

rm -f config.status
./bootstrap.sh
sed -i 's|-specs=/usr/lib/rpm/redhat/redhat-hardened-ld||g' ltmain.sh
%mingw_configure
%mingw_make_build
%install
%mingw_make_install
find %{buildroot} -name '*.la' -delete
rm -rf %{buildroot}%{mingw32_datadir}
rm -rf %{buildroot}%{mingw64_datadir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libmng -f %{oreon_filedir}/mingw32-libmng.list
%files -n mingw32-libmng-static -f %{oreon_filedir}/mingw32-libmng-static.list
%files -n mingw64-libmng -f %{oreon_filedir}/mingw64-libmng.list
%files -n mingw64-libmng-static -f %{oreon_filedir}/mingw64-libmng-static.list

%changelog

%autochangelog
