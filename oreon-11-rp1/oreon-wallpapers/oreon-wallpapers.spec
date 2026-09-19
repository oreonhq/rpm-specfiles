%global source0_hash 774820b5289b1ab48f5720470ab177933dd352a5cf338ecc4dec1f328475573f

Name:           oreon-wallpapers
Version:        11
Release:        1%{?dist}
Summary:        Extra Oreon wallpapers for KDE Plasma

License:        LicenseRef-Oreon
URL:            https://oreonhq.com
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch

BuildRequires:  kde-filesystem

Requires:       kde-filesystem
# avif wallpapers need qt image plugin
Requires:       (kf6-kimageformats if qt6-qtbase-gui)

%description
Extra Oreon desktop wallpapers for the KDE Plasma wallpaper picker.
These are selectable wallpapers only and do not change the default wallpaper.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%install
bash ./install-wallpapers.sh %{buildroot} %{_builddir}/%{name}-%{version}/images

%files
%license COPYING
%{_datadir}/wallpapers/Oreon_Cavern/
%{_datadir}/wallpapers/Oreon_Hypnotic/
%{_datadir}/wallpapers/Oreon_Mirror/
%{_datadir}/wallpapers/Oreon_Northern/
%{_datadir}/wallpapers/Oreon_Ocean/
%{_datadir}/wallpapers/Oreon_Ocean_Sunset/
%{_datadir}/wallpapers/Oreon_Protoplanetary/
%{_datadir}/wallpapers/Oreon_Trench/
%{_datadir}/wallpapers/Oreon_Untitled/

%changelog
%autochangelog