%global source0_hash 8451e513da59d878d0c68ee33c5371a850340ac5080b3166c3c43e49573e95b6
%bcond check 0
%global goipath         contrib.go.opencensus.io/resource
%global forgeurl        https://github.com/census-ecosystem/opencensus-go-resource
Version:                0.1.2
%gometa
%global common_description %{expand:
Go packages for auto discovery of resource information in various environments.
The resourcekeys packages defines well-known type and label key strings that are
used by the other packages.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTING.md README.md\\\
                        README-ocdiscover.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go packages for auto discovery of resource information in various environments
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/opencensus-go-resource-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(cloud.google.com/go/compute/metadata)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires:  golang(go.opencensus.io/resource)
BuildRequires:  golang(go.opencensus.io/resource/resourcekeys)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
mv cmd/ocdiscover/README.md README-ocdiscover.md

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
