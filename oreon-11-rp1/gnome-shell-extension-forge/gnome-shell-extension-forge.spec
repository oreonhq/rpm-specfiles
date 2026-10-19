%global source0_hash 72d8f1ffeb7d20ae9cb70ea12b7c4fdf851f67301a08766bee18614aaacfe295
%global extension       forge
%global uuid            %{extension}@jmmaranan.com
Name:           gnome-shell-extension-%{extension}
Version:        89
Release:        1%{?dist}
Summary:        Tiling and window manager for GNOME Shell
License:        GPL-3.0-or-later AND MIT
URL:            https://github.com/forge-ext/forge
BuildArch:      noarch
Source0:        https://github.com/%{extension}-ext/%{extension}/archive/v49-%{version}/%{extension}-49-%{version}.tar.gz
Patch:          0001-Adjust-makefile-for-Fedora.patch
Requires:       gnome-shell >= 45
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}
# oreon:deps
BuildRequires:  gettext
BuildRequires:  make
# /oreon:deps
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
%make_install
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml
mv locale %{buildroot}%{_datadir}/locale
%find_lang %{extension}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
