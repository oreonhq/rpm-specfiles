%global source0_hash 0adbf796c862abf4019686be31b59830f1d7e96632efa7c8e003fcf66df51aa8

Summary: Fedora Waves KDM theme
Name: fedorawaves-kdm-theme
Version: 1.1
Release: 33%{?dist}
BuildArch: noarch
License: GPL-1.0-or-later
Source0: %{name}-%{version}.tar.bz2
URL: http://www.redhat.com

Requires: kdebase-kdm

%description
This package contains the Fedora Waves KDM theme that is the default
theme in Fedora 9.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/usr/share/kde4/apps/kdm/themes/FedoraWaves
install -p -m 644 usr/share/kde4/apps/kdm/themes/FedoraWaves/*	\
	$RPM_BUILD_ROOT/usr/share/kde4/apps/kdm/themes/FedoraWaves

%files
%{_datadir}/kde4/apps/kdm/themes/*

%changelog
%autochangelog
