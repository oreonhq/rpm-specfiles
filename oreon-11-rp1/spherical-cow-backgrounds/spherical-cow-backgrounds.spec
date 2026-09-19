%global source0_hash none

Name:           spherical-cow-backgrounds
Version:        18.0.0
Release:        26%{?dist}
Summary:        Spherical Cow desktop backgrounds

License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F18_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.xz

BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires: make
BuildRequires:  kde4-filesystem
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}

%description
This package contains desktop backgrounds for the Spherical Cow theme.
Pulls in both Gnome and KDE themes.

%package        single
Summary:        Single screen images for Spherical Cow Backgrounds
License:        CC-BY-SA-4.0

%description    single
This package contains single screen images for Spherical Cow
Backgrounds.

%package        kde
Summary:        Spherical Cow Wallpapers for KDE

Requires:       %{name}-single = %{version}-%{release}
Requires:       kde-filesystem

%description    kde
This package contains KDE desktop wallpapers for the Spherical Cow
theme.

%package        gnome
Summary:        Spherical Cow Wallpapers for Gnome

Requires:       %{name}-single = %{version}-%{release}

%description    gnome
This package contains Gnome desktop wallpapers for the Spherical Cow
theme.

%package        xfce
Summary:        Spherical Cow Wallpapers for XFCE4

Requires:       %{name}-single = %{version}-%{release}
Requires:       xfdesktop

%description    xfce
This package contains XFCE4 desktop wallpapers for the Spherical Cow
theme.

%package        extras-single
Summary:        Single screen images for Spherical Cow Extras Backrounds
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1

%description    extras-single
This package contains single screen images for Spherical Cow supplemental
wallpapers.

%package        extras-gnome
Summary:        Extra Spherical Cow Wallpapers for Gnome
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-single

%description    extras-gnome
This package contains Spherical Cow supplemental wallpapers for Gnome

%package        extras-kde
Summary:        Extra Spherical Cow Wallpapers for KDE
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-single

%description    extras-kde
This package contains Spherical Cow supplemental wallpapers for Gnome

%package        extras-xfce
Summary:        Extra Spherical Cow Wallpapers for XFCE
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-single

%description    extras-xfce
This package contains Spherical Cow supplemental wallpapers for XFCE

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc

%files single
%doc CC-BY-SA?3.0 Attribution
%dir %{_datadir}/backgrounds/spherical-cow
%dir %{_datadir}/backgrounds/spherical-cow/default
%{_datadir}/backgrounds/spherical-cow/default/normalish
%{_datadir}/backgrounds/spherical-cow/default/standard
%{_datadir}/backgrounds/spherical-cow/default/wide

%files kde
%{_kde4_datadir}/wallpapers/Spherical_Cow/

%files gnome
%{_datadir}/backgrounds/spherical-cow/default/spherical-cow.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-spherical-cow.xml

%files xfce
%{_datadir}/xfce4/backdrops/spherical-cow.png

%files extras-single
%doc CC-BY-SA?3.0 CC-BY-SA?2.0 CC-BY?2.0 Attribution-Extras
%{_datadir}/backgrounds/spherical-cow/extras/*.jpg

%files extras-gnome
%{_datadir}/backgrounds/spherical-cow/extras/spherical-cow-extras.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-spherical-cow-extras.xml

%files extras-kde
%{_kde4_datadir}/wallpapers/Spherical_Cow_*/

%files extras-xfce
%{_datadir}/xfce4/backdrops/*.jpg

%changelog
%autochangelog
