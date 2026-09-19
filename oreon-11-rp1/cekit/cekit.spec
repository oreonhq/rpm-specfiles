%global source0_hash dcd7e1f9479b332d9e763bdec428219c735c35d2ab6824d565a9a0a006a9912b

%global modname cekit
%global _description \
CEKit helps to build container images from image definition files

Name:           %{modname}
Version:        4.16.0
Release:        1%{?dist}
Summary:        Container image creation tool
License:        MIT
URL:            https://cekit.io
Source0:        https://github.com/cekit/cekit/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch

Requires:       git

%if 0%{?rhel} && 0%{?rhel} < 8
%global click python36-click
%global jinja python36-jinja2
%global pyyaml python36-PyYAML
%else
%global click python3-click
%global jinja python3-jinja2
%global pyyaml python3-pyyaml

BuildRequires:  python3-colorlog

Requires:       python3-colorlog

%endif

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pykwalify
BuildRequires:  %{pyyaml}
BuildRequires:  %{jinja}

Requires:       %{jinja}
Requires:       python3-setuptools
Requires:       python3-pykwalify
Requires:       %{pyyaml}
Requires:       %{click}
Requires:       python3-packaging

%if 0%{?fedora}
Suggests:       python3-docker
Suggests:       python3-docker-squash
Suggests:       docker
%endif

%description %_description

%package -n %{modname}-bash-completion
Summary:        %{summary}
Requires:       bash-completion
%description -n %{modname}-bash-completion %_description

Bash completion.

%package -n %{modname}-zsh-completion
Summary:        %{summary}
Requires:       zsh
%description -n %{modname}-zsh-completion %_description

ZSH completion.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n cekit-%{version}

%if 0%{?rhel} && 0%{?rhel} < 8
# Remove version requirement for packaging
sed -i 's/^packaging.*$/packaging/' requirements.txt
# Remove requirement for odcs
sed -i 's/^odcs.*$//' requirements.txt
# Remove requirement for colorlog
sed -i 's/^colorlog.*$//' requirements.txt
%endif

%build
%py3_build

%install
mkdir -p %{buildroot}/%{_sysconfdir}/bash_completion.d
cp support/completion/bash/cekit %{buildroot}/%{_sysconfdir}/bash_completion.d/cekit

mkdir -p %{buildroot}/%{_datadir}/zsh/site-functions
cp support/completion/zsh/_cekit %{buildroot}/%{_datadir}/zsh/site-functions/_cekit

%py3_install

%files -n %{modname}-bash-completion
%doc README.rst
%license LICENSE
%{_sysconfdir}/bash_completion.d/cekit

%files -n %{modname}-zsh-completion
%doc README.rst
%license LICENSE
%{_datadir}/zsh/site-functions/_cekit

%files -n %{modname}
%doc README.rst
%license LICENSE

%{python3_sitelib}/cekit/
%{python3_sitelib}/cekit-*.egg-info/

%{_bindir}/cekit
%{_bindir}/cekit-cache

%changelog
%autochangelog
