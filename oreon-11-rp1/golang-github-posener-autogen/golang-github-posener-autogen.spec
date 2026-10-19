%global source0_hash 3adbaaa9619c0e732c74de02181f9dc19acada2ddc6ec48c0b93b15a35dced63
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/posener/autogen
Version:                0.0.3
%gometa
%global common_description %{expand:
Automatically generate files.}
%global golicenses      LICENSE
%global godocs          example
Name:           %{goname}
Release:        1%{?dist}
Summary:        Automatically generate files
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/autogen-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/posener/script)
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
