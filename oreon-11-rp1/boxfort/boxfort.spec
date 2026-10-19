%global source0_hash 47fde5ce6fbbd7166268e97edc0fc22ed2bf0bf4d93b81ee30d664a8c35a155c
%global forgeurl https://github.com/Snaipe/BoxFort
Version:        0.1.8
%forgemeta
Name:           boxfort
Release:        1%{?dist}
Summary:        Convenient & cross-platform sandboxing C library
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/BoxFort-%{version}.tar.gz
ExcludeArch:    ppc64le s390x
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
# /oreon:deps
%description
BoxFort is a simple, cross-platform sandboxing C library powering Criterion.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%meson -Ddefault_library=shared
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n boxfort-devel -f %{oreon_filedir}/boxfort-devel.list

%changelog

%autochangelog
