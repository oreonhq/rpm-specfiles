%global source0_hash abbc9cb565bf94408aefee054d1cf59932b70a6c4d50e3a9149b886775e682fe
Name:		smtpping
Version:	1.1.5
Release:        1%{?dist}
Summary:        Small tool for measuring SMTP parameters
License:	GPL-2.0-or-later
URL:		https://github.com/halonsecurity/smtpping
Source0:        https://github.com/halonsecurity/smtpping/archive/v%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  coreutils
BuildRequires:  gcc-c++
# /oreon:deps
%description
A simple, portable tool for measuring SMTP server delay,
delay variation and throughput.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%cmake -DMAN_INSTALL_DIR:PATH=%{_mandir}
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
