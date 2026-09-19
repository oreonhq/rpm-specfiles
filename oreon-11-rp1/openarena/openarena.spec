%global source0_hash none

Name:           openarena
Version:        0.8.8
Release:        36%{?dist}
Summary:        Open source first person shooter
License:        GPL-2.0-only AND CC0-1.0
URL:            http://openarena.ws/
Source0:        http://download.tuxfamily.org/openarena/rel/081/oa081.zip
Source10:       http://download.tuxfamily.org/openarena/rel/085/oa085p.zip
Source11:       http://download.tuxfamily.org/openarena/rel/088/oa088p.zip
Source2:        %{name}.sh
# From https://github.com/flathub/ws.openarena.OpenArena/blob/master/ws.openarena.OpenArena.png
Source3:        ws.openarena.OpenArena.png
Source4:        %{name}.desktop
Source5:        %{name}.appdata.xml

# We need 1.36-11 or newer for the new standalone game and protocol cvars
Requires:       quake3 >= 1.36-11
Requires:       hicolor-icon-theme
Requires:       opengl-games-utils
Requires:       rsync
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Provides:       openarena-data = %{version}-%{release}
Obsoletes:      openarena-data < 0.7.1-4
BuildArch:      noarch

%description
OpenArena is an open-source content package for Quake III Arena licensed under
the GPL, effectively creating a free stand-alone game.

%prep
%setup -q -c
unzip -qq -o %{SOURCE10}
unzip -qq -o %{SOURCE11}
mkdir doc
for file in CHANGES COPYING CREDITS README readme_088.txt; do
    cat %{name}-0.8.1/$file | sed s/\\r// > doc/$file
    touch -r %{name}-0.8.1/$file doc/$file
done

%build
echo We build nothing

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT%{_bindir}

cp -pr %{name}-0.8.1/baseoa $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/%{name}
sed -i -e 's|/usr|%{_prefix}|' $RPM_BUILD_ROOT%{_bindir}/%{name}
ln -s %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}_ded
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/openarena.png
chmod 644 $RPM_BUILD_ROOT%{_datadir}/%{name}/baseoa/*
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE4}
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*

mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
install -pm 644 %{SOURCE5} $RPM_BUILD_ROOT%{_metainfodir}/
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.appdata.xml

%files
%doc doc/CREDITS doc/README doc/CHANGES doc/*.txt
%license doc/COPYING
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%changelog
%autochangelog
