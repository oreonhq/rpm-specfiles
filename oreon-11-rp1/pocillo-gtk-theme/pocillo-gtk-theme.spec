%global source0_hash 6a61ba549e2d2c126a0ddb901ab000cb3d6b00eee11e011b4c7154cc38c22723
Name:           pocillo-gtk-theme
Version:        0.11
Release:        1%{?dist}
Summary:        Pocillo is a Material Design theme for the Budgie Desktop
BuildArch:      noarch
License:        GPL-2.0-or-later
URL:            https://github.com/UbuntuBudgie/pocillo-gtk-theme
Source0:        https://github.com/UbuntuBudgie/%{name}/releases/download/v%{version}/pocillo-precompiled.tar.gz#/%{name}-%{version}-precompiled.tar.gz
Requires: (pocillo-gtk2-theme if gtk2)
Requires: (pocillo-gtk3-theme if gtk3)
Requires: (pocillo-gtk4-theme if gtk4)
Requires: (pocillo-openbox-theme if openbox)
Requires: (pocillo-plank-theme if plank)
# oreon:deps

# /oreon:deps
%description

%package -n pocillo-gtk2-theme
Summary:        GTK+2 support for the Pocillo GTK theme
Requires:       gtk-murrine-engine
Recommends:     pocillo-gtk-theme
%description -n pocillo-gtk2-theme

This package contains the Pocillo GTK+2 theme.

%package -n pocillo-gtk3-theme
Summary:        GTK3 support for the Pocillo GTK theme
Requires:       gtk3
Recommends:     pocillo-gtk-theme
%description -n pocillo-gtk3-theme

This package contains the Pocillo GTK3 theme.

%package -n pocillo-gtk4-theme
Summary:        GTK4 support for the Pocillo GTK theme
Requires:       gtk4
Recommends:     pocillo-gtk-theme
%description -n pocillo-gtk4-theme

This package contains the Pocillo GTK4 theme.

%package -n pocillo-openbox-theme
Summary:        Openbox support for the Pocillo GTK theme
Recommends:     pocillo-gtk-theme
%description -n pocillo-openbox-theme

This package contains the Pocillo Openbox theme.

%package -n pocillo-plank-theme
Summary:        Plank support for the Pocillo GTK theme
Requires:       plank
Recommends:     pocillo-gtk-theme
%description -n pocillo-plank-theme

This package contains the Pocillo Plank theme.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
mv Pocillo/COPYING .
rm -rf Pocillo-*/COPYING
rm -rf **/INSTALL_GDM_THEME.md

%build

%install
mkdir -p %{buildroot}%{_datadir}/themes/
cp -R Pocillo* %{buildroot}%{_datadir}/themes/
%oreon_autofiles pocillo-gtk2-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles pocillo-gtk3-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles pocillo-gtk4-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles pocillo-openbox-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles pocillo-plank-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n pocillo-gtk2-theme -f %{oreon_filedir}/pocillo-gtk2-theme.list
%files -n pocillo-gtk3-theme -f %{oreon_filedir}/pocillo-gtk3-theme.list
%files -n pocillo-gtk4-theme -f %{oreon_filedir}/pocillo-gtk4-theme.list
%files -n pocillo-openbox-theme -f %{oreon_filedir}/pocillo-openbox-theme.list
%files -n pocillo-plank-theme -f %{oreon_filedir}/pocillo-plank-theme.list

%changelog

%autochangelog
