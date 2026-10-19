%global source1_hash b0d4dcf25b78163b7a58e16f12d8ac72aa2723712895e0778d6f06606b516f1f
%global source0_hash 4709f05395ccbad6c0a5b40a4619d60aafe3473b1a79bafb3aa700b1f756fd63
Name:           fuse-encfs
Version:        1.9.5
Release:        1%{?dist}
Summary:        Encrypted pass-thru filesystem in userspace
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Url:            https://github.com/vgough/encfs
Source0:        https://github.com/vgough/encfs/releases/download/v%{version}/encfs-%{version}.tar.gz
Source1:        https://github.com/vgough/encfs/releases/download/v%{version}/encfs-%{version}.tar.gz.asc
Source2:        895F5BC123A02740.gpg
Requires:       fuse >= 2.6
Provides:       encfs = %{version}-%{release}
Provides:       encfs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gnupg2
BuildRequires:  libattr-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel-engine
BuildRequires:  perl(Locale::TextDomain)
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(tinyxml2)
# /oreon:deps
%description
EncFS implements an encrypted filesystem in userspace using FUSE.  FUSE
provides a Linux kernel module which allows virtual filesystems to be written
in userspace.  EncFS encrypts all data and filenames in the filesystem and
passes access through to the underlying filesystem.  Similar to CFS except that
it does not use NFS.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n encfs-%{version}
rm -rf vendor/github.com/leethomasson
mkdir %{_target_platform}

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
    -DCMAKE_SKIP_RPATH=ON \
    -DBUILD_STATIC_LIBS=OFF \
    -DBUILD_SHARED_LIBS=ON \
    -DINSTALL_LIBENCFS=ON \
    -DUSE_INTERNAL_TINYXML=OFF
%cmake_build
%install
%cmake_install
rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/*.so
%find_lang encfs
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
