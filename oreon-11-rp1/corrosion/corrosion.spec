%global source0_hash e9e95b1ee2bad52681f347993fb1a5af5cce458c5ce8a2636c9e476e4babf8e3

Name:           corrosion
Version:        0.6.1
Release:        %autorelease
Summary:        Easy Rust and C/C++ Integration
License:        MIT

URL:            https://github.com/corrosion-rs/corrosion
Source:         %{url}/archive/v%{version}/corrosion-%{version}.tar.gz

%global debug_package %{nil}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cargo
BuildRequires:  rust

Requires:       cmake
Requires:       cargo
Requires:       rust

%description
Corrosion, formerly known as cmake-cargo, is a tool for integrating Rust
into an existing CMake project. Corrosion can automatically import
executables, static libraries, and dynamic libraries from a workspace or
package manifest (Cargo.toml file).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%doc RELEASES.md
%{_libdir}/cmake/Corrosion/
%{_datadir}/cmake/Corrosion.cmake
%{_datadir}/cmake/CorrosionGenerator.cmake
%{_datadir}/cmake/FindRust.cmake

%changelog
%autochangelog
