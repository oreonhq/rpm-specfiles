%global source0_hash 875940795480ade6c16375fa07d8550e7ed2841937d86cc762f77a2cec6bfac9

Name:           frog-protocols
Version:        0.01
Release:        4%{?dist}
Summary:        Faster moving Wayland protocols

License:        MIT
URL:            https://github.com/misyltoad/frog-protocols
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  meson

# This is a development package so add it for convention
Provides:       %{name}-devel = %{version}-%{release}

%description
%{name} contains Wayland protocol definitions for protocols
being developed in a more agile fashion to enable shipping
functionality to users more quickly. It is intended to
accelerate development of formal Wayland protocols.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE.md
%doc README.md
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/

%changelog
%autochangelog
