%global source0_hash b6a98797e4fb9c9a705f5d53112aa5214561857e929a644928b9e658930d9440
%global abi 4
Name: libxmp
Version: 4.7.3
Release:        1%{?dist}
Summary:        A multi-format module playback library
Source0:        https://downloads.sourceforge.net/project/xmp/libxmp/%{version}/libxmp-%{version}.tar.gz
Provides: bundled(md5-plumb)
License: 0BSD AND BSD-3-Clause AND ISC AND MIT AND LicenseRef-Fedora-Public-Domain
URL: http://xmp.sourceforge.net/
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Libxmp is a library that renders module files to PCM data. It supports
over 90 mainstream and obscure module formats including Protracker (MOD),
Scream Tracker 3 (S3M), Fast Tracker II (XM), and Impulse Tracker (IT).

Many compressed module formats are supported, including popular Unix, DOS,
and Amiga file packers including gzip, bzip2, SQSH, Powerpack, etc.

%package devel
Summary: A multi-format module playback library development files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake-filesystem
%description devel
Libxmp is a library that renders module files to PCM data. It supports
over 90 mainstream and obscure module formats including Protracker (MOD),
Scream Tracker 3 (S3M), Fast Tracker II (XM), and Impulse Tracker (IT).

Many compressed module formats are supported, including popular Unix, DOS,
and Amiga file packers including gzip, bzip2, SQSH, Powerpack, etc.

This package contains the header and development library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
for file in docs/Changelog ; do
        iconv -f iso8859-1 -t utf8 -o $file.utf $file && touch -r $file $file.utf && mv $file.utf $file
done

%build

%configure
%make_build
%install
%make_install
install -Dpm644 docs/libxmp.3 %{buildroot}%{_mandir}/man3/libxmp.3
chmod 755 %{buildroot}%{_libdir}/libxmp.so.*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%make_build check
%files -f %{oreon_filedir}/main.list
%files -n libxmp-devel -f %{oreon_filedir}/libxmp-devel.list

%changelog

%autochangelog
