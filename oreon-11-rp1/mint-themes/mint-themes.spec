%global source0_hash bd67cbe9489ca3cf1f9ff2951b9f41740db072caa3d7adad787603dc3ce8c531
Name:           mint-themes
Epoch:          1
Version:        2.4.1
Release:        1%{?dist}
Summary:        Mint themes
License:        GPL-3.0-or-later
URL:            https://github.com/linuxmint/%{name}
Source0:        https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Recommends:     mint-x-icons
# oreon:deps
BuildRequires:  fdupes
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  python3-libsass
# /oreon:deps
%description
A collection of mint themes.

%package -n     mint-y-theme
Summary:        The Mint-Y theme 
Recommends:     mint-y-icons
%description -n	mint-y-theme
The Mint-Y theme.  This theme is based on the Arc theme.

%package -n     mint-themes-gtk3
Summary:        Mint themes for GTK3
Recommends:     mint-themes = %{epoch}:%{version}
Recommends:     mint-y-theme = %{epoch}:%{version}
%description -n	mint-themes-gtk3
A collection of mint themes for GTK3.

%package -n     mint-themes-gtk4
Summary:        Mint themes for GTK4
Recommends:     mint-themes = %{epoch}:%{version}
Recommends:     mint-y-theme = %{epoch}:%{version}
%description -n	mint-themes-gtk4
A collection of mint themes for GTK4.

%package -n	cinnamon-themes
Summary:        Mint themes for GTK3 
Requires:       filesystem
Requires:       mint-themes-gtk3 = %{epoch}:%{version}
Requires:       mint-themes-gtk4 = %{epoch}:%{version}
%description -n	cinnamon-themes
Collection of the best themes available for Cinnamon

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

make
%install
%{__cp} -pr usr/ %{buildroot}
%fdupes -s %{buildroot}
%oreon_autofiles mint-y-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mint-themes-gtk3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mint-themes-gtk4 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cinnamon-themes usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mint-y-theme -f %{oreon_filedir}/mint-y-theme.list
%files -n mint-themes-gtk3 -f %{oreon_filedir}/mint-themes-gtk3.list
%files -n mint-themes-gtk4 -f %{oreon_filedir}/mint-themes-gtk4.list
%files -n cinnamon-themes -f %{oreon_filedir}/cinnamon-themes.list

%changelog

%autochangelog
