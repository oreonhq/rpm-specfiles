%global source0_hash 1e9977c23745bf8843a37f315171d9af97814a0971aeac3d774f017650ac09ef
%global branch 1.28
Name:          engrampa
Version:       %{branch}.2
Release:        1%{?dist}
Summary:        MATE Desktop file archiver
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  PackageKit-glib-devel
BuildRequires:  caja-devel
BuildRequires:  desktop-file-utils
BuildRequires:  file-devel
BuildRequires:  gtk3-devel
BuildRequires:  json-glib-devel
BuildRequires:  libSM-devel
BuildRequires:  make
BuildRequires:  mate-common
# /oreon:deps
%description
Mate File Archiver is an application for creating and viewing archives files,
such as zip, xv, bzip2, cab, rar and other compress formats.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure                 \
   --disable-schemas-compile \
   --disable-static        \
   --enable-caja-actions   \
   --enable-magic
make %{?_smp_mflags} V=1
%install
%{make_install}
desktop-file-install                                \
    --delete-original                               \
    --dir %{buildroot}%{_datadir}/applications      \
%{buildroot}%{_datadir}/applications/engrampa.desktop
find %{buildroot} -name "*.la" -exec rm -f {} ';'
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
