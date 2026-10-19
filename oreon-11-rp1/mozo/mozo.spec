%global source0_hash fe98984ffd6aa8c36d0594bcefdba03de39b42d41e007251680384f3cef44924
%global branch 1.28
Name:          mozo
Version:       %{branch}.0
Release:        1%{?dist}
Summary:        MATE Desktop menu editor
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
Requires:      mate-menus
BuildArch:     noarch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  mate-menus-devel
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-devel
# /oreon:deps
%description
MATE Desktop menu editor

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
make %{?_smp_mflags} V=1
%install
%{make_install}
desktop-file-install                                  \
        --dir=%{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/applications/mozo.desktop
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
