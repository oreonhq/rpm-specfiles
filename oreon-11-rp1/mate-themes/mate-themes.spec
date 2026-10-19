%global source0_hash 224e89d364eb3b73f1cf756d05494a98421a93cbf54349a2c85fc607eb755ed7
%global branch 3.22
%global rel_ver 3.22.26
Name:          mate-themes
Version:       %{rel_ver}
Release:        1%{?dist}
Summary:        MATE Desktop themes
License:       GPL-2.0-or-later
URL:           http://mate-desktop.org
BuildArch:     noarch
Source0:        http://pub.mate-desktop.org/releases/themes/%{branch}/%{name}-%{version}.tar.xz
Requires:      mate-icon-theme
Requires:      gtk2-engines
Requires:      gtk-murrine-engine
# oreon:deps
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gtk2-devel
BuildRequires:  make
BuildRequires:  mate-common
# /oreon:deps
%description
MATE Desktop themes

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
make %{?_smp_mflags} V=1
%install
%{make_install}
find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
