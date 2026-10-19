%global source0_hash 41399efdc8469b69215ac16aba367a5d00b728b2a593ededd2aee62d2002446b
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/macaron.v1
%global forgeurl        https://github.com/go-macaron/macaron
Version:                1.4.0
%gometa
%global goaltipaths     github.com/go-macaron/macaron
%global common_description %{expand:
Package Macaron is a high productive and modular web framework in Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        High productive and modular web framework in Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/macaron-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/go-macaron/inject)
BuildRequires:  golang(github.com/smartystreets/goconvey/convey)
BuildRequires:  golang(github.com/unknwon/com)
BuildRequires:  golang(golang.org/x/crypto/pbkdf2)
BuildRequires:  golang(gopkg.in/ini.v1)
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
