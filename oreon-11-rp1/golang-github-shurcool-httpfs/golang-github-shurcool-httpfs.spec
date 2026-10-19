%global source0_hash 765234096a2eec0cefda8e4a8402be002d4a8deca2def5a3ae1ece7116823d93
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/shurcooL/httpfs
%global commit          8d4bc4ba774931155e6cd5ef6098cb038dd45135
%gometa
%global common_description %{expand:
Collection of Go packages for working with the http.FileSystem interface.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Collection of Go packages for working with the http.FileSystem interface
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/httpfs-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/shurcooL/httpgzip)
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
