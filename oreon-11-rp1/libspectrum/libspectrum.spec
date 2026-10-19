%global source0_hash 4cce5764227f040238877d9e0ce3aede2bac1b1adfa8ed535d68bb405df395c3
Name:           libspectrum
Version:        1.6.4
Release:        1%{?dist}
Summary:        A library for reading spectrum emulator file formats
License:        GPL-2.0-or-later
URL:            http://fuse-emulator.sourceforge.net/libspectrum.php
Source0:        http://downloads.sourceforge.net/fuse-emulator/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  audiofile-devel
BuildRequires:  bzip2-devel
BuildRequires:  glib2-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libspectrum-devel -f %{oreon_filedir}/libspectrum-devel.list

%changelog

%autochangelog
