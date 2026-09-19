%global source0_hash none

%global bgname f22
%global Bg_Name F22
# Extras will be enabled later
%global with_extras 1

Name:           %{bgname}-backgrounds
Version:        22.1.1
Release:        22%{?dist}
Summary:        Fedora 22 default desktop background

License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F22_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.xz

BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires:  kde4-filesystem
BuildRequires: make
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}
Requires:       %{name}-xfce = %{version}-%{release}
Requires:       %{name}-mate = %{version}-%{release}

%description
This package contains desktop backgrounds for the Fedora 22 default theme.
Pulls in themes for GNOME, KDE, Mate and Xfce desktops.

%package        base
Summary:        Base images for Fedora 22 default background
License:        CC-BY-SA-4.0

%description    base
This package contains base images for Fedora 22 default background.

%package        kde
Summary:        Fedora 22 default wallpaper for KDE

Requires:       %{name}-base = %{version}-%{release}
Requires:       kde-filesystem

%description    kde
This package contains KDE desktop wallpaper for the Fedora 22
default theme.

%package        gnome
Summary:        Fedora 22 default wallpaper for Gnome and Cinnamon

Requires:       %{name}-base = %{version}-%{release}

%description    gnome
This package contains Gnome/Cinnamon desktop wallpaper for the
Fedora 22 default theme.

%package        mate
Summary:        Fedora 22 default wallpaper for Mate

Requires:       %{name}-base = %{version}-%{release}

%description    mate
This package contains Mate desktop wallpaper for the Fedora 22
default theme.

%package        xfce
Summary:        Fedora 22 default background for XFCE4

Requires:       %{name}-base = %{version}-%{release}
Requires:       xfdesktop

%description    xfce
This package contains XFCE4 desktop background for the Fedora 22
default theme.

%if %{with_extras}
%package        extras-base
Summary:        Base images for F22 Extras Backrounds
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1

%description    extras-base
This package contains base images for F22 supplemental
wallpapers.

%package        extras-gnome
Summary:        Extra F22 Wallpapers for Gnome and Cinnamon
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-base

%description    extras-gnome
This package contains F22 supplemental wallpapers for Gnome
and Cinnamon

%package        extras-mate
Summary:        Extra F22 Wallpapers for Mate
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-base

%description    extras-mate
This package contains F22 supplemental wallpapers for Mate

%package        extras-kde
Summary:        Extra F22 Wallpapers for KDE
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-base

%description    extras-kde
This package contains F22 supplemental wallpapers for Gnome

%package        extras-xfce
Summary:        Extra F22 Wallpapers for XFCE
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-base

%description    extras-xfce
This package contains F22 supplemental wallpapers for XFCE
%endif

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc

%files base
%doc CC-BY-SA-3.0 Attribution
%dir %{_datadir}/backgrounds/%{bgname}
%dir %{_datadir}/backgrounds/%{bgname}/default
%{_datadir}/backgrounds/%{bgname}/default/normalish
%{_datadir}/backgrounds/%{bgname}/default/standard
%{_datadir}/backgrounds/%{bgname}/default/wide
%{_datadir}/backgrounds/%{bgname}/default/tv-wide
%{_datadir}/backgrounds/%{bgname}/default/%{bgname}.xml

%files kde
%{_kde4_datadir}/wallpapers/%{Bg_Name}/

%files gnome
%{_datadir}/gnome-background-properties/%{bgname}.xml

%files mate
%{_datadir}/mate-background-properties/%{bgname}.xml

%files xfce
%{_datadir}/xfce4/backdrops/%{bgname}.png

%if %{with_extras}
%files extras-base
%doc CC-BY-SA-3.0 CC-BY-3.0 CC0-1.0 Attribution-Extras
%{_datadir}/backgrounds/%{bgname}/extras/*.jpg
%{_datadir}/backgrounds/%{bgname}/extras/*.png
%{_datadir}/backgrounds/%{bgname}/extras/%{bgname}-extras.xml

%files extras-gnome
%{_datadir}/gnome-background-properties/%{bgname}-extras.xml

%files extras-kde
%{_kde4_datadir}/wallpapers/%{Bg_Name}_*/

%files extras-mate
%{_datadir}/mate-background-properties/%{bgname}-extras.xml

%files extras-xfce
%{_datadir}/xfce4/backdrops/*.jpg
%{_datadir}/xfce4/backdrops/*.png
%endif

%changelog
%autochangelog
