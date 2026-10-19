%global source0_hash 0912b2f72a9ae8112bf07e766287c7378fb544a9bcaeaedf967ef836438d3f57
%global relnum 41
%global Bg_Name F41
%global bgname %(t="%{Bg_Name}";echo ${t,,})
%global with_extras 0
Name:           %{bgname}-backgrounds
Version:        %{relnum}.0.2
Release:        1%{?dist}
Summary:        Fedora 41 default desktop background
License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/Design
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
BuildRequires:  optipng
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

%prep
%global oreon_srcdir %{name}
%oreon_prep
%build

%make_build
%install
%make_install
optipng %{buildroot}/%{_datadir}/backgrounds/%{bgname}/default/*.png
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n f41-backgrounds-base -f %{oreon_filedir}/f41-backgrounds-base.list
%files -n f41-backgrounds-budgie -f %{oreon_filedir}/f41-backgrounds-budgie.list
%files -n f41-backgrounds-gnome -f %{oreon_filedir}/f41-backgrounds-gnome.list
%files -n f41-backgrounds-kde -f %{oreon_filedir}/f41-backgrounds-kde.list
%files -n f41-backgrounds-mate -f %{oreon_filedir}/f41-backgrounds-mate.list
%files -n f41-backgrounds-xfce -f %{oreon_filedir}/f41-backgrounds-xfce.list

%changelog

%autochangelog
