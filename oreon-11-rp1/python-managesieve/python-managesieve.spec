%global source0_hash 47293d32ac8a8a6346a829a2badf25d12464fd71598ca572eaadde25184e9359

%global pypi_name managesieve

# Pull from GitLab (prerequisite for Packit)
%global forgeurl https://gitlab.com/htgoebel/managesieve

Name:           python-%{pypi_name}
Version:        0.7.1
Release:        %autorelease
Summary:        Accessing a Sieve-Server for managing Sieve scripts
%global tag v%{version}
%forgemeta
License:        PSF-2.0 AND GPL-3.0-only
URL:            https://managesieve.readthedocs.io/
Source0:        %forgesource
# ssl.wrap_socket is deprecated and Python 3.12 removed it entirely
# https://gitlab.com/htgoebel/managesieve/-/issues/8
Patch:          fix_ssl_wrap_socket_error.patch
BuildArch:      noarch

BuildRequires:  python3-devel, git-core
BuildRequires:  python3-pytest
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description
This module allows accessing a Sieve-Server for managing Sieve scripts there.
It is accompanied by a simple yet functional user application ‘sieveshell’.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
# Package `cyrus-imapd-utils` also provides /usr/bin/sieveshell
# However `python-managesieve` provided a Python script installed at
# /usr/bin/sieveshell from its inception when version 0.6 was packaged
# in 2020. Upstream's HISTORY file documents it being present since 0.2
# released in 2004. Clearly this has been missed during package review.
# https://bugzilla.redhat.com/show_bug.cgi?id=2228002
Conflicts:      cyrus-imapd-utils

%description -n python3-%{pypi_name}
This module allows accessing a Sieve-Server for managing Sieve scripts there.
It is accompanied by a simple yet functional user application ‘sieveshell’.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1 -S git

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files managesieve

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.txt HISTORY
%{_bindir}/sieveshell

%changelog
%autochangelog
