%global source0_hash d5b79a488a88f4e4d04184efa0bc116929baf9b34617af70d8debfb37f7431f4
Name:           nq
Version:        1.0
Release:        1%{?dist}
Summary:        Unix command line queue utility
License:        CC0-1.0
URL:            https://github.com/leahneukirchen/nq
Source0:        https://github.com/leahneukirchen/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Recommends:     (tmux or screen)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Test::Harness)
# /oreon:deps
%description
The nq utility provides a very lightweight queuing system without requiring 
setup, maintenance, supervision or any long-running processes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build CFLAGS='%{build_cflags}'
%check

%make_build check
%install
%make_install PREFIX=%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
