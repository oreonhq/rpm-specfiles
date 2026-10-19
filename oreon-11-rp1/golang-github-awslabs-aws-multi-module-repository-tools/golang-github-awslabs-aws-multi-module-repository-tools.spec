%global source0_hash 9761d9624cec8326e4b2f7c348d3690fb0a366b34329d0be0774124785304c16
%bcond check 0
%global goipath         github.com/awslabs/aws-go-multi-module-repository-tools
%global commit          b6ea8596afb401d42d28ccb2b8dadb20b4847fa7
%gometa -f
%global common_description %{expand:
%global golicenses      LICENSE LICENSE.txt NOTICE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        None
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/aws-go-multi-module-repository-tools-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

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
