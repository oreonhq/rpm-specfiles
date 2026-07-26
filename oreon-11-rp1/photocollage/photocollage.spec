%global source0_hash 6dd869669e7453fa7c4a3efe5d238969c36490dce4b22b0fd7e915d0e987a403

Summary:        Graphical tool to make photo collage posters
Name:           photocollage
Version:        1.5.0
Release:        %autorelease
Url:            https://github.com/adrienverge/PhotoCollage
License:        GPL-2.0-or-later

Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-setuptools
BuildRequires:  desktop-file-utils

Requires:       python3-pillow >= 2.0
Requires:       python3-cairo >= 1.10
Requires:       python3-gobject >= 3.0
Requires:       gettext-runtime >= 0.18

%description
PhotoCollage allows you to create photo collage posters. It assembles
the input photographs it is given to generate a big poster. Photos are
automatically arranged to fill the whole poster, then you can change the
final layout, dimensions, border or swap photos in the generated grid.
Eventually the final poster image can be saved in any size.

%generate_buildrequires
%pyproject_buildrequires

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n photocollage-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.rst
%license LICENSE
%{python3_sitelib}/*
%{_bindir}/photocollage
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
%autochangelog
