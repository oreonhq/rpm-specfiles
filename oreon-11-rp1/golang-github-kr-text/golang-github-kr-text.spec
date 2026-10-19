%global source0_hash 59b5e4a7fd4097be87fad0edcaf342fdc971d0c8fdfb4f2d7424561471992e7c
%bcond check 0
%global goipath         github.com/kr/text
Version:                0.2.0
%gometa
%global common_description %{expand:
Miscellaneous functions for formatting text.}
%global godocs          Readme Readme-colwriter Readme-mc
Name:           %{goname}
Release:        1%{?dist}
Summary:        Miscellaneous functions for formatting text
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/text-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1
mv colwriter/Readme Readme-colwriter
mv mc/Readme Readme-mc

%build

%if 0%{?el9}
export GOPATH="%{gobuilddir}:%{gopath}"
export GO111MODULE=off
%endif
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%gobuild -o %{gobuilddir}/bin/go-mc %{goipath}/mc
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
