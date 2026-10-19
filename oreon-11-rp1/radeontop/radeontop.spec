%global source0_hash 2c1e2aace1a749d8e4530047ce245004e0f7d1d32a99037917e03d83e60f7ad1
%global with_snapshot   0
%global postrelease     .post4
%global debug_package   %{nil}
Summary:        AMD Radeon video cards monitoring utility
Name:           radeontop
Version:        1.4
Release:        1%{?dist}
License:        GPL-3.0-only
URL:            https://github.com/clbr/%{name}
Source0:        https://github.com/clbr/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-no-rebuild.patch
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  sed
# /oreon:deps
%description
RadeonTop is a monitoring utility for AMD Radeon cards from R600 and up.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}%{?shortcommit:-%{checkout}}
sed -i -e 's/unknown/%{version}/' getver.sh

%build

%set_build_flags
%make_build 
%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_lib}
%find_lang %{name}
install -Dm 0644 -p %{name}.metainfo.xml \
        %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
