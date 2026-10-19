%global source0_hash 764c5475b88b96f2fc0f1f7938cc093220483143984db386f04368fe146542a5
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/tklauser/go-sysconf
Version:                0.3.14
%gometa
%global common_description %{expand:
Sysconf for Go, without using cgo.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Sysconf for Go, without using cgo
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-sysconf-%{version}.tar.gz
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

sed -i '/{sysconf.SC_NPROCESSORS_CONF, C._SC_NPROCESSORS_CONF, "_NPROCESSORS_CONF"},/d' cgotest/sysconf_cgotest_linux.go
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
