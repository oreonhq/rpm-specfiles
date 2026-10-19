%global source0_hash 53ef0814f506544614ed61ab7be5221cc8d3a9f14f7ef9698c90fe7e46014b9e
%global branch 1.28
Name:        mate-user-guide
Summary:        User Guide for MATE desktop
Version:     %{branch}.0
Release:        1%{?dist}
License:     GPL-2.0-or-later
URL:         http://mate-desktop.org
BuildArch:   noarch
Source0:        http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
Requires: yelp
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  make
BuildRequires:  mate-common
# /oreon:deps
%description
Documentations for MATE desktop.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
make %{?_smp_mflags} V=1
%install
%{make_install}
desktop-file-install                               \
  --delete-original                                \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
$RPM_BUILD_ROOT%{_datadir}/applications/mate-user-guide.desktop
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
