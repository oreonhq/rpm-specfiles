%global source0_hash 685d6b3342b9928e23e87bbd88f914af125697c3db504f96a013d168b6afbf2e

# EFI/UEFI binaries are not ELF, but PE32/PE32+/COFF
%global debug_package %{nil}

# Disable Linux build flags because it breaks EFI binary build
%undefine _auto_set_build_flags
%global set_build_flags %{nil}
%global _cmake_shared_libs %{nil}

%global commit a17333f691c39e48cc3eac2eb251cf5b2f67e399
%global commitdate 20251111
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global madler_zlib_ver 1.3.2
%global madler_zlib_tag v%{madler_zlib_ver}
%global zstd_ver 1.5.7
%global zstd_tag v%{zstd_ver}

Name:           btrfs-efi
Version:        20230328^git%{commitdate}.%{shortcommit}
Release:        1%{?dist}
Summary:        EFI driver to enable Btrfs support

License:        LGPL-2.1-or-later
URL:            https://github.com/maharmstone/btrfs-efi
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:        https://github.com/madler/zlib/archive/%{madler_zlib_tag}/zlib-%{madler_zlib_ver}.tar.gz
Source2:        https://github.com/facebook/zstd/archive/%{zstd_tag}/zstd-%{zstd_ver}.tar.gz

# Fix with native GCC
## Proposed upstream: https://github.com/maharmstone/btrfs-efi/pull/5
Patch:          0001-cmake-Refactor-to-use-an-EFI-building-module.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  gnu-efi-devel >= 3.0.18
BuildRequires:  make

ExclusiveArch:  %{efi}

%description
%{summary}.

%dnl -------------------------------------------------------------

%package unsigned-%{efi_arch}
Summary:        EFI driver for %{efi_arch} to enable Btrfs support
License:        LGPL-2.1-or-later AND Zlib AND BSD-3-Clause AND BSD-2-Clause
Requires:       efi-filesystem
Provides:       %{name}-driver-%{efi_arch}
Conflicts:      %{name}-driver-%{efi_arch}
# Modified versions for building in the EFI driver
Provides:       bundled(lzo)
Provides:       bundled(xxhash)
Provides:       bundled(madler_zlib) = %{madler_zlib_ver}
Provides:       bundled(zstd) = %{zstd_ver}

BuildArch:      noarch

%description unsigned-%{efi_arch}
%{summary}.

%files unsigned-%{efi_arch}
%license LICENCE
%doc README.md
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/btrfs%{efi_arch}.efi

%dnl -------------------------------------------------------------

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -S git_am
mkdir -p src/{zlib,zstd}
tar -C src/zlib --strip-components=1 -xf %{S:1}
tar -C src/zstd --strip-components=1 -xf %{S:2}

%conf
%cmake

%build
%cmake_build

%install
%cmake_install

%changelog
%autochangelog
