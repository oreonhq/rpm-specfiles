%global source0_hash 6344a69fc1ed847d4ed3e272e0da5998948c6b828cb7af39c6321aba6cf88126
%define __cmake_in_source_build 1
Name:           innoextract
Version:        1.9
Release:        1%{?dist}
License:        zlib
Summary:        Tool to extract installers created by Inno Setup
Url:            https://constexpr.org/innoextract/
Source0:        https://constexpr.org/%{name}//files/%{name}-%{version}.tar.gz
Patch0:         innoextract-boost190.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  xz-devel
# /oreon:deps
%description
Inno Setup is a tool to create installers for Microsoft Windows
applications. innoextract allows to extract such installers under
non-windows systems without running the actual installer using wine.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 0 -p1

%build

%cmake \
    -DCMAKE_INSTALL_DATAROOTDIR="%{_datadir}" \
    -DCMAKE_INSTALL_MANDIR="%{_mandir}" \
    -DCMAKE_INSTALL_BINDIR="%{_bindir}" \
    -DUSE_LDGOLD=FALSE \
    .
make %{?_smp_mflags}
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
