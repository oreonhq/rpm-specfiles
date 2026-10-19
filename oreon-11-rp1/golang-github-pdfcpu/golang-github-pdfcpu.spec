%global source0_hash 29fd5d6dc46c4cff9e0be556447bf030f38be3ea29fbde0ac0307b109f91c160
%bcond check 0
%global goipath         github.com/pdfcpu/pdfcpu
Version:                0.16.0
%gometa
%global common_description %{expand:
A PDF processor written in Go.}
%global golicenses      LICENSE.txt
%global godocs          CODE_OF_CONDUCT.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A PDF processor written in Go
License:        ASL 2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/pdfcpu-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

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
