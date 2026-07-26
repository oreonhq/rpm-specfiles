%global source0_hash 6904f5eaa0c37de0a5afa272f8c24b6f16e974817c4c7576341e11bb612e4932

%global uuid gamerzilla@gamerzilla.identicalsoftware.com
%global min_gs_version 3.20

Name:           gnome-shell-extension-gamerzilla
Version:        0.1.4
Release:        %autorelease
Summary:        A gnome-shell extension to connect to gamerzilla
License:        GPL-2.0-or-later
URL:            https://github.com/dulsi/gamerzilla-shell-extension
Source0:        http://www.identicalsoftware.com/gamerzilla/gamerzilla-shell-extension-%{version}.tgz

BuildArch:      noarch
BuildRequires:  glib2
BuildRequires:  make
Requires:       gnome-shell-extension-common >= %{min_gs_version}
Requires:       gamerzillagobj

%description
Gamerzilla shell extension configures your gamerzilla connection
information and uploads achievements online.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gamerzilla-shell-extension-%{version}/%{uuid}

%build

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas
install -Dp -m 0644 {extension.js,metadata.json,stylesheet.css,prefs.js} \
    %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/
install -Dp -m 0644 schemas/org.gnome.shell.extensions.gamerzilla.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/

# remove precompiled gschemas
rm -rf %{builddir}/%{_datadir}/gnome-shell/extensions/%{uuid}/schemas/

%files
%license ../LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.gamerzilla.gschema.xml

%changelog
%autochangelog
