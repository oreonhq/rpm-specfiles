%global source0_hash 699a5a347b1e12dc5b122e192e19f4db01621826bf41b9ebefb1cbc63ae2180b
Name:           pcaudiolib
Version:        1.1
Release:        1%{?dist}
Summary:        Portable C Audio Library
License:        GPL-3.0-or-later
URL:            https://github.com/rhdunn/pcaudiolib
Source0:        https://github.com/rhdunn/pcaudiolib/archive/refs/tags/1.1.tar.gz#/pcaudiolib-1.1.tar.gz
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
%description
The Portable C Audio Library (pcaudiolib) provides a C API to different
audio devices.

%package devel
Summary: Development files for pcaudiolib
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for the Portable C Audio Library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup
rm -rf src/TPCircularBuffer

%build

./autogen.sh
%configure --without-coreaudio
%make_build
%install
%make_install
rm -vf %{buildroot}%{_libdir}/*.{a,la}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n pcaudiolib-devel -f %{oreon_filedir}/pcaudiolib-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1-19
- Prepare for Oreon 11 (RP1)
