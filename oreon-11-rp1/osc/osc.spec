%global source0_hash d652eab574785cda0a12b84ef76f36f9554ec1fedacbd46edee08085b5a37e07

# SUSE guys use OBS to automatically handle release numbers,
# when rebasing check what they are using on
# https://download.opensuse.org/repositories/openSUSE:/Tools/Fedora_Rawhide/src/
# update the obsrel to match the upstream release number
%global obsrel 473.3

# osc plugin support
%global osc_plugin_dir %{_prefix}/lib/osc-plugins

# for obs source services
%global obsroot %{_prefix}/lib/obs
%global obs_srcsvc_dir %{obsroot}/service

# Real release number
%global baserelease 1

Name:           osc
Summary:        Open Build Service Commander
Version:        1.25.0
# Bump the release as necessary to ensure we're one level up from upstream
Release:        %{obsrel}.%{baserelease}%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/%{name}
Source:         %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  diffstat
BuildRequires:  python3-devel
BuildRequires:  python3-distro
BuildRequires:  python3-rpm
BuildRequires:  python3-progressbar2
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-cryptography
BuildRequires:  python3-urllib3
BuildRequires:  python3-ruamel-yaml
BuildRequires:  argparse-manpage
# needed for git scm tests
BuildRequires:  git-core
Requires:       python3-distro
Requires:       python3-rpm
Requires:       python3-cryptography
Requires:       python3-urllib3
Requires:       python3-lxml
Requires:       python3-progressbar2
# for MFA via ssh
Recommends:     /usr/bin/ssh-keygen

%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     obs-build
Recommends:     obs-service-source_validator
%else
Requires:       obs-service-source_validator
%endif

# To ensure functional parity
Conflicts:      obs-build < 20191205

%description
Commandline client for the Open Build Service.

See http://en.opensuse.org/openSUSE:OSC , as well as
http://en.opensuse.org/openSUSE:Build_Service_Tutorial for a general
introduction.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%if 0%{?fedora} > 41
%pyproject_wheel
%else
%py3_build
%endif
# write rpm macros
cat << EOF > macros.osc
%%osc_plugin_dir %{osc_plugin_dir}
EOF

# build man page
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
%if 0%{?fedora} > 41
%pyproject_install
%else
%py3_install
%endif

mkdir -p %{buildroot}%{_localstatedir}/lib/osc-plugins

install -Dm0644 contrib/complete.csh %{buildroot}%{_sysconfdir}/profile.d/osc.csh
install -Dm0644 contrib/git-obs-complete.zsh %{buildroot}%{zsh_completions_dir}/git-obs.zsh

install -Dm0644 contrib/complete.sh %{buildroot}%{bash_completions_dir}/osc
install -Dm0644 contrib/git-obs-complete.bash %{buildroot}%{bash_completions_dir}/git-obs.bash

install -Dm0755 contrib/osc.complete %{buildroot}%{_datadir}/osc/complete

install -Dm0644 contrib/osc.fish %{buildroot}%{fish_completions_dir}/osc.fish
install -Dm0644 contrib/git-obs-complete.fish %{buildroot}%{fish_completions_dir}/git-obs.fish

# symlink /usr/bin/git-obs to /usr/libexec/git/obs
mkdir -p %{buildroot}%{_libexecdir}/git
ln -s %{_bindir}/git-obs %{buildroot}%{_libexecdir}/git/obs

mkdir -p %{buildroot}%{obs_srcsvc_dir}

mkdir -p %{buildroot}%{osc_plugin_dir}

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/

# install rpm macros
install -Dm0644 macros.osc %{buildroot}%{_rpmmacrodir}/macros.osc

# install man page
install -Dm0644 osc.1 %{buildroot}%{_mandir}/man1/osc.1
install -Dm0644 git-obs.1 %{buildroot}%{_mandir}/man1/git-obs.1

# inject argcomplete marker to the generated git-obs executable
sed -i '3i # PYTHON_ARGCOMPLETE_OK'  %{buildroot}%{_bindir}/git-obs

%check
python3 -m unittest

%files
%doc AUTHORS README.md NEWS
%license COPYING
%{_bindir}/osc*
%{_bindir}/git-obs
%{_bindir}/git-osc-precommit-hook
%{_libexecdir}/git/obs
%{python3_sitelib}/osc*
%{_sysconfdir}/profile.d/osc.csh
%{zsh_completions_dir}/git-obs.zsh
%{bash_completions_dir}/osc
%{bash_completions_dir}/git-obs.bash
%{fish_completions_dir}/osc.fish
%{fish_completions_dir}/git-obs.fish
%dir %{_localstatedir}/lib/osc-plugins
%{_mandir}/man1/osc.*
%{_mandir}/man1/git-obs.*
%{_datadir}/osc
%{_rpmconfigdir}/macros.d/macros.osc
%dir %{obsroot}
%dir %{obs_srcsvc_dir}
%dir %{osc_plugin_dir}

%changelog
%autochangelog
