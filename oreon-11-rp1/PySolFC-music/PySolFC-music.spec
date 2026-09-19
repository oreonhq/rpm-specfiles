%global source0_hash 535b7cb0f563ad507ddab6957469cd9d163c45b3b38c4f76957c04aec4ae97ae

%define mainversion 1.1

Name:           PySolFC-music
Version:        4.50
Release:        18%{?dist}
Summary:        Music for PySolFC

License:        GPL-2.0-or-later
URL:            https://pysolfc.sourceforge.io/
Source0:        https://github.com/shlomif/pysol-music/archive/%{version}/pysol-music-%{version}.tar.gz
Requires:       PySolFC >= %{mainversion}

BuildArch: noarch

%description
This package contains the background music for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n pysol-music-%{version}

%build

%install
install -d -m755 $RPM_BUILD_ROOT%{_datadir}/PySolFC/music
cp -a data/music/* $RPM_BUILD_ROOT%{_datadir}/PySolFC/music

%files
%doc README NEWS COPYING
%dir %{_datadir}/PySolFC/music
%{_datadir}/PySolFC/music/*

%changelog
%autochangelog
