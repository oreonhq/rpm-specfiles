%global source0_hash 51ef3ab185d632aa97d614ed31b7f2d01ccd3a58599db96525c57afa10f1b15f
%bcond check 0
%global goipath         github.com/fvbommel/util
Version:                0.0.3
%gometa
%global godevelheader %{expand:
Obsoletes:      golang-vbom-util-devel < 0-0.8
}
%global goaltipaths     vbom.ml/util
%global common_description %{expand:
Go utility packages.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go utility packages
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/util-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/bruth/assert)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
rm -rf sortorder

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
