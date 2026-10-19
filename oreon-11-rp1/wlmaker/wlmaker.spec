%global source0_hash aa7c23b6ea501df412101aaaa022576f05eefa56bdde33c0f6eb6d34aa5a2389
%global libbase_commit aa0da7a355b04b1dd8572a94261a0b0c497e1a85
%global libbase_url https://github.com/phkaeser/libbase
%bcond docs 1
%global toolchain clang
Name:           wlmaker
Version:        0.8.1
Release:        1%{?dist}
Summary:        Wayland compositor inspired by Window Maker
License:        Apache-2.0
URL:            https://github.com/phkaeser/wlmaker
Source0:        https://github.com/phkaeser/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{libbase_url}/archive/%{libbase_commit}/libbase-%{libbase_commit}.tar.gz
Patch0:         0001-fix-config-path.patch
Patch1:         0002-remove-google-chrome.patch
ExcludeArch:    %{ix86}
%if %{with docs}
%endif
Requires:       hicolor-icon-theme
Recommends:     firefox
Recommends:     foot
Recommends:     wdisplays
%if %{with docs}
Suggests:       %{name}-doc = %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  bison
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  hicolor-icon-theme
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libxdg-basedir)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)
BuildRequires:  plantuml
BuildRequires:  sed
# /oreon:deps
%description
Wayland Maker is a Wayland compositor inspired by Window Maker.

Key features:
- Compositor for windows in stacking mode.
- Supports multiple workspaces.
- Appearance inspired by Window Maker, following the look and feel of NeXTSTEP.
- Easy to use, lightweight, low gimmicks and fast.
- Dock and clip, to be extended for dockable apps.

%package        doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch
%description    doc
This package provides additional developer documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -b 1

# Drop bundled dependencies
rm -r dependencies

# Ensure libbase can be found; we move instead of symlinking because the build
# uses relative paths for the includes and that confuses things
rm -r submodules/libbase
mv ../libbase-%{libbase_commit}/ submodules/libbase

# Do not abort on warnings
sed -i 's/-Werror//' CMakeLists.txt submodules/libbase/CMakeLists.txt

%conf
%cmake -Dconfig_OPTIM=ON

%build

%cmake_build
%if %{with docs}
%cmake_build --target doc
%endif
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
desktop-file-validate %{buildroot}%{_datadir}/applications/{%{name},%{name}.wlmclock,%{name}.wlmeyes}.desktop
%files -f %{oreon_filedir}/main.list
%files -n wlmaker-doc -f %{oreon_filedir}/wlmaker-doc.list

%changelog

%autochangelog
