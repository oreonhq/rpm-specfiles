%global source0_hash f69673a09dad34882dbeebb0dcf993951446180235bbc3c7bedeeeea952de413
Name:           constantine-backgrounds
Version:        12.1.1
Release:        1%{?dist}
Summary:        Constantine desktop backgrounds
License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F12_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.lzma
BuildArch:      noarch
Requires:       %{name}-single = %{version}-%{release}
# oreon:deps
BuildRequires:  kde4-filesystem
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles constantine-backgrounds-single usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles constantine-backgrounds-extras usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles constantine-backgrounds-kde usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles constantine-backgrounds-extras-kde usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n constantine-backgrounds-single -f %{oreon_filedir}/constantine-backgrounds-single.list
%files -n constantine-backgrounds-extras -f %{oreon_filedir}/constantine-backgrounds-extras.list
%files -n constantine-backgrounds-kde -f %{oreon_filedir}/constantine-backgrounds-kde.list
%files -n constantine-backgrounds-extras-kde -f %{oreon_filedir}/constantine-backgrounds-extras-kde.list

%changelog

%autochangelog
