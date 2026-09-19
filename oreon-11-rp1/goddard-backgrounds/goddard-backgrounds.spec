%global source0_hash 622e0230a17f86a872c56ffa0934d4da26b25aeec9907d1ba6464ac160755818

Name:           goddard-backgrounds
Version:        13.0.0
Release:        31%{?dist}
Summary:        Goddard desktop backgrounds

# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA
URL:            https://fedoraproject.org/wiki/F12_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.lzma

BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires:  kde4-filesystem
BuildRequires: make
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}

%description
This package contains desktop backgrounds for the Goddard theme. Pulls in both
Gnome and KDE themes.

%package        single
Summary:        Single screen images for Goddard Backgrounds

%description    single
This package contains Single screen images for Goddard Backgrounds

%package        kde 
Summary:        Goddard Wallpapers for KDE 
%if 0%{?fedora} == 13
Provides:       system-backgrounds-kde
%endif

Requires:       %{name}-single = %{version}-%{release} 
Requires:       kde-filesystem

%description    kde 
This package contains KDE desktop wallpapers for the Goddard theme.

%package        gnome 
Summary:        Goddard Wallpapers for Gnome 

Requires:       %{name}-single = %{version}-%{release} 
%if 0%{?fedora} == 13
# FIXME: Which provides I should use?
Provides:        system-backgrounds
#Provides:        system-backgrounds-gnome
%endif

%description    gnome 
This package contains Gnome desktop wallpapers for the Goddard theme.

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
%doc COPYING Credits
#There'll be also dual wallpapers in dual subpackage in the future, hence the 
# %%dir ownership is separated
%dir %{_datadir}/backgrounds/goddard
%dir %{_datadir}/backgrounds/goddard/default
%{_datadir}/backgrounds/goddard/default/normalish
%{_datadir}/backgrounds/goddard/default/standard
%{_datadir}/backgrounds/goddard/default/wide

%files kde
%{_kde4_datadir}/wallpapers/Goddard/

%files gnome
%{_datadir}/backgrounds/goddard/default/goddard.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-goddard.xml

%changelog
%autochangelog
