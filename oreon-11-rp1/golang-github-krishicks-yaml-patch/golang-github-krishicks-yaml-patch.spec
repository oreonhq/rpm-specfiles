%global source0_hash b5b7a772010487f718efb8cf0442159579d4418be4aab25b2d0a1e74ce3179b0
%bcond check 0
%global goipath         github.com/krishicks/yaml-patch
Version:                0.0.10
%global commit          05b317776495082a4efae44ea92f06cd6e3b875f
%gometa
%global common_description %{expand:
Yaml-patch is a version of Evan Phoenix's json-patch, which is an implementation
of JavaScript Object Notation (JSON) Patch, directly transposed to YAML.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Library to apply YAML versions of RFC6902 patches
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/yaml-patch-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/jessevdk/go-flags)
BuildRequires:  golang(github.com/onsi/ginkgo)
BuildRequires:  golang(github.com/onsi/gomega)
BuildRequires:  golang(gopkg.in/yaml.v2)
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
