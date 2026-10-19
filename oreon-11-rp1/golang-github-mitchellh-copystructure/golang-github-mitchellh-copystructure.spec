%global source0_hash 0f3c6a9d91d695470c22acaba390878a03e3c106a453c4b0b8abebfb76c1a009
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/mitchellh/copystructure
Version:                1.2.0
%gometa
%global common_description %{expand:
Copystructure is a Go library for deep copying values in Go.
This allows you to copy Go values that may contain reference values such as
maps, slices, or pointers, and copy their data as well instead of just their
references.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go library for deep copying values in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/copystructure-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
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
