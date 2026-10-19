%global source0_hash e558d2172aaa3bd51d5b82651f8697903de2a945fa0e555103b1f9d06e609541
Summary:        Knights flying on ostriches compete against other riders
Name: ostrichriders
Version: 0.6.5
Release:        18%{?dist}
License: GPL-3.0-or-later
Url: http://www.identicalsoftware.com/ostrichriders
Source0:        http://www.identicalsoftware.com/ostrichriders/%{name}-%{version}.tgz
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  SFML2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fontconfig-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
Enemy knights are invading the kingdom. As one of the elite ostrich riders,
it is your duty to defend the kingdom. With lance in hand you fly off.
Remember to stay above your opponent least you fall to his lance. Collect the
eggs least your opponent hatches stronger than before. Work together with
other knights.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

export PKG_CONFIG_PATH=%{_libdir}/SFML2/pkgconfig
export CXXFLAGS="%{optflags} -I%{_includedir}/SFML2"
export LDFLAGS="%{?build_ldflags} -L%{_libdir}/SFML2"
%make_build
%install
%make_install PREFIX=%{_prefix}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
