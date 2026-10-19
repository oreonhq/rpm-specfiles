%global source0_hash 28413457cbf923b9b81e546caffabb8edd5c18f263e698ad86f564fd4b5b344d
%global _hardened_build 1
%{!?make_build: %global make_build %{__make} %{?_smp_mflags}}
Name:           s3fs-fuse
Version:        1.97
Release:        1%{?dist}
Summary:        FUSE-based file system backed by Amazon S3
License:        GPL-2.0-or-later
URL:            https://github.com/s3fs-fuse/s3fs-fuse
Source0:        https://github.com/s3fs-fuse/s3fs-fuse/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        passwd-s3fs
Requires:       fuse3-libs
Requires:       fuse3
Requires:       mailcap
Conflicts:      fuse-s3fs
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
# /oreon:deps
%description
s3fs is a FUSE file system that allows you to mount an Amazon S3 bucket as a
local file system. It stores files natively and transparently in S3 (i.e.,
you can use other programs to access the same files). Maximum file size is
5 TB when using multipart upload.

s3fs is stable and is being used in number of production environments, e.g.,
rsync backup to s3.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

cp -p %{SOURCE1} passwd-s3fs
./autogen.sh
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
