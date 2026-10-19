%global source0_hash 0f9d5a1c4901375aa827b2ddc252ed9aa465a4d7e94725b1946964ec9804061f
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/dnaeon/go-vcr
Version:                4.0.7
%gometa
%global common_description %{expand:
Go-vcr simplifies testing by recording your HTTP interactions and replaying them
in future runs in order to provide fast, deterministic and accurate testing of
your code.}
%global golicenses      LICENSE
%global godocs          example README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Record your http interactions for fast, deterministic and accurate tests
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-vcr-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(gopkg.in/yaml.v2)
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
