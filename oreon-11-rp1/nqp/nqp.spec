%global source0_hash 120de1ac6f3246e7c5d04261ef18e64d9c3663f6670e952528d0d5c04b889cf2
Name:           nqp
Version:        2026.08
Release:        1%{?dist}
Summary:        Perl 6 compiler implementation that runs on MoarVM
License:        Artistic-2.0
URL:            https://github.com/Raku/nqp
Source0:        https://github.com/Raku/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  moarvm-devel
BuildRequires:  perl
# /oreon:deps
%description
This is "Not Quite Perl" -- a lightweight Raku-like environment for virtual
machines. The key feature of NQP is that it's designed to be a very small
environment (as compared with, say, raku or Rakudo) and is focused on being
a high-level way to create compilers and libraries for virtual machines like
MoarVM, the JVM, and others.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{__perl} Configure.pl --backends=moar --prefix=%{_prefix}
%make_build
%install
%make_install
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
