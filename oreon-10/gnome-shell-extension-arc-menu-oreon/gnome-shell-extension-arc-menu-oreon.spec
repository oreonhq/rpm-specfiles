%global ename  arc-menu-oreon
	
%global extdir %{_datadir}/gnome-shell/extensions/arcmenu@arcmenu.com

%global gschemadir  %{_datadir}/glib-2.0/schemas
	
Name:           gnome-shell-extension-%{ename}
	
Version:        69.0
	
Release:        4%{?dist}
	
Summary:        Integrated icon taskbar and status panel for Gnome Shell
	
License:        GPL-2.0-or-later
	
URL:            https://gitlab.com/arcmenu/ArcMenu
	
Source0:        ArcMenu-v%{version}.zip
Patch0:         0001-oreon-gschema-defaults.patch
	
# correct install paths
	
BuildArch:      noarch
	
BuildRequires:  gettext
	
BuildRequires:  make
	
BuildRequires:  glib2

BuildRequires:  glib2-devel

%description
	
Dash to Panel is an icon taskbar for Gnome Shell. This extension moves the dash
	
into the gnome main panel so that the application launchers and system tray are
	
combined into a single panel, similar to that found in KDE Plasma and Windows
	
7+. A separate dock is no longer needed for easy access to running and favorited
	
applications.
	
 
	
%prep
%autosetup -n ArcMenu-v%{version} -p 1


%build
%make_build


%install
%make_install

%{__rm} -fr %{buildroot}%{extdir}/{COPYING*,README*,RELEASENOTES*}

# Disable notifications in Arc Menu extension
find %{buildroot}%{extdir} -name "*.js" -exec sed -i 's/Main\.notify(/\/\/ Main.notify(/g' {} \;
find %{buildroot}%{extdir} -name "*.js" -exec sed -i 's/Util\.notify(/\/\/ Util.notify(/g' {} \;
find %{buildroot}%{extdir} -name "*.js" -exec sed -i 's/\.notify(/\/\/ .notify(/g' {} \;

%post
if [ -x /usr/bin/gsettings ]; then
    /usr/bin/gsettings set org.gnome.shell.extensions.arcmenu update-notifier-enabled false 2>/dev/null || true
    /usr/bin/gsettings set org.gnome.shell.extensions.arcmenu menu-button-icon 'resource:///org/gnome/shell/extensions/arcmenu/icons/scalable/actions/distro-oreon-symbolic.svg' 2>/dev/null || true
    /usr/bin/gsettings set org.gnome.shell.extensions.arcmenu menu-button-icon-size 40 2>/dev/null || true
fi

%files
%license LICENSE
%doc README.md
%{extdir}
%{gschemadir}/org.gnome.shell.extensions.arcmenu.gschema.xml
%{gschemadir}
%{_datadir}
