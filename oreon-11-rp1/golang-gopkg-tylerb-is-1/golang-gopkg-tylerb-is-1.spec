%global source0_hash 97fcac292d9d4e49d62cb705fbe74ca17b700ee65bfa633ce2a6236dcc798e22
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/tylerb/is.v1
%global forgeurl        https://github.com/tylerstillwater/is
Version:                1.5
%global tag             v1.5
%gometa
%global common_description %{expand:
Is provides a quick, clean and simple framework for writing Go tests.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Is provides a quick, clean and simple framework for writing Go tests
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{tag}/is-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
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
