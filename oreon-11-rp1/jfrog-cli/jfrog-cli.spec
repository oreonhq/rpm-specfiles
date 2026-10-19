%global source0_hash 56c7a2b12d4f4f506962c10ba5f0e437875d2fb7f873d0a41272d7d7a5180827
%bcond check 1
%global goipath         github.com/jfrog/jfrog-cli
Version:                2.87.0
%gometa -L -f
Name:           jfrog-cli
Release:        1%{?dist}
Summary:        CLI to automate access to JFrog products
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND LicenseRef-Fedora-Public-Domain AND MIT AND MPL-2.0 AND Unlicense
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description
JFrog CLI is a client that provides a simple interface that automates access to
the JFrog products.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1
# these tests require access to Artifactory instance
rm -v \
  access_test.go \
  artifactorybulkrepository_test.go \
  artifactory_test.go \
  buildinfo_test.go \
  distribution_test.go \
  docker_test.go \
  evidence_test.go \
  go_test.go \
  gradle_test.go \
  helm_test.go \
  ide_test.go \
  lifecycle_test.go \
  main_test.go \
  maven_test.go \
  npm_test.go \
  nuget_test.go \
  pipenv_test.go \
  pip_test.go \
  plugins_test.go \
  poetry_test.go \
  transfer_test.go \

%build

%global gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/jf %{goipath}
%{gobuilddir}/bin/jf completion bash > jf.bash
%{gobuilddir}/bin/jf completion fish > jf.fish
%{gobuilddir}/bin/jf completion zsh  > jf.zsh
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm 0644 jf.bash %{buildroot}%{bash_completions_dir}/jf
install -Dpm 0644 jf.fish %{buildroot}%{fish_completions_dir}/jf.fish
install -Dpm 0644 jf.zsh  %{buildroot}%{zsh_completions_dir}/_jf
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
