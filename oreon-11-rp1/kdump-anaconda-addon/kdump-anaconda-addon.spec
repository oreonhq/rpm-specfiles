%global source0_hash none

%global gitcommit 2a3605a2182218ab5017beff064c81ae7936832f
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global snapshotdate 20250925

Name: kdump-anaconda-addon
Version: 006
Release: 17.%{snapshotdate}git%{gitshortcommit}%{?dist}
Url: https://github.com/rhinstaller/kdump-anaconda-addon
License: GPL-2.0-only
Summary: Kdump configuration anaconda addon

BuildArch: noarch
Requires: anaconda-core >= 34.13
Requires: hicolor-icon-theme
BuildRequires: intltool gettext
BuildRequires: make
Obsoletes: kexec-tools-anaconda-addon < 2.0.17-9
Provides: kexec-tools-anaconda-addon = %{version}-%{release}

Source0:        https://github.com/rhinstaller/kdump-anaconda-addon/archive/refs/tags/%{gitcommit}.tar.gz#/kdump-anaconda-addon-%{gitshortcommit}.tar.gz

%description
Kdump anaconda addon

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{gitcommit}

%build

%install
%make_install

%find_lang kdump-anaconda-addon

%files -f kdump-anaconda-addon.lang
%doc README
%license LICENSE
%{_datadir}/anaconda/addons/com_redhat_kdump
%{_datadir}/anaconda/dbus/confs/org.fedoraproject.Anaconda.Addons.Kdump.conf
%{_datadir}/anaconda/dbus/services/org.fedoraproject.Anaconda.Addons.Kdump.service
%{_datadir}/icons/hicolor/scalable/apps/kdump.svg

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 006-17.
- Prepare for Oreon 11 (RP1)
