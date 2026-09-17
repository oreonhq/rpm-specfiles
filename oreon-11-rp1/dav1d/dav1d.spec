%global source0_hash e099f53253f6c247580c554d53a13f1040638f2066edc3c740e4c2f15174ce22

Name:           dav1d
Version:        1.5.3
Release:        1%{?dist}
Summary:        AV1 cross-platform Decoder

# src/ext/x86/x86inc.asm is ISC
# tools/compat/getopt.c is ISC
License:        BSD-2-Clause AND ISC
URL:            https://code.videolan.org/videolan/dav1d
Source:        https://code.videolan.org/videolan/dav1d/-/archive/1.5.3/dav1d-1.5.3.tar.bz2

BuildRequires:  gcc
BuildRequires:  nasm >= 2.14
BuildRequires:  meson >= 0.49.0
BuildRequires:  pkgconfig(libxxhash)

Requires:       libdav1d%{?_isa} = %{version}-%{release}

%description
dav1d is a new AV1 cross-platform Decoder, open-source, and focused on speed
and correctness.

%package     -n libdav1d
Summary:        Library files for dav1d

%description -n libdav1d
Library files for dav1d, the AV1 cross-platform Decoder.

%package     -n libdav1d-devel
Summary:        Development files for dav1d
Requires:       libdav1d%{?_isa} = %{version}-%{release}

%description -n libdav1d-devel
Development files for dav1d, the AV1 cross-platform Decoder.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc CONTRIBUTING.md NEWS README.md
%{_bindir}/dav1d

%files -n libdav1d
%license COPYING doc/PATENTS
%{_libdir}/libdav1d.so.7{,.*}

%files -n libdav1d-devel
%{_includedir}/dav1d/
%{_libdir}/libdav1d.so
%{_libdir}/pkgconfig/dav1d.pc

%changelog
* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.3-1
- Prepare for Oreon 11 (RP1)
