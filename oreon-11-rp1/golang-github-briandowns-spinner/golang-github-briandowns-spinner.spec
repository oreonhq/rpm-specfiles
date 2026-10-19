%global source0_hash 7741d8b38aa70606627b51c5957bb00ae4a90726fbf8fcddb42d413373782c5e
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/briandowns/spinner
Version:                1.23.2
%gometa -f
%global common_description %{expand:
Go (golang) package with 90 configurable terminal spinner/progress indicators.}
%global golicenses      LICENSE NOTICE.txt
%global godocs          _example README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go package providing a terminal spinner/progress indicator
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/spinner-%{version}.tar.gz
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
