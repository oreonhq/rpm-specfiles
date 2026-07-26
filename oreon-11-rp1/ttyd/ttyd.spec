%global source0_hash 039dd995229377caee919898b7bd54484accec3bba49c118e2d5cd6ec51e3650

Name:           ttyd
Version:        1.7.7
Release:        %autorelease
Summary:        Share your terminal over HTTP
License:        MIT
URL:            https://github.com/tsl0922/ttyd
Source:         https://github.com/tsl0922/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Needed to make CMake find Libwebsockets
Patch0:         ttyd-CMakeLists.txt.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  json-c-devel
BuildRequires:  libuv-devel
BuildRequires:  libwebsockets-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconf
BuildRequires:  zlib-devel

%description
ttyd is a simple command-line tool for sharing terminal over the web, inspired
by GoTTY.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_bindir}/ttyd
%{_mandir}/man1/ttyd.1.*
%license LICENSE

%changelog
%autochangelog
