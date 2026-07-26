%global source0_hash 4e4a891988316271974ff4e9585ed1ef729a123d22c08bd473129179dc857feb

Name:		SDL2_net
Version:	2.2.0
Release:	10%{?dist}
Summary:	SDL portable network library
License:	zlib
URL:		http://www.libsdl.org/projects/SDL_net/
Source0:	http://www.libsdl.org/projects/SDL_net/release/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	SDL2-devel >= 2.0

%description
This is a portable network library for use with SDL.

%package	devel
Summary:	Libraries and includes to develop SDL networked applications
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	SDL2-devel%{?_isa} >= 2.0

%description	devel
This is a portable network library for use with SDL.

This is the libraries and include files you can use to develop SDL
networked applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Fix end-of-line encoding
sed -i 's/\r//' README.txt CHANGES.txt LICENSE.txt

%build
%configure --disable-static --disable-gui
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%license LICENSE.txt
%doc README.txt CHANGES.txt
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_includedir}/SDL2/*
%{_libdir}/cmake/SDL2_net/
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
