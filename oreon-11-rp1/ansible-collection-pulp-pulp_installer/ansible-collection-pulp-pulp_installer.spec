%global source0_hash 12fd9c04839fe7df5ba001fccdd51a31f205bcc42648d9dd91f083b91688feb5

%global forgeurl https://github.com/pulp/pulp_installer

Name:           ansible-collection-pulp-pulp_installer
Version:        3.22.1
Release:        9%{?dist}
Summary:        A collection of roles to install or upgrade Pulp 3

License:        GPL-2.0-or-later
URL:            %{ansible_collection_url pulp pulp_installer}
Source0:        %{forgeurl}/archive/%{version}/pulp.pulp_installer-%{version}.tar.gz

# Patch galaxy.yml to exclude unnecessary files from the built collection.
# This is a downstream only patch.
Patch:          build_ignore.patch

BuildArch:      noarch
BuildRequires:  ansible-packaging

%global _description %{expand:
The Pulp 3 Ansible installer is a collection of Ansible roles that you can use
to install or upgrade Pulp 3, or add plugins to an existing installation.

Each Ansible role installs and configures a component of Pulp, or other services
required by Pulp (PostgreSQL, Redis and a webserver.)}

%description %_description

%package doc
Summary:        Documentation for the pulp.pulp_installer collection

%description doc %_description

This is documentation for the pulp.pulp_installer collection.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pulp_installer-%{version}

%build
%ansible_collection_build

%install
%ansible_collection_install

mkdir -p %{buildroot}%{_docdir}/%{name}-doc
# Remove dangling symlinks
cp -p -r --dereference docs %{buildroot}%{_docdir}/%{name}-doc

%files -f %{ansible_collection_filelist}
%license LICENSE COPYRIGHT COMMITMENT
%doc README.md CHANGES

%files doc
%license LICENSE COPYRIGHT COMMITMENT
%doc %{_docdir}/%{name}-doc

%changelog
%autochangelog
