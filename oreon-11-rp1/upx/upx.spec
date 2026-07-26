%global source0_hash 8eb914115b306fd9fd2110bd3d27ddb8ae7c5a03bb965f7d10f046a3a4ff9dfe

Name:           upx
Version:        5.1.1
Release:        1%{?dist}
Summary:        Ultimate Packer for eXecutables

License:        GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/upx/upx
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}-src.tar.xz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ucl-devel >= 1.01
BuildRequires:  zlib-devel
BuildRequires:  perl-podlators
Provides:       bundled(lzma-sdk) = 4.43

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

%files
%license COPYING LICENSE
%doc NEWS README README.SRC doc/THANKS.txt upx-doc.*
%{_bindir}/upx
%{_mandir}/man1/upx.1*

%changelog
%autochangelog
