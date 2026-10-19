%global source0_hash 582808364cc268544e3e6775b15d7fffbc28ccfb930a29840bb25e32d7d95e1f
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/jinzhu/inflection
Version:                1.0.0
%gometa
%global common_description %{expand:
Inflection pluralizes and singularizes English nouns.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Pluralizes and singularizes English nouns
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/inflection-%{version}.tar.gz
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
