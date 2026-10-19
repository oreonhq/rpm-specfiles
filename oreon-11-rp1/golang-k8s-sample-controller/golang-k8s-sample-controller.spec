%global source0_hash b54bbdfe663d85d74a6a5aeea567f65cb87a46bb72f2fcbfa7f1e9f9e6e2d680
%bcond check 0
%global goipath         k8s.io/sample-controller
%global forgeurl        https://github.com/kubernetes/sample-controller
Version:                1.22.0
%global tag             kubernetes-1.22.0
%global distprefix      %{nil}
%gometa
%global common_description %{expand:
This package implements a simple controller for watching Foo resources as
defined with a CustomResourceDefinition (CRD).}
%global golicenses      LICENSE
%global godocs          docs CONTRIBUTING.md code-of-conduct.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Simple controller for watching Foo resources
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{tag}/sample-controller-%{tag}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

%gobuild -o %{gobuilddir}/bin/sample-controller %{goipath}
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
