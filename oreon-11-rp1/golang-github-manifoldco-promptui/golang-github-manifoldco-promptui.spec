%global source0_hash 84a72dfb56f61436a04fdde28f62b32aa07af75895e3423f199f7872aea43114
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/manifoldco/promptui
Version:                0.9.0
%gometa
%global common_description %{expand:
Interactive prompt for command-line applications.}
%global golicenses      LICENSE.md
%global godocs          _examples CHANGELOG.md CODE_OF_CONDUCT.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Interactive prompt for command-line applications
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/promptui-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/chzyer/readline)
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
