%global source0_hash 6dc9c7fc93bb488bb0520a6c780a8d3c0fb5486a4711aca49b4c53fac7393023
Summary:        Visual tool for comparing and merging files
Name:          beediff
Version:       1.9
Release:        40%{?dist}
License:       GPL-2.0-or-later
URL:           http://www.beesoft.org/index.php?id=beediff
Source0:        http://www.beesoft.org/download/beediff_%{version}_src.tar.gz
Source1:       beediff.desktop
Requires:      diffutils
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  make
BuildRequires:  qt4-devel
# /oreon:deps
%description
This package provides a visual application (beediff) for comparing and
merging files. User have a possibility to work with two text
files. Every one is in separate panel. Panels are side by side. All
differences of both textes are highlighted in colors. Operation
buttons (merge, remove) are located direct inside compared textes in
appropriate positions. Program is user friendly, very simply and
efficient.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
sed -i -e 's|^QMAKE_CXXFLAGS_RELEASE.*|QMAKE_CXXFLAGS_RELEASE = %{optflags}|' beediff.pro

%build

%{qmake_qt4}
make %{?_smp_mflags}
%install
install -D -m 0755 beediff %{buildroot}%{_bindir}/beediff
install -D -p -m 0644 img/beediff.png %{buildroot}%{_datadir}/pixmaps/beediff.png
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
