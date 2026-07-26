%global source0_hash none

Name:           verne-backgrounds
Version:        15.92.1
Release:        30%{?dist}
Summary:        Verne desktop backgrounds

License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F16_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.xz

BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires: make
BuildRequires:  kde4-filesystem
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}

%description
This package contains desktop backgrounds for the Verne theme. Pulls in both
Gnome and KDE themes.

%package        single
Summary:        Single screen images for Verne Backgrounds
License:        CC-BY-SA-4.0

%description    single
This package contains single screen images for Verne Backgrounds

#%package        animated
#Summary:        Images for Time of Day animation for Verne Backgrounds
#Group:          Applications/Multimedia
#Requires:       %{name}-single = %{version}-%{release}

#%description    animated
#This package contains single screen images for Time of Day animation for
#Verne Backgrounds

#%package        animated-gnome
#Summary:        Time of Day animation for Verne Backgrounds for Gnome
#Group:          Applications/Multimedia
#Requires:       %{name}-animated = %{version}-%{release}

#%description    animated-gnome
#This package contains Time of Day animated wallpaper for Gnome dekstop for
#the Verne theme.

%package        kde
Summary:        Verne Wallpapers for KDE

Requires:       %{name}-single = %{version}-%{release}
Requires:       kde-filesystem

%description    kde
This package contains KDE desktop wallpapers for the Verne theme.

%package        gnome
Summary:        Verne Wallpapers for Gnome

Requires:       %{name}-single = %{version}-%{release}

%description    gnome
This package contains Gnome desktop wallpapers for the Verne theme.

%package        xfce
Summary:        Verne Wallpapers for XFCE4

Requires:       %{name}-single = %{version}-%{release}
Requires:       xfdesktop

%description    xfce
This package contains XFCE4 desktop wallpapers for the Verne theme.

%package        extras-single
Summary:        Single screen images for Verne Extras Backrounds
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1

%description    extras-single
This package contains single screen images for Verne supplemental wallpapers

%package        extras-gnome
Summary:        Extra Verne Wallpapers for Gnome
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-single

%description    extras-gnome
This package contains Verne supplemental wallpapers for Gnome

%package        extras-kde
Summary:        Extra Verne Wallpapers for KDE
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-single

%description    extras-kde
This package contains Verne supplemental wallpapers for Gnome

%package        extras-xfce
Summary:        Extra Verne Wallpapers for XFCE
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-single

%description    extras-xfce
This package contains Verne supplemental wallpapers for XFCE

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc

%files single
%doc CC-BY-SA?3.0 Attribution
%dir %{_datadir}/backgrounds/verne
%dir %{_datadir}/backgrounds/verne/default
%{_datadir}/backgrounds/verne/default/normalish
%{_datadir}/backgrounds/verne/default/standard
%{_datadir}/backgrounds/verne/default/wide

#%files animated
#%defattr(-,root,root,-)
#%dir %{_datadir}/backgrounds/verne/default-tod
#%{_datadir}/backgrounds/verne/default-tod/normalish
#%{_datadir}/backgrounds/verne/default-tod/standard
#%{_datadir}/backgrounds/verne/default-tod/wide

#%files animated-gnome
#%defattr(-,root,root,-)
#%{_datadir}/backgrounds/verne/default-tod/verne.xml
#%{_datadir}/gnome-background-properties/desktop-backgrounds-verne-animated.xml

%files kde
%{_kde4_datadir}/wallpapers/Verne/

%files gnome
%{_datadir}/backgrounds/verne/default/verne.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-verne.xml

%files xfce
%{_datadir}/xfce4/backdrops/verne.png

%files extras-single
%doc CC-BY-SA?3.0 Attribution-Extras
%defattr(-,root,root,-)
%{_datadir}/backgrounds/verne/extras/*.jpg

%files extras-gnome
%{_datadir}/backgrounds/verne/extras/verne-extras.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-verne-extras.xml

%files extras-kde
%{_kde4_datadir}/wallpapers/Verne_*/

%files extras-xfce
%{_datadir}/xfce4/backdrops/*.jpg

%changelog
%autochangelog
