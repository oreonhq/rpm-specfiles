%global source0_hash 58c130106bc5e04eedc5e3e0ae77e0e66435ae2d9c3d497a80b4ecb5922532c7

%global forgeurl https://gitlab.com/fedora/sigs/go/go2rpm
%define tag v%{version}

Name:           go2rpm
Version:        1.19.0
%forgemeta
Release:        %autorelease
Summary:        Convert Go packages to RPM

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
Requires:       askalono-cli
Requires:       compiler(go-compiler)
# Enforce a minimum version of go-vendor-tools
Requires:       (go2rpm+vendor if go-vendor-tools)
# Recommend go2rpm all extra that includes packages needed for the vendor
# profile
Recommends:     go2rpm+all

%description
Convert Go packages to RPM.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup %{forgesetupargs}

%generate_buildrequires
%pyproject_buildrequires -x all,test

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{name}

%check
%pytest -m "not network"

%files  -f %{pyproject_files}
%license LICENSE
%doc README.md
%doc NEWS.md
%{_bindir}/%{name}

%pyproject_extras_subpkg -n go2rpm all vendor

%changelog
%autochangelog
