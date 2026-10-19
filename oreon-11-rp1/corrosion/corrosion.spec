%global source0_hash e9e95b1ee2bad52681f347993fb1a5af5cce458c5ce8a2636c9e476e4babf8e3
Name:           corrosion
Version:        0.6.1
Release:        1%{?dist}
Summary:        Easy Rust and C/C++ Integration
License:        MIT
URL:            https://github.com/corrosion-rs/corrosion
Source0:        https://github.com/%{name}-rs/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%global debug_package %{nil}
Requires:       cmake
Requires:       cargo
Requires:       rust
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rust
# /oreon:deps
%description
Corrosion, formerly known as cmake-cargo, is a tool for integrating Rust
into an existing CMake project. Corrosion can automatically import
executables, static libraries, and dynamic libraries from a workspace or
package manifest (Cargo.toml file).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
