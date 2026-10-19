%global source0_hash f5e7e125739b41564de1d3616ef8ca2fa0876aa332a9b4e136ef4da8684f9a43
%bcond check 0
%global goipath         github.com/emersion/go-smtp
Version:                0.15.0
%gometa
%global common_description %{expand:
An SMTP client & server library written in Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        SMTP client & server library written in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-smtp-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/emersion/go-sasl)
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
