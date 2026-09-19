%global source0_hash 48b77dc33315e6f760791a2984f98ea4bff28504ff37d460d8291585f49fcd3a

Name:           clinfo
Summary:        Enumerate OpenCL platforms and devices
Version:        3.0.25.02.14
Release:        %autorelease
# Automatically converted from old format: CC0 - review is highly recommended.
License:        CC0-1.0
URL:            https://github.com/Oblomov/clinfo
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ocl-icd-devel

%description
A simple OpenCL application that enumerates all possible platform and
device properties. Inspired by AMD's program of the same name, it is
coded in pure C99 and it tries to output all possible information,
including that provided by platform-specific extensions, and not to
crash on platform-unsupported properties (e.g. 1.2 properties on 1.1
platforms).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%set_build_flags
%make_build

%install
install -Dpm0755 -t %{buildroot}%{_bindir} %{name}
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 man1/%{name}.1

%files
%license LICENSE legalcode.txt
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
