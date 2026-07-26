%global source0_hash none

Name:           paper-icon-theme
Summary:        Modern freedesktop icon theme
License:        CC-BY-SA-4.0

%global git_commit aa3e8af7a1f0831a51fd7e638a4acb077a1e5188
%global git_date 20200312
%global git_short %(c="%{git_commit}"; echo "${c:0:7}")

Version:        1.5.0
Release:        20.%{git_date}git%{git_short}%{?dist}

URL:            https://snwh.org/paper
Source0:        https://github.com/snwh/%{name}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz

BuildArch:      noarch

BuildRequires:  meson

Requires:       adwaita-icon-theme
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme

%description
Paper is a modern freedesktop icon theme whose design is based around
the use of bold colors and simple geometric shapes to compose icons.
Each icon has been meticulously designed for pixel-perfect viewing.

While it does take some inspiration from the icons in Google's
Material Design, some aspects have been adjusted to better suit a
desktop environment.

%prep
%autosetup -n %{name}-%{git_commit}

# remove stray executable bit from files
find -executable -type f -exec chmod -x {} +

%build
%meson
%meson_build

%install
%meson_install

touch %{buildroot}/%{_datadir}/icons/Paper/icon-theme.cache
touch %{buildroot}/%{_datadir}/icons/Paper-Mono-Dark/icon-theme.cache

%transfiletriggerin -- %{_datadir}/icons/Paper %{_datadir}/icons/Paper-Mono-Dark
gtk-update-icon-cache --force %{_datadir}/icons/Paper &>/dev/null || :
gtk-update-icon-cache --force %{_datadir}/icons/Paper-Mono-Dark &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/Paper %{_datadir}/icons/Paper-Mono-Dark
gtk-update-icon-cache --force %{_datadir}/icons/Paper &>/dev/null || :
gtk-update-icon-cache --force %{_datadir}/icons/Paper-Mono-Dark &>/dev/null || :

%files
%license COPYING LICENSE
%doc AUTHORS README.md

%{_datadir}/icons/Paper/index.theme
%{_datadir}/icons/Paper/cursor.theme
%{_datadir}/icons/Paper/*/

%{_datadir}/icons/Paper-Mono-Dark/index.theme
%{_datadir}/icons/Paper-Mono-Dark/*/

%ghost %{_datadir}/icons/Paper/icon-theme.cache
%ghost %{_datadir}/icons/Paper-Mono-Dark/icon-theme.cache

%changelog
%autochangelog
