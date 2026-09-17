%global source0_hash none

Name:           lxqt-themes
Version:        2.3.0
Release:        2%{?dist}
Summary:        LXQt standard themes

License:        LGPL-2.0-or-later
URL:            https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# Pagure do not provide tarballs yet.
# To generate this tarball, clone from pagure
# https://pagure.io/lxqt-themes-fedora/
# Remove the .git dir and manual compress it
# ---
# Bypassed until it's fixed for 2.0.0
# ---
# Source1:        lxqt-themes-fedora-1.0.tar.xz
# Upstream dropped openbox config. But we missed the change deadline, so let's keep it for one more release and drop it in the next
# Source2:        lxqt-rc.xml

BuildArch:      noarch

BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  perl

Requires:       hicolor-icon-theme
Requires:       desktop-backgrounds-compat
Requires:       breeze-cursor-themes
Requires:       breeze-icon-theme

%description
This package contains the standard themes for the LXQt desktop, namely
ambiance, dark, frost, kde-plasma, light and system.

%package fedora
Summary: Default Fedora theme for LXQt
Requires: lxqt-themes = %{version}
Requires: breeze-cursor-theme
Requires: breeze-icon-theme
%if 0%{?rhel}
Requires: redhat-logos
%endif
%if 0%{?fedora}
Requires: fedora-logos
%endif

%description fedora
%{summary}.

%prep
%autosetup
#%%setup -b 1

%build
%cmake
%cmake_build
#pushd %%{_builddir}/lxqt-themes-fedora-1.0
#tar Jxf %%{SOURCE1}
#%%cmake
#%%cmake_build
#popd

%install
%cmake_install
#pushd %%{_builddir}/lxqt-themes-fedora-1.0
#%%cmake_install
#popd
# --- System Center has broken icons, is that because of this?
#mkdir -p %{buildroot}%{_sysconfdir}/xdg/openbox/
#install -m644 %{SOURCE2} %{buildroot}%{_sysconfdir}/xdg/openbox/lxqt-rc.xml

%files
%license COPYING
%doc AUTHORS CHANGELOG README.md
%{_datadir}/lxqt/graphics
%dir %{_datadir}/lxqt/themes
%{_datadir}/lxqt/themes/{ambiance,dark,frost,kde-plasma,light,system,Clearlooks,Leech,kvantum,silver,Arch-Colors,KDE-Plasma,Valendas,graphite}
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/lxqt/palettes
%{_datadir}/lxqt/wallpapers

%files fedora
#%%{_datadir}/sddm/themes/02-lxqt-fedora/
#%%{_datadir}/lxqt/themes/fedora-lxqt
#%%{_sysconfdir}/xdg/openbox/lxqt-rc.xml

%changelog
%autochangelog
