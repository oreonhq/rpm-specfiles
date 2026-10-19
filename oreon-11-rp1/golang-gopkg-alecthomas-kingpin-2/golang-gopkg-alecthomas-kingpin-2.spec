%global source0_hash c728098f6d9c9bf2c0eb0f47c3e07babeb6613b2429c43284e8b779e186a92ab
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/alecthomas/kingpin.v2
%global forgeurl        https://github.com/alecthomas/kingpin
Version:                2.3.2
%gometa -f
%global common_description %{expand:
Kingpin is a fluent-style, type-safe command-line parser. It supports flags,
nested commands, and positional arguments.}
%global golicenses      COPYING
%global godocs          _examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go command line and flag parser
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/kingpin-%{version}.tar.gz
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
