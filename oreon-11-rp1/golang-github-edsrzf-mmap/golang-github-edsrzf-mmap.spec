%global source0_hash 9e92e9a7daeac05b86e15a5cf301767dad5a47648a33e05527911ccfa055d244
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/edsrzf/mmap-go
Version:                1.2.0
%gometa
%global common_description %{expand:
Mmap-go is a portable mmap package for the Go programming language. It has been
tested on Linux (386, amd64), OS X, and Windows (386). It should also work on
other Unix-like platforms, but hasn't been tested with them. I'm interested to
hear about the results.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Portable mmap package for Go
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/mmap-go-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/sys/unix)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

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
