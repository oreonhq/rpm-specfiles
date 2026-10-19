%global source0_hash 1ebb01ab14e98afd1727f68f64981c37bd23305b1f131f5667c02b94cf593192
%ifnarch s390x
%bcond check 0
%else
%bcond check 1
%endif
Name:           gtk4-layer-shell
Version:        1.3.0
Release:        1%{?dist}
Summary:        Library to create panels and other desktop components for Wayland
License:        MIT
URL:            https://github.com/wmww/gtk4-layer-shell
Source0:        https://github.com/wmww/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  python3-gobject
BuildRequires:  vala
# /oreon:deps
%description
A library for using the Layer Shell and Session Lock Wayland protocols with
GTK4. This Library is compatible with C, C++ and any language that supports
GObject introspection files (Python, Vala, etc).

The Layer Shell protocol allows building desktop shell components such as
panels, notifications and wallpapers. It can be used to anchor your windows to a
corner or edge of the output, or stretch them across the entire output.

The Session Lock protocol allows building lock screens.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
    %if %{with check}
    -Dsmoke-tests=false \
    -Dtests=true \
    %endif
    %{nil}
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%meson_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n gtk4-layer-shell-devel -f %{oreon_filedir}/gtk4-layer-shell-devel.list

%changelog

%autochangelog
