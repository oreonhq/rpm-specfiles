%global source0_hash eb89245b4dd6561e42ea14de96558bfba0bb05c1e8a3b3a81700a55ac91405bc
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/mattn/go-shellwords
Version:                1.0.15
%gometa
%global common_description %{expand:
Parse line as shell words.}
%global golicenses      LICENSE
%global godocs          _example README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Parse line as shell words
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-shellwords-%{version}.tar.gz
Patch:          https://github.com/junegunn/go-shellwords/commit/bf4f893cf83848d86c56798000808945f406d750.patch
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

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
