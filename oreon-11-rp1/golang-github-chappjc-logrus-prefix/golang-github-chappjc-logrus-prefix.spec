%global source0_hash faf02b3f2216672f815b499e72c6c74bf0dcc6adce202650a6b73221d0f2f5a9
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/chappjc/logrus-prefix
%global commit          3a1d64819adb569fb9952144dd90c0abe92e2822
%gometa
%global common_description %{expand:
Logrus Prefixed Log Formatter.}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Logrus Prefixed Log Formatter
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/logrus-prefix-%{commit}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/gomega)
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
