%global source0_hash 44ff119a27b343ec47a797fa8701c19b9e672230bc15f3c6a6cede9641ea6332
Name:           samurai
Version:        1.3
Release:        1%{?dist}
Summary:        ninja-compatible build tool written in C
License:        Apache-2.0
URL:            https://github.com/michaelforney/samurai
Source0:        https://github.com/michaelforney/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
samurai is a ninja-compatible build tool written in C99
with a focus on simplicity, speed, and portability.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%make_build
%install
%make_install PREFIX=%{_prefix} MANDIR=%{_mandir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
