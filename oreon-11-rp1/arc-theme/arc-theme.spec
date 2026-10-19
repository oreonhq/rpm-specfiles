%global source0_hash aa32825da7e2329fdaac64d35f0afab85e2e2f3c71cc41547bafafa379444ccf
%global _vpath_srcdir ..
%global common_desc							\
Arc is a flat theme with transparent elements for GTK 3, GTK 2 and	\
Gnome-Shell which supports GTK 3 and GTK 2 based desktop environments	\
like Gnome, Cinnamon, Budgie, Pantheon, XFCE, Mate, etc.
Name:		arc-theme
Version:	20221218
Release:        1%{?dist}
Summary:        Flat theme with transparent elements
License:	GPL-3.0-or-later
URL:		https://github.com/jnsh/%{name}
Source0:        https://github.com/jnsh/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	filesystem
Requires:	gtk-murrine-engine
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cinnamon
BuildRequires:  gnome-shell
BuildRequires:  gtk-murrine-engine
BuildRequires:  gtk3-devel
BuildRequires:  gtk4-devel
BuildRequires:  inkscape
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  optipng
BuildRequires:  sassc
# /oreon:deps
%description
%{common_desc}

%package plank
Summary:	Arc-theme for Plank dock
Requires:	%{name} == %{version}-%{release}
%description plank
%{common_desc}

This package contains the %{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{__mkdir} -p regular solid
pushd regular
%meson -Dthemes=cinnamon,gnome-shell,gtk2,gtk3,gtk4,metacity,plank,xfwm
%meson_build
popd
pushd solid
%meson -Dthemes=cinnamon,gnome-shell,gtk2,gtk3,gtk4,metacity,plank,xfwm -Dtransparency=false
%meson_build
popd
%install
pushd regular
%meson_install
popd
pushd solid
%meson_install
popd
%{__mkdir} -p %{buildroot}/%{_datadir}/plank/themes/{Arc{,-solid},Arc-Lighter{,-solid},Arc-Darker{,-solid},Arc-Dark{,-solid}}
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-solid/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-solid/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-Lighter/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-Lighter/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-Lighter-solid/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-Lighter-solid/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-Dark/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-Dark/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-Dark-solid/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-Dark-solid/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-Darker/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-Darker/
%{__install} -pm 0644 %{buildroot}/%{_datadir}/themes/Arc-Darker-solid/plank/dock.theme %{buildroot}/%{_datadir}/plank/themes/Arc-Darker-solid/
rm -fvr %{buildroot}/%{_datadir}/themes/{Arc{,-solid},Arc-Lighter{,-solid},Arc-Darker{,-solid},Arc-Dark{,-solid}}/plank
%oreon_autofiles arc-theme-plank usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n arc-theme-plank -f %{oreon_filedir}/arc-theme-plank.list

%changelog

%autochangelog
