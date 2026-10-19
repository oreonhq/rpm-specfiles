%global source0_hash 7328c22d783dcd25798db8a0aba7f4986dd9b12dbca8969b52e1a96c563409eb
%ifnarch %{ix86} %{arm}
%bcond check 0
%endif
%global goipath         github.com/xlab/treeprint
Version:                1.1.0
%gometa
%global common_description %{expand:
Package Treeprint provides a simple ASCII tree composing tool.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Simple ASCII tree composing tool
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/treeprint-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
