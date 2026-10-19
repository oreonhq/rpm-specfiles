%global source0_hash cf3c15fd497b226f52621c80c26baf94bcb6778a1cc27f28c28a6fcf7c810898
%bcond check 0
%global goipath         github.com/uber/athenadriver
Version:                1.1.15
%gometa -L -f
%global common_description %{expand:
A fully-featured AWS Athena database driver.}
%global golicenses      LICENSE
%global godocs          examples ChangeLog.txt README.md
Name:           golang-github-uber-athenadriver
Release:        1%{?dist}
Summary:        A fully-featured AWS Athena database driver
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/athenadriver-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%build

%gobuild -o %{gobuilddir}/bin/athenareader %{goipath}/athenareader
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/athenareader %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
