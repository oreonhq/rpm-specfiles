%global source0_hash 0df7affff21cd87ed298e6a3970ed08a1dd66a6efa676454ee5b091ad503badf

Name:    zsh-autosuggestions
Version: 0.7.1
Release: 4%{?dist}

Summary: Fish-like autosuggestions for zsh
License: MIT
URL:     https://github.com/zsh-users/zsh-autosuggestions
Source0: https://github.com/zsh-users/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: make
BuildRequires: zsh

Requires: zsh

%description
This package provides autosuggestions for the shell zsh. It suggests commands
as you type based on history and completions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
make

%install
install -D --preserve-timestamps --target-directory=%{buildroot}%{_datadir}/%{name} %{name}.zsh

%check

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_datadir}/%{name}

%changelog
%autochangelog
