%global source0_hash fe698a2645db779ebf34d06eb14ca6f5e5f9d0961d1b887671d830e3b312ced8
%bcond check 0
%global goipath         github.com/jdeflander/goarrange
Version:                1.0.0
%gometa -L -f
%global common_description %{expand:
Automatic arrangement of Go source code.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           goarrange
Release:        1%{?dist}
Summary:        Automatic arrangement of Go source code
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
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

%gobuild -o %{gobuilddir}/bin/goarrange %{goipath}
%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
