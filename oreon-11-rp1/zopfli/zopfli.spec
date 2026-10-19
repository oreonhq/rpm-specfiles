%global source0_hash e955a7739f71af37ef3349c4fa141c648e8775bceb2195be07e86f8e638814bd
%undefine __cmake_in_source_build
%global so_ver 1.0.3
Name:           zopfli
Version:        %{so_ver}
Release:        1%{?dist}
Summary:        Zlib compatible better compressor
License:        Apache-2.0
URL:            https://github.com/google/%{name}
Source0:        https://github.com/google/%{name}/archive/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
Zopfli is a compression algorithm bit-stream compatible with
compression used in gzip, Zip, PNG, HTTP requests, and others. Zopfli
compresses more (~5%) but is slower (~100x) and uses more CPU, and is
hence best suited for applications where data is compressed once and
sent over a network many times, for example, static content for the
web.

%package        devel
Requires:       %{name} = %{version}-%{release}
Summary:        Development files for zopfli and zopflipng.
%description    devel
Devolopment files for zopfli and zopflipng.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{name}-%{version}
%oreon_prep
%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DZOPFLI_BUILD_SHARED=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n zopfli-devel -f %{oreon_filedir}/zopfli-devel.list

%changelog

%autochangelog
