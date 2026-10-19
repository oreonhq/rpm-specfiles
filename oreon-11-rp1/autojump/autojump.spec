%global source0_hash 00daf3698e17ac3ac788d529877c03ee80c3790472a85d0ed063ac3a354c37b1
%global owner wting
Name:           autojump
Version:        22.5.3
Release:        1%{?dist}
Summary:        A fast way to navigate your filesystem from the command line
License:        GPL-3.0-or-later
URL:            https://github.com/%{owner}/%{name}
Source0:        https://github.com/%{owner}/%{name}/archive/release-v%{version}/%{name}-%{version}.tar.gz
Patch0:         remove-homebrew-check.patch
Patch1:         install-add-distribution-arg.patch
Patch2:         use-unittest-mock.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  pandoc
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
# /oreon:deps
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
rm %{buildroot}%{_bindir}/%{name}_argparse.py
mkdir -p %{buildroot}%{python3_sitelib}
mv %{buildroot}%{_bindir}/%{name}_*.py %{buildroot}%{python3_sitelib}/
%oreon_autofiles autojump-zsh usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles autojump-fish usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{__python3} -m pytest tests -vv
%files -f %{oreon_filedir}/main.list
%files -n autojump-zsh -f %{oreon_filedir}/autojump-zsh.list
%files -n autojump-fish -f %{oreon_filedir}/autojump-fish.list

%changelog

%autochangelog
