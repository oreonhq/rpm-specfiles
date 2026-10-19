%global source0_hash f685da6ca9d97329b4b200077d12db0ad4f9964d4515479e6c00bba721ab0626
%global build_type_safety_c 0
Summary:        A slick-looking LightDM greeter
Name:		slick-greeter
Version:	2.2.7
Release:        1%{?dist}
License:	GPL-3.0-or-later
URL:		https://github.com/linuxmint/%{name}
Source0:        https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	10_%{name}-cinnamon.gschema.override.in
Source2:	10_%{name}-mate.gschema.override
Source3:	%{name}.conf
ExcludeArch:    %{ix86}
Provides:	lightdm-greeter = 1.2
Provides:	lightdm-%{name} = %{version}
Requires:	lightdm%{?_isa}
Requires:	google-noto-sans-fonts
Requires:	system-logos
Requires:	desktop-backgrounds-compat
Recommends:	lightdm-settings
Recommends:	onboard
Requires:	(%{name}-cinnamon = %{version}-%{release} if cinnamon)
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(liblightdm-gobject-1)
BuildRequires:  pkgconfig(xapp)
BuildRequires:  vala
# /oreon:deps
%description
A cross-distro LightDM greeter based on unity-greeter.

%package -n %{name}-cinnamon
Summary: Slick-greeter customisation for the CINNAMON desktop
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires:	desktop-backgrounds-basic
Requires:	mint-y-icons
Requires:	mint-y-theme
Recommends: paper-icon-theme
%description -n %{name}-cinnamon
Slick-greeter customisation for the CINNAMON desktop.

%package -n %{name}-mate
Summary: Slick-greeter customisation for the MATE desktop
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
%description -n %{name}-mate
Slick-greeter customisation for the MATE desktop.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%{__install} -pm 0644 %{SOURCE2} %{name}.conf.example

%build

%meson
%meson_build
%install
%meson_install
%{__mkdir} -p %{buildroot}%{_datadir}/lightdm/lightdm.conf.d	\
	%{buildroot}%{_datadir}/glib-2.0/schemas	\
	%{buildroot}%{_sysconfdir}/lightdm
%{__install} --target-directory=%{buildroot}%{_datadir}/lightdm/lightdm.conf.d	\
	-Dpm 0644 debian/90-%{name}.conf
%{__sed} -e 's!@color@!#202020!g'	\
	-e 's!@wallpaper@!%{_datadir}/backgrounds/tiles/default_blue.jpg!'	\
	< %{SOURCE1}								\
	> %{buildroot}%{_datadir}/glib-2.0/schemas/10_%{name}-cinnamon.gschema.override
%{__install} --target-directory=%{buildroot}%{_datadir}/glib-2.0/schemas	\
	-Dpm 0644 %{SOURCE2}
%{__install} --target-directory=%{buildroot}%{_sysconfdir}/lightdm	\
	-Dpm 0644 %{SOURCE3}
%{__chmod} -c a+x %{buildroot}%{_bindir}/*
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{_bindir}/desktop-file-validate %{buildroot}%{_datadir}/xgreeters/*.desktop
%pre

%{_sbindir}/update-alternatives --remove lightdm-greeter	\
	%{_datadir}/xgreeters/%{name}.desktop 2> /dev/null ||:
%files -f %{oreon_filedir}/main.list
%files -n slick-greeter-cinnamon -f %{oreon_filedir}/slick-greeter-cinnamon.list
%files -n slick-greeter-mate -f %{oreon_filedir}/slick-greeter-mate.list

%changelog

%autochangelog
