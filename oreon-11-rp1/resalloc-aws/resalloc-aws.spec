%global source0_hash b5deb739e0848cb3d9539274df72d9ee986ebb32268db27e63319ae2a41ac30c

Name:       resalloc-aws
Summary:    Resource allocator scripts for AWS
Version:    1.10
Release:    2%{?dist}
License:    GPL-2.0-or-later
URL:        https://github.com/praiskup/resalloc-aws
BuildArch:  noarch

Requires:   awscli
Requires:   resalloc-helpers

# Source is created by:
# git clone %%url && cd copr
# tito build --tgz --tag %%name-%%version-%%release
Source0: %{name}-%{version}.tar.gz

%description
When allocating/removing a machine in AWS/EC2 from command-line, there are many
non-trivial options in the 'aws-cli' command.  This project provides a
simplified wrapping command.

The 'resalloc-aws-new' script is able to (a) start a machine, (b) wait till SSH
is available and (c) run a specified playbook.

The 'resalloc-aws-delete' removes a machine started by 'resalloc-aws-new'
script.

These scripts are primarily designed to be used with 'resalloc-server', but they
might be used separately.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 bin/resalloc-aws-new %{buildroot}%{_bindir}
install -p -m 0755 bin/resalloc-aws-delete %{buildroot}%{_bindir}
install -p -m 0755 bin/resalloc-aws-list %{buildroot}%{_bindir}
install -p -m 0755 bin/resalloc-aws-minimal-spot-zone %{buildroot}%{_bindir}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}-delete
%{_bindir}/%{name}-new
%{_bindir}/%{name}-list
%{_bindir}/%{name}-minimal-spot-zone

%changelog
%autochangelog
