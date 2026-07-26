%global source0_hash 7b6f2090e944afd8adc59455923062d9e97c86c4592d7449988ea80bd3badd6f

Name:           gears-backgrounds
Version:        0.0.1
Release:        34%{?dist}
Summary:        Gears desktop backgrounds

# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA
URL:            https://fedoraproject.org/wiki/Artwork/F10Themes/Gears
Source0:        gears-%{version}.tar.gz

BuildArch:      noarch

%description
This package contains desktop backgrounds for the Gears theme.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gears-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
# copy image files
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/gears
cp -a $RPM_BUILD_DIR/gears-%{version}/*.png \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/gears
# copy metadata xml file
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties
cp -a $RPM_BUILD_DIR/gears-%{version}/desktop-backgrounds-gears.xml \
        $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties

%files
%doc COPYING
%dir %{_datadir}/backgrounds/gears
%{_datadir}/backgrounds/gears/*.png
%dir %{_datadir}/gnome-background-properties
%{_datadir}/gnome-background-properties/desktop-backgrounds-gears.xml

%changelog
%autochangelog
