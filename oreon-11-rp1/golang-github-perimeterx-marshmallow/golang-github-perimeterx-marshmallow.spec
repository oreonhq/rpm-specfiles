%global source0_hash d4f804a42181649e45f344764b273d9610aa439ca66f4efc8906fd07acc3b624
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/perimeterx/marshmallow
Version:                1.1.5
%gometa -f
%global common_description %{expand:
Marshmallow provides a flexible and performant JSON unmarshalling in Go. It
specializes in dealing with unstructured struct - when some fields are known
and some aren't, with zero performance overhead nor extra coding needed.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Marshmallow provides a flexible and performant JSON unmarshalling in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/marshmallow-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

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
