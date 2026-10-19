%global source0_hash 171a5a49d62d92d287df07b1a353f5780a50c4b45b52b41bef8fe02a7210089d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/mdlayher/socket
Version:                0.4.1
%gometa -f
%global common_description %{expand:
Package socket provides a low-level network connection type which integrates
with Go's runtime network poller to provide asynchronous I/O and deadline
support. MIT Licensed.}
%global golicenses      LICENSE.md
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Package socket provides a low-level network connection type which integrates with Go's runtime network poller to provide asynchronous I/O and deadline support. MIT Licensed
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/socket-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

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
