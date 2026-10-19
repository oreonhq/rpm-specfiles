%global source0_hash 9bee136cc3a676e8a11e5ad23339f32fe1a6aea473abca1cc625beb71ebbafc9
%bcond_with compat
Name:           snoopy
Version:        2.5.2
Release:        4%{?dist}
Summary:        A preload library to send shell commands to syslog
License:        GPL-2.0-or-later
URL:            https://github.com/a2o/snoopy
Source0:        https://github.com/a2o/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        snoopy-disable
Source2:        snoopy-enable
Patch0:         https://github.com/a2o/snoopy/commit/77afb175f45b03d7a92f88a90f664d8be083baf5.patch#/snoopy-glibc-2_43.diff
Patch1101:      %{name}-disable-utmp-tests.diff
%if %{with compat}
%if 0%{?el8}
Recommends:     %{name}-compat = %{version}-%{release}
%endif
%else
%endif
# oreon:deps
BuildRequires:  /usr/bin/hostname
BuildRequires:  /usr/bin/ps
BuildRequires:  /usr/bin/socat
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description

%if %{with compat}
%package        compat
Summary:        Compatibility scripts for %{name}
BuildArch:      noarch
Provides:       deprecated()
Requires:       %{name} = %{version}-%{release}
%description compat

This package contains compatibility scripts for Snoopy.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N
%ifarch aarch64 s390x
%autopatch -p1
%else
%autopatch -p1 -M 1100
%endif
%if %{with compat}
# compat scripts
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
%endif

%build

%configure
%make_build
%install
%make_install
%if %{with compat}
for cmd in disable enable; do
  install -p snoopy-${cmd} %{buildroot}%{_sbindir}/
done
%endif
rm %{buildroot}%{_libdir}/libsnoopy.la
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build check
%files -f %{oreon_filedir}/main.list
%files -n snoopy-compat -f %{oreon_filedir}/snoopy-compat.list

%changelog

%autochangelog
