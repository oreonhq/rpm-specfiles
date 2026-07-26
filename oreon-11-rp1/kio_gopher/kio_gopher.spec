%global source0_hash ed3b8a0dcdaf9e9ec1f5c31db2526a94fa5cebfd63684f99466e39316d18c4c6

%undefine __cmake_in_source_build

Name:           kio_gopher
Version:        0.1.99
Release:        18%{?dist}
Summary:        Gopher KIO slave

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://userbase.kde.org/Kio_gopher

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: https://download.kde.org/%{stable}/kio-gopher/kio-gopher-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)

%description
This KIO slave adds support for the Gopher protocol to any KIO-enabled
application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n kio-gopher-%{version}

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install

%find_lang kio5_gopher --all-name --with-html

%files -f kio5_gopher.lang
%doc README
%license COPYING
%{_kf5_plugindir}/kio/gopher.so

%changelog
%autochangelog
