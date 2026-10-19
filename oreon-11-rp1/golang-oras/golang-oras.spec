%global source0_hash 09436b3048aab42fdfd5662f71da7d211f9d6e7ce66740cbbd8f3695ae621f6a
%bcond check 1
%bcond bootstrap 0
%if %{with bootstrap}
%global debug_package %{nil}
%endif
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         oras.land/oras
%global forgeurl        https://github.com/oras-project/oras
Version:                1.2.2
%gometa -L -f
%global common_description %{expand:
Work with OCI registries, but for secure supply chain - managing content like
artifacts, images, SBOM.}
%global golicenses      LICENSE
%global godocs          docs CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        MAINTAINERS.md OWNERS.md README.md SECURITY.md
Name:           golang-oras
Release:        1%{?dist}
Summary:        OCI registry client - managing content like artifacts, images, packages
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/oras-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(oras.land/oras-go/v2)
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

# Remove e2e tests
rm -rf test/e2e

%if %{without bootstrap}
%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%endif
%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%endif
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%if %{without bootstrap}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
