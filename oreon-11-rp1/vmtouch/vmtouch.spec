%global source0_hash d57b7b3ae1146c4516429ab7d6db6f2122401db814ddd9cdaad10980e9c8428c
Name:           vmtouch
Version:        1.3.1
Release:        1%{?dist}
Summary:        Portable file system cache diagnostics and control
License:        LicenseRef-Callaway-BSD
URL:            http://hoytech.com/vmtouch/
Source0:        https://github.com/hoytech/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  /usr/bin/pod2man
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
%description
Vmtouch is a tool for learning about and controlling the file system cache of
Unix and Unix-like systems.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

make CFLAGS='%{optflags}'
%install
make install PREFIX=%{buildroot}%{_prefix} MANDIR=%{buildroot}%{_mandir}/man8
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
