%global source0_hash c8eec7d4525a852057df5d44ce89be08ef4f813244ded18a49f1344d909a4f27
%bcond check 0
%global debug_package %{nil}
%global goipath         mvdan.cc/editorconfig
%global forgeurl        https://github.com/mvdan/editorconfig
Version:                0.2.0
%gometa
%global common_description %{expand:
A small package to parse and use EditorConfig files. Currently passes all of
the official test cases.
Note that an official library exists for Go. This alternative implementation
started with a different design:
- Specialised INI parser, for full compatibility with the spec
- Ability to cache parsing files and compiling pattern matches
- Storing and querying all properties equally
- Minimising pointers and maps to store data}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        EditorConfig support in Go
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/editorconfig-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
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

go test %{gotestflags}
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
