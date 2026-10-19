%global source0_hash c5f451948a1b359487bf3f22c19ae18707d2fbd554c0ad9cc26edd8b09e40c62
Name:           lovelock-backgrounds
Version:        14.91.1
Release:        1%{?dist}
Summary:        Lovelock desktop backgrounds
License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F14_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.xz
BuildArch:      noarch
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}
# oreon:deps
BuildRequires:  kde4-filesystem
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lovelock-backgrounds-single -f %{oreon_filedir}/lovelock-backgrounds-single.list
%files -n lovelock-backgrounds-kde -f %{oreon_filedir}/lovelock-backgrounds-kde.list
%files -n lovelock-backgrounds-gnome -f %{oreon_filedir}/lovelock-backgrounds-gnome.list
%files -n lovelock-backgrounds-xfce -f %{oreon_filedir}/lovelock-backgrounds-xfce.list
%files -n lovelock-backgrounds-stripes-single -f %{oreon_filedir}/lovelock-backgrounds-stripes-single.list
%files -n lovelock-backgrounds-stripes-kde -f %{oreon_filedir}/lovelock-backgrounds-stripes-kde.list
%files -n lovelock-backgrounds-stripes-gnome -f %{oreon_filedir}/lovelock-backgrounds-stripes-gnome.list
%files -n lovelock-backgrounds-stripes-xfce -f %{oreon_filedir}/lovelock-backgrounds-stripes-xfce.list

%changelog

%autochangelog
