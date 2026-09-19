%global source0_hash 02de0e29d6edb18efb6f7400c4230d8ce006d76cd30c5f01fec58a14d5d85afe

Name: clamtk
Version: 6.18
Release: 6%{dist}
Summary: Easy to use graphical user interface for Clam anti virus
License: GPL-1.0-or-later AND Artistic-2.0
URL: https://github.com/dave-theunsub/clamtk

Source0: https://github.com/dave-theunsub/clamtk/releases/download/v%{version}/clamtk-%{version}.tar.xz
BuildArch: noarch

BuildRequires: desktop-file-utils
BuildRequires: perl-generators
Requires: perl(LWP::UserAgent), perl(LWP::Protocol::https)
Requires: perl(Text::CSV), perl(Time::Piece), perl(Locale::gettext), perl(JSON)
Requires: clamav >= 0.95, clamav-update, data(clamav)
Requires: gnome-icon-theme-legacy, cronie

%description
ClamTk is a front end for ClamAV anti virus.
It is meant to be lightweight and easy to use.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
rm -rf %{buildroot}/
install -p -D -m0755 clamtk %{buildroot}/%{_bindir}/clamtk
install -p -D -m0644 images/clamtk.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

# For appdata.xml
install -p -D -m0644 images/%{name}.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

install -p -D -m0644 clamtk.1.gz %{buildroot}/%{_mandir}/man1/%{name}.1.gz
install -p -D -m0644 clamtk.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -p -d %{buildroot}/%{perl_vendorlib}/ClamTk
install -p -m0644 lib/*.pm %{buildroot}/%{perl_vendorlib}/ClamTk/

install -p -D -m0644 com.github.davetheunsub.clamtk.appdata.xml %{buildroot}/%{_datadir}/metainfo/com.github.davetheunsub.clamtk.appdata.xml

# Install locale files
for n in po/*.mo ; do
    install -p -D -m0644 $n %{buildroot}/%{_datadir}/locale/`basename $n .mo`/LC_MESSAGES/clamtk.mo
done

    desktop-file-install --delete-original  \
	--add-category="GTK"                    \
    --add-category="GNOME"                  \
	--add-category="Utility"                \
    --dir %{buildroot}/%{_datadir}/applications %{buildroot}/%{_datadir}/applications/*

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc CHANGES DISCLAIMER.md LICENSE README.md credits.md

# The main executable
%{_bindir}/%{name}

# Main Perl libraries
%{perl_vendorlib}/ClamTk

# Images
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

# Desktop file
%{_datadir}/applications/%{name}.desktop

# Man pages
%{_mandir}/man1/%{name}.1*

# Appdata
%{_datadir}/metainfo/com.github.davetheunsub.clamtk.appdata.xml

%changelog
%autochangelog
