%global source0_hash 43a2771ca2e0f0071bb9a3d42120cff8660f955415e2d5e34d6636d214427085
%global srcname paperwork
Name:           %{srcname}
Version:        2.2.5
Release:        1%{?dist}
Summary:        Using scanner and OCR to grep dead trees the easy way
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/OpenPaperwork/paperwork
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
Patch:          0001-Drop-extra-icon-dirs.patch
BuildArch:      noarch
ExcludeArch: %{ix86}
Requires:       hicolor-icon-theme
Requires:       python3-%{srcname} = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 45
BuildRequires:  python3dist(setuptools-scm[toml]) >= 8
Requires:       python3-paperwork = %{version}-%{release}
# /oreon:deps
%package -n       python3-paperwork+dev
Summary:        Metapackage for python3-paperwork dev extras
Requires:       python3-paperwork = %{version}-%{release}
Provides:       python3dist(paperwork[dev]) = %{version}-%{release}

%description -n python3-paperwork+dev
Metapackage for python3-paperwork dev extras.

%package -n       python3-paperwork+lint
Summary:        Metapackage for python3-paperwork lint extras
Requires:       python3-paperwork = %{version}-%{release}
Provides:       python3dist(paperwork[lint]) = %{version}-%{release}

%description -n python3-paperwork+lint
Metapackage for python3-paperwork lint extras.

%description

%package -n     python3-%{srcname}
Summary:        Using scanner and OCR to grep dead trees the easy way
BuildRequires:  python3-gobject
BuildRequires:  libnotify
BuildRequires:  /usr/bin/xvfb-run
Requires:       tesseract-osd
Requires:       libinsane-gobject
%description -n python3-%{srcname}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p2

%build

%pyproject_wheel
%install
%pyproject_install
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    xvfb-run -a \
        python3 -m paperwork_gtk.main install \
            --data_base_dir %{buildroot}%{_datadir} \
            --icon_base_dir %{buildroot}%{_datadir}/icons
%oreon_autofiles main usr/lib/python3*/site-packages/paperwork* usr/lib64/python3*/site-packages/paperwork* usr/bin/*

%check

export %{py3_test_envvars}
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
xvfb-run -a paperwork-gtk chkdeps
xvfb-run -a %{python3} -m unittest discover --verbose -s tests
%files
%files -n python3-paperwork -f %{oreon_filedir}/python3-paperwork.list

%changelog

%autochangelog
