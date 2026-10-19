%global source0_hash 4264edf9f5f5ff9bccaee1ab3f5b2613a0db526bc90c15d7c82eb05a3fc81307
%ifnarch s390x
%bcond_without test
%else
%bcond_with test
%endif
%global forgeurl https://github.com/WayfireWM/wf-config
Name:           wf-config
Version:        0.11.0
%forgemeta
Release:        1%{?dist}
Summary:        Library for managing configuration files, written for wayfire
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with test}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(doctest)
BuildRequires:  cmake(glm)
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libxml-2.0)
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%if %{with test}
%meson \
    -Dtests=enabled
%else
%meson \
    -Dtests=disabled
%endif
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with test}
%check

%meson_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n wf-config-devel -f %{oreon_filedir}/wf-config-devel.list

%changelog

%autochangelog
