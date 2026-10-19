%global source0_hash c33fa783d7e021bad1c502be6ed7bcb250cfda139a7d883f7cf06efe1cc3df72
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/readline.v1
%global forgeurl        https://github.com/chzyer/readline
Version:                1.4
%global commit          2972be24d48e78746da79ba8e24e8b488c9880de
%gometa
%global common_description %{expand:
Readline is a pure Go implementation of GNU Readline like library.}
%global golicenses      LICENSE
%global godocs          example CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Pure Go implementation of GNU Readline-like library
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/readline-%{commit}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/chzyer/test)
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
