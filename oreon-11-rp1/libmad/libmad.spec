Name:          libmad
Version:       0.16.4
Release:       %autorelease
Summary:       MPEG audio decoder library
License:       GPL-2.0-or-later
URL:           https://codeberg.org/tenacityteam/libmad
Source0:        https://codeberg.org/tenacityteam/libmad/archive/0.16.4.tar.gz#/libmad-0.16.4.tar.gz
Patch0:        https://codeberg.org/tenacityteam/libmad/commit/326363f04e583b563f63941db3cf7f50e76aceb2.patch#/cmake_fix.patch
# fix CPU arch detection on x86
Patch1:        libmad-x86.patch
# oreon url source checksums begin
%global source0_sha256 f4eb229452252600ce48f3c2704c9e6d97b789f81e31c37b0c67dd66f445ea35
%global source0_file 0.16.4.tar.gz
# oreon url source checksums end
BuildRequires: cmake
BuildRequires: gcc-c++

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/0.16.4.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f4eb229452252600ce48f3c2704c9e6d97b789f81e31c37b0c67dd66f445ea35" || { echo "oreon: Source0 SHA256 mismatch for 0.16.4.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n %{name}

%build
%cmake -DOPTIMIZE=ACCURACY
%cmake_build

%install
%cmake_install

%files
%doc CHANGES CREDITS README.md TODO
%license COPYING COPYRIGHT
%{_libdir}/libmad.so.0{,.*}

%files devel
%{_libdir}/libmad.so
%{_libdir}/cmake/mad/
%{_libdir}/pkgconfig/mad.pc
%{_includedir}/mad.h

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16.4-1
- Prepare for Oreon 11 (RP1)
