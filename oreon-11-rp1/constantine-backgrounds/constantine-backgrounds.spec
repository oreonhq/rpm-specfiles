%global source0_hash none

Name:           constantine-backgrounds
Version:        12.1.1
Release:        33%{?dist}
Summary:        Constantine desktop backgrounds

License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F12_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.lzma

BuildArch:      noarch

#BuildRequires:  inkscape
# for %%_kde4_* macros
BuildRequires:	kde4-filesystem
BuildRequires: make
Requires:       %{name}-single = %{version}-%{release}

%if 0%{?fedora} == 12
Provides: system-backgrounds
%endif

%description
This package contains desktop backgrounds for the Constantine theme.

%package        single
Summary:        Single screen images for Constantine Backgrounds
Conflicts:      %{name} < 12.0.0

%description    single
This package contains Single screen images for Constantine Backgrounds

%package        extras
Summary:        Extra Constantine Backgrounds

%description    extras
This package contains aditional desktop backgrounds for the Constantine theme.

%package        kde 
Summary:        Constantine Wallpapers for KDE 
Obsoletes:      constantine-kde-theme <= 11.90.0
%if 0%{?fedora} == 12
Provides:       system-backgrounds-kde
%endif

Requires:       %{name}-single = %{version}-%{release} 
Requires:       kde-filesystem

%description    kde 
This package contains KDE desktop wallpapers for the Constantine theme.

%package        extras-kde
Summary:        Extra Constantine Wallpapers for KDE 

Requires:       %{name}-extras = %{version}-%{release}

%description    extras-kde
This package contains aditional KDE desktop wallpapers for the Constantine theme.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc
%{_datadir}/backgrounds/constantine/default/standard.dual
%{_datadir}/backgrounds/constantine/default/wide.dual
%{_datadir}/backgrounds/constantine/default/normalish.dual
%{_datadir}/backgrounds/constantine/default/constantine.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-constantine.xml

%files single
%doc COPYING Credits
%dir %{_datadir}/backgrounds/constantine
%dir %{_datadir}/backgrounds/constantine/default
%{_datadir}/backgrounds/constantine/default/standard
%{_datadir}/backgrounds/constantine/default/wide
%{_datadir}/backgrounds/constantine/default/normalish

%files extras
%doc COPYING Credits
%dir %{_datadir}/backgrounds/constantine
%{_datadir}/backgrounds/constantine/extras
%{_datadir}/gnome-background-properties/desktop-backgrounds-constantine-extras.xml

%files kde
%{_kde4_datadir}/wallpapers/Constantine/

%files extras-kde
%{_kde4_datadir}/wallpapers/Constantine_mosaico/
%{_kde4_datadir}/wallpapers/Constantine_4flowers/
%{_kde4_datadir}/wallpapers/Constantine_constantine/
%{_kde4_datadir}/wallpapers/Constantine_pruebas/
%{_kde4_datadir}/wallpapers/Constantine_rose/
%{_kde4_datadir}/wallpapers/Constantine_rain/

%changelog
%autochangelog
