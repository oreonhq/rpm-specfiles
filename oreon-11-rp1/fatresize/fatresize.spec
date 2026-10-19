%global source0_hash d4049a77b0f44fefdaea1ededbb0ac0317b0db3958d1a3f9847fea6ce8f15f6e
Name:           fatresize
Version:        1.1.0
License:        GPL-3.0-or-later
Summary:        FAT16/FAT32 resizer
URL:            https://github.com/ya-mouse/fatresize
VCS:            git:https://github.com/ya-mouse/fatresize
%bcond_with     releasetag
%global         gituser         ya-mouse
%global         gitname         fatresize
%global         gitdate         20221116
%global         commit          ab78c48fe46d0eb29fcdfa3c6586ade223218433
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
%if %{with releasetag}
Release:        1%{?dist}
Source0:        https://github.com/%{gituser}/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
%else
Release:        1%{?dist}
%endif
Patch0:         fatresize-autoconf2.72.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-utils
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  parted-devel
BuildRequires:  w3m
# /oreon:deps
%description
The FAT16/FAT32 non-destructive resizer.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{with releasetag}
# Build from git release version
%autosetup -n %{gitname}-%{version} -p1
%else
%autosetup -n %{gitname}-%{commit} -p1
%endif

#docbook-to-man not available in Fedora
sed -i -e 's|docbook-to-man|docbook2man|;' Makefile.am

%build

autoreconf -ifv
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

make check
./fatresize --help > /dev/null
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
