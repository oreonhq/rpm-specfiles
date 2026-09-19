%global source0_hash 69119ae3e47055edf7dc3418a063484cf57d658c9550e44b1d67a3eacf7b9424

%global forgeurl https://github.com/fedora-infra/koji-fedoramessaging-messages
Version:        1.3.0
%forgemeta

%global srcname koji-fedoramessaging-messages
%global modname koji_fedoramessaging_messages

Name:           python-koji-fedoramessaging-messages
Release:        %autorelease
Summary:        A schema package for koji-fedoramessaging

License:        GPL-3.0-or-later
URL:            https://github.com/fedora-infra/%{srcname}
Source:         %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
A schema package for koji-fedoramessaging, the fedora-messaging
plugin for Koji.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -L %{modname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSES/GPL-3.0-or-later.txt

%changelog
%autochangelog
