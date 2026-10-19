%global source0_hash a35116c25419836955a509bfb9f705657dc34bc414ce314ee92f3df983244d7b
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/seccomp/libseccomp-golang
Version:                0.12.0
%gometa -L
%global common_description %{expand:
The libseccomp library provides an easy to use, platform independent, interface
to the Linux Kernel's syscall filtering mechanism.  The libseccomp API is
designed to abstract away the underlying BPF based syscall filter language and
present a more conventional function-call based filtering interface that should
be familiar to, and easily adopted by, application developers.
The libseccomp-golang library provides a Go based interface to the libseccomp
library.}
%global golicenses      LICENSE
%global godocs          CHANGELOG README
Name:           golang-github-seccomp-libseccomp
Release:        1%{?dist}
Summary:        Libseccomp Go bindings
License:        BSD-2-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/libseccomp-golang-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  pkgconfig(libseccomp)
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

%ifnarch i686 ppc64le s390x riscv64
%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
