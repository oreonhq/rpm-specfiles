%global source0_hash fbf23f8a857f3a40d536d8a1fe5fd17a06a8828b4e16d02ae4cbaed033cca689
%bcond check 1
%global debug_package %{nil}
%global goipath         bazil.org/fuse
%global forgeurl        https://github.com/bazil/fuse
%global commit          fb710f7dfd05053a3bc9516dd5a7a8f84ead8aab
%gometa
%global common_description %{expand:
bazil.org/fuse is a Go library for writing FUSE userspace filesystems.
It is a from-scratch implementation of the kernel-userspace communication
protocol, and does not use the C library from the project called FUSE.
bazil.org/fuse embraces Go fully for safety and ease of programming.}
%global golicenses      LICENSE
%global godocs          doc examples README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Fuse library for Go
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/fuse-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/tv42/httpunix)
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
