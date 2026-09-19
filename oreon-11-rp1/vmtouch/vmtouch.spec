%global source0_hash d57b7b3ae1146c4516429ab7d6db6f2122401db814ddd9cdaad10980e9c8428c

Name:           vmtouch
Version:        1.3.1
Release:        12%{?dist}
Summary:        Portable file system cache diagnostics and control

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://hoytech.com/vmtouch/
Source0:        https://github.com/hoytech/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  /usr/bin/pod2man
BuildRequires:  perl-generators

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

%files
%doc CHANGES README.md TODO TUNING.md
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
%autochangelog
