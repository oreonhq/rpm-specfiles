%global source0_hash d5f19ef91ff78f41f2c70c68051f1aa63d56344908a8334ce040d40157567d02
%bcond check 0
%global goipath         github.com/RaveNoX/go-jsoncommentstrip
Version:                1.0.0
%gometa -f
%global common_description %{expand:
Library for strip JSON comments.}
%global golicenses      LICENSE.md
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Library for strip JSON comments
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-jsoncommentstrip-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

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
