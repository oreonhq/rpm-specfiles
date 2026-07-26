%global source0_hash 074147578bfc0d2f91a6702270517803ff4e960e9f175dfe14b00eee6febc0c6

Name:           nqp
Version:        2025.12
Release:        %autorelease
Summary:        Perl 6 compiler implementation that runs on MoarVM
License:        Artistic-2.0
URL:            https://github.com/Raku/nqp
Source0:        %{url}/releases/download/%{version}/nqp-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  moarvm-devel >= %{version}

%description
This is "Not Quite Perl" -- a lightweight Raku-like environment for virtual
machines. The key feature of NQP is that it's designed to be a very small
environment (as compared with, say, raku or Rakudo) and is focused on being
a high-level way to create compilers and libraries for virtual machines like
MoarVM, the JVM, and others.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%{__perl} Configure.pl --backends=moar --prefix=%{_prefix}
%make_build

%install
%make_install

%check
make test

%files
%license LICENSE
%doc README.pod
%{_bindir}/nqp
%{_bindir}/nqp-m
%{_datadir}/nqp/lib/*.moarvm
%{_datadir}/nqp/lib/profiler

%changelog
%autochangelog
