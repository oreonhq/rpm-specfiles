%global source0_hash c5f451948a1b359487bf3f22c19ae18707d2fbd554c0ad9cc26edd8b09e40c62

Name:           lovelock-backgrounds
Version:        14.91.1
Release:        31%{?dist}
Summary:        Lovelock desktop backgrounds

License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F14_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.xz

BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires:  kde4-filesystem
BuildRequires: make
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}

%description
This package contains desktop backgrounds for the Lovelock theme. Pulls in both
Gnome and KDE themes.

%package        single
Summary:        Single screen images for Lovelock Backgrounds
License:        CC-BY-SA-4.0

%description    single
This package contains single screen images for Lovelock Backgrounds

#%package        animated
#Summary:        Images for Time of Day animation for Lovelock Backgrounds
#Group:          Applications/Multimedia
#License:        CC-BY-SA-4.0
#Requires:       %{name}-single = %{version}-%{release}

#%description    animated
#This package contains single screen images for Time of Day animation for 
#Lovelock Backgrounds

#%package        animated-gnome
#Summary:        Time of Day animation for Lovelock Backgrounds for Gnome
#Group:          Applications/Multimedia
#License:        CC-BY-SA-4.0
#Requires:       %{name}-animated = %{version}-%{release}

#%description    animated-gnome
#This package contains Time of Day animated wallpaper for Gnome dekstop for
#the Lovelock theme.

%package        kde 
Summary:        Lovelock Wallpapers for KDE 

Requires:       %{name}-single = %{version}-%{release} 
Requires:       kde-filesystem

%description    kde 
This package contains KDE desktop wallpapers for the Lovelock theme.

%package        gnome 
Summary:        Lovelock Wallpapers for Gnome 

Requires:       %{name}-single = %{version}-%{release} 

%description    gnome 
This package contains Gnome desktop wallpapers for the Lovelock theme.

%package        xfce 
Summary:        Lovelock Wallpapers for XFCE4 

Requires:       %{name}-single = %{version}-%{release} 
Requires:       xfdesktop

%description    xfce 
This package contains XFCE4 desktop wallpapers for the Lovelock theme.

%package        stripes-single
Summary:        Single screen images for Lovelock Stripes Backgrounds
License:        CC-BY-SA-4.0

%description    stripes-single
This package contains single screen images for Lovelock Stripes Backgrounds

#%package        stripes-animated
#Summary:        Images for Time of Day animation for Lovelock Stripes Backgrounds
#Group:          Applications/Multimedia
#Requires:       %{name}-stripes-single = %{version}-%{release}

#%description    stripes-animated
#This package contains single screen images for Time of Day animation for 
#Lovelock Stripes Backgrounds

#%package        stripes-animated-gnome
#Summary:        Time of Day animation for Lovelock Stripes Backgrounds for Gnome
#Group:          Applications/Multimedia
#Requires:       %{name}-stripes-animated = %{version}-%{release}

#%description    stripes-animated-gnome
#This package contains Time of Day animated wallpaper for Gnome dekstop for
#the Lovelock Stripes theme.

%package        stripes-kde 
Summary:        Lovelock Stripes Wallpapers for KDE 

Requires:       %{name}-stripes-single = %{version}-%{release} 
Requires:       kde-filesystem

%description    stripes-kde 
This package contains KDE desktop wallpapers for the Lovelock Stripes theme.

%package        stripes-gnome 
Summary:        Lovelock Stripes Wallpapers for Gnome 

Requires:       %{name}-stripes-single = %{version}-%{release} 

%description    stripes-gnome 
This package contains Gnome desktop wallpapers for the Lovelock Stripes
theme.

%package        stripes-xfce 
Summary:        Lovelock Stripes Wallpapers for XFCE4 

Requires:       %{name}-stripes-single = %{version}-%{release} 
Requires:       xfdesktop

%description    stripes-xfce 
This package contains XFCE4 desktop wallpapers for the Lovelock Stripes
theme.

#%package        extras-single
#Summary:        Single screen images for Lovelock Extras Backrounds
#Group:          Applications/Multimedia
#License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1

#%description    extras-single
#This package contains single screen images for Lovelock supplemental wallpapers

#%package        extras-gnome
#Summary:        Extra Lovelock Wallpapers for Gnome
#Group:          Applications/Multimedia

#Requires:       %{name}-extras-single

#%description    extras-gnome
#This package contains Lovelock supplemental wallpapers for Gnome

#%package        extras-kde
#Summary:        Extra Lovelock Wallpapers for KDE
#Group:          Applications/Multimedia

#Requires:       %{name}-extras-single

#%description    extras-kde
#This package contains Lovelock supplemental wallpapers for Gnome

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

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
%dir %{_datadir}/backgrounds/lovelock
%dir %{_datadir}/backgrounds/lovelock/default
%{_datadir}/backgrounds/lovelock/default/normalish
%{_datadir}/backgrounds/lovelock/default/standard
%{_datadir}/backgrounds/lovelock/default/wide

#%files animated
#%defattr(-,root,root,-)
#%dir %{_datadir}/backgrounds/lovelock/default-tod
#%{_datadir}/backgrounds/lovelock/default-tod/normalish
#%{_datadir}/backgrounds/lovelock/default-tod/standard
#%{_datadir}/backgrounds/lovelock/default-tod/wide

#%files animated-gnome
#%defattr(-,root,root,-)
#%{_datadir}/backgrounds/lovelock/default-tod/lovelock.xml
#%{_datadir}/gnome-background-properties/desktop-backgrounds-lovelock-animated.xml

%files kde
%{_kde4_datadir}/wallpapers/Lovelock/

%files gnome
%{_datadir}/backgrounds/lovelock/default/lovelock.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-lovelock.xml

%files xfce
%{_datadir}/xfce4/backdrops/lovelock.png

%files stripes-single
%doc CC-BY-SA?3.0 Attribution-Stripes
%dir %{_datadir}/backgrounds/lovelock
%dir %{_datadir}/backgrounds/lovelock/default-stripes
%{_datadir}/backgrounds/lovelock/default-stripes/normalish
%{_datadir}/backgrounds/lovelock/default-stripes/standard
%{_datadir}/backgrounds/lovelock/default-stripes/wide

#%files stripes-animated
#%defattr(-,root,root,-)
#%dir %{_datadir}/backgrounds/lovelock/default-stripes-tod
#%{_datadir}/backgrounds/lovelock/default-stripes-tod/normalish
#%{_datadir}/backgrounds/lovelock/default-stripes-tod/standard
#%{_datadir}/backgrounds/lovelock/default-stripes-tod/wide

#%files stripes-animated-gnome
#%defattr(-,root,root,-)
#%{_datadir}/backgrounds/lovelock/default-stripes-tod/lovelock.xml
#%{_datadir}/gnome-background-properties/desktop-backgrounds-lovelock-stripes-animated.xml

%files stripes-kde
%{_kde4_datadir}/wallpapers/Lovelock_Stripes/

%files stripes-gnome
%{_datadir}/backgrounds/lovelock/default-stripes/lovelock.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-lovelock-stripes.xml

%files stripes-xfce
%{_datadir}/xfce4/backdrops/lovelock-stripes.png

#%files extras-single
#%doc CC-BY\ 2.0 CC-BY-SA\ 2.0 CC-BY-SA\ 3.0 Attribution
#%defattr(-,root,root,-)
#%{_datadir}/backgrounds/lovelock/extras/*.jpg

#%files extras-gnome
#%defattr(-,root,root,-)
#%{_datadir}/backgrounds/lovelock/extras/lovelock-extras.xml
#%{_datadir}/gnome-background-properties/desktop-backgrounds-lovelock-extras.xml

#%files extras-kde
#%defattr(-,root,root,-)
#%{_kde4_datadir}/wallpapers/Lovelock_*/

%changelog
%autochangelog
