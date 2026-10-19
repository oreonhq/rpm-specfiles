%global source0_hash 1c5bf9d6d6b678d5bd42df42529da84d3942f0ba707355ca47fb98ccc0df77cf
Name:           chunkfs
Version:        0.8
Release:        15%{?dist}
Summary:        FUSE based filesystem that allows you to mount an arbitrary file or block device
License:        GPL-2.0-or-later
URL:            https://chunkfs.florz.de/
Source0:        https://chunkfs.florz.de/%{name}_%{version}.tar.xz
Source100:      CMakeLists.txt
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fuse-devel
BuildRequires:  gcc
BuildRequires:  perl-podlators
# /oreon:deps
%description
ChunkFS is a FUSE based filesystem that allows you to mount an arbitrary file
or block device as a directory tree of files that each represent a chunk of
user-specified size of the mounted file. The chunk size is global per mount,
but at mount time any value can be specified. (If the file size isn't a
multiple of the specified chunk size, the last file in the tree simply will be
smaller than the chunk size.) Only read access is supported at the moment.

UnChunkFS is the inversion of ChunkFS—it allows you to mount a ChunkFS tree (or
a copy of it, of course), and gives you a single file named image that has the
same contents as the file or device you created the tree from by mounting it as
a ChunkFS.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
install %{SOURCE100} .

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
