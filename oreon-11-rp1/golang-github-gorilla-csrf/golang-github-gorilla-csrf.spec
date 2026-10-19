%global source0_hash 4399ac78e57691e3b5d67f440567e11eca999fce05c986d2ea7410b5f49e8438
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/gorilla/csrf
Version:                1.7.3
%gometa
%global common_description %{expand:
Gorilla/csrf provides Cross Site Request Forgery (CSRF) prevention middleware
for Go web applications & services.}
%global golicenses      LICENSE
%global godocs          AUTHORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Cross Site Request Forgery (CSRF) prevention middleware
License:        BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/csrf-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/gorilla/securecookie)
BuildRequires:  golang(github.com/pkg/errors)
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
