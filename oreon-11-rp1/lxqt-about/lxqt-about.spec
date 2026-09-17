%global source0_hash f2adecb400e3bff0095c0677bfa517a79e094107d802f0a560d4719ac786734a

Name:          lxqt-about
Summary:       About application for LXQt desktop suite
Version:       2.3.0
Release:       2%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           https://lxqt-project.org/
Source0:       https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(lxqt)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: desktop-file-utils
BuildRequires: perl

%description
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-about
Requires:       lxqt-about
%description l10n
This package provides translations for the lxqt-about package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
desktop-file-edit \
    --remove-category=LXQt --add-category=X-LXQt \
    --remove-category=Help --add-category=X-Help \
    --remove-only-show-in=LXQt --add-only-show-in=X-LXQt \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name} --with-qt

%files
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/lxqt-about.svg

%files l10n -f %{name}.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lxqt/translations/%{name}

%changelog
%autochangelog
