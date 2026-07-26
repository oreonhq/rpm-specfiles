%global source0_hash edecbc3db1f0c21935ae38b23d635f27afcab8d058badd749633966757a8c1e0

Name:           opensuse-distro-aliases
Version:        0.2.0
Release:        %autorelease
Summary:        Aliases for active openSUSE releases

License:        MIT
URL:            https://github.com/rpm-software-management/opensuse-distro-aliases
Source:         %{pypi_source opensuse_distro_aliases}
BuildArch:      noarch

BuildRequires:  python3-devel

%generate_buildrequires
%pyproject_buildrequires

%global _description %{expand:
This project provides a list of the currently
maintained openSUSE distributions. It is the openSUSE equivalent of
fedora-distro-aliases.}

%description %_description

%package -n     python3-opensuse-distro-aliases
Summary:        %{summary}

%description -n python3-opensuse-distro-aliases %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n opensuse_distro_aliases-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files opensuse_distro_aliases

%check
%pyproject_check_import -t

%files -n python3-opensuse-distro-aliases -f %{pyproject_files}
%license COPYING
%doc README.rst

%changelog
%autochangelog
