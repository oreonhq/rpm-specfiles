%global source0_hash 4dae4b2fcb58ac259435d46a560000b0dc7d0c79ea3f7e2fb0a431cbbd009593
Summary:        KDE Wallpapers
Name:    kde-wallpapers
Version: 15.08.3
Release:        1%{?dist}
License: LGPL-3.0-only
URL:     http://www.kde.org/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/Attic/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildArch: noarch
Requires: kde-filesystem
Conflicts: kdebase-workspace < 4.6.1-2
Obsoletes: kdebase-workspace-wallpapers < 4.7.2-10
Provides:  kdebase-workspace-wallpapers = %{version}-%{release}
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q 
sed -i 's/cmake_minimum_required(VERSION [0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*)/cmake_minimum_required(VERSION 3.5)/' CMakeLists.txt 2>/dev/null || true
sed -i 's/cmake_minimum_required(VERSION [0-9][0-9]*\.[0-9][0-9]*)/cmake_minimum_required(VERSION 3.5)/' CMakeLists.txt 2>/dev/null || true

%install
mkdir -p %{buildroot}%{_datadir}/wallpapers
for d in Ariya Auros Autumn Azul Blue_Wood Castilla_Sky Elarun Flores Flying_Field Fog_on_the_West_Lake Grass Hanami Horos Media_Life Prato; do
	cp -a "$d" %{buildroot}%{_datadir}/wallpapers/
done
rm -rfv %{buildroot}%{_kde4_datadir}/wallpapers/Autumn/
rm -rfv %{buildroot}%{_kde4_datadir}/wallpapers/Elarun/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 15.08.3-25
- Import
