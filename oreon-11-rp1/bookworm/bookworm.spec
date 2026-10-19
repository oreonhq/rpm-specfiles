%global source0_hash 9a3b31ac7f3f32201fccd983e8bded90ba0916d551d6304988b62a1e8373fdfa
%global commit c7c3643760caea4bd26b1d56ed033a52f6e34124
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:     bookworm
Version:  1.1.3
Release:        1%{?dist}
Summary:        Simple, focused eBook reader
License:  GPL-3.0-only
URL:      https://github.com/babluboy/bookworm
Source0:        https://github.com/babluboy/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:   bookworm-patch0-python3.patch
Patch1:   bookworm-patch1-webkitgtk41.patch
Requires:      hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  granite-devel
BuildRequires:  gtk3-devel
BuildRequires:  libappstream-glib
BuildRequires:  libgee-devel
BuildRequires:  meson
BuildRequires:  poppler-glib-devel
BuildRequires:  vala
BuildRequires:  webkit2gtk4.1-devel
# /oreon:deps
%description

Read the books you love without having to worry about the different
format complexities like epub, pdf, mobi, cbr, etc. This version
supports EPUB, MOBI, FB2, PDF, FB2 and Comics (CBR and CBZ) formats
with support for more formats to follow soon.

Check the Bookworm website for details on features, shortcuts,
installation guides for supported distros :
https://babluboy.github.io/bookworm/

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
%patch -P0 -p1
%patch -P1 -p1

%build

%meson
%meson_build
%install
%meson_install
%find_lang com.github.babluboy.bookworm
desktop-file-validate %{buildroot}/%{_datadir}/applications/com.github.babluboy.bookworm.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/com.github.babluboy.bookworm.appdata.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
