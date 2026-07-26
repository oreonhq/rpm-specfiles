%global source0_hash babd40fabb53b629384db0a05055c517ddfeb5c37d63b6b6abfeae9f234bec50

# Review Request:
# https://bugzilla.redhat.com/show_bug.cgi?id=432613

%define kdeversion 4.4.0

Name:           kgrab
Version:        0.1.1
Release:        56%{?dist}
Summary:        A screen grabbing utility

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://extragear.kde.org
Source0:        ftp://ftp.kde.org/pub/kde/stable/%{kdeversion}/src/extragear/%{name}-%{version}-kde%{kdeversion}.tar.bz2

BuildRequires:  kdelibs4-devel >= 4
BuildRequires:  kde-filesystem >= 4
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires: make

%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api} }

%description
kgrab is a screen grabbing utility for KDE.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{version}-kde%{kdeversion}

%build

mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}

# validate desktop file
desktop-file-install --vendor ""                          \
        --dir %{buildroot}%{_datadir}/applications/kde4   \
        %{buildroot}%{_datadir}/applications/kde4/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%license COPYING COPYING.DOC COPYING.LIB
%{_kde4_bindir}/kgrab
%{_datadir}/applications/kde4/kgrab.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kgrab.xml
%{_kde4_iconsdir}/hicolor/*/apps/kgrab.*
%{_kde4_appsdir}/kgrab/

%changelog
%autochangelog
