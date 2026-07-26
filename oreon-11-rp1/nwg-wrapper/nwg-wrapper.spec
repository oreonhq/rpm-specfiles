%global source0_hash 7d14b53bde012eed5de9d0480b31179466f473daf87202a0245a652eefba3812

# -*-Mode: rpm-spec -*-

# Use 0 for release and 1 for git
%global   git 0
Version:  0.1.3
%global   forgeurl https://github.com/nwg-piotr/nwg-wrapper
%if %{?git}
%global   commit b186a827404eb2c5e4d757bf122d5d74521b7dcd
%global   date 20220703
%endif
%forgemeta

%global sys_name nwg_wrapper

Name:    nwg-wrapper
Summary: A GTK3 wrapper to display text on the desktop for wlroots
Release: 15%{?dist}

License: MIT
URL:      %{forgeurl}
Source0:  %{forgesource}

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: python3-gobject
Requires: gtk-layer-shell
Requires: gtk3
Recommends: python3-i3ipc
Recommends: wlr-randr

%description

nwg-wrapper is a GTK3-based wrapper to display a script output, or a
text file content on the desktop in sway or other wlroots-based
compositors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup -a

%build
%py3_build

%install
%py3_install
for lib in %{buildroot}%{python3_sitelib}/%{sys_name}/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/%{sys_name}/
%{python3_sitelib}/%{sys_name}-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
