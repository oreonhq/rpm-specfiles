%global source0_hash 29d844be31db4714408980f6faea024e6cb36fcdd64537dab750ca7676f9a547
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/coreos/ioprogress
%global commit          4637e494fd9b23c5565ee193e89f91fdc1639bc0
%gometa
%global common_description %{expand:
Ioprogress is a Go library with implementations of io.Reader and io.Writer that
draws progress bars. The primary use case for these are for CLI applications but
alternate progress bar writers can be supplied for alternate environments.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Go package for progress bars around io.Reader/Writers
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/ioprogress-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
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
