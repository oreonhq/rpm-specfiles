%global source0_hash 810d65cbbff2bb74533ada8f91aecc61b91c483634dd2c17c90ae2cfa4a7fbd1
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/alecthomas/participle/v2
Version:                2.1.1
%gometa -L -f
%global common_description %{expand:
A parser library for Go.}
%global golicenses      COPYING
%global godocs          _examples CHANGES.md TUTORIAL.md README.md\\\
                        bin/README.hermit.md
Name:           golang-github-alecthomas-participle2
Release:        1%{?dist}
Summary:        A parser library for Go
License:        MIT
URL:            %{gourl}
Source0:        https://github.com/alecthomas/participle/archive/v%{version}/participle-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
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
