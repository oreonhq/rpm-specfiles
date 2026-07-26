%global source0_hash 7dfb138b6ceeab34d58906be2598812d6dcc83885e650f93414d4851027c968c

%global build_flags prefix=%{_prefix} lib_dir=%{_libdir} libexec_dir=%{_libexecdir}/%{name} etc_dir=%{_sysconfdir}/%{name}

Name:           authbind
Version:        2.1.2
Release:        %autorelease
Summary:        Allow non-root users to open restricted ports

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://www.chiark.greenend.org.uk/ucgi/~ian/git/authbind.git/
Source0:        https://deb.debian.org/debian/pool/main/a/%{name}/%{name}_%{version}.tar.gz
Patch0:         authbind-makefile-fixes.patch

BuildRequires:  gcc
BuildRequires:  make

%description
This package allows a package to be started as non-root but still bind to low
ports, without any changes to the application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name} -p1

%build
%set_build_flags
%make_build %{build_flags} OPTIMISE="$CFLAGS" LDFLAGS="$LDFLAGS"

%install
%make_install %{build_flags} STRIP=/bin/true

%files
%license debian/copyright
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.1*
%{_libexecdir}/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/byaddr
%dir %{_sysconfdir}/%{name}/byport
%dir %{_sysconfdir}/%{name}/byuid

%changelog
%autochangelog
