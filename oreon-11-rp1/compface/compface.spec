%global source0_hash a6998245f530217b800f33e01656be8d1f0445632295afa100e5c1611e4f6825
Name:           compface
Version:        1.5.2
Release:        1%{?dist}
Summary:        Library and tools for handling X-Face data
License:        LicenseRef-compface
URL:            http://ftp.xemacs.org/pub/xemacs/aux/
Source0:        http://ftp.xemacs.org/pub/xemacs/aux/%{name}-%{version}.tar.gz
Source1:        compface-test.xbm
Source2:        compface-README.copyright
Patch0:         libcompface_1.5.2-4.diff.gz
Patch1:         compface-1.5.2-stack-smashing.patch
Patch2:         compface-1.5.2-build.patch
Patch3: compface-configure-c99.patch
Patch4: compface-c99.patch
# oreon:deps
BuildRequires:  diffutils
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
This is the Compface image compression and decompression library and its
user tools. Compface converts 48x48 .xbm format (X bitmap) images to a
compressed format that can be placed in the X-Face: mail header. Some mail
programs are able to display such images when opening messages.

%package        devel
Summary:        Library and development files for handling X-Face data 
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
These files are needed when building software that uses the Compface
library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1 -b .stack-smashing
%patch -P2 -p0
%patch -P3 -p1
%patch -P4 -p1

%build

CFLAGS="$RPM_OPT_FLAGS -fPIC" %configure
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT STRIP=/bin/true
mkdir -p _extdoc && install -p -m 0644 %{SOURCE2} _extdoc/README.copyright
%oreon_autofiles compface-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}:$LD_LIBRARY_PATH
./compface %{SOURCE1} | ./uncompface -X > __test.xbm
cmp %{SOURCE1} __test.xbm
%files -f %{oreon_filedir}/main.list
%files -n compface-devel -f %{oreon_filedir}/compface-devel.list

%changelog

%autochangelog
