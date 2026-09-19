%global source0_hash e955a7739f71af37ef3349c4fa141c648e8775bceb2195be07e86f8e638814bd

%undefine __cmake_in_source_build
%global so_ver 1.0.3

Name:           zopfli
Version:        %{so_ver}
Release:        15%{?dist}
Summary:        Zlib compatible better compressor

License:        Apache-2.0
URL:            https://github.com/google/%{name}
Source0:        %{URL}/archive/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

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

%autosetup -n %{name}-%{name}-%{version}

%build
# TODO: Please submit an issue to upstream (rhbz#2381653)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DZOPFLI_BUILD_SHARED=ON
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc CONTRIBUTORS README README.zopflipng
%{_bindir}/%{name}
%{_bindir}/%{name}png

%{_libdir}/lib%{name}.so.1
%{_libdir}/lib%{name}.so.%{so_ver}

%{_libdir}/lib%{name}png.so.1
%{_libdir}/lib%{name}png.so.%{so_ver}

%files          devel
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}png.so

%{_includedir}/%{name}.h
%{_includedir}/%{name}png_lib.h
%{_libdir}/cmake/Zopfli/*.cmake

%changelog
%autochangelog
