%global source0_hash 88cfc3b6a7492a14916634358e365ed57b9fa12a3efdcd21e09f857a55b950f5

%global commit 04b854e6411cd9ca75582c108aea63ae3c202f0e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20230925
%global fgittag %{gitdate}.git%{shortcommit}

Summary: GNOME Monitor Configuration Tool
Name: gnome-monitor-config
Version: 0
Release: 0.18%{?fgittag:.%{fgittag}}%{?dist}
#Note that the license isn't included in source yet, see this pull request:
#https://github.com/jadahl/gnome-monitor-config/pull/1
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://github.com/jadahl/gnome-monitor-config
Source0:  https://github.com/jadahl/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: gcc
BuildRequires: cairo-devel

# 32bit package serves very little purpose:
ExcludeArch: %{ix86}

%description
A CLI configuration tool used for changing monitor settings in GNOME.
This can be used in Wayland, with functionality similar to xrandr on X11.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build
%meson
%meson_build

%install
install -m 755 */src/%{name} -D %{buildroot}%{_bindir}/%{name}

%files
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
