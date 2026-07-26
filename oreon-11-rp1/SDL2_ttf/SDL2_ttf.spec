%global source0_hash 0b2bf1e7b6568adbdbc9bb924643f79d9dedafe061fa1ed687d1d9ac4e453bfd

Name:		SDL2_ttf
Version:	2.24.0
Release:	3%{?dist}
Summary:	TrueType font rendering library for SDL2
License:	Zlib
URL:		https://github.com/libsdl-org/SDL_ttf
Source0:	https://github.com/libsdl-org/SDL_ttf/releases/download/release-%{version}/SDL2_ttf-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:	SDL2-devel
BuildRequires:  libGL-devel
BuildRequires:	freetype-devel
BuildRequires:  harfbuzz-devel
BuildRequires:	zlib-devel

%description
This library allows you to use TrueType fonts to render text in SDL2
applications.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	SDL2-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
rm -rf external
# Fix end-of-line encoding
sed -i 's/\r//' README.txt CHANGES.txt LICENSE.txt

%build
%cmake -DSDL2TTF_HARFBUZZ=true
%cmake_build

%install
%cmake_install
find %{buildroot} -type f -name '*.la' -delete -print

%ldconfig_scriptlets

%files
%license LICENSE.txt
%doc README.txt CHANGES.txt
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_includedir}/SDL2/*
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/SDL2_ttf/

%changelog
%autochangelog
