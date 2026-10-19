%global source0_hash none
Name:           leonidas-backgrounds
Version:        11.0.0
Release:        1%{?dist}
Summary:        Leonidas desktop backgrounds
License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F11_Artwork
Source0:        %{name}-%{version}.tar.lzma
BuildArch:      noarch
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-lion-dual = %{version}-%{release}
# oreon:deps

# /oreon:deps
%description
This package contains desktop backgrounds for the leonidas theme.

%prep

%setup -q

%package        common
Summary:        Leonidas desktop backgrounds shared between GNOME and KDE
%description    common
This package includes the common files used by both GNOME and KDE.

%package        kdm
Summary:        Leonidas desktop background for KDM
%description    kdm
Leonidas desktop background used in KDM.

%package        landscape
Summary:        Leonidas desktop backgrounds with the landscape theme
%description    landscape
This package includes additional Leonidas backgrounds based on the landscape
theme that was used in F11 Leonidas Beta.

%package        lion
Summary:        Extra leonidas desktop background featuring lion 
Requires:       %{name}-lion-dual = %{version}-%{release}
%description    lion
This package includes extra leonidas background featuring the lion that is 
present in F11 Leonidas only on dual screens both on single screens as well.

%package        lion-dual
Summary:        Shared dual screen lion themed Leonidas desktop backgrounds
%description    lion-dual
This package includes dual screen images shared between the 
leonidas-backgrounds and leonidas-backgrounds-lion packages.

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape/normal
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape/wide
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape/normal.dual
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape/wide.dual
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion/normal
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion/normalish
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion/wide
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion/normal.dual
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion/normalish.dual
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion/wide.dual
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties
cp -a $RPM_BUILD_DIR/%{name}-%{version}/landscape/normal \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape
cp -a $RPM_BUILD_DIR/%{name}-%{version}/landscape/wide \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape
cp -a $RPM_BUILD_DIR/%{name}-%{version}/landscape/normal.dual \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape
cp -a $RPM_BUILD_DIR/%{name}-%{version}/landscape/wide.dual \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape
cp -a $RPM_BUILD_DIR/%{name}-%{version}/lion/normal \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion
cp -a $RPM_BUILD_DIR/%{name}-%{version}/lion/normalish \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion
cp -a $RPM_BUILD_DIR/%{name}-%{version}/lion/wide \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion
cp -a $RPM_BUILD_DIR/%{name}-%{version}/lion/normal.dual \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion
cp -a $RPM_BUILD_DIR/%{name}-%{version}/lion/normalish.dual \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion
cp -a $RPM_BUILD_DIR/%{name}-%{version}/lion/wide.dual \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/lion
cp -a $RPM_BUILD_DIR/%{name}-%{version}/leonidas.xml \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas
cp -a $RPM_BUILD_DIR/%{name}-%{version}/leonidas-lion.xml \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas
cp -a $RPM_BUILD_DIR/%{name}-%{version}/leonidas_left.xml \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas
cp -a $RPM_BUILD_DIR/%{name}-%{version}/leonidas_right.xml \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas
cp -a $RPM_BUILD_DIR/%{name}-%{version}/desktop-backgrounds-leonidas.xml \
        $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties
cp -a $RPM_BUILD_DIR/%{name}-%{version}/desktop-backgrounds-leonidas-lion.xml \
        $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties
cp -a $RPM_BUILD_DIR/%{name}-%{version}/desktop-backgrounds-leonidas-landscape.xml \
        $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n leonidas-backgrounds-common -f %{oreon_filedir}/leonidas-backgrounds-common.list
%files -n leonidas-backgrounds-kdm -f %{oreon_filedir}/leonidas-backgrounds-kdm.list
%files -n leonidas-backgrounds-landscape -f %{oreon_filedir}/leonidas-backgrounds-landscape.list
%files -n leonidas-backgrounds-lion -f %{oreon_filedir}/leonidas-backgrounds-lion.list
%files -n leonidas-backgrounds-lion-dual -f %{oreon_filedir}/leonidas-backgrounds-lion-dual.list

%changelog

%autochangelog
