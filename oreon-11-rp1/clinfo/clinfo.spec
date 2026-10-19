%global source0_hash e944132329c6613b686ba0fcd373b15ebb553c367a01a734af8519ddb095c01f
Name:           clinfo
Summary:        Enumerate OpenCL platforms and devices
Version:        3.1.26.09.26
Release:        1%{?dist}
License:        CC0-1.0
URL:            https://github.com/Oblomov/clinfo
Source0:        https://github.com/Oblomov/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ocl-icd-devel
# /oreon:deps
%description
A simple OpenCL application that enumerates all possible platform and
device properties. Inspired by AMD's program of the same name, it is
coded in pure C99 and it tries to output all possible information,
including that provided by platform-specific extensions, and not to
crash on platform-unsupported properties (e.g. 1.2 properties on 1.1
platforms).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%make_build
%install
install -Dpm0755 -t %{buildroot}%{_bindir} %{name}
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 man1/%{name}.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
