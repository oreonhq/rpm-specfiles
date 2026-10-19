%global source0_hash dcd7e1f9479b332d9e763bdec428219c735c35d2ab6824d565a9a0a006a9912b
%global modname cekit
Version:        4.16.0
Release:        1%{?dist}
Summary:        Container image creation tool
License:        MIT
URL:            https://cekit.io
Source0:        https://github.com/cekit/cekit/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch
Requires:       git
%global click python3-click
%global jinja python3-jinja2
%global pyyaml python3-pyyaml
Requires:       python3-colorlog
Requires:       %{jinja}
Requires:       python3-setuptools
Requires:       python3-pykwalify
Requires:       %{pyyaml}
Requires:       %{click}
Requires:       python3-packaging
# oreon:deps
BuildRequires:  python3-colorlog
BuildRequires:  python3-devel
BuildRequires:  python3-jinja2
BuildRequires:  python3-pykwalify
BuildRequires:  python3-pyyaml
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n %{modname}-bash-completion
Summary:        Container image creation tool
Requires:       bash-completion
%description -n %{modname}-bash-completion

Bash completion.

%package -n %{modname}-zsh-completion
Summary:        Container image creation tool
Requires:       zsh
%description -n %{modname}-zsh-completion

ZSH completion.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n cekit-%{version}

%build

%py3_build
%install
mkdir -p %{buildroot}/%{_sysconfdir}/bash_completion.d
cp support/completion/bash/cekit %{buildroot}/%{_sysconfdir}/bash_completion.d/cekit
mkdir -p %{buildroot}/%{_datadir}/zsh/site-functions
cp support/completion/zsh/_cekit %{buildroot}/%{_datadir}/zsh/site-functions/_cekit
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n cekit-bash-completion -f %{oreon_filedir}/cekit-bash-completion.list
%files -n cekit-zsh-completion -f %{oreon_filedir}/cekit-zsh-completion.list

%changelog

%autochangelog
