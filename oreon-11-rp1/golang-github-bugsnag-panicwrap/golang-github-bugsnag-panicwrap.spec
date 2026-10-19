%global source0_hash 786bda4ed5bb42272772e5c7784703c90468ad113ba897f534ec15be4ccf7e9b
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/bugsnag/panicwrap
Version:                1.3.4
%gometa -L
%global common_description %{expand:
Panicwrap is a Go library that re-executes a Go binary and monitors stderr
output from the binary for a panic. When it find a panic, it executes a
user-defined handler function. Stdout, stderr, stdin, signals, and exit codes
continue to work as normal, making the existence of panicwrap mostly invisble to
the end user until a panic actually occurs.
Since a panic is truly a bug in the program meant to crash the runtime, globally
catching panics within Go applications is not supposed to be possible. Despite
this, it is often useful to have a way to know when panics occur. panicwrap
allows you to do something with these panics, such as writing them to a file, so
that you can track when panics occur.
Panicwrap is not a panic recovery system. Panics indicate serious problems with
your application and should crash the runtime. panicwrap is just meant as a way
to monitor for panics. If you still think this is the worst idea ever, read the
section below on why.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md
Name:           golang-github-bugsnag-panicwrap
Release:        1%{?dist}
Summary:        Go library for catching and handling panics in Go applications
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/panicwrap-%{version}.tar.gz
Patch:          0001-Add-RISCV-as-valid-architecture.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
