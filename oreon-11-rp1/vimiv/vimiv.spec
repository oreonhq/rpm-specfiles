%global source0_hash 7196341c41ad372f4d5d98bc96fba4aa55ad6e78d93afd617a62866bdaa6c087

Name:       vimiv
Version:    0.9.1
Release:    34%{?dist}
Summary:    An image viewer with vim-like keybindings

License:    MIT
URL:        http://karlch.github.io/%{name}
Source0:    https://github.com/karlch/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-setuptools

Requires:       gtk3
Requires:       hicolor-icon-theme
Requires:       python3-gexiv2

%description
Vimiv is an image viewer with vim-like keybindings. It is written in python3
using the Gtk3 toolkit. Some of the features are:

- Thumbnail mode
- Simple library browser
- Basic image editing
- Command line with tab completion

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%py3_build

%install
%py3_install

install -p -Dm644 config/vimivrc $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/vimivrc
install -p -Dm644 config/keys.conf $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/keys.conf

install -p -Dm644 man/vimiv.1 $RPM_BUILD_ROOT/%{_mandir}/man1/vimiv.1
install -p -Dm644 man/vimivrc.5 $RPM_BUILD_ROOT/%{_mandir}/man5/vimivrc.5

install -p -Dm644 %{name}.appdata.xml $RPM_BUILD_ROOT/%{_datadir}/metainfo/%{name}.appdata.xml

appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/metainfo/%{name}.appdata.xml

desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{name}.desktop

for i in 16 32 64 128 256 512; do
    install -p -Dm644 icons/%{name}_${i}x${i}.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

install -p -Dm644 icons/%{name}.svg $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files
%{python3_sitearch}/%{name}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_mandir}/man5/%{name}*
%config(noreplace) %{_sysconfdir}/%{name}/
%license LICENSE
%doc readme.md

%changelog
%autochangelog
