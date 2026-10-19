%global source2_hash f28314aa33159c5c82cfae3eb4f6012be2775ebf1a4fb8e5c6c10233339c0e17
%global source1_hash b6b3f40991ec85500b4294cabe58b971ff5b37b6adbe153cbd382e914b664065
%global source0_hash fc0f1eb6b6766470326f2c014693809190e67dba84274a6fbae9d4912d066706
Name:           libmd
Version:        1.3.0
Release:        1%{?dist}
Summary:        Library that provides message digest functions from BSD systems
License:        BSD-2-Clause AND BSD-3-Clause AND ISC AND Beerware AND LicenseRef-Fedora-Public-Domain
URL:            https://www.hadrons.org/software/libmd/
Source0:        https://libbsd.freedesktop.org/releases/%{name}-%{version}.tar.xz
Source1:        https://libbsd.freedesktop.org/releases/%{name}-%{version}.tar.xz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/4F3E74F436050C10F5696574B972BF3EA4AE57A3
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
# /oreon:deps
%description
The libmd library provides a few message digest ("hash") functions, as
found on various BSD systems, either on their libc or on a library with
the same name, and with a compatible API.

%package devel
Summary:        Development files for the message digest library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description devel
The libmd-devel package includes header files and libraries necessary
for developing programs which use the message digest library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%build

%configure --disable-static
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libmd-devel -f %{oreon_filedir}/libmd-devel.list

%changelog

%autochangelog
