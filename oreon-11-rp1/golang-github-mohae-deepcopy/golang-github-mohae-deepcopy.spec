%global source0_hash 6b171346026b553c49584c10a72267ebabae71e229b08c42cf9d23bd4ddcd6f2
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/mohae/deepcopy
%global commit          c48cc78d482608239f6c4c92a4abd87eb8761c90
%gometa
%global common_description %{expand:
DeepCopy makes deep copies of things: unexported field values are not copied.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Deep copy things
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/deepcopy-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

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
