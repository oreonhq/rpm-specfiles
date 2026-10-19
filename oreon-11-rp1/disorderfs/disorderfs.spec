%global source2_hash 7d0051d4b6a72cef4e00ae84b75795cc5076ae88ed6d2d920290a21281363e0d
%global source1_hash ba22ccfa49344c4dfcb0223e83a2b90bf5885329f4d00c2c4edfa9f069b94fc6
%global source0_hash d0c27cf09e3029873c146c66403177f7dafc91e6639fd95b232846b195f72ad0
Name:           disorderfs
Version:        0.6.2
Release:        1%{?dist}
Summary:        FUSE filesystem that introduces non-determinism
URL:            https://salsa.debian.org/reproducible-builds/%{name}
License:        GPL-3.0-or-later
Source0:        https://reproducible-builds.org/_lfs/releases/%{name}/%{name}-%{version}.tar.bz2
Source1:        https://reproducible-builds.org/_lfs/releases/%{name}/%{name}-%{version}.tar.bz2.asc
Source2:        https://salsa.debian.org/reproducible-builds/reproducible-website/-/raw/master/reproducible-builds-developers-keys.asc
Requires:       fuse
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  bc
BuildRequires:  fuse
BuildRequires:  fuse-devel
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkg-config
# /oreon:deps
%description
disorderfs is an overlay FUSE filesystem that introduces non-determinism
into filesystem metadata.  For example, it can randomize the order
in which directory entries are read.  This is useful for detecting
non-determinism in the build process.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{version}

%build

%set_build_flags
%make_build
%install
%make_install PREFIX=/usr
%oreon_autofiles main

%check

make -C tests test || true
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
