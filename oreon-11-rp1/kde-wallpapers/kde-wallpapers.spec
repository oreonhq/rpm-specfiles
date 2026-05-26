# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 4dae4b2fcb58ac259435d46a560000b0dc7d0c79ea3f7e2fb0a431cbbd009593
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Summary: KDE Wallpapers
Name:    kde-wallpapers
Version: 15.08.3
Release: 25%{?dist}

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License: LGPL-3.0-only
URL:     http://www.kde.org/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

BuildArch: noarch

BuildRequires: kdelibs4-devel >= 4.14
BuildRequires: make
Requires: kde-filesystem

# Horos wallpaper moved back here in 4.6.1-2 (originally moved to main in 4.6.0-8)
Conflicts: kdebase-workspace < 4.6.1-2

# pkg renamed
Obsoletes: kdebase-workspace-wallpapers < 4.7.2-10
Provides:  kdebase-workspace-wallpapers = %{version}-%{release}

%description
%{summary}.


%prep
%oreon_verify_sources
%setup -q 


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform} 


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

## unpackaged files
# omit conflicts with plasma-workspace-wallpapers-5.5.x
rm -rfv %{buildroot}%{_kde4_datadir}/wallpapers/Autumn/
# omit conflicts with plasma-workspace-wallpapers-5.16.x
rm -rfv %{buildroot}%{_kde4_datadir}/wallpapers/Elarun/


%files 
%license LICENSE
%{_kde4_datadir}/wallpapers/Auros/
%{_kde4_datadir}/wallpapers/Ariya/
%{_kde4_datadir}/wallpapers/Azul/
%{_kde4_datadir}/wallpapers/Blue_Wood
%{_kde4_datadir}/wallpapers/Castilla_Sky/
#{_kde4_datadir}/wallpapers/Elarun/
%{_kde4_datadir}/wallpapers/Flores/
%{_kde4_datadir}/wallpapers/Flying_Field/
%{_kde4_datadir}/wallpapers/Fog_on_the_West_Lake/
%{_kde4_datadir}/wallpapers/Grass/
%{_kde4_datadir}/wallpapers/Hanami/
%{_kde4_datadir}/wallpapers/Horos/
%{_kde4_datadir}/wallpapers/Media_Life/
%{_kde4_datadir}/wallpapers/Prato/


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 15.08.3-25
- Import
