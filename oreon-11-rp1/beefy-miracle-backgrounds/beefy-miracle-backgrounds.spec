%global source0_hash 57c97b3f377bb3ceaaf92eb749af421e8af3433129e1b356faef1fe1f75b3467
Name:           beefy-miracle-backgrounds
Version:        16.91.0
Release:        31%{?dist}
Summary:        Beefy Miracle desktop backgrounds
License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F17_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.xz
BuildArch:      noarch
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}
# oreon:deps
BuildRequires:  kde4-filesystem
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles beefy-miracle-backgrounds-single usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles beefy-miracle-backgrounds-kde usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles beefy-miracle-backgrounds-gnome usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles beefy-miracle-backgrounds-xfce usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n beefy-miracle-backgrounds-single -f %{oreon_filedir}/beefy-miracle-backgrounds-single.list
%files -n beefy-miracle-backgrounds-kde -f %{oreon_filedir}/beefy-miracle-backgrounds-kde.list
%files -n beefy-miracle-backgrounds-gnome -f %{oreon_filedir}/beefy-miracle-backgrounds-gnome.list
%files -n beefy-miracle-backgrounds-xfce -f %{oreon_filedir}/beefy-miracle-backgrounds-xfce.list

%changelog

%autochangelog
