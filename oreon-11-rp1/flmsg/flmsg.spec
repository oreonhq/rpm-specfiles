%global source0_hash dde474c2bce436396a9b9c56e5db608a1b37ddc554999792d3fadffb19cf7916
%global alpha 0
Name:           flmsg
Version:        4.0.24
Release:        1%{?dist}
Summary:        Fast Light Message Amateur Radio Forms Manager
License:        GPL-3.0-or-later AND GPL-2.0-only
URL:            http://www.w1hkj.com/
Source0:        http://www.w1hkj.com/files/%{name}/%{name}-%{version}.tar.gz
Source100:      flmsg.appdata.xml
Provides:       bundled(mongoose)
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
flmsg is a editor / file management tool for ics213 forms which form the
basis for emergency communications data transfers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
