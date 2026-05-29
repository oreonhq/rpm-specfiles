%global source0_hash 814fb5979a3a4b8576b1f901e606b482bebb41cb7e57926e6d5765ee786b96d3

%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif

%if %{defined rhel}
%bcond_with docs
%else
%bcond_without docs
%endif

Name: conmon
%if %{defined rhel}
Epoch: 3
%else
Epoch: 2
%endif
Version: 2.2.1
License: Apache-2.0
Release: %autorelease
Summary: OCI container runtime monitor
URL: https://github.com/containers/%{name}
# Tarball fetched from upstream
Source0:        https://github.com/containers/conmon/archive/refs/tags/v2.2.1.tar.gz

%if %{with docs}
BuildRequires: go-md2man
%endif
BuildRequires: gcc
BuildRequires: git-core
BuildRequires: glib2-devel
BuildRequires: libseccomp-devel
BuildRequires: pkgconfig
BuildRequires: systemd-devel
BuildRequires: systemd-libs
BuildRequires: make
Requires: glib2
Requires: systemd-libs
Requires: libseccomp

%description
%{summary}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -S git %{name}-%{version}
sed -i 's/install.bin: bin\/conmon/install.bin:/' Makefile

%build
%{__make} DEBUGFLAG="-g" bin/conmon

%if %{with docs}
%{__make} GOMD2MAN=go-md2man -C docs
%endif

%install
%{__make} PREFIX=%{buildroot}%{_prefix} install.bin

%if %{with docs}
%{__make} PREFIX=%{buildroot}%{_prefix} -C docs install
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%if %{with docs}
%{_mandir}/man8/%{name}.8.gz
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.1-1
- Prepare for Oreon 11 (RP1)
