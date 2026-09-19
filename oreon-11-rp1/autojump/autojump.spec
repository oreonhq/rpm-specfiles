%global source0_hash 00daf3698e17ac3ac788d529877c03ee80c3790472a85d0ed063ac3a354c37b1

%global owner wting

Name:           autojump
Version:        22.5.3
Release:        26%{?dist}

Summary:        A fast way to navigate your filesystem from the command line

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/%{owner}/%{name}
Source:         https://github.com/%{owner}/%{name}/archive/release-v%{version}/%{name}-%{version}.tar.gz
Patch0:         remove-homebrew-check.patch
Patch1:         install-add-distribution-arg.patch
Patch2:         use-unittest-mock.patch

BuildArch:      noarch

BuildRequires:  pandoc
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  make

%description
autojump is a faster way to navigate your filesystem. It works by maintaining 
a database of the directories you use the most from the command line.

%package zsh
Requires:       %{name} = %{version}-%{release}
Summary:        Autojump for zsh

%description zsh
autojump is a faster way to navigate your filesystem. It works by maintaining 
a database of the directories you use the most from the command line.
autojump-zsh is designed to work with zsh.

%package fish
Requires:       %{name} = %{version}-%{release}
Summary:        Autojump for fish shell

%description fish
autojump is a faster way to navigate your filesystem. It works by maintaining 
a database of the directories you use the most from the command line.
autojump-fish is designed to work with fish shell.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-release-v%{version}

# Use system argparse
sed -i 's|autojump_argparse|argparse|' bin/%{name}
# Fix shebangs, non .py files need to be specified manually, so we provide bin/* as well as .
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python3} -pn . ./bin/*
sed -i '1{/^#!/d}' bin/%{name}_*.py

%build
make docs

%install
./install.py --destdir %{buildroot} --prefix usr --zshshare %{buildroot}%{_datadir}/zsh/site-functions --distribution
# Do not need bundled modules
rm %{buildroot}%{_bindir}/%{name}_argparse.py
# Move modules to proper directory
mkdir -p %{buildroot}%{python3_sitelib}
mv %{buildroot}%{_bindir}/%{name}_*.py %{buildroot}%{python3_sitelib}/

%check
%{__python3} -m pytest tests -vv

%files
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{name}
%{python3_sitelib}/%{name}_data.py
%{python3_sitelib}/%{name}_match.py
%{python3_sitelib}/%{name}_utils.py
%{python3_sitelib}/__pycache__/%{name}*.pyc
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/icon.png
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh
%config(noreplace) %{_datadir}/%{name}/%{name}.bash

%files zsh
%config(noreplace) %{_datadir}/%{name}/%{name}.zsh
%{_datadir}/zsh/site-functions/_j

%files fish
%config(noreplace) %{_datadir}/%{name}/%{name}.fish

%changelog
%autochangelog
