%global source0_hash 28acc3ae26e32c7343ceedf339de65a20ea8735f3b730fff4271c3eaa490d8db
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/flynn/json5
%global commit          7620272ed63390e979cf5882d2fa0506fe2a8db5
%gometa
%global common_description %{expand:
This is a Go package that implements decoding of JSON5.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Go JSON5 decoder package based on encoding/json
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/json5-%{commit}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/kylelemons/godebug/pretty)
BuildRequires:  golang(github.com/robertkrimen/otto)
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
