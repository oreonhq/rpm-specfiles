%global source0_hash none

Name:           leonidas-backgrounds
Version:        11.0.0
Release:        32%{?dist}
Summary:        Leonidas desktop backgrounds

License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/F11_Artwork

# This is a Fedora maintained package which is specific to our distribution. 
# The source is only available from within this srpm.
# Images in the source archive are basically crops/resizes of 
# https://fedoraproject.org/w/uploads/e/e9/Artwork_F11_Betamockup1_n.jpg
# and
# https://fedoraproject.org/wiki/File:King_4096x1536.xcf.bz2
Source0:        %{name}-%{version}.tar.lzma

BuildArch:      noarch
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-lion-dual = %{version}-%{release}

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
# prepare the dir structure
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

# copy the landscape images
cp -a $RPM_BUILD_DIR/%{name}-%{version}/landscape/normal \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape
cp -a $RPM_BUILD_DIR/%{name}-%{version}/landscape/wide \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape
cp -a $RPM_BUILD_DIR/%{name}-%{version}/landscape/normal.dual \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape
cp -a $RPM_BUILD_DIR/%{name}-%{version}/landscape/wide.dual \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas/landscape

# copy the lion images
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

# copy slideshow xml files
cp -a $RPM_BUILD_DIR/%{name}-%{version}/leonidas.xml \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas
cp -a $RPM_BUILD_DIR/%{name}-%{version}/leonidas-lion.xml \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas
cp -a $RPM_BUILD_DIR/%{name}-%{version}/leonidas_left.xml \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas
cp -a $RPM_BUILD_DIR/%{name}-%{version}/leonidas_right.xml \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/leonidas

# copy metadata xmls file
cp -a $RPM_BUILD_DIR/%{name}-%{version}/desktop-backgrounds-leonidas.xml \
        $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties
cp -a $RPM_BUILD_DIR/%{name}-%{version}/desktop-backgrounds-leonidas-lion.xml \
        $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties
cp -a $RPM_BUILD_DIR/%{name}-%{version}/desktop-backgrounds-leonidas-landscape.xml \
        $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties

%files
%doc COPYING
%{_datadir}/gnome-background-properties/desktop-backgrounds-leonidas.xml
%{_datadir}/backgrounds/leonidas/leonidas.xml

%files common
%doc COPYING
%dir %{_datadir}/backgrounds/leonidas
%dir %{_datadir}/backgrounds/leonidas/lion
%dir %{_datadir}/backgrounds/leonidas/lion/normal
%dir %{_datadir}/backgrounds/leonidas/lion/normal/2048x1536
%dir %{_datadir}/backgrounds/leonidas/lion/normalish
%dir %{_datadir}/backgrounds/leonidas/lion/normalish/1280x1024
%dir %{_datadir}/backgrounds/leonidas/lion/wide
%dir %{_datadir}/backgrounds/leonidas/lion/wide/1920x1200
%{_datadir}/backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.jpg
%{_datadir}/backgrounds/leonidas/lion/normalish/1280x1024/leonidas-1-noon.jpg
%{_datadir}/backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon.jpg

%files lion-dual
%doc COPYING
%dir %{_datadir}/backgrounds/leonidas
%dir %{_datadir}/backgrounds/leonidas/lion
%{_datadir}/backgrounds/leonidas/lion/normal.dual
%{_datadir}/backgrounds/leonidas/lion/normalish.dual
%{_datadir}/backgrounds/leonidas/lion/wide.dual

%files lion
%doc COPYING
%dir %{_datadir}/backgrounds/leonidas/lion/normal
%dir %{_datadir}/backgrounds/leonidas/lion/normal/2048x1536
%dir %{_datadir}/backgrounds/leonidas/lion/normalish
%dir %{_datadir}/backgrounds/leonidas/lion/normalish/1280x1024
%dir %{_datadir}/backgrounds/leonidas/lion/wide
%dir %{_datadir}/backgrounds/leonidas/lion/wide/1920x1200
%{_datadir}/gnome-background-properties/desktop-backgrounds-leonidas-lion.xml
%{_datadir}/backgrounds/leonidas/leonidas-lion.xml
%{_datadir}/backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon_right.jpg
%{_datadir}/backgrounds/leonidas/lion/normalish/1280x1024/leonidas-1-noon_right.jpg
%{_datadir}/backgrounds/leonidas/lion/wide/1920x1200/leonidas-1-noon_right.jpg

%files kdm
%doc COPYING
%dir %{_datadir}/backgrounds/leonidas
%dir %{_datadir}/backgrounds/leonidas/lion/normal
%dir %{_datadir}/backgrounds/leonidas/lion/normal/2048x1536
%{_datadir}/backgrounds/leonidas/lion/normal/2048x1536/leonidas-1-noon.png

%files landscape
%doc COPYING
%dir %{_datadir}/backgrounds/leonidas
%{_datadir}/backgrounds/leonidas/landscape
%{_datadir}/gnome-background-properties/desktop-backgrounds-leonidas-landscape.xml
%{_datadir}/backgrounds/leonidas/leonidas_left.xml
%{_datadir}/backgrounds/leonidas/leonidas_right.xml

%changelog
%autochangelog
