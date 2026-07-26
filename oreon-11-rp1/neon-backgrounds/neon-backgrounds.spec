%global source0_hash 8a57e0c94b46fe83050c0cd5321c127e9a05361496efc0305df5eb59e4e8a156

Name:           neon-backgrounds
Version:        0.0.1
Release:        34%{?dist}
Summary:        Neon desktop backgrounds

License:        CC-BY-SA-4.0
URL:            https://fedoraproject.org/wiki/Artwork/F10Themes/Neon
Source0:        neon-%{version}.tar.gz

BuildArch:      noarch

%description
This package contains desktop backgrounds for the Neon theme.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n neon-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
# copy image files
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/neon
cp -a $RPM_BUILD_DIR/neon-%{version}/*.png \
        $RPM_BUILD_ROOT/%{_datadir}/backgrounds/neon
# copy metadata xml file
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties
cp -a $RPM_BUILD_DIR/neon-%{version}/desktop-backgrounds-neon.xml \
        $RPM_BUILD_ROOT/%{_datadir}/gnome-background-properties

%files
%doc COPYING
%dir %{_datadir}/backgrounds/neon
%{_datadir}/backgrounds/neon/*.png
%dir %{_datadir}/gnome-background-properties
%{_datadir}/gnome-background-properties/desktop-backgrounds-neon.xml

%changelog
%autochangelog
