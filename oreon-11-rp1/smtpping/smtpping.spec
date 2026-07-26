%global source0_hash beca8c44133b91ebe9fdfd044d8dee0947aa7683cba7b0e509ce15cda8fef74a

Name:		smtpping
Version:	1.1.4
Release:	11%{?dist}
Summary:	Small tool for measuring SMTP parameters

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/halonsecurity/smtpping
Source0:	https://github.com/halonsecurity/smtpping/archive/v%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	coreutils
BuildRequires:	gcc-c++

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

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_mandir}/man1/*.1*
%{_bindir}/smtpping

%changelog
%autochangelog
