%global source0_hash ce6f6a59a6451072fe71c980c89f265761b692e14415b39fb8038eda99fbfe36
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/gobuffalo/envy
Version:                1.10.2
%gometa
%global common_description %{expand:
Envy makes working with ENV variables in Go trivial.}
%global golicenses      LICENSE.txt
%global godocs          README.md SHOULDERS.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Work with ENV variables in Go trivially
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/envy-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/joho/godotenv)
BuildRequires:  golang(github.com/rogpeppe/go-internal/modfile)
BuildRequires:  golang(github.com/stretchr/testify/require)
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
