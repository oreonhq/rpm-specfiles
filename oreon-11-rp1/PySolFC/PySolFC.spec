%global source0_hash none

%global cardsets_minimal_ver 3.0.0

Name:           PySolFC
Version:        3.4.0
Release:        7%{?dist}
Summary:        A collection of solitaire card games
License:        GPL-2.0-or-later
URL:            https://pysolfc.sourceforge.io
Source0:        https://downloads.sourceforge.net/pysolfc/%{name}-%{version}.tar.xz
Source1:        pysol-start-script
Source2:        https://downloads.sourceforge.net/pysolfc/PySolFC-Cardsets--Minimal-%{cardsets_minimal_ver}.tar.xz
Patch0:         PySolFC-desktop-exec.patch
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  desktop-file-utils
BuildRequires:  perl-interpreter
BuildRequires:  tcl-devel < 1:9
BuildRequires:  tk-devel < 1:9

%if 0%{?fedora}
# optional but nice to have but not available in any epel branch
# freecell-solver already requires libsfreecell-solver
Recommends:     freecell-solver
Recommends:     python%{python3_pkgversion}-freecell_solver
%endif

Requires:       python%{python3_pkgversion}-imaging
Requires:       tile
# used to get sound working with PulseAudio
Requires:       python%{python3_pkgversion}-pygame
# really required
# Requires:       tcl >= 9
# Requires:       tk >= 9
Requires:       tix
Requires:       python%{python3_pkgversion}-tkinter
Requires:       python%{python3_pkgversion}-imaging-tk
%if 0%{?fedora} || 0%{?rhel} > 7
Recommends:     PySolFC-cardsets
Recommends:     PySolFC-music
%else
# el7 doesn't detect these dependencies
Requires:       python%{python3_pkgversion}-pysol-cards
Requires:       python3-configobj
Requires:       python36-attrs
%endif

Provides:       pysol = %{version}-%{release}

%description
%{name} is a collection of more than 1000 solitaire card games. It is a fork
of PySol solitaire. Its features include modern look and feel (uses Tile widget
set), multiple card-sets and tableau backgrounds, sound, unlimited undo, player
statistics, a hint system, demo games, a solitaire wizard, support for user
written plug-ins, an integrated HTML help browser, and lots of documentation.

%prep
%autosetup -p1 -a2

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
# install desktop file
desktop-file-install \
    --delete-original \
    --dir=$RPM_BUILD_ROOT/%{_datadir}/applications \
    $RPM_BUILD_ROOT/%{_datadir}/applications/pysol.desktop

# install the startup wrapper
mv $RPM_BUILD_ROOT%{_bindir}/pysol.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m755 %{SOURCE1} $RPM_BUILD_ROOT/%{_bindir}/pysol
cp -a PySolFC-Cardsets--Minimal-%{cardsets_minimal_ver}/cardset-* $RPM_BUILD_ROOT%{_datadir}/PySolFC
find "$RPM_BUILD_ROOT%{python3_sitelib}/pysollib" -name '*.py' | xargs -L1 perl -ln -i -E 'say if (not (($. == 1) and (m&^#![ \t]*/usr/&)))'

%find_lang pysol

%files -f pysol.lang
%license COPYING
%doc README.md
%{python3_sitelib}/pysollib
%{python3_sitelib}/*dist-info
%{_bindir}/pysol
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/applications/*.desktop

%changelog
%autochangelog
