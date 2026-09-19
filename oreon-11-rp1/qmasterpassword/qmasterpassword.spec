%global source0_hash 4488f5a0a4c9555525e2614ceeb0c99220eb8e693f71837e98d3c5623e647cc1

Name:           qmasterpassword
Version:        2.0.3
Release:        4%{?dist}
Summary:        Stateless graphical Master Password Manager

%global project_name qMasterPassword
%global git_tag v%{version}

License:        GPL-3.0-only
URL:            https://github.com/bkueng/qMasterPassword
Source0:        https://github.com/bkueng/%{project_name}/archive/%{git_tag}/%{project_name}-%{git_tag}.tar.gz
Patch0:         qmasterpassword-2.0.3-identicon-fix-build-with-cplusplus20.patch

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel >= 6.5.0
BuildRequires:  qt6-qttools-devel >= 6.5.0
BuildRequires:  openssl-devel
BuildRequires:  libscrypt-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
qMasterPassword is a password manager based on Qt. Access all your passwords
using only a single master password. But in contrast to other managers it does
not store any passwords: Unique passwords are generated from the master password
and a site name. This means you automatically get different passwords for each
account and there is no password file that can be lost or get stolen. There is
also no need to trust any online password service.

https://spectre.app also contains other compatible software for various
platforms, like Android or iOS.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{project_name}-%{version} -p1

%build
%{cmake} \
        -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DDISABLE_FILL_FORM_SHORTCUTS=1
%{cmake_build}

%install
%{cmake_install}
%find_lang translation --with-qt

desktop-file-install --dir %{buildroot}%{_datadir}/applications \
        data/%{project_name}.desktop

install -m 0644 -p -D data/icons/app_icon.png \
        %{buildroot}%{_datadir}/pixmaps/%{name}.png

install -m 0644 -p -D data/%{project_name}.appdata.xml \
        %{buildroot}%{_metainfodir}/%{project_name}.appdata.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{project_name}.appdata.xml
%{cmake} \
        -GNinja \
        -DCMAKE_BUILD_TYPE=Debug
%{cmake_build} --target test

%files -f translation.lang
%license LICENSE
%doc README.md HISTORY
%{_bindir}/%{project_name}
%{_datadir}/applications/%{project_name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_metainfodir}/%{project_name}.appdata.xml

%changelog
%autochangelog
