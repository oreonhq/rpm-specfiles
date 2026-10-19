%global source0_hash 08ee0bebd49e0f52004286fcb264093f8524ed3d26dba235c7d6d772670a3bcd
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/google/go-cmdtest
Version:                0.4.0
%gometa
%global common_description %{expand:
The cmdtest package simplifies testing of command-line interfaces. It provides a
simple, cross-platform, shell-like language to express command execution. It can
compare actual output with the expected output, and can also update a file with
new "golden" output that is deemed correct.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Simplify testing of command-line interfaces
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-cmdtest-%{version}.tar.gz
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
