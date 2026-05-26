Name: mythes-ro
Summary: Romanian thesaurus
Version: 3.3
Release: 32%{?dist}
Source: http://downloads.sourceforge.net/rospell/th_ro_RO.%{version}.zip
# oreon url source checksums begin
%global source0_sha256 097f0a58be60859292fb0c8109669d579abd19a500b9d93bda3c16b9aa446be0
%global source0_file th_ro_RO.3.3.zip
# oreon url source checksums end
URL: http://rospell.sourceforge.net/
License: GPL-2.0-or-later
BuildArch: noarch
Requires: mythes
Supplements: (mythes and langpacks-ro)

%description
Romanian thesaurus.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/th_ro_RO.3.3.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "097f0a58be60859292fb0c8109669d579abd19a500b9d93bda3c16b9aa446be0" || { echo "oreon: Source0 SHA256 mismatch for th_ro_RO.3.3.zip" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_ro_RO.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_ro_RO_v2.dat
cp -p th_ro_RO.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_ro_RO_v2.idx


%files
%doc README COPYING.GPL 
%{_datadir}/mythes/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3-32
- Prepare for Oreon 11 (RP1)
