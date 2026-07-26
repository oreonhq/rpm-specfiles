%global source0_hash 7984a74edef94571d872d0629b224abaa956a36f632f5c5516b33d22e49eb566

%global debug_package %{nil}

Name: mypaint2-brushes
Version: 2.0.2
Release: 14%{?dist}
Summary: Collections of brushes for MyPaint
# Automatically converted from old format: CC0 - review is highly recommended.
License: CC0-1.0
URL: https://github.com/mypaint/mypaint-brushes
Source0: https://github.com/mypaint/mypaint-brushes/releases/download/v%{version}/mypaint-brushes-%{version}.tar.xz
BuildArch: noarch

BuildRequires: make

%description
Brushes used by MyPaint 2 and other software using libmypaint2.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?isa} = %{version}-%{release}

%description devel
This package contains files needed for development with %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n mypaint-brushes-%{version}

%build
%configure
%make_build

%install
%make_install

%check
make check

%files
%license COPYING
%doc README
%{_datadir}/mypaint-data/2.0

%files devel
%{_datadir}/pkgconfig/mypaint-brushes-2.0.pc

%changelog
%autochangelog
