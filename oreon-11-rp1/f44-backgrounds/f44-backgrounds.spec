%global source0_hash af89f257364e67aea21b6b7f5e98505026a962181a9ab5594a65938a30d2d3ff
%global relnum 44
%global Bg_Name F44
%global bgname %(t="%{Bg_Name}";echo ${t,,})
%bcond          extras 0
Name:           %{bgname}-backgrounds
Version:        %{relnum}.0.0
Release:        1%{?dist}
Summary:        Fedora 44 default desktop background
License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/Design
Source0:        https://forge.fedoraproject.org/design/backgrounds/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildArch:      noarch
Requires:       %{name}-budgie = %{version}-%{release}
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}
Requires:       %{name}-mate = %{version}-%{release}
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  kde-filesystem
BuildRequires:  make
# /oreon:deps
%description
This package contains desktop backgrounds for the Fedora  %{relnum} default
theme.  Pulls in themes for GNOME, KDE, Mate and Xfce desktops.

%package        base
Summary:        Base images for Fedora  %{relnum} default background
License:        CC-BY-SA-4.0
Requires:       (jxl-pixbuf-loader if gdk-pixbuf2)
Requires:       (kf6-kimageformats if qt6-qtbase-gui)
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

%if %{with extras}
%package        extras-base
Summary:        Base images for  Extras Backgrounds
License:        CC-BY-4.0 AND CC-BY-SA-4.0 AND CC0-1.0
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
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%make_build %{?with_extras:SUBDIRS="default extras"}
%install
%make_install %{?with_extras:SUBDIRS="default extras"}
chmod 644 %{buildroot}%{_datadir}/wallpapers/%{Bg_Name}/metadata.json
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n f44-backgrounds-base -f %{oreon_filedir}/f44-backgrounds-base.list
%files -n f44-backgrounds-budgie -f %{oreon_filedir}/f44-backgrounds-budgie.list
%files -n f44-backgrounds-gnome -f %{oreon_filedir}/f44-backgrounds-gnome.list
%files -n f44-backgrounds-kde -f %{oreon_filedir}/f44-backgrounds-kde.list
%files -n f44-backgrounds-mate -f %{oreon_filedir}/f44-backgrounds-mate.list
%files -n f44-backgrounds-extras-base -f %{oreon_filedir}/f44-backgrounds-extras-base.list
%files -n f44-backgrounds-extras-gnome -f %{oreon_filedir}/f44-backgrounds-extras-gnome.list
%files -n f44-backgrounds-extras-mate -f %{oreon_filedir}/f44-backgrounds-extras-mate.list
%files -n f44-backgrounds-extras-kde -f %{oreon_filedir}/f44-backgrounds-extras-kde.list
%files -n f44-backgrounds-extras-xfce -f %{oreon_filedir}/f44-backgrounds-extras-xfce.list

%changelog

%autochangelog
