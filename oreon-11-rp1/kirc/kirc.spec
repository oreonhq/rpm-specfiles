%global source0_hash a54bc4d1a644f6fcb610f702454affc241b26da7fbde51951e0ec59133fa7b1d
Name:           kirc
Version:        1.2.2
Release:        1%{?dist}
Summary:        Tiny IRC client written in POSIX C99
License:        MIT
URL:            https://github.com/mcpcpc/kirc
Source0:        https://github.com/mcpcpc/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
kirc ("KISS for IRC") is a tiny open-source Internet Relay Chat (IRC) client
designed with usability and cross-platform compatibility in mind.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%make_build
%install
%make_install PREFIX="%{_prefix}"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
