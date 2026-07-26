%global source0_hash 5e955b4c6e165f96d32f322ff8e4e55797fcc83b04083abbfe212cc2e9de4e83

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# all packages requiring libXISF are now disabled on i686
ExcludeArch:    %{ix86}

Name:           libXISF
Version:        0.2.13
Release:        %autorelease
Summary:        Library to load and write XISF format
License:        GPL-3.0-or-later
URL:            https://gitea.nouspiro.space/nou/libXISF
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  cmake >= 3.14
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(zlib)

%description
LibXISF is C++ library to load and save images in XISF format that
is native format PixInsight astronomical image processing program.
It implements XISF 1.0 specifications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n libxisf

# remove bundled libraries
for d in "lz4" "pugixml" "zlib"
do
  rm -rf $d
done

%build
%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DUSE_BUNDLED_LIBS=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/%{name}.so.0
%{_libdir}/%{name}.so.%{version}

%files devel
%{_includedir}/%{name}_global.h
%{_includedir}/libxisf.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/libxisf.pc

%changelog
%autochangelog
