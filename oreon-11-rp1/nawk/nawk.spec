%global source0_hash 7ae5b9fc6a8149bc45ea0ba3ba434a69a16d1460d19f6d01b6f04cc885b8e02b
Name:    nawk
Version: 20260426
Release:        1%{?dist}
Summary:        "The one true awk" descended from UNIX V7
License: MIT
URL:     https://github.com/onetrueawk/awk
Source0:        https://github.com/onetrueawk/awk/archive/%{version}.tar.gz
Patch0:  nawk-manpage.patch
# oreon:deps
BuildRequires:  bison
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
This is the version of awk described in The AWK Programming Language, Second
Edition, by Al Aho, Brian Kernighan, and Peter Weinberger (Addison-Wesley,
2024, ISBN-13 978-0138269722, ISBN-10 0138269726).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir awk-%{version}
%oreon_prep
%build

make CFLAGS="%{optflags}" CC="%{__cc}" HOSTCC="%{__cc}"
%check

make test
%install
rm -rf %{buildroot}
install -D -p -m 0755 a.out %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 awk.1 %{buildroot}%{_mandir}/man1/%{name}.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
