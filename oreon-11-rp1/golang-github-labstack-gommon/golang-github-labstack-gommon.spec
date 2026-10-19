%global source0_hash c23fa6b18c3f3c4dc917e7fb6d40db88ca2d13f51dbc9a8e8e098b8aa03611e9
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/labstack/gommon
Version:                0.3.0
%gometa
%global common_description %{expand:
Common packages for Go.}
%global golicenses      LICENSE
%global godocs          README.md README-log.md README-color.md\\\
                        README-bytes.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Common packages for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gommon-%{version}.tar.gz
Patch0:         test-fix.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/mattn/go-colorable)
BuildRequires:  golang(github.com/mattn/go-isatty)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/valyala/fasttemplate)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1

# rename READMEs so they are not in conflict when using the godocs macro
mv log/README.md README-log.md
mv color/README.md README-color.md
mv bytes/README.md README-bytes.md

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
