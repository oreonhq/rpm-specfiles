%global source0_hash 230aceb83b895e9b509b142010b7b2a241f162433177b17d85165917cbe558b5
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/golang/glog
Version:                1.0.0
%gometa
%global common_description %{expand:
This is an efficient pure Go implementation of leveled logs in the
manner of the open source C++ package.
By binding methods to booleans it is possible to use the log package
without paying the expense of evaluating the arguments to the log.
Through the -vmodule flag, the package also provides fine-grained
control over logging at the file level.}
%global golicenses      LICENSE
%global godocs          README
Name:           %{goname}
Release:        1%{?dist}
Summary:        Leveled execution logs for Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/glog-%{version}.tar.gz
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
