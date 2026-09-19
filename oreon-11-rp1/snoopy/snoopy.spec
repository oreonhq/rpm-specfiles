%global source0_hash 9bee136cc3a676e8a11e5ad23339f32fe1a6aea473abca1cc625beb71ebbafc9

# compat was already shipped on Fedora < 42 and EL9,  even though
# they never had snoopy <= 2.4.x,
# so we need to keep it for the duration of the lifecycle, but we can drop this
# in Fedora >= 42 and RHEL >= 10
%if 0%{?rhel} && 0%{?rhel} < 10
%bcond_without compat
%else
%bcond_with compat
%endif

Name:           snoopy
Version:        2.5.2
Release:        4%{?dist}
Summary:        A preload library to send shell commands to syslog
License:        GPL-2.0-or-later
URL:            https://github.com/a2o/snoopy
Source0:        %{url}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        snoopy-disable
Source2:        snoopy-enable

# Upstream patches (0001~0500)
Patch0:         https://github.com/a2o/snoopy/commit/77afb175f45b03d7a92f88a90f664d8be083baf5.patch#/snoopy-glibc-2_43.diff

# Proposed upstream patches (0501~1000)

# Fedora-only patches (1001+)
# arch-specific (1101+)
Patch1101:      %{name}-disable-utmp-tests.diff

BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make
# For tests
BuildRequires:  %{_bindir}/hostname
BuildRequires:  %{_bindir}/socat
BuildRequires:  %{_bindir}/ps

%if %{with compat}
%if 0%{?el8}
Recommends:     %{name}-compat = %{version}-%{release}
%endif
%else
# drop in Fedora 44 (upgrading from 41 no longer supported)
# and EPEL 11
%if (0%{?fedora} && 0%{?fedora} < 44) || (0%{?rhel} && 0%{?rhel} < 11)
Obsoletes:      %{name}-compat < 2.5.1-6%{?dist}
%endif
%endif

%global _description %{expand:
Snoopy is designed to aid a sysadmin by providing a log of commands executed.
Snoopy is completely transparent to the user and applications.
It is linked into programs to provide a wrapper around calls to execve().
Logging is done via syslog.}

%description %{_description}

%if %{with compat}
%package        compat
Summary:        Compatibility scripts for %{name}

BuildArch:      noarch

# this is only needed for the lifetime of Fedora and EPEL releases that
# originally shipped snoopy <= 2.4.x (which has snoopy-disable and
# snoopy-enable instead of snoopyctl)
#
# per policy we can't mark a package as deprecated on a released
# Fedora branch
Provides:       deprecated()
Requires:       %{name} = %{version}-%{release}

%description compat %{_description}

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

# Get rid of libtool archive file
rm %{buildroot}%{_libdir}/libsnoopy.la

%check
%make_build check

%files
%license COPYING
%doc README.md ChangeLog doc/FAQ.md doc/FILTER_exclude_spawns_of.md
# Note, the plain .so file needs to be here since it's a preload library
%{_libdir}/libsnoopy.so*
%{_sbindir}/snoopyctl
%config(noreplace) %{_sysconfdir}/snoopy.ini

%if %{with compat}
%files compat
%{_sbindir}/snoopy-disable
%{_sbindir}/snoopy-enable
%endif

%changelog
%autochangelog
