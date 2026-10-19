%global source0_hash 9597a878364545266b09b440101bd220a3d66ca50b12ece6078a75b73d533586
%global extension       just-perfection
%global uuid            %{extension}-desktop@%{extension}
Name:           gnome-shell-extension-%{extension}
Version:        37.0
Release:        1%{?dist}
BuildArch:      noarch
Summary:        GNOME Shell extension to change behavior and disable UI elements
License:        GPL-3.0-only
URL:            https://gitlab.gnome.org/jrahmatzadeh/just-perfection
Source0:        https://gitlab.gnome.org/jrahmatzadeh/%{extension}/-/archive/%{version}/%{extension}-%{version}.tar.gz
Requires:       gnome-shell >= 45
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}
# oreon:deps
BuildRequires:  gettext
BuildRequires:  glib2-devel
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{extension}-%{version}

# fix spurious-executable-perm and script-without-shebang rpmlint warnings/errors
find -type f -print -exec chmod 644 {} \;

%build

glib-compile-resources \
    --sourcedir src/data \
    src/data/resources.gresource.xml
%install
pushd src
install -d -m 0755 %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -r --preserve=timestamps \
    *.js stylesheet.css metadata.json \
    lib data/resources.gresource \
    %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml
popd
pushd po
for po in *.po; do
    install -d -m 0755 %{buildroot}%{_datadir}/locale/${po%.po}/LC_MESSAGES
    msgfmt -o %{buildroot}%{_datadir}/locale/${po%.po}/LC_MESSAGES/%{extension}.mo $po
done
popd
%find_lang %{extension}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
