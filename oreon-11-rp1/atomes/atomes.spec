%global source0_hash 21cd2916e9cae7b22b154dcd5e355ce5cb159bc3f8a3b59d88bc5ed0dfc7fe16
Name:           atomes
%global upname atomes-GNU
Version:        1.3.1
Release:        1%{?dist}
Summary:        An atomistic toolbox
License:        AGPL-3.0-or-later
Source0:        https://github.com/Slookeur/%{upname}/archive/refs/tags/v%{version}.tar.gz
URL:            https://%{name}.ipcms.fr/
Requires: gtk3
Requires: mesa-libGLU
Provides: %{name} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  gnupg2
BuildRequires:  libappstream-glib
BuildRequires:  libgfortran
BuildRequires:  make
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pangoft2)
# /oreon:deps
%description
atomes: a toolbox to analyze, to visualize 
and to create/edit three-dimensional atomistic models.
It offers a workspace that allows to have many projects opened simultaneously.
The different projects in the workspace can exchange data: 
analysis results, atomic coordinates...
atomes also provides an advanced input preparation system 
for further calculations using well known molecular dynamics codes:

    Classical MD: DLPOLY and LAMMPS
    ab-initio MD: CPMD and CP2K
    QM-MM MD: CPMD and CP2K

To prepare the input files for these calculations is likely to be the key, 
and most complicated step towards MD simulations.
atomes offers a user-friendly assistant to help and guide the scientist
step by step to achieve this crucial step.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# %%{gpgverify} --keyring='%%{SOURCE2}' --signature='%%{SOURCE1}' --data='%%{SOURCE0}'
%autosetup -n %{upname}-%{version}

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/fr.ipcms.%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
