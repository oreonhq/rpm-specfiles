%global source0_hash b0f4bf293148b365569c73e34e5d2f6b6dc682875a137bb89768735f55800d20

%global srcname virt-lightning
%global libname virt_lightning

%global common_description %{expand:
A CLI to start local Cloud image on libvirt!

Virt-Lightning can quickly deploy a bunch of new VM. It also prepares the
Ansible inventory file!

This is handy to quickly validate a new Ansible playbook, or a role on a large
number of environments.}

Name:           %{srcname}
Version:        2.3.2
Release:        %autorelease
Summary:        CLI to start Cloud image on libvirt

License:        Apache-2.0
URL:            https://virt-lightning.org
VCS:            https://github.com/virt-lightning/virt-lightning
Source0:        %{pypi_source virt-lightning}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
Requires:       libvirt-daemon

%description %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{libname}

%check
%pytest

%files -f %{pyproject_files}
%license LICENSE-2.0.txt
%doc README.md changelog.md conf/example.ini
%{_bindir}/virt-lightning
%{_bindir}/vl

%changelog
%autochangelog
