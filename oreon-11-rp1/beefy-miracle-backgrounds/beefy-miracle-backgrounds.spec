%global source0_hash c1b852af14c7b053e490c4a429ee09501d184e90c7408584f708fa44a649705e

Name:           beefy-miracle-backgrounds
Version:        16.91.0
Release:        31%{?dist}
Summary:        Beefy Miracle desktop backgrounds

License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F17_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.xz

BuildArch:      noarch

# for %%_kde4_* macros
BuildRequires:  kde4-filesystem
BuildRequires: make
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}

%description
This package contains desktop backgrounds for the Beefy Miracle theme.
Pulls in both Gnome and KDE themes.

%package        single
Summary:        Single screen images for Beefy Miracle Backgrounds
License:        CC-BY-SA-4.0

%description    single
This package contains single screen images for Beefy Miracle
Backgrounds.

%package        kde
Summary:        Beefy Miracle Wallpapers for KDE

Requires:       %{name}-single = %{version}-%{release}
Requires:       kde-filesystem

%description    kde
This package contains KDE desktop wallpapers for the Beefy Miracle
theme.

%package        gnome
Summary:        Beefy Miracle Wallpapers for Gnome

Requires:       %{name}-single = %{version}-%{release}

%description    gnome
This package contains Gnome desktop wallpapers for the Beefy Miracle
theme.

%package        xfce
Summary:        Beefy Miracle Wallpapers for XFCE4

Requires:       %{name}-single = %{version}-%{release}
Requires:       xfdesktop

%description    xfce
This package contains XFCE4 desktop wallpapers for the Beefy Miracle
theme.

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
%dir %{_datadir}/backgrounds/beefy-miracle
%dir %{_datadir}/backgrounds/beefy-miracle/default
%{_datadir}/backgrounds/beefy-miracle/default/normalish
%{_datadir}/backgrounds/beefy-miracle/default/standard
%{_datadir}/backgrounds/beefy-miracle/default/wide

%files kde
%{_kde4_datadir}/wallpapers/Beefy_Miracle/

%files gnome
%{_datadir}/backgrounds/beefy-miracle/default/beefy-miracle.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-beefy-miracle.xml

%files xfce
%{_datadir}/xfce4/backdrops/beefy-miracle.png

%changelog
%autochangelog
