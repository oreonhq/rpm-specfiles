%global source0_hash f4eb229452252600ce48f3c2704c9e6d97b789f81e31c37b0c67dd66f445ea35
Name:          libmad
Version:       0.16.4
Release:        1%{?dist}
Summary:        MPEG audio decoder library
License:       GPL-2.0-or-later
URL:           https://codeberg.org/tenacityteam/libmad
Source0:        https://codeberg.org/tenacityteam/libmad/archive/0.16.4.tar.gz#/libmad-0.16.4.tar.gz
Patch0:        https://codeberg.org/tenacityteam/libmad/commit/326363f04e583b563f63941db3cf7f50e76aceb2.patch#/cmake_fix.patch
Patch1:        libmad-x86.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1
and the MPEG-2 extension to Lower Sampling Frequencies, as well as the
so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II,
and Layer III a.k.a. MP3) are fully implemented.

%package devel
Summary:       MPEG audio decoder library development files
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

%cmake -DOPTIMIZE=ACCURACY
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libmad-devel -f %{oreon_filedir}/libmad-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16.4-1
- Prepare for Oreon 11 (RP1)
