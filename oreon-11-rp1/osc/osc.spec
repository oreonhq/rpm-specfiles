%global source0_hash 72e90ff3d278fc072f640223cf911635eed58c7ecbac4da722205a0ebf83ddf0
%global obsrel 473.3
%global osc_plugin_dir %{_prefix}/lib/osc-plugins
%global obsroot %{_prefix}/lib/obs
%global obs_srcsvc_dir %{obsroot}/service
%global baserelease 1
Name:           osc
Summary:        Open Build Service Commander
Version:        1.27.3
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/%{name}
Source0:        https://github.com/openSUSE/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-distro
Requires:       python3-rpm
Requires:       python3-cryptography
Requires:       python3-urllib3
Requires:       python3-lxml
Requires:       python3-progressbar2
Recommends:     /usr/bin/ssh-keygen
Requires:       obs-service-source_validator
Conflicts:      obs-build < 20191205
# oreon:deps
BuildRequires:  argparse-manpage
BuildRequires:  diffstat
BuildRequires:  git-core
BuildRequires:  python3-cryptography
BuildRequires:  python3-devel
BuildRequires:  python3-distro
BuildRequires:  python3-pip
BuildRequires:  python3-progressbar2
BuildRequires:  python3-rpm
BuildRequires:  python3-ruamel-yaml
BuildRequires:  python3-setuptools
BuildRequires:  python3-urllib3
# /oreon:deps
%description
Commandline client for the Open Build Service.

See http://en.opensuse.org/openSUSE:OSC , as well as
http://en.opensuse.org/openSUSE:Build_Service_Tutorial for a general
introduction.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%py3_build
cat << EOF > macros.osc
%%osc_plugin_dir %{osc_plugin_dir}
EOF
PYTHONPATH=. argparse-manpage \
    --output=osc.1 \
    --format=single-commands-section \
    --module=osc.commandline \
    --function=argparse_manpage_get_parser \
    --project-name=osc \
    --prog=osc \
    --description="Command-line client for Open Build Service" \
    --author="Contributors to the osc project. See the project's GIT history for the complete list." \
    --url="https://github.com/openSUSE/osc/"
PYTHONPATH=. argparse-manpage \
    --output=git-obs.1 \
    --format=single-commands-section \
    --module=osc.commandline_git \
    --function=argparse_manpage_get_parser \
    --project-name=osc \
    --prog=git-obs \
    --description="Git based command-line client for Open Build Service" \
    --author="Contributors to the osc project. See the project's GIT history for the complete list." \
    --url="https://github.com/openSUSE/osc/"
%install
%py3_install
mkdir -p %{buildroot}%{_localstatedir}/lib/osc-plugins
install -Dm0644 contrib/complete.csh %{buildroot}%{_sysconfdir}/profile.d/osc.csh
install -Dm0644 contrib/git-obs-complete.zsh %{buildroot}%{zsh_completions_dir}/git-obs.zsh
install -Dm0644 contrib/complete.sh %{buildroot}%{bash_completions_dir}/osc
install -Dm0644 contrib/git-obs-complete.bash %{buildroot}%{bash_completions_dir}/git-obs.bash
install -Dm0755 contrib/osc.complete %{buildroot}%{_datadir}/osc/complete
install -Dm0644 contrib/osc.fish %{buildroot}%{fish_completions_dir}/osc.fish
install -Dm0644 contrib/git-obs-complete.fish %{buildroot}%{fish_completions_dir}/git-obs.fish
mkdir -p %{buildroot}%{_libexecdir}/git
ln -s %{_bindir}/git-obs %{buildroot}%{_libexecdir}/git/obs
mkdir -p %{buildroot}%{obs_srcsvc_dir}
mkdir -p %{buildroot}%{osc_plugin_dir}
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
install -Dm0644 macros.osc %{buildroot}%{_rpmmacrodir}/macros.osc
install -Dm0644 osc.1 %{buildroot}%{_mandir}/man1/osc.1
install -Dm0644 git-obs.1 %{buildroot}%{_mandir}/man1/git-obs.1
sed -i '3i # PYTHON_ARGCOMPLETE_OK'  %{buildroot}%{_bindir}/git-obs
%oreon_autofiles main

%check

python3 -m unittest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
