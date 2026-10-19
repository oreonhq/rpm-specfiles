%global source0_hash 27f55a026b51f6f18197e6bcfdd7c79544e41529d166daf6c93a1117e9ed45f0
%global debug_package %{nil}
Name:		pinta
Version:	3.1.2
Release:        1%{?dist}
Summary:        An easy to use drawing and image editing program
License:	LicenseRef-Callaway-MIT AND LicenseRef-Callaway-CC-BY
URL:		http://pinta-project.com/
Source0:        http://github.com/PintaProject/Pinta/releases/download/%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:	%mono_arches
ExcludeArch:	armv7hl
Requires:	hicolor-icon-theme
Requires:	mono-addins
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-sharp2-devel
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  mono-addins-devel
BuildRequires:  mono-devel
# /oreon:deps
%description
Pinta is an image drawing/editing program.
It's goal is to provide a simplified alternative to GIMP for casual users.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
%make_build
%install
%make_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml
%find_lang %name
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
