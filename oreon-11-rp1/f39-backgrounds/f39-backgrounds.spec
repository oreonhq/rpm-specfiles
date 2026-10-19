%global source0_hash f9d1e12ecd57fa87bf88b5f80371a565f8ea819c8d7d8e5ff5ed4bf8bab5cafa
%global relnum 39
%global Bg_Name F39
%global bgname %(t="%{Bg_Name}";echo ${t,,})
%global with_extras 1
Name:           %{bgname}-backgrounds
Version:        %{relnum}.0.5
Release:        1%{?dist}
Summary:        Fedora 39 default desktop background
License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/_Artwork
Source0:        https://github.com/fedoradesign/backgrounds/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildArch:      noarch
Requires:       %{name}-budgie = %{version}-%{release}
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}
Requires:       %{name}-xfce = %{version}-%{release}
Requires:       %{name}-mate = %{version}-%{release}
# oreon:deps
BuildRequires:  kde-filesystem
BuildRequires:  make
# /oreon:deps
%description
This package contains desktop backgrounds for the Fedora  %{relnum} default
theme.  Pulls in themes for GNOME, KDE, Mate and Xfce desktops.

%package        base
Summary:        Base images for Fedora  %{relnum} default background
License:        CC-BY-SA-4.0
%description    base
This package contains base images for Fedora  %{relnum} default background.

%package        budgie
Summary:        Fedora  %{relnum} default wallpaper for Budgie
Requires:       %{name}-base = %{version}-%{release}
Recommends:	%{name}-gnome = %{version}-%{release}
%description    budgie
This package contains Budgie desktop wallpaper for the
Fedora  %{relnum} default theme.

%package        gnome
Summary:        Fedora  %{relnum} default wallpaper for Gnome and Cinnamon
Requires:       %{name}-base = %{version}-%{release}
%description    gnome
This package contains Gnome/Cinnamon desktop wallpaper for the
Fedora  %{relnum} default theme.

%package        kde
Summary:        Fedora  %{relnum} default wallpaper for KDE
Requires:       %{name}-base = %{version}-%{release}
Requires:       kde-filesystem
%description    kde
This package contains KDE desktop wallpaper for the Fedora  %{relnum}
default them

%package        mate
Summary:        Fedora %{relnum} default wallpaper for Mate
Requires:       %{name}-base = %{version}-%{release}
%description    mate
This package contains Mate desktop wallpaper for the Fedora  %{relnum}
default theme.

%package        xfce
Summary:        Fedora  %{relnum} default background for XFCE4
Requires:       %{name}-base = %{version}-%{release}
Requires:       xfdesktop
%description    xfce
This package contains XFCE4 desktop background for the Fedora  %{relnum}
default theme.

%package        extras-base
Summary:        Base images for  Extras Backgrounds
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
%description    extras-base
This package contains base images for  supplemental
wallpapers.

%package        extras-gnome
Summary:        Extra  Wallpapers for Gnome and Cinnamon
Requires:       %{name}-extras-base = %{version}-%{release}
%description    extras-gnome
This package contains  supplemental wallpapers for Gnome
and Cinnamon

%package        extras-mate
Summary:        Extra  Wallpapers for Mate
Requires:       %{name}-extras-base = %{version}-%{release}
%description    extras-mate
This package contains  supplemental wallpapers for Mate

%package        extras-kde
Summary:        Extra  Wallpapers for KDE
Requires:       %{name}-extras-base = %{version}-%{release}
%description    extras-kde
This package contains  supplemental wallpapers for Gnome

%package        extras-xfce
Summary:        Extra  Wallpapers for XFCE
Requires:       %{name}-extras-base = %{version}-%{release}
%description    extras-xfce
This package contains  supplemental wallpapers for XFCE

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

%make_build
%install
%make_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n f39-backgrounds-base -f %{oreon_filedir}/f39-backgrounds-base.list
%files -n f39-backgrounds-budgie -f %{oreon_filedir}/f39-backgrounds-budgie.list
%files -n f39-backgrounds-gnome -f %{oreon_filedir}/f39-backgrounds-gnome.list
%files -n f39-backgrounds-kde -f %{oreon_filedir}/f39-backgrounds-kde.list
%files -n f39-backgrounds-mate -f %{oreon_filedir}/f39-backgrounds-mate.list
%files -n f39-backgrounds-xfce -f %{oreon_filedir}/f39-backgrounds-xfce.list
%files -n f39-backgrounds-extras-base -f %{oreon_filedir}/f39-backgrounds-extras-base.list
%files -n f39-backgrounds-extras-gnome -f %{oreon_filedir}/f39-backgrounds-extras-gnome.list
%files -n f39-backgrounds-extras-mate -f %{oreon_filedir}/f39-backgrounds-extras-mate.list
%files -n f39-backgrounds-extras-kde -f %{oreon_filedir}/f39-backgrounds-extras-kde.list
%files -n f39-backgrounds-extras-xfce -f %{oreon_filedir}/f39-backgrounds-extras-xfce.list

%changelog

%autochangelog
