%global source0_hash 626d7d19f8e4ceae70f60e2e662291789e0f54ab86945317a3d5693c30f847a2

Name:    nawk
Version: 20251225
Release: 3%{?dist}
Summary: "The one true awk" descended from UNIX V7
License: MIT
URL:     https://github.com/onetrueawk/awk
Source0: https://github.com/onetrueawk/awk/archive/%{version}.tar.gz

# rename awk to nawk
Patch0:  nawk-manpage.patch
BuildRequires: make gcc bison

%description
This is the version of awk described in The AWK Programming Language, Second
Edition, by Al Aho, Brian Kernighan, and Peter Weinberger (Addison-Wesley,
2024, ISBN-13 978-0138269722, ISBN-10 0138269726).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n awk-%{version}

%build
make CFLAGS="%{optflags}" CC="%{__cc}" HOSTCC="%{__cc}"

%check
make test

%install
rm -rf %{buildroot}

# The binary is created as a.out, so renamed it to nawk
install -D -p -m 0755 a.out %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 awk.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc FIXES FIXES.1e README.md ChangeLog
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
