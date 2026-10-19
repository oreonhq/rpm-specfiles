%global source2_hash 339b2aeb2708447658502336bde42a64ffba199ea26fbf04766768e57815b124
%global source1_hash 62d7a8823c0f2bd519f16df4e55fcf38f96a65dc75019cd708d1ab9bafd9c0a0
%global source0_hash 5a83dbab402390695367cf1ea456140e51ff68171cbc0352ceba4be227715e07
Name:           iec16022
Version:        0.3.1
Release:        1%{?dist}
Summary:        Generate ISO/IEC 16022 2D barcodes
License:        GPL-2.0-or-later
URL:            https://github.com/rdoeffinger/iec16022
Source0:        https://github.com/rdoeffinger/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/rdoeffinger/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/C61D16E59E2CD10C895838A40899A2B906D4D9C7
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  popt-devel
# /oreon:deps
%description
The iec16022 is a program for producing ISO/IEC 16022 2D barcodes, also
known as Data Matrix. These barcodes are defined in the ISO/IEC 16022
standard.

%package        libs
Summary:        ISO/IEC 16022 libraries
%description    libs
The iec16022-libs package provides libraries for producing ISO/IEC 16022
2D barcodes, also known as Data Matrix. These barcodes are defined in the
ISO/IEC 16022 standard.

%package        devel
Summary:        Development files for the iec16022 library
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description    devel
The iec16022-devel package includes header files and libraries necessary
for developing programs which use the iec16022 C library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build

%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/libiec16022.la
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}
make -C test check
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n iec16022-libs -f %{oreon_filedir}/iec16022-libs.list
%files -n iec16022-devel -f %{oreon_filedir}/iec16022-devel.list

%changelog

%autochangelog
