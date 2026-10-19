%global source0_hash 804b125d1e2864b1e74af816da9b2ab8b19472b9af974437ee7355ada5e628f5
Name:          mate-calc
Version:       1.28.0
Release:        1%{?dist}
Summary:        MATE Desktop calculator
License:       GPL-2.0-or-later
URL:           http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.28/%{name}-%{version}.tar.xz
Patch1:        mate-calc_0001-a11y-Allow-the-screen-reader-to-announce-status-chan.patch
Patch2:        mate-calc_0002-Fix-invalid-memory-access-with-invalid-powers.patch
# oreon:deps
BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gtk3-devel
BuildRequires:  libmpc-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  mpfr-devel
# /oreon:deps
%description
mate-calc is a powerful graphical calculator with financial, logical and scientific modes.
It uses a multiple precision package to do its arithmetic to give a high degree of accuracy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
    --disable-schemas-compile
make %{?_smp_mflags} V=1
%install
%{make_install}
desktop-file-install                               \
        --delete-original                          \
        --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/*.desktop
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
