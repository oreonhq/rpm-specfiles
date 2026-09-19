%global source0_hash dd1e5c26deb22de4df668d06af99cae54b9b56ba2b667e8cccfe4f2680470b4f

Name:      plasma-welcome-fedora
Version:   6.3.4
Release:   3%{?dist}
Summary:   Fedora-related customizations for Plasma-welcome
# License is specified in 01-EnableExtraRepos.qml
License:   (GPL-2.0-only OR GPL-3.0-only) AND CC-BY-SA-4.0
URL:       https://pagure.io/fedora-kde/plasma-welcome-fedora
Source0:   https://pagure.io/fedora-kde/plasma-welcome-fedora/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildArch: noarch

BuildRequires: make
BuildRequires: gettext

BuildRequires: kf6-rpm-macros

Requires:  plasma-welcome
Requires:  fedora-third-party
Requires:  fedora-workstation-repositories
Requires:  fedora-flathub-remote

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version}

%build
make build_all

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/* COPYING
%{_kf6_datadir}/plasma/plasma-welcome/intro-customization.desktop
%{_kf6_datadir}/plasma/plasma-welcome/extra-pages
%{_datadir}/icons/hicolor/scalable/apps/fedora-loves-kde.svg
%{_datadir}/icons/hicolor/scalable/apps/mascot_konqi_3rdparty.svg

%changelog
%autochangelog
