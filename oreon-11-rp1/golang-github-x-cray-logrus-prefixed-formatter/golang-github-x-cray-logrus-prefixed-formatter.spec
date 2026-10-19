%global source0_hash a966d81bbaef60a98073b589c2054f0171ccc09539589b71c30c936009fbb164
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/x-cray/logrus-prefixed-formatter
Version:                0.5.2
%gometa -f
%global common_description %{expand:
Logrus Prefixed Log Formatter.}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Logrus Prefixed Log Formatter
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/logrus-prefixed-formatter-%{version}.tar.gz
%if 0%{?fc37}
%endif
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
