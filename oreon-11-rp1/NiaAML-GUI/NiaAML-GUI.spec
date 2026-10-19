%global source0_hash ff96c5ef827c0df1630529ee68630ce6a80e64ee8b26c82fa745d55d42673cf5
Name:           NiaAML-GUI
Version:        0.4.3
Release:        1%{?dist}
Summary:        GUI for NiaAML Python package
License:        MIT
URL:            https://github.com/firefly-cpp/NiaAML-GUI
Source0:        https://github.com/firefly-cpp/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExcludeArch:    %{ix86}
Requires:       hicolor-icon-theme
%global app_id io.github.firefly-cpp.niaaml_gui
%global common_description %{expand:
This is a basic graphical user interface intended for users of the NiaAML
Python package.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-NiaAML-GUI = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%prep

%autosetup -p1
# Do not upper-bound the version of Python!
# https://github.com/firefly-cpp/NiaAML-GUI/commit/d0084e6d2f05c6af848678db731c41a49c1a2a22#commitcomment-146060179
sed -r -i 's/^(python[[:blank:]]*=[[:blank:]]*"[^"]+),[^"]+"/\1"/' \
    pyproject.toml

%install
%pyproject_install
desktop-file-install --dir='%{buildroot}%{_datadir}/applications' \
    AppData/%{app_id}.desktop
install -t '%{buildroot}%{_metainfodir}' -p -m 0644 -D \
    AppData/%{app_id}.metainfo.xml
install -t '%{buildroot}%{_datadir}/icons/hicolor/256x256/apps' -p -m 0644 -D \
    AppData/niaaml-gui.png
%oreon_autofiles main

%build

%pyproject_wheel
%check

appstream-util validate-relax --nonet \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'
%pytest
%files

%changelog

%autochangelog
