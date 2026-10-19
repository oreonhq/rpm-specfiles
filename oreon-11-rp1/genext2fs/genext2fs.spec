%global source0_hash e3503a5bae3fd4b5b2c2d4f49b5b7f8d08e7accb20ab28c0f9647389b2c8a079
Name:           genext2fs
Version:        1.6.3
Release:        1%{?dist}
Summary:        ext2 filesystem generator
License:        GPL-2.0-only
URL:            https://github.com/bestouff/genext2fs/
Source0:        https://github.com/bestouff/%{name}//archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  attr
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  e2fsprogs
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3
# /oreon:deps
%description
genext2fs generates an ext2 filesystem as a normal (non-root) user.
It does not require you to mount the image file to copy files on it,
nor does it require that you become the superuser to make device nodes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf -fi

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
