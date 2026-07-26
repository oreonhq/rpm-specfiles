%global source0_hash 43a2771ca2e0f0071bb9a3d42120cff8660f955415e2d5e34d6636d214427085

%global srcname paperwork

Name:           %{srcname}
Version:        2.2.5
Release:        %autorelease
Summary:        Using scanner and OCR to grep dead trees the easy way

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/OpenPaperwork/paperwork
Source:         %pypi_source %{srcname}
Patch:          0001-Drop-extra-icon-dirs.patch

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel

Requires:       hicolor-icon-theme
Requires:       python3-%{srcname} = %{version}-%{release}

%global _description %{expand: \
Paperwork is a tool to make papers searchable.

The basic idea behind Paperwork is "scan & forget": You should be able to just
scan a new document and forget about it until the day you need it again.

Let the machine do most of the work.
}

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-gobject
BuildRequires:  libnotify
BuildRequires:  /usr/bin/xvfb-run

# Fallback to old orientation heuristic just freezes, so ensure this is
# available.
Requires:       tesseract-osd
Requires:       libinsane-gobject

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p2

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

PYTHONPATH=%{buildroot}%{python3_sitelib} \
    xvfb-run -a \
        python3 -m paperwork_gtk.main install \
            --data_base_dir %{buildroot}%{_datadir} \
            --icon_base_dir %{buildroot}%{_datadir}/icons

%pyproject_save_files -l paperwork_gtk

%check
export %{py3_test_envvars}

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

xvfb-run -a paperwork-gtk chkdeps
xvfb-run -a %{python3} -m unittest discover --verbose -s tests

%files
%{_bindir}/paperwork-gtk
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/*.metainfo.xml

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.markdown

%changelog
%autochangelog
