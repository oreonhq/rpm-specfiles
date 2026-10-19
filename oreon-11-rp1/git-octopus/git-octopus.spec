%global source0_hash bc3945553e060e0b1bd7b5356c2a47c13eb47db4648b1da39aab594071be18df
%global with_bundled 0
%global debug_package %{nil}
%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%endif
%global provider        github
%global provider_tld    com
%global project         lesfurets
%global repo            git-octopus
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global pre_rel         beta.3
Name:           git-octopus
Version:        2.0
Release:        1%{?dist}
Summary:        Git commands for continuous delivery
License:        LGPL-3.0-only
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/v%{version}-%{pre_rel}/%{name}-%{version}-%{pre_rel}.tar.gz
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
Requires:   git >= 1.8
Requires:   %{_bindir}/shasum
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  compiler(go-compiler)
BuildRequires:  golang
BuildRequires:  make
# /oreon:deps
%description
The continuous merge workflow is meant for continuous integration/delivery and
is based on feature branching. git-octopus provides git commands to implement
it.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}%{?pre_rel:-%pre_rel}

%build

mkdir -p src/%{provider}.%{provider_tld}/%{project}
ln -s ../../../ src/%{import_path}
export GOPATH=$(pwd):%{gopath}
make %{?_smp_mflags} build-docs 
%gobuild -o bin/git-octopus %{import_path}/
%install
install -d -p %{buildroot}%{_bindir}
install -p -v -m 0755 bin/git-octopus %{buildroot}%{_bindir}
make prefix="%{buildroot}%{_prefix}" \
              docdir="%{buildroot}%{_docdir}/%{name}%{?el7:-%{version}}" install-docs
%oreon_autofiles main

%check

%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
ln -s ./ ./vendor/src # ./vendor/src -> ./vendor
export GOPATH=%{buildroot}/%{gopath}:$(pwd)/vendor:%{gopath}
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
