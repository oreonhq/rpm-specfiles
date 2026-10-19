%global source0_hash f41c069f394e578580c6d3f592d993588a5b02dbc1e973f13eb4064eaddfefd4
%bcond_without tests
Summary:        Static code analysis tool for SELinux policy source files
Name: selint
Version: 1.5.1
Release:        1%{?dist}
URL: https://github.com/SELinuxProject/selint
License: Apache-2.0
Source0:        https://github.com/SELinuxProject/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  libconfuse-devel
BuildRequires:  make
BuildRequires:  pkgconfig(check)
BuildRequires:  uthash-devel
# /oreon:deps
%description
SELint is a program to perform static code analysis on SELinux policy source
files. SELint seeks to help policy developers write policy that is more
maintainable, readable and secure, and to reduce the time spent debugging
challenging policy issues.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -fiv -Wall -Wno-portability
%configure %{!?with_tests:--without-check}
%make_build
%install
%make_install
%oreon_autofiles main
%if %{with tests}
%check

%make_build check
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
