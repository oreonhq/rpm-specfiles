%global source0_hash 99e2f394570f8fb0b1a2cde2926980fd9685ce60e1500b575057f8424c9ad555
Name:           j4-dmenu-desktop
Version:        3.2
Release:        1%{?dist}
Summary:        Generic menu for desktop managers
License:        GPL-3.0-only
URL:            https://github.com/enkore/j4-dmenu-desktop
Source0:        https://github.com/enkore/%{name}/archive/r%{version}/%{name}-r%{version}.tar.gz
# oreon:deps
BuildRequires:  catch-devel
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  spdlog-devel
# /oreon:deps
%description
%{name} is a replacement for i3-dmenu-desktop.
It's purpose is to find .desktop files and offer you a menu to start an
application using dmenu.  It should work just fine on about any desktop
environment.  You can also execute shell commands using it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-r%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
install -d %{buildroot}%{_mandir}/man1
cp %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
%oreon_autofiles main

%check

%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
