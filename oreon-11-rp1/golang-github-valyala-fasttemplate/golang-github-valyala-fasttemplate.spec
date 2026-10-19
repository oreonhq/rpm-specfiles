%global source0_hash 14881149dfc3d49606728d0c8e704cfaeb7fbbf2c42d20e771cf1bbae9fb1044
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/valyala/fasttemplate
Version:                1.2.1
%gometa
%global common_description %{expand:
Simple and fast template engine for Go.
Fasttemplate performs only a single task - it substitutes template placeholders
with user-defined values.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Simple and fast template engine for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/fasttemplate-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/valyala/bytebufferpool)
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
