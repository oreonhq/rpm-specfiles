%global source0_hash 4c7b8b3e78124e1005c9f221a2123b6ec02f3942d2be10f79fe3a5c96a52a96c

%global pkgname click-completion

Name:           python-click-completion
Version:        0.5.2
Release:        22%{?dist}
Summary:        Add automatic completion support for fish, Zsh, Bash and PowerShell to Click
License:        MIT
URL:            https://github.com/click-contrib/click-completion
Source0:        %{url}/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%{?python_enable_dependency_generator}

%description
Enhanced completion for Click

Add automatic completion support for fish, Zsh, Bash and PowerShell to Click.

All the supported shells are able to complete all the command line arguments
and options defined with click. In addition, fish and Zsh are also displaying
the options and commands help during the completion.

%package     -n python3-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}
%description -n python3-%{pkgname}
Enhanced completion for Click

Add automatic completion support for fish, Zsh, Bash and PowerShell to Click.

All the supported shells are able to complete all the command line arguments
and options defined with click. In addition, fish and Zsh are also displaying
the options and commands help during the completion.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkgname}-%{version}
sed -i 's|^#!/usr/bin/env python||' click_completion/__init__.py
sed -i 's|^#!/usr/bin/env python||' examples/click-completion-*
chmod -x examples/click-completion-*

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-%{pkgname}
%license LICENSE
%doc examples README.md
%{python3_sitelib}/click_completion*/

%changelog
%autochangelog
