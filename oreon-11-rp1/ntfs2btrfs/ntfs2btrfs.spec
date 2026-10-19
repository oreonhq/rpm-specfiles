%global source0_hash be3d2deb3c042c862df3ca75b46245300f45e279206bddabd8aa1fc8c92c1a58
%bcond ix86 0
Name:           ntfs2btrfs
Version:        20260810
Release:        1%{?dist}
Summary:        Conversion tool from NTFS to Btrfs
License:        GPL-2.0-or-later
URL:            https://github.com/maharmstone/ntfs2btrfs
Source0:        https://github.com/maharmstone/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Provides:       bundled(ntfs-3g-system-compression)
ExcludeArch:    %{shrink:
%if %{without ix86}
  %{ix86}
%endif
  ppc64
  s390x
}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(fmt)
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  zlib-devel
# /oreon:deps
%description
ntfs2btrfs is a tool which does in-place conversion of Microsoft's NTFS
filesystem to the open-source filesystem Btrfs, much as btrfs-convert
does for ext2.

The original image is saved as a reflink copy at image/ntfs.img,
and if you want to keep the conversion you can delete this to
free up space.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
