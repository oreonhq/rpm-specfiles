%global source0_hash 979424115de9e3b70ee91fc3839f77bbe54699a9e32b98be6936eea7e80a213f
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/streadway/handy
%global commit          0f66f006fb2ebde51f4ce769641df75d602989e7
%gometa
%global common_description %{expand:
Collection of useful HTTP handlers that form a handler stack of filters. Many
are opinionated for a specific purpose.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Net/http handler filters
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/handy-%{commit}.tar.gz
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

%gocheck -d retry
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
