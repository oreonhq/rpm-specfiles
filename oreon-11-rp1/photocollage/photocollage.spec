%global source0_hash 7e04bf557e2b255bf90f254480f814d03f69e5507e882002d469211663090e84
Summary:        Graphical tool to make photo collage posters
Name:           photocollage
Version:        1.5.0
Release:        1%{?dist}
Url:            https://github.com/adrienverge/PhotoCollage
License:        GPL-2.0-or-later
Source0:        https://github.com/adrienverge/PhotoCollage/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-pillow >= 2.0
Requires:       python3-cairo >= 1.10
Requires:       python3-gobject >= 3.0
Requires:       gettext-runtime >= 0.18
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-photocollage = %{version}-%{release}
# /oreon:deps
%package -n       python3-photocollage+dev
Summary:        Metapackage for python3-photocollage dev extras
Requires:       python3-photocollage = %{version}-%{release}
Provides:       python3dist(photocollage[dev]) = %{version}-%{release}

%description -n python3-photocollage+dev
Metapackage for python3-photocollage dev extras.

%description
PhotoCollage allows you to create photo collage posters. It assembles
the input photographs it is given to generate a big poster. Photos are
automatically arranged to fill the whole poster, then you can change the
final layout, dimensions, border or swap photos in the generated grid.
Eventually the final poster image can be saved in any size.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir photocollage-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main

%files

%changelog

%autochangelog
