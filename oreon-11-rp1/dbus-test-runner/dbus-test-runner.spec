%global source0_hash 645a32fbd909baf2c01438f0cbda29dc9cd01a7aba5504c45610d88e8a57cb76
Name:           dbus-test-runner
Version:        19.04.0
Release:        1%{?dist}
Summary:        Utility to run executables under a new DBus session for testing
License:        GPL-3.0-only
URL:            https://launchpad.net/%{name}
Source0:        https://launchpad.net/%{name}/19.04/19.04.0/+download/%{name}-19.04.0.tar.gz
Requires:       dbus-daemon
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  intltool
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
# /oreon:deps
%description
dbus-test-runner is a simple little executable for running a couple of
programs under a new DBus session.

Use this DBus tool for unit testing of code that accesses DBus at runtime.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --enable-static=no
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_mandir}/man1/
LD_LIBRARY_PATH=%{buildroot}%{_libdir} help2man --no-info \
    --version-string='%{version}' --help-option='--help-all' \
    -o %{buildroot}%{_mandir}/man1/%{name}-%{version}.1 \
    %{buildroot}%{_bindir}/%{name}
find %{buildroot} -name "*.la" -delete
%oreon_autofiles dbus-test-runner-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dbus-test-runner-devel -f %{oreon_filedir}/dbus-test-runner-devel.list

%changelog

%autochangelog
