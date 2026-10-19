%global source0_hash 6341709088e5d18cadaf8f3425a7c512f0eca7539f83885ed41c7ce5170b5efc
%define service recompress
Name:           obs-service-%{service}
Version:        0.5.2
Release:        1%{?dist}
Summary:        An OBS source service: Recompress files
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/obs-service-%{service}
Source0:        https://github.com/openSUSE/%{name}/archive/refs/tags/%{version}.tar.gz#./%{name}-%{version}.tar.gz
Requires:       bzip2
Requires:       gzip
Requires:       xz
Requires:       zstd
BuildArch:      noarch
# oreon:deps
BuildRequires:  /usr/bin/prove
BuildRequires:  bzip2
BuildRequires:  gzip
BuildRequires:  make
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
BuildRequires:  xz
BuildRequires:  zstd
# /oreon:deps
%description
This is a source service for openSUSE Build Service.

It supports to compress, uncompress or recompress files from or to

 none : No Compression
 gz   : Gzip Compression
 bz2  : Bzip2 Compression
 xz   : XZ Compression

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%make_install
%oreon_autofiles main

%check

%make_build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
