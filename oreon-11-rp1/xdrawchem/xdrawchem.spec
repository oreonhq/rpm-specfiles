%global source0_hash 009b525e570cd79b3e59880877871e258071fecdef6c397d7533f3920faa9a7e

%global tag 1.10.2-1

Name:		xdrawchem
Version:	1.10.2
Release:	16%{?dist}
Summary:	2D chemical structures drawing tool
URL:            https://www.woodsidelabs.com/chemistry/%{name}.php
Source0:        https://github.com/bryanherger/%{name}/archive/%{tag}/%{name}-%{tag}.tar.gz
Source1:	%{name}.desktop
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:  pkgconfig(openbabel-3)
BuildRequires:	qt5-qtbase-devel

Requires:       hicolor-icon-theme

# remove -O0 -g3 from CXXFLAGS
Patch0:         %{name}-cxxflags.patch
Patch1:         %{name}-warn.patch
Patch2:         %{name}-porting_to_openbabel3.patch

%description
%{name} is a two-dimensional molecule drawing program for Unix
operating systems.  It is similar in functionality to other molecule
drawing programs such as ChemDraw (TM, CambridgeSoft).  It can read
and write MDL Molfiles and CML files to allow sharing between
%{name} and other chemistry applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tag}/%{name}-qt5

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

# menu
mkdir -p %{buildroot}%{_datadir}/applications
install -Dpm 644 ring/%{name}-icon.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	%{SOURCE1}
pushd %{buildroot}%{_datadir}/%{name}
rm -f caslist.txt \
      CMakeLists.txt \
      COPYRIGHT.txt \
      GPL.txt \
      HISTORY.txt
popd

rm -rf %{buildroot}%{_datadir}/%{name}/doc

%find_lang %{name} --without-mo --with-qt

%files -f %{name}.lang
%license GPL.txt COPYRIGHT.txt
%doc doc/*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
%autochangelog
