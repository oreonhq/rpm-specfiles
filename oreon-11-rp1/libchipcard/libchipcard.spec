%global source1_hash 61fa18f1c3e137ff9e4843f562f47895d312350294f4cf71e65116b3005c8b92
%global source0_hash 6c07f527417f7562074f99012da4d11eb4dbafd33f49e66b442ccd6e3b8cfd20
Name: libchipcard
Summary:        A library for easy access to smart cards (chipcards)
Version: 5.1.6
Release:        13%{?dist}
Source0:        https://www.aquamaniac.de/rdm/attachments/download/382/libchipcard-%{version}.tar.gz
Source1: https://www.aquamaniac.de/rdm/attachments/download/381/libchipcard-%{version}.tar.gz.asc
Source2: keyfile.asc
License: LGPL-2.0-only and GPL-2.0-or-later and LGPL-2.1-or-later
URL: https://www.aquamaniac.de/rdm/projects/libchipcard
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  gwenhywfar-devel
BuildRequires:  libsysfs-devel
BuildRequires:  pcsc-lite-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description 
Libchipcard allows easy access to smart cards. It provides basic access
to memory and processor cards and has special support for German medical
cards, German "GeldKarte" and FinTS (homebanking, formerly known as HBCI) 
cards (both type 0 and type 1).
It accesses the readers via CTAPI or IFD interfaces and has successfully
been tested with Towitoko, Kobil, SCM, Orga, Omnikey and Reiner-SCT readers.
This package contains the chipcard-daemon needed to access card readers.

%package devel
Summary: Development headers for libchipcard
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gwenhywfar-devel
%description devel
This package contains chipcard-config and header files for writing
drivers, services or even your own chipcard daemon for LibChipCard.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%build

%configure \
  --disable-static
%make_build
%install
%make_install
rm -fv %{buildroot}%{_libdir}/lib*.la
pushd tutorials
make clean
rm -rf .deps
rm -f Makefile*
popd
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libchipcard-devel -f %{oreon_filedir}/libchipcard-devel.list

%changelog

%autochangelog
