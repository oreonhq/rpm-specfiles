%global source0_hash a7d457be4ef942e46844ee8f301206b111394cbcbde3599747a6904c54ff116b
Name:           upx
Version:        5.2.1
Release:        1%{?dist}
Summary:        Ultimate Packer for eXecutables
License:        GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/upx/upx
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}-src.tar.xz
Provides:       bundled(lzma-sdk) = 4.43
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-podlators
BuildRequires:  ucl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
UPX is a free, portable, extendable, high-performance executable
packer for several different executable formats. It achieves an
excellent compression ratio and offers very fast decompression. Your
executables suffer no memory overhead or other drawbacks.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{version}-src

%build

%cmake
%cmake_build
%install
%cmake_install
mv %{buildroot}%{_datadir}/doc/upx/upx-doc.* .
rm -f %{buildroot}%{_datadir}/doc/upx/*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
