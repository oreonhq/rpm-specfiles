%global source0_hash babd40fabb53b629384db0a05055c517ddfeb5c37d63b6b6abfeae9f234bec50
%define kdeversion 4.4.0
Name:           kgrab
Version:        0.1.1
Release:        56%{?dist}
Summary:        A screen grabbing utility
License:        GPL-2.0-or-later
URL:            http://extragear.kde.org
Source0:        ftp://ftp.kde.org/pub/kde/stable/%{kdeversion}/src/extragear/%{name}-%{version}-kde%{kdeversion}.tar.bz2
%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api} }
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  kde-filesystem
BuildRequires:  kdelibs4-devel
BuildRequires:  make
# /oreon:deps
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
desktop-file-install --vendor ""                          \
        --dir %{buildroot}%{_datadir}/applications/kde4   \
        %{buildroot}%{_datadir}/applications/kde4/%{name}.desktop
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
