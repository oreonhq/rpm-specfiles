%global source0_hash a353cb46e9b1a281061d816353ea010d0a6fe78e6a17aa0b7b74271ca5e4acfc

Name:           libspectrum
Version:        1.5.0
Release:        13%{?dist}
Summary:        A library for reading spectrum emulator file formats
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://fuse-emulator.sourceforge.net/libspectrum.php
Source0:        http://downloads.sourceforge.net/fuse-emulator/%{name}-%{version}.tar.gz
BuildRequires:  audiofile-devel >= 0.2.3
BuildRequires:  bzip2-devel
BuildRequires:  glib2-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  zlib-devel
#required by generate.pl
BuildRequires:  perl
BuildRequires: make

%description
A library for reading various spectrum emulator file formats.

%package devel
Summary:    Development files for libspectrum
Requires:   %{name} = %{version}-%{release}
Requires:   libgcrypt-devel

%description devel
Development files for libspectrum.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"

%ldconfig_scriptlets

%files
%{_libdir}/libspectrum.so.*
%{_mandir}/man3/libspectrum.3*
%doc README ChangeLog THANKS AUTHORS COPYING

%files devel
%exclude %{_libdir}/libspectrum.la
%{_libdir}/libspectrum.so
%{_includedir}/libspectrum.h
%{_libdir}/pkgconfig/libspectrum.pc
%doc doc/libspectrum.txt

%changelog
%autochangelog
