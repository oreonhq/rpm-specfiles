%global source0_hash a6a2e291801458d92510263b175d16f98024dc3816ebddbde79b5009f6c3b065
Summary:        X font list utility
Name:       xlsfonts
Version:    1.0.9
Release:        1%{?dist}
License:    MIT
URL:        http://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Obsoletes: xorg-x11-utils < 7.5-39
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
# /oreon:deps
%description
xlsfonts lists the fonts available on an X server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
