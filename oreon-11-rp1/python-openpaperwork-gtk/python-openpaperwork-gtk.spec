%global source0_hash 8375835cafe03feb6c74e88c64b760248fce1123bb778c5ceaf616df244c387b

%global srcname openpaperwork-gtk
%global srcname_ openpaperwork_gtk

Name:           python-%{srcname}
Version:        2.2.5
Release:        %autorelease
Summary:        OpenPaperwork GTK plugins

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/OpenPaperwork/paperwork/tree/master/openpaperwork-gtk
Source:         %pypi_source %{srcname_}

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  python3-devel

%description
Paperwork is a GUI to make papers searchable.

A bunch of plugins for Paperwork related to GLib and GTK.

%package -n     python3-%{srcname}
Summary:        %{summary}

Requires:       gdk-pixbuf2
Requires:       gtk3
Requires:       libhandy1
Requires:       libnotify
Requires:       pango

%description -n python3-%{srcname}
Paperwork is a GUI to make papers searchable.

A bunch of plugins for Paperwork related to GLib and GTK.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname_}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname_}

%check
%{py3_test_envvars} %{python3} -m unittest discover --verbose -s tests

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md ChangeLog

%changelog
%autochangelog
