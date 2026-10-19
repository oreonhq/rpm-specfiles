%global source0_hash 7cebd83fd34883d51e143389aa88f8173ea7b67c760b12b7de847f3c3c8cee34
Name:       gsmartcontrol
Version:    2.0.2
Release:        1%{?dist}
Summary:        Graphical user interface for smartctl
License:    (GPL-2.0-only OR GPL-3.0-only) AND LicenseRef-Callaway-BSD AND Zlib AND BSL-1.0 AND LicenseRef-Callaway-MIT
URL:        http://gsmartcontrol.sourceforge.net
Source0:        https://github.com/ashaduri/gsmartcontrol/archive/refs/tags/v%{version}.tar.gz
Requires:       smartmontools >= 5.43
Requires:       hicolor-icon-theme
Requires:       xterm
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gtkmm30-devel
BuildRequires:  make
BuildRequires:  pcre-devel
# /oreon:deps
%description
GSmartControl is a graphical user interface for smartctl (from
smartmontools package), which is a tool for querying and controlling
SMART (Self-Monitoring, Analysis, and Reporting Technology) data on
modern hard disk drives. It allows you to inspect the drive's SMART
data to determine its health, as well as run various tests on it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
