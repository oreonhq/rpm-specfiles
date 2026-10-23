%global extdir      %{_datadir}/gnome-shell/extensions/dash-to-panel@jderose9.github.com
%global gschemadir  %{_datadir}/glib-2.0/schemas


Name:           gnome-shell-extension-dash-to-panel-oreon
Version:        73
Release:        3%{?dist}
#Release:        5.%%{commit_date}git%%{commit_short}%%{?dist}
Summary:        Gnome Shell

License:        GPLv2+
URL:            https://github.com/home-sweet-gnome/dash-to-panel
Source0:        dash-to-panel-%{version}.zip
Patch0:         0001-oreon-gschema-defaults.patch
Patch1:         0002-oreon-hide-show-apps-button.patch

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common
Requires:       dconf-editor
Requires:       dconf
#Requires:       libdbusmenu-gtk3

%description
This extension enhances the dash moving it out of the overview and
transforming it in a dock for an easier launching of applications
and a faster switching between windows and desktops without having
to leave the desktop view.


%prep
%autosetup -n dash-to-panel-%{version} -p 1


%build
%make_build


%install
%make_install

%{__rm} -fr %{buildroot}%{extdir}/{COPYING*,README*}

# Fedora handles this using triggers.
%postun
if [ $1 -eq 0 ] ; then
  %{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
fi

%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :

%files
%license COPYING
%doc README.md
%{extdir}
%{gschemadir}/*gschema.xml
%{_datadir}/locale/*/LC_MESSAGES/dash-to-panel.mo

%changelog
