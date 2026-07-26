%global source0_hash d358803381182a23625b45c450dcc3adf01d6606521f0ccea70dd4650d79bf4d

%global bashcompdir %(pkg-config --variable=completionsdir bash-completion)
%global zshcompdir %{_datadir}/zsh/site-functions

Name: creds
Version: 0.1.0
Release: 18%{?dist}
Summary: Simple encrypted credential management with GPG

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://github.com/joemiller/creds
Source0: https://github.com/joemiller/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: bash-completion

Requires: gnupg2

%description
Simple encrypted credential management with GPG.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Remove shebang from Bash completion file.
sed -i -e '/^#!\//, 1d' completions/bash/_%{name}.sh

%build

%install
# NOTE: creds comes with a Makefile, but the paths therein are hard-coded which
# makes it unsuitable for RPM packaging purposes.
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{name} %{buildroot}%{_bindir}

# Install Bash/Zsh completion files.
mkdir -p %{buildroot}%{bashcompdir}
mv completions/bash/_%{name}.sh %{buildroot}%{bashcompdir}/%{name}
mkdir -p %{buildroot}%{zshcompdir}
mv completions/zsh/_%{name}.sh %{buildroot}%{zshcompdir}/_%{name}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{bashcompdir}/%{name}
# Since Zsh is not a requirement for this package, it must own all the
# directories below %%{_datadir} to avoid unowned directories.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/UnownedDirectories/
%dir %(dirname %{zshcompdir})
%dir %{zshcompdir}
%{zshcompdir}/_%{name}

%changelog
%autochangelog
