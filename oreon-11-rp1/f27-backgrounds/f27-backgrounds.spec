%global source0_hash d8a0a9221868bd51ad8e771d7f9a28eb1b249791b16b2da3ab4c09a7d54a23f5
%global relnum 27
%global Bg_Name F%{relnum}
%global bgname %(t="%{Bg_Name}";echo ${t,,})
%global with_animated 0
%global with_extras 1
Name:		%{bgname}-backgrounds
Version:	%{relnum}.0.1
Release:        1%{?dist}
Summary:        Fedora 27 default desktop background
License:	CC-BY-SA-4.0
URL:		https://fedoraproject.org/wiki/F%{relnum}_Artwork
Source0:        https://github.com/fedoradesign/backgrounds/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:	metadata.desktop
BuildArch:	noarch
Requires:	%{name}-gnome = %{version}-%{release}
Requires:	%{name}-kde = %{version}-%{release}
Requires:	%{name}-xfce = %{version}-%{release}
Requires:	%{name}-mate = %{version}-%{release}
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
This package contains desktop backgrounds for the Fedora %{relnum} default
theme.  Pulls in themes for GNOME, KDE, Mate and Xfce desktops.

%package	base
Summary:	Base images for Fedora %{relnum} default background
License:	CC-BY-SA-4.0
%description	base
This package contains base images for Fedora %{relnum} default background.

%package	kde
Summary:	Fedora %{relnum} default wallpaper for KDE
Requires:	%{name}-base = %{version}-%{release}
Requires:	kde-filesystem
Supplements:	%{name}-animated = %{version}-%{release}
%description    kde
This package contains KDE desktop wallpaper for the Fedora %{relnum}
default them

%package	gnome
Summary:	Fedora %{relnum} default wallpaper for Gnome and Cinnamon
Requires:	%{name}-base = %{version}-%{release}
Supplements:	%{name}-animated = %{version}-%{release}
%description	gnome
This package contains Gnome/Cinnamon desktop wallpaper for the
Fedora %{relnum} default theme.

%package	mate
Summary:	Fedora %{relnum} default wallpaper for Mate
Requires:	%{name}-base = %{version}-%{release}
Supplements:	%{name}-animated = %{version}-%{release}
%description	mate
This package contains Mate desktop wallpaper for the Fedora %{relnum}
default theme.

%package	xfce
Summary:	Fedora %{relnum} default background for XFCE4
Requires:	%{name}-base = %{version}-%{release}
Requires:	xfdesktop
%description	xfce
This package contains XFCE4 desktop background for the Fedora %{relnum}
default theme.

%package	extras-base
Summary:	Base images for F%{relnum} Extras Backrounds
License:	LicenseRef-Callaway-CC-BY AND LicenseRef-Callaway-CC-BY-SA
%description	extras-base
This package contains base images for F%{relnum} supplemental
wallpapers.

%package	extras-gnome
Summary:	Extra F%{relnum} Wallpapers for Gnome and Cinnamon
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:	%{name}-extras-base = %{version}-%{release}
%description	extras-gnome
This package contains F%{relnum} supplemental wallpapers for Gnome
and Cinnamon

%package	extras-mate
Summary:	Extra F%{relnum} Wallpapers for Mate
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:	%{name}-extras-base = %{version}-%{release}
%description    extras-mate
This package contains F%{relnum} supplemental wallpapers for Mate

%package	extras-kde
Summary:	Extra F%{relnum} Wallpapers for KDE
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:	%{name}-extras-base = %{version}-%{release}
%description	extras-kde
This package contains F%{relnum} supplemental wallpapers for Gnome

%package	extras-xfce
Summary:	Extra F%{relnum} Wallpapers for XFCE
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:	%{name}-extras-base = %{version}-%{release}
%description	extras-xfce
This package contains F%{relnum} supplemental wallpapers for XFCE

%prep
%global oreon_srcdir %{name}
%oreon_prep
%build

%make_build
%install
%make_install
install -D -p -m644 %{SOURCE1} \
%{buildroot}%{_datadir}/plasma/desktoptheme/%{Bg_Name}/metadata.desktop
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n f27-backgrounds-base -f %{oreon_filedir}/f27-backgrounds-base.list
%files -n f27-backgrounds-kde -f %{oreon_filedir}/f27-backgrounds-kde.list
%files -n f27-backgrounds-gnome -f %{oreon_filedir}/f27-backgrounds-gnome.list
%files -n f27-backgrounds-mate -f %{oreon_filedir}/f27-backgrounds-mate.list
%files -n f27-backgrounds-xfce -f %{oreon_filedir}/f27-backgrounds-xfce.list
%files -n f27-backgrounds-extras-base -f %{oreon_filedir}/f27-backgrounds-extras-base.list
%files -n f27-backgrounds-extras-gnome -f %{oreon_filedir}/f27-backgrounds-extras-gnome.list
%files -n f27-backgrounds-extras-mate -f %{oreon_filedir}/f27-backgrounds-extras-mate.list
%files -n f27-backgrounds-extras-kde -f %{oreon_filedir}/f27-backgrounds-extras-kde.list
%files -n f27-backgrounds-extras-xfce -f %{oreon_filedir}/f27-backgrounds-extras-xfce.list

%changelog

%autochangelog
