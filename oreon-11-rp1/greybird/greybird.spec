%global source0_hash 74dcec9b9bcf6c869941b661c50ce0d752b4eb4e193747db536ffd7e97d32453
%global theme_name     Greybird
Name:           greybird
Version:        3.23.4
Release:        1%{?dist}
Summary:        A clean minimalistic theme for Xfce, GTK+ 2 and 3
License:        GPL-2.0-or-later OR LicenseRef-Callaway-CC-BY-SA
URL:            http://shimmerproject.org/project/%{name}/ 
Source0:        https://github.com/shimmerproject/%{theme_name}/archive/v%{version}.tar.gz
Requires:       gtk-murrine-engine
BuildArch:      noarch
Obsoletes:      greybird-gtk2-theme < 3.22.11
Obsoletes:      greybird-gtk3-theme < 3.22.11
Obsoletes:      greybird-metacity-theme < 3.22.11
Obsoletes:      greybird-xfce4-notifyd-theme < 3.22.11
Obsoletes:      greybird-xfwm4-themes < 3.22.11
Provides:       greybird = %{name}-%{release}
# oreon:deps
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  librsvg2-devel
BuildRequires:  meson
BuildRequires:  sassc
# /oreon:deps
%description
Greybird is a theme for GTK2/3 and xfwm4/metacity started out on the basis of
Bluebird, but aims at reworking the intense blue tone to a more neutral
grey-ish look that will be more pleasant to look at in everyday use.

%package light-theme
Summary:        Greybird light themes
Requires:       gtk-murrine-engine
Obsoletes:      greybird-gtk2-theme < 3.22.11
Obsoletes:      greybird-gtk3-theme < 3.22.11
Obsoletes:      greybird-metacity-theme < 3.22.11
Obsoletes:      greybird-xfce4-notifyd-theme < 3.22.11
Obsoletes:      greybird-xfwm4-themes < 3.22.11
Provides:       greybird-light-theme = %{name}-%{release}
%description light-theme
Light Themes as part of the Greybird theme.

%package dark-theme
Summary:        Greybird Dark themes
Requires:       gtk-murrine-engine
Obsoletes:      greybird-gtk2-theme < 3.22.11
Obsoletes:      greybird-gtk3-theme < 3.22.11
Obsoletes:      greybird-metacity-theme < 3.22.11
Obsoletes:      greybird-xfce4-notifyd-theme < 3.22.11
Obsoletes:      greybird-xfwm4-themes < 3.22.11
Provides:       greybird-dark-theme = %{name}-%{release}
%description dark-theme
Dark Themes as part of the Greybird theme.

%package metacity-theme
Summary:        Greybird Metacity themes
Requires:       metacity
Requires:       greybird-light-theme
Requires:       greybird-dark-theme
%description metacity-theme
Themes for Metacity as part of the Greybird theme.

%package xfwm4-theme
Summary:        Greybird Xfwm4 themes
Requires:       xfwm4
Requires:       greybird-light-theme
Requires:       greybird-dark-theme
%description xfwm4-theme
Themes for Xfwm4 as part of the Greybird theme.

%package xfce4-notifyd-theme
Summary:        Greybird Xfce4 notifyd theme
Requires:       xfce4-notifyd
Requires:       greybird-light-theme
%description xfce4-notifyd-theme
Themes for Xfce4 notifyd as part of the Greybird theme.

%package plank
Summary:        Greybird plank themes
Requires:       plank
Requires:       greybird-light-theme
Requires:       greybird-dark-theme
%description plank
Themes for plank as part of the Greybird theme.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{theme_name}-%{version}

# Cleanup
# Remove Unity theme
sed -i '/unity/d' light/meson.build
sed -i '/unity/d' dark/meson.build
rm -fr light/unity
rm -fr dark/unity

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n greybird-light-theme -f %{oreon_filedir}/greybird-light-theme.list
%files -n greybird-dark-theme -f %{oreon_filedir}/greybird-dark-theme.list
%files -n greybird-metacity-theme -f %{oreon_filedir}/greybird-metacity-theme.list
%files -n greybird-xfwm4-theme -f %{oreon_filedir}/greybird-xfwm4-theme.list
%files -n greybird-xfce4-notifyd-theme -f %{oreon_filedir}/greybird-xfce4-notifyd-theme.list
%files -n greybird-plank -f %{oreon_filedir}/greybird-plank.list

%changelog

%autochangelog
