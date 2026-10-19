%global source0_hash none
Name:           solar-backgrounds
Version:        0.92.0
Release:        1%{?dist}
Summary:        Solar desktop backgrounds
License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/Artwork/F10Themes/Solar
Source0:        solar-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%description
This package contains desktop backgrounds for the Solar theme.

%package        common
Summary:        Solar desktop backgrounds shared between GNOME and KDE
%description    common
This package includes the common files for the solar-backgrounds-extras and
solar-kde-theme packages.

%package        extras
Summary:        Solar HD desktop backgrounds
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}
%description    extras
This package includes more resolutions for the Solar theme desktop backgrounds.

%prep

%setup -q -n solar-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar/standard
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar/standard.dual
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar/wide
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar/wide.dual
cp -a -r $RPM_BUILD_DIR/solar-%{version}/standard \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar
cp -a -r $RPM_BUILD_DIR/solar-%{version}/standard.dual \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar 
cp -a -r $RPM_BUILD_DIR/solar-%{version}/wide \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar
cp -a -r $RPM_BUILD_DIR/solar-%{version}/wide.dual \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar
cp -a -r $RPM_BUILD_DIR/solar-%{version}/normalish \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar
cp -a -r $RPM_BUILD_DIR/solar-%{version}/normalish.dual \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar
cp -a $RPM_BUILD_DIR/solar-%{version}/solar.xml \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar
cp -a $RPM_BUILD_DIR/solar-%{version}/solar-hd.xml \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties
cp -a $RPM_BUILD_DIR/solar-%{version}/desktop-backgrounds-solar.xml \
        $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties
cp -a $RPM_BUILD_DIR/solar-%{version}/desktop-backgrounds-solar-hd.xml \
        $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n solar-backgrounds-common -f %{oreon_filedir}/solar-backgrounds-common.list
%files -n solar-backgrounds-extras -f %{oreon_filedir}/solar-backgrounds-extras.list

%changelog

%autochangelog
