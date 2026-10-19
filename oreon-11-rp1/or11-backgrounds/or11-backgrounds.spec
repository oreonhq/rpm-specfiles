%global source0_hash none
%global relnum 11
%global Bg_Name OR11
%global bgname %(t="%{Bg_Name}";echo ${t,,})
%bcond          extras 0
Name:           %{bgname}-backgrounds
Version:        11.0.0
Release:        2%{?dist}
Summary:        Oreon 11 default desktop background
License:        CC-BY-SA-4.0
URL:            https://oreonhq.com
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch
Requires:       %{name}-budgie = %{version}-%{release}
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}
Requires:       %{name}-mate = %{version}-%{release}
Provides:       f44-backgrounds = %{version}-%{release}
# oreon:deps
BuildRequires:  kde-filesystem
BuildRequires:  make
# /oreon:deps
%description
This package contains desktop backgrounds for the Oreon %{relnum} default theme.
It pulls in themes for GNOME, KDE, MATE, Budgie, and Xfce desktops.

It provides compatibility symbol names for Fedora f44-backgrounds so packages that
still depend on those names can resolve against the Oreon wallpaper set.

%package        base
Summary:        Base images for Oreon %{relnum} default background
License:        CC-BY-SA-4.0
Provides:       f44-backgrounds-base = %{version}-%{release}
%description    base
This package contains base images for Oreon %{relnum} default background.

%package        budgie
Summary:        Oreon %{relnum} default wallpaper for Budgie
Requires:       %{name}-base = %{version}-%{release}
Recommends:     %{name}-gnome = %{version}-%{release}
Provides:       f44-backgrounds-budgie = %{version}-%{release}
%description    budgie
This package contains Budgie desktop wallpaper for the Oreon %{relnum} default theme.

%package        gnome
Summary:        Oreon %{relnum} default wallpaper for Gnome and Cinnamon
Requires:       %{name}-base = %{version}-%{release}
Provides:       f44-backgrounds-gnome = %{version}-%{release}
%description    gnome
This package contains Gnome and Cinnamon desktop wallpaper for the Oreon %{relnum}
default theme.

%package        kde
Summary:        Oreon %{relnum} default wallpaper for KDE
Requires:       %{name}-base = %{version}-%{release}
Requires:       kde-filesystem
Requires:       oreon-wallpapers
Provides:       f44-backgrounds-kde = %{version}-%{release}
Provides:       system-backgrounds-kde = %{version}-%{release}
%description    kde
This package contains KDE desktop wallpaper for the Oreon %{relnum} default theme.

%package        mate
Summary:        Oreon %{relnum} default wallpaper for Mate
Requires:       %{name}-base = %{version}-%{release}
Provides:       f44-backgrounds-mate = %{version}-%{release}
%description    mate
This package contains Mate desktop wallpaper for the Oreon %{relnum} default theme.

%if %{with extras}
%package        extras-base
Summary:        Base images for Extras Backgrounds
License:        CC-BY-4.0 AND CC-BY-SA-4.0 AND CC0-1.0
%description    extras-base
This package contains base images for supplemental wallpapers.

%package        extras-gnome
Summary:        Extra Wallpapers for Gnome and Cinnamon
Requires:       %{name}-extras-base = %{version}-%{release}
%description    extras-gnome
This package contains supplemental wallpapers for Gnome and Cinnamon.

%package        extras-mate
Summary:        Extra Wallpapers for Mate
Requires:       %{name}-extras-base = %{version}-%{release}
%description    extras-mate
This package contains supplemental wallpapers for Mate.

%package        extras-kde
Summary:        Extra Wallpapers for KDE
Requires:       %{name}-extras-base = %{version}-%{release}
%description    extras-kde
This package contains supplemental wallpapers for KDE.

%package        extras-xfce
Summary:        Extra Wallpapers for XFCE
Requires:       %{name}-extras-base = %{version}-%{release}
%description    extras-xfce
This package contains supplemental wallpapers for XFCE.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}

%build

%make_build %{?with_extras:SUBDIRS="default extras"}
%install
%make_install %{?with_extras:SUBDIRS="default extras"}
chmod 644 %{buildroot}%{_datadir}/wallpapers/%{Bg_Name}/metadata.json
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n or11-backgrounds-base -f %{oreon_filedir}/or11-backgrounds-base.list
%files -n or11-backgrounds-budgie -f %{oreon_filedir}/or11-backgrounds-budgie.list
%files -n or11-backgrounds-gnome -f %{oreon_filedir}/or11-backgrounds-gnome.list
%files -n or11-backgrounds-kde -f %{oreon_filedir}/or11-backgrounds-kde.list
%files -n or11-backgrounds-mate -f %{oreon_filedir}/or11-backgrounds-mate.list
%files -n or11-backgrounds-extras-base -f %{oreon_filedir}/or11-backgrounds-extras-base.list
%files -n or11-backgrounds-extras-gnome -f %{oreon_filedir}/or11-backgrounds-extras-gnome.list
%files -n or11-backgrounds-extras-mate -f %{oreon_filedir}/or11-backgrounds-extras-mate.list
%files -n or11-backgrounds-extras-kde -f %{oreon_filedir}/or11-backgrounds-extras-kde.list
%files -n or11-backgrounds-extras-xfce -f %{oreon_filedir}/or11-backgrounds-extras-xfce.list

%changelog

%autochangelog
