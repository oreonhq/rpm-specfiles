%global source0_hash 646f622e9e7e9e65eef9d0ab58999d4920ddb33d98e6a75232627cfe3bd508f9
Name:           papirus-icon-theme
Version:        20260801
Release:        1%{?dist}
Summary:        Free and open source SVG icon theme based on Paper Icon Set
License:        GPL-3.0-only AND CC-BY-SA-4.0 AND LGPL-3.0-or-later
URL:            https://github.com/PapirusDevelopmentTeam/papirus-icon-theme
Source0:        https://github.com/PapirusDevelopmentTeam/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Obsoletes:      papirus-icon-theme < 20240501-2
Recommends:     papirus-icon-theme-dark = %{?epoch:%{epoch}:}%{version}-%{release}
Recommends:     papirus-icon-theme-light = %{?epoch:%{epoch}:}%{version}-%{release}
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
Papirus is a free and open source SVG icon theme for Linux, based on Paper
Icon Set with a lot of new icons and a few extras, like Hardcode-Tray support,
KDE color scheme support, Folder Color support, and others.

This package contains the following variants:

 - Papirus (for Arc / Arc Darker)

%package        dark
Summary:        Papirus dark icon theme for Arc Dark
Requires:       papirus-icon-theme = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      papirus-icon-theme < 20240501-2
%description    dark
Papirus is a free and open source SVG icon theme for Linux, based on Paper
Icon Set with a lot of new icons and a few extras, like Hardcode-Tray support,
KDE color scheme support, Folder Color support, and others.

This package contains the following variants:

 - Papirus Dark (for Arc Dark)

%package        light
Summary:        Papirus light icon theme for light theme with Breeze color
Requires:       papirus-icon-theme = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      papirus-icon-theme < 20240501-2
%description    light
Papirus is a free and open source SVG icon theme for Linux, based on Paper
Icon Set with a lot of new icons and a few extras, like Hardcode-Tray support,
KDE color scheme support, Folder Color support, and others.

This package contains the following variants:

 - Papirus Light (light theme with Breeze colors)

%prep
%oreon_prep
%build

%install
%make_install
export THEMES="Papirus Papirus-Dark Papirus-Light"
for t in $THEMES; do
    /bin/touch %{buildroot}/%{_datadir}/icons/$t/icon-theme.cache
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

export THEMES="Papirus Papirus-Dark Papirus-Light"
for t in $THEMES; do
    /bin/touch --no-create %{_datadir}/icons/$t &>/dev/null || :
done
%postun

if [ $1 -eq 0 ] ; then
    export THEMES="Papirus Papirus-Dark Papirus-Light"
    for t in $THEMES; do
        /bin/touch --no-create %{_datadir}/icons/$t &>/dev/null
        /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$t &>/dev/null || :
    done
fi
%posttrans

export THEMES="Papirus Papirus-Dark Papirus-Light"
for t in $THEMES; do
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$t &>/dev/null || :
done
%files -f %{oreon_filedir}/main.list
%files -n papirus-icon-theme-dark -f %{oreon_filedir}/papirus-icon-theme-dark.list
%files -n papirus-icon-theme-light -f %{oreon_filedir}/papirus-icon-theme-light.list

%changelog

%autochangelog
