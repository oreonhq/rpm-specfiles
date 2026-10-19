%global source0_hash b57a2f87312d57ad234d31f1489bf609813a342e4f165436a093b52a9a912259
%bcond check 0
%global goipath         github.com/appc/spec
Version:                0.8.11
%gometa
%global common_description %{expand:
This package contains schema definitions and tools for the App Container (appc)
specification. These include technical details on how an appc image is
downloaded over a network, cryptographically verified, and executed on a host.
See SPEC.md for details of the specification itself.}
%global golicenses      LICENSE
%global godocs          examples CHANGELOG.md CONTRIBUTING.md GUIDE.md\\\
                        POLICY.md README.md SPEC.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        App Container Specification and Tooling
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/spec-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/coreos/go-semver/semver)
BuildRequires:  golang(github.com/google/gofuzz)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(go4.org/errorutil)
BuildRequires:  golang(golang.org/x/net/html)
BuildRequires:  golang(golang.org/x/net/html/atom)
BuildRequires:  golang(gopkg.in/inf.v0)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in ace actool; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
mv %{gobuilddir}/bin/ace %{gobuilddir}/bin/ace-validator
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
