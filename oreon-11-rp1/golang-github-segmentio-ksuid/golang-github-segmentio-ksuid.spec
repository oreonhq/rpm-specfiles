%global source0_hash b8cec5b4e99f84249b34d8932f866b7abe47eb5fa7ef7b2f15e0a3ab3d62b8f6
%bcond check 0
%global goipath         github.com/segmentio/ksuid
Version:                1.0.4
%gometa
%global common_description %{expand:
K-Sortable Globally Unique IDs.}
%global golicenses      LICENSE.md
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        K-Sortable Globally Unique IDs
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/ksuid-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
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
