%global source0_hash cf85f373f09e9177c0b21dbfbb427efaedc02d035d2aade65eb58a3cbf9ad267

# https://github.com/sgan81/apfs-fuse/issues/164
%global _lto_cflags %nil

# Force out of source build
%undefine __cmake_in_source_build

%global date         20200928
%global gittag       ee71aa5c87c0831c1ae17048951fe9cd7579c3db
%global short_gittag %(c=%{gittag}; echo ${c:0:7})

Name:          apfs-fuse
Summary:       A read-only FUSE driver for Apple's APFS
Version:       0
Release:       33.%{date}git%{short_gittag}%{?dist}
License:       GPL-2.0-or-later
URL:           https://github.com/sgan81/apfs-fuse
Source0:       https://github.com/sgan81/%{name}/archive/%{short_gittag}/%{name}-%{short_gittag}.tar.gz
Source1:       https://github.com/lzfse/lzfse/archive/lzfse-1.0.tar.gz
# Add missing header to fix the build
Patch:         https://github.com/sgan81/apfs-fuse/pull/205.patch
Provides:      bundled(lzfse) = 1.0
Requires:      fuse3
BuildRequires: gcc gcc-c++
BuildRequires: fuse3-devel libicu-devel zlib-devel bzip2-devel
BuildRequires: cmake git

%description
apfs-fuse is a read-only driver for the new Apple File System, APFS. Since
Apple didn't document the disk format, this driver should be considered
experimental. Not all compression methods are supported yet, thus the driver
may return compressed files instead of uncompressed ones.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{gittag} -S git
cd 3rdparty
rmdir lzfse
tar zxf %{SOURCE1}
mv lzfse-* lzfse

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
mkdir -p %{buildroot}/%{_bindir}
cp -a %{_vpath_builddir}/apfs* %{buildroot}/%{_bindir}/

mkdir -p %{buildroot}/%{_sbindir}
ln -sr %{buildroot}/%{_bindir}/apfs-fuse %{buildroot}/%{_sbindir}/mount.apfs

%files
%{_bindir}/apfs*
%{_sbindir}/mount.apfs
%doc README.md
%license LICENSE

%changelog
%autochangelog
