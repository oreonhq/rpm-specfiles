%global source0_hash none

Name:           laughlin-backgrounds
Version:        14.1.0
Release:        33%{?dist}
Summary:        Laughlin desktop backgrounds

License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F14_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.lzma

BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires:  kde4-filesystem
BuildRequires: make
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}

%description
This package contains desktop backgrounds for the Laughlin theme. Pulls in both
Gnome and KDE themes.

%package        single
Summary:        Single screen images for Laughlin Backgrounds
License:        CC-BY-SA-4.0

%description    single
This package contains single screen images for Laughlin Backgrounds

%package        animated
Summary:        Images for Time of Day animation for Laughlin Backgrounds
License:        CC-BY-SA-4.0
Requires:       %{name}-single = %{version}-%{release}

%description    animated
This package contains single screen images for Time of Day animation for 
Laughlin Backgrounds

%package        animated-gnome
Summary:        Time of Day animation for Laughlin Backgrounds for Gnome
License:        CC-BY-SA-4.0
Requires:       %{name}-animated = %{version}-%{release}

%description    animated-gnome
This package contains Time of Day animated wallpaper for Gnome dekstop for
the Laughlin theme.

%package        kde 
Summary:        Laughlin Wallpapers for KDE 
%if 0%{?fedora} == 14
Provides:       system-backgrounds-kde = %{version}-%{release}
%endif

Requires:       %{name}-single = %{version}-%{release} 
Requires:       kde-filesystem

%description    kde 
This package contains KDE desktop wallpapers for the Laughlin theme.

%package        gnome 
Summary:        Laughlin Wallpapers for Gnome 

Requires:       %{name}-single = %{version}-%{release} 
%if 0%{?fedora} == 14
Provides:        system-backgrounds-gnome = %{version}-%{release}
%endif

%description    gnome 
This package contains Gnome desktop wallpapers for the Laughlin theme.

%package        extras-single
Summary:        Single screen images for Laughlin Extras Backrounds
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1

%description    extras-single
This package contains single screen images for Laughlin supplemental wallpapers

%package        extras-gnome
Summary:        Extra Laughlin Wallpapers for Gnome
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-single

%description    extras-gnome
This package contains Laughlin supplemental wallpapers for Gnome

%package        extras-kde
Summary:        Extra Laughlin Wallpapers for KDE
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:       %{name}-extras-single

%description    extras-kde
This package contains Laughlin supplemental wallpapers for Gnome

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
#There'll be also dual wallpapers in dual subpackage in the future, hence the 
# %%dir ownership is treated separately
%dir %{_datadir}/backgrounds/laughlin
%dir %{_datadir}/backgrounds/laughlin/default
%{_datadir}/backgrounds/laughlin/default/normalish
%{_datadir}/backgrounds/laughlin/default/standard
%{_datadir}/backgrounds/laughlin/default/wide

%files animated
%dir %{_datadir}/backgrounds/laughlin/default-tod
%{_datadir}/backgrounds/laughlin/default-tod/normalish
%{_datadir}/backgrounds/laughlin/default-tod/standard
%{_datadir}/backgrounds/laughlin/default-tod/wide

%files animated-gnome
%{_datadir}/backgrounds/laughlin/default-tod/laughlin.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-laughlin-animated.xml

%files kde
%{_kde4_datadir}/wallpapers/Laughlin/

%files gnome
%{_datadir}/backgrounds/laughlin/default/laughlin.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-laughlin.xml

%files extras-single
%doc CC-BY?2.0 CC-BY-SA?2.0 CC-BY-SA?3.0 Attribution
%defattr(-,root,root,-)
%{_datadir}/backgrounds/laughlin/extras/*.jpg

%files extras-gnome
%{_datadir}/backgrounds/laughlin/extras/laughlin-extras.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-laughlin-extras.xml

%files extras-kde
%{_kde4_datadir}/wallpapers/Laughlin_*/

%changelog
%autochangelog
