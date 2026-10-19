%global source0_hash 8d265ee08e66fbda2e6c2b348624cd4552ff2c8fe72247d8904b06500c476adf
%global build_flags prefix=%{_prefix} lib_dir=%{_libdir} libexec_dir=%{_libexecdir}/%{name} etc_dir=%{_sysconfdir}/%{name}
Name:           authbind
Version:        2.2.0
Release:        1%{?dist}
Summary:        Allow non-root users to open restricted ports
License:        GPL-2.0-only
URL:            https://www.chiark.greenend.org.uk/ucgi/~ian/git/authbind.git/
Source0:        https://deb.debian.org/debian/pool/main/a/%{name}/%{name}_%{version}.tar.gz
Patch0:         authbind-makefile-fixes.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
This package allows a package to be started as non-root but still bind to low
ports, without any changes to the application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

%set_build_flags
%make_build %{build_flags} OPTIMISE="$CFLAGS" LDFLAGS="$LDFLAGS"
%install
%make_install %{build_flags} STRIP=/bin/true
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
