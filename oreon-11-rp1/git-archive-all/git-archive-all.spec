%global source0_hash 0c440d15be18e336672549231510fa3c66d0cb95069a5e4800fdd876ab6814df

%global modname %(n=%{name}; echo ${n//-/_})

Name:           git-archive-all
Version:        1.23.1
Release:        15%{?dist}
Summary:        Archive git repository with its submodules

License:        MIT
URL:            https://github.com/Kentzo/git-archive-all
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
# git-submodule is in git, not in git-core
Requires:       git

BuildArch:      noarch

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/%{name}

%changelog
%autochangelog
