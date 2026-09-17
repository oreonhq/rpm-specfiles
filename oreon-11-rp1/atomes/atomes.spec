%global source0_hash 351ff5dc040ae0dd79d7669e18c11ccb693f0ad7624f761f02f2bfb382a32e0a

Name:           atomes
%global upname atomes-GNU
Version:        1.2.1
Release:        4%{?dist}
Summary:        An atomistic toolbox
License:        AGPL-3.0-or-later
Source0:        https://github.com/Slookeur/%{upname}/archive/refs/tags/v%{version}.tar.gz
# Source1:        ./v%%{version}.tar.gz.asc
# Source2:        %%{name}.gpg
URL:            https://%{name}.ipcms.fr/

BuildRequires: gnupg2
BuildRequires: make
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: pkgconf-pkg-config
BuildRequires: gcc
BuildRequires: gcc-gfortran
BuildRequires: libgfortran
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

# pkg-config 
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(pangoft2)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libswscale)

# Runtime requirements
Requires: gtk3
Requires: mesa-libGLU

Provides: %{name} = %{version}-%{release}

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
#make %%{?_smp_mflags}
%make_build

%install
%make_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/fr.ipcms.%{name}.appdata.xml

%files
%license COPYING
%{_bindir}/%{name}
%{_libexecdir}/%{name}_startup_testing
%{_datadir}/doc/%{name}/
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}/
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}-mime.xml
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/pixmaps/%{name}-workspace.svg
%{_datadir}/pixmaps/%{name}-project.svg
%{_datadir}/pixmaps/%{name}-coordinates.svg
%{_metainfodir}/fr.ipcms.%{name}.appdata.xml

%changelog
%autochangelog
