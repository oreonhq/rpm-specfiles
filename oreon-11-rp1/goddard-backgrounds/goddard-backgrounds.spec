%global source0_hash 622e0230a17f86a872c56ffa0934d4da26b25aeec9907d1ba6464ac160755818
Name:           goddard-backgrounds
Version:        13.0.0
Release:        1%{?dist}
Summary:        Goddard desktop backgrounds
License:        LicenseRef-Callaway-CC-BY-SA
URL:            https://fedoraproject.org/wiki/F12_Artwork
Source0:        https://fedorahosted.org/released/design-team/%{name}-%{version}.tar.lzma
BuildArch:      noarch
Requires:       %{name}-gnome = %{version}-%{release}
Requires:       %{name}-kde = %{version}-%{release}
# oreon:deps
BuildRequires:  kde4-filesystem
BuildRequires:  make
# /oreon:deps
%description
This package contains desktop backgrounds for the Goddard theme. Pulls in both
Gnome and KDE themes.

%package        single
Summary:        Single screen images for Goddard Backgrounds
%description    single
This package contains Single screen images for Goddard Backgrounds

%package        kde 
Summary:        Goddard Wallpapers for KDE 
Requires:       %{name}-single = %{version}-%{release} 
Requires:       kde-filesystem
%description    kde 
This package contains KDE desktop wallpapers for the Goddard theme.

%package        gnome 
Summary:        Goddard Wallpapers for Gnome 
Requires:       %{name}-single = %{version}-%{release} 
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n goddard-backgrounds-single -f %{oreon_filedir}/goddard-backgrounds-single.list
%files -n goddard-backgrounds-kde -f %{oreon_filedir}/goddard-backgrounds-kde.list
%files -n goddard-backgrounds-gnome -f %{oreon_filedir}/goddard-backgrounds-gnome.list

%changelog

%autochangelog
