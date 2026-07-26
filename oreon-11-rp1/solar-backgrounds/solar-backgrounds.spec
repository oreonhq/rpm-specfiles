%global source0_hash none

Name:           solar-backgrounds
Version:        0.92.0
Release:        32%{?dist}
Summary:        Solar desktop backgrounds

License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/Artwork/F10Themes/Solar
Source0:        solar-%{version}.tar.gz

BuildArch:      noarch

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
# copy image files
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
# copy slideshow xml files
cp -a $RPM_BUILD_DIR/solar-%{version}/solar.xml \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar
cp -a $RPM_BUILD_DIR/solar-%{version}/solar-hd.xml \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/solar
# copy metadata xmls file
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties
cp -a $RPM_BUILD_DIR/solar-%{version}/desktop-backgrounds-solar.xml \
        $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties
cp -a $RPM_BUILD_DIR/solar-%{version}/desktop-backgrounds-solar-hd.xml \
        $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties

%files
%doc COPYING
%dir %{_datadir}/backgrounds/solar
%dir %{_datadir}/backgrounds/solar/standard
%dir %{_datadir}/backgrounds/solar/wide
%dir %{_datadir}/gnome-background-properties
%{_datadir}/backgrounds/solar/standard/1600x1200
%{_datadir}/backgrounds/solar/wide/1680x1050
%{_datadir}/backgrounds/solar/solar.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-solar.xml

%files common
%doc COPYING
%dir %{_datadir}/backgrounds/solar/standard
%dir %{_datadir}/backgrounds/solar/wide
%dir %{_datadir}/backgrounds/solar/normalish
%dir %{_datadir}/backgrounds/solar/standard/2048x1536
%dir %{_datadir}/backgrounds/solar/wide/1920x1200
%dir %{_datadir}/backgrounds/solar/normalish/1280x1024
%{_datadir}/backgrounds/solar/standard/2048x1536/solar-0-morn.png
%{_datadir}/backgrounds/solar/wide/1920x1200/solar-0-morn.png
%{_datadir}/backgrounds/solar/normalish/1280x1024/solar-0-morn.png

%files extras
%doc COPYING
%{_datadir}/backgrounds/solar/standard.dual
%{_datadir}/backgrounds/solar/wide.dual
%{_datadir}/backgrounds/solar/normalish.dual
%{_datadir}/backgrounds/solar/standard/1024x768
%{_datadir}/backgrounds/solar/standard/2048x1536/solar-1-noon.png
%{_datadir}/backgrounds/solar/standard/2048x1536/solar-2-evening.png
%{_datadir}/backgrounds/solar/standard/2048x1536/solar-3-night.png
%{_datadir}/backgrounds/solar/wide/1920x1200/solar-1-noon.png
%{_datadir}/backgrounds/solar/wide/1920x1200/solar-2-evening.png
%{_datadir}/backgrounds/solar/wide/1920x1200/solar-3-night.png
%{_datadir}/backgrounds/solar/normalish/1280x1024/solar-1-noon.png
%{_datadir}/backgrounds/solar/normalish/1280x1024/solar-2-evening.png
%{_datadir}/backgrounds/solar/normalish/1280x1024/solar-3-night.png
%{_datadir}/backgrounds/solar/solar-hd.xml
%{_datadir}/gnome-background-properties/desktop-backgrounds-solar-hd.xml

%changelog
%autochangelog
