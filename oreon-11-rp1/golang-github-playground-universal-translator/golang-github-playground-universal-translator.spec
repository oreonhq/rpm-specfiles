%global source0_hash 227dd35a0011a1adfa69eae49b157436c5a4753e16bc670bd1f5a4a4b5b0aef6
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-playground/universal-translator
Version:                0.18.2
%gometa
%global common_description %{expand:
i18n Translator for Go/Golang using CLDR data + pluralization
rules.}
%global golicenses      LICENSE
%global godocs          _examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        i18n Translator for Go/Golang
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/universal-translator-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

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
