%global source0_hash 72d8f1ffeb7d20ae9cb70ea12b7c4fdf851f67301a08766bee18614aaacfe295

%global extension       forge
%global uuid            %{extension}@jmmaranan.com

Name:           gnome-shell-extension-%{extension}
Version:        89
Release:        %autorelease
Summary:        Tiling and window manager for GNOME Shell
# main source code: GPL-3.0-or-later
# lib/css/index.js (installed as css.js): MIT
License:        GPL-3.0-or-later AND MIT
URL:            https://github.com/forge-ext/forge
BuildArch:      noarch

Source:         %{url}/archive/v49-%{version}/%{extension}-49-%{version}.tar.gz
# downstream-only
Patch:          0001-Adjust-makefile-for-Fedora.patch

BuildRequires:  make
BuildRequires:  gettext
Requires:       gnome-shell >= 45
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}

%description
Forge is a GNOME Shell extension that provides tiling/window management.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{extension}-49-%{version}

# relocate files we don't want to ship in the extension directory
mv lib/css/LICENSE LICENSE-css
mv lib/css/README.md README-css.md

%build
%make_build

%install
# install main extension files
%make_install

# install the schema file
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml

# install locale files
mv locale %{buildroot}%{_datadir}/locale
%find_lang %{extension}

%files -f %{extension}.lang
%license LICENSE LICENSE-css
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml

%changelog
%autochangelog
