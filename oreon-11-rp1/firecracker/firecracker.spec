%global source0_hash 72ec81313225dd9ec3011379d9868dc68cb3de59e70c13d6e4d3a90553cb09ef

# The RPM macro cargo_target can be defined to specify the Rust target to use
# during the build.  When undefined, the distro's default target is used.

# Disable tests by default since VMs can't run in containerized Fedora builds.
%bcond check    0

# The cpu-template-helper program only supports aarch64 and x86_64 CPUs.
%bcond cth      %{lua:print(("ax"):find(rpm.expand("%{_target_cpu}"):sub(1,1)) or 0)}

# The jailer's documentation says only musl targets are supported.
%bcond jailer   %{lua:print(rpm.expand("%{?cargo_target}"):find("musl") or 0)}

Name:           firecracker
Version:        1.13.1
Release:        2%{?dist}

Summary:        Secure and fast microVMs for serverless computing
SourceLicense:  Apache-2.0
License:        Apache-2.0 AND (Apache-2.0 OR BSD-2-Clause OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-3-Clause AND MIT AND (MIT OR Unlicense) AND Unicode-3.0 AND Unicode-DFS-2016
URL:            https://firecracker-microvm.github.io/

Source0:        https://github.com/firecracker-microvm/firecracker/archive/v%{version}/%{name}-%{version}.tar.gz

# Bundle forked versions of existing crates to avoid conflicts with upstreams.
Source1:        https://github.com/firecracker-microvm/micro-http/archive/98d85677ba603d16c40103c09059b54c38d71825/micro_http-98d8567.tar.gz
Provides:       bundled(crate(micro_http)) = 0.1.0^git98d8567

# Edit crate dependencies to track what is packaged in Fedora.
Patch:          %{name}-1.13.1-remove-aws-lc-rs.patch
Patch:          %{name}-1.13.0-remove-criterion.patch
Patch:          %{name}-1.13.0-remove-device_tree.patch

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  libseccomp-devel
%if %{defined cargo_target}
BuildRequires:  rust-std-static-%{cargo_target}
%endif

ExclusiveArch:  aarch64 x86_64

%description
Firecracker is an open source virtualization technology that is purpose-built
for creating and managing secure, multi-tenant container and function-based
services that provide serverless operational models.  Firecracker runs
workloads in lightweight virtual machines, called microVMs, which combine the
security and isolation properties provided by hardware virtualization
technology with the speed and flexibility of containers.
%{!?with_jailer:
This package does not include all of the security features of an official
release.  It is not production ready without additional sandboxing.}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
mkdir forks
tar --transform='s,^[^/]*,micro_http,' -C forks -xzf %{SOURCE1}
sed -i -e 's,^\(micro_http\) = .*,\1 = { path = "../../forks/\1" },' src/*/Cargo.toml
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build -- --package={%{?with_cth:cpu-template-helper,}firecracker,%{?with_jailer:jailer,}rebase-snap,seccompiler,snapshot-editor} %{?cargo_target:--target=%{cargo_target}}
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies

%install
install -pm 0755 -Dt %{buildroot}%{_bindir} target/%{?cargo_target}/rpm/{%{?with_cth:cpu-template-helper,}firecracker,%{?with_jailer:jailer,}rebase-snap,seccompiler-bin,snapshot-editor}

# Ship the built-in seccomp JSON as an example that can be edited and compiled.
ln -fn resources/seccomp/%{cargo_target}.json seccomp-filter.json ||
ln -fn resources/seccomp/unimplemented.json seccomp-filter.json

# Prune unused images from the documentation directory prior to installation.
for image in docs/images/*
do grep --exclude-dir=images -FIqre "${image##*/}" docs *.md || rm -f "$image"
done

%if %{with check}
%check
%cargo_test -- %{!?with_cth:--exclude=cpu-template-helper} %{!?with_jailer:--exclude=jailer} %{?cargo_target:--target=%{cargo_target}} --workspace
%endif

%files
%{?with_cth:%{_bindir}/cpu-template-helper}
%{_bindir}/firecracker
%{?with_jailer:%{_bindir}/jailer}
%{_bindir}/rebase-snap
%{_bindir}/seccompiler-bin
%{_bindir}/snapshot-editor
%doc seccomp-filter.json
%doc src/firecracker/swagger/firecracker.yaml
%doc docs CHANGELOG.md CHARTER.md CODE_OF_CONDUCT.md CONTRIBUTING.md CREDITS.md FAQ.md MAINTAINERS.md README.md SECURITY.md SPECIFICATION.md
%license LICENSE LICENSE.dependencies NOTICE THIRD-PARTY

%changelog
%autochangelog
