%global source0_hash 875940795480ade6c16375fa07d8550e7ed2841937d86cc762f77a2cec6bfac9
Name:           frog-protocols
Version:        0.01
Release:        1%{?dist}
Summary:        Faster moving Wayland protocols
License:        MIT
URL:            https://github.com/misyltoad/frog-protocols
Source0:        https://github.com/misyltoad/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Provides:       %{name}-devel = %{version}-%{release}
# oreon:deps
BuildRequires:  meson
# /oreon:deps
%description
%{name} contains Wayland protocol definitions for protocols
being developed in a more agile fashion to enable shipping
functionality to users more quickly. It is intended to
accelerate development of formal Wayland protocols.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
