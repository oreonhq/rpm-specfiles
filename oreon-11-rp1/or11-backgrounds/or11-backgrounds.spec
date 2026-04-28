%global relnum 11
%global Bg_Name OR11
%global bgname %(t="%{Bg_Name}";echo ${t,,})

# Disable Extras subpackages by default (upstream extras Makefile is not validated for Oreon)
%bcond          extras 0

Name:           %{bgname}-backgrounds
Version:        11.0.0
Release:        1%{?dist}
Summary:        Oreon %{relnum} default desktop background

License:        CC-BY-SA-4.0
URL:            https://oreonhq.com
# Modified from Fedora f44-backgrounds 44.0.0; wallpaper assets are Oreon-branded (see README in tarball).
Source0:        %{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  kde-filesystem
BuildRequires:  make

Requires:       %{name}-budgie = %{version}-%{release}
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}
%if 0%{?rhel} < 10
Requires:       %{name}-xfce = %{version}-%{release}
%endif
Requires:       %{name}-mate = %{version}-%{release}

Provides:       f44-backgrounds = %{version}-%{release}

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
Provides:       f44-backgrounds-kde = %{version}-%{release}

%description    kde
This package contains KDE desktop wallpaper for the Oreon %{relnum} default theme.

%package        mate
Summary:        Oreon %{relnum} default wallpaper for Mate
Requires:       %{name}-base = %{version}-%{release}
Provides:       f44-backgrounds-mate = %{version}-%{release}

%description    mate
This package contains Mate desktop wallpaper for the Oreon %{relnum} default theme.

%if 0%{?rhel} < 10
%package        xfce
Summary:        Oreon %{relnum} default background for XFCE4

Requires:       %{name}-base = %{version}-%{release}
Requires:       xfdesktop
Provides:       f44-backgrounds-xfce = %{version}-%{release}

%description    xfce
This package contains XFCE4 desktop background for the Oreon %{relnum} default theme.
%endif

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
%setup -q -n %{name}-%{version}


%build
%make_build %{?with_extras:SUBDIRS="default extras"}

%install
%make_install %{?with_extras:SUBDIRS="default extras"}
chmod 644 %{buildroot}%{_datadir}/wallpapers/%{Bg_Name}/metadata.json

%if 0%{?rhel} >= 10
rm -fr %{buildroot}%{_datadir}/xfce4
%endif

%files
%doc

%files base
%license CC-BY-SA-4.0 Attribution
%dir %{_datadir}/backgrounds/%{bgname}
%dir %{_datadir}/backgrounds/%{bgname}/default
%{_datadir}/backgrounds/%{bgname}/default/%{bgname}*.{png,xml}

%files kde
%{_datadir}/wallpapers/%{Bg_Name}/

%files gnome
%{_datadir}/gnome-background-properties/%{bgname}.xml
%dir %{_datadir}/gnome-background-properties/

%files budgie
%{_datadir}/gnome-background-properties/%{bgname}-budgie.xml

%files mate
%{_datadir}/mate-background-properties/%{bgname}.xml
%dir %{_datadir}/mate-background-properties/

%if 0%{?rhel} < 10
%files xfce
%{_datadir}/xfce4/backdrops/%{bgname}*.png
%if %{with extras}
%exclude %{_datadir}/xfce4/backdrops/%{bgname}-extras*.png
%endif
%dir %{_datadir}/xfce4/
%dir %{_datadir}/xfce4/backdrops/
%endif

%if %{with extras}
%files extras-base
%license CC-BY-SA-4.0 Attribution
%{_datadir}/backgrounds/%{bgname}/extras/

%files extras-gnome
%{_datadir}/gnome-background-properties/%{bgname}-extras.xml

%files extras-kde
%{_datadir}/wallpapers/%{Bg_Name}_*/

%files extras-mate
%{_datadir}/mate-background-properties/%{bgname}-extras.xml

%files extras-xfce
%{_datadir}/xfce4/backdrops/%{bgname}-extras*.png
%endif

%changelog
* Mon Apr 27 2026 Oreon Packaging Team <packaging@oreonhq.com> - 11.0.0-1
- Import from Fedora f44-backgrounds, rebrand to Oreon 11 and single PNG wallpaper
