%global source0_hash 1f4f54c237cd3b70c8a125044eb2578e8263c12b42d401a42c02c32f10f62548
Name:           catimg
Version:        2.8.0
Release:        3%{?dist}
Summary:        Print images in a terminal with 256 colors support
License:        MIT
URL:            https://github.com/posva/catimg
Source0:        https://github.com/posva/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: catimg-c99.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
%{name} prints images in a terminal with 256 colors support. It supports
JPEG, PNG, ICO and GIF formats.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
install -D --preserve-timestamps --mode 644 completion/_catimg %{buildroot}%{_datadir}/zsh/site-functions/_catimg
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
