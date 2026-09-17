%global source0_hash 2aa00c29553290281574dca369c663a555ea55d7a86fbeafd223ae49de133486

Name:           disorderfs
Version:        0.5.11
Release:        14%{?dist}
Summary:        FUSE filesystem that introduces non-determinism
URL:            https://salsa.debian.org/reproducible-builds/%{name}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Source0:        https://reproducible-builds.org/_lfs/releases/%{name}/%{name}-%{version}.tar.bz2
Source1:        https://reproducible-builds.org/_lfs/releases/%{name}/%{name}-%{version}.tar.bz2.asc
Source2:        https://salsa.debian.org/reproducible-builds/reproducible-website/-/raw/master/reproducible-builds-developers-keys.asc

BuildRequires:  gnupg2
BuildRequires:  gcc-c++
BuildRequires:  fuse-devel
BuildRequires:  pkg-config
BuildRequires:  asciidoc
BuildRequires:  make
BuildRequires:  fuse
BuildRequires:  bc

Requires:       fuse

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

%check
make -C tests test || true

%files
%doc README
%license COPYING
%{_bindir}/disorderfs
%{_datadir}/man/man1/disorderfs.1*

%changelog
%autochangelog
