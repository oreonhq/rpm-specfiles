%global source0_hash 338c6174e5c8652eaa34f956be3451f7491a4416ab489aef63151f802b00bf93
Name:    liblogging
Version: 1.0.8
Release:        1%{?dist}
Summary:        An easy to use logging library
License: BSD-2-Clause
URL:     http://www.liblogging.org/
Source0:        http://download.rsyslog.com/liblogging/liblogging-%{version}.tar.gz
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%package stdlog
Summary: An easy to use logging library - stdlog component
BuildRequires:  gcc
BuildRequires: dos2unix
BuildRequires: make
%package stdlog-devel
Summary: An easy to use logging library - stdlog development files
Requires: %{name}-stdlog%{_isa} = %{version}-%{release}
Requires: pkgconfig
%description
liblogging (the upstream project) is a collection of several components.
Namely: stdlog, journalemu, rfc3195.

%description stdlog
liblogging (the upstream project) is a collection of several components.
Namely: stdlog, journalemu, rfc3195.
The stdlog component of liblogging can be viewed as an enhanced version of the
syslog(3) API. It retains the easy semantics, but makes the API more
sophisticated "behind the scenes" with better support for multiple threads
and flexibility for different log destinations (e.g. syslog and systemd
journal).

%description stdlog-devel
This package contains development files for the %{name}-stdlog package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure \
  --disable-journal \
  --disable-rfc3195 \
  --disable-static \
  --enable-stdlog \
make V=1 %{?_smp_mflags}
dos2unix COPYING
%install
make DESTDIR=%{buildroot} install
rm -f \
  %{buildroot}%{_bindir}/stdlogctl \
  %{buildroot}%{_libdir}/liblogging-stdlog.la \
  %{buildroot}%{_mandir}/man1/stdlogctl.1 \
%ldconfig_scriptlets stdlog
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n liblogging-stdlog -f %{oreon_filedir}/liblogging-stdlog.list
%files -n liblogging-stdlog-devel -f %{oreon_filedir}/liblogging-stdlog-devel.list

%changelog

%autochangelog
