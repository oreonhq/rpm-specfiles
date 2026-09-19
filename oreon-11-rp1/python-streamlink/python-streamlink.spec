%global source0_hash afa26582cabf343f49733d79e2bc9a5bbe90aec7dbb246ec5f97796499c637ee

%global srcname streamlink
%global _description %{expand:Streamlink is a command-line utility that pipes video streams from various
services into a video player, such as VLC. The main purpose of Streamlink is to
allow the user to avoid buggy and CPU heavy flash plugins but still be able to
enjoy various streamed content. There is also an API available for developers
who want access to the video stream data. This project was forked from
Livestreamer, which is no longer maintained.}

Name:           python-%{srcname}
Version:        8.2.1
Release:        2%{?dist}
Summary:        Python library for extracting streams from various websites

# src/streamlink/packages/requests_file.py is Apache-2.0
License:        BSD-2-Clause AND Apache-2.0
URL:            https://streamlink.github.io
Source0:        %{pypi_source %{srcname}}
# Fix documentation build
Patch0:         %{name}-8.1.0-documentation.patch
# Fix tests with pytest < 8.4.0
Patch1:         %{name}-8.1.0-pytest_8.3.patch
BuildRequires:  make
BuildRequires:  python3-devel
# For easy patching of pyproject.toml
BuildRequires:  tomcli
BuildArch:      noarch

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
Provides:       %{srcname} = %{version}-%{release}
# src/streamlink/packages/requests_file.py is a bundled copy of
# https://pypi.org/project/requests-file/, but it seems to have been forked;
# the contents do not correspond exactly to any version from 1.0 to 1.5.1
Provides:       bundled(python3dist(requests-file))
Obsoletes:      %{name}-doc < 6.7.0-1
Recommends:     /usr/bin/ffmpeg

%description -n python3-%{srcname}
%{_description}

%package bash-completion
Summary:        Bash completion for %{srcname}
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
Bash command line completion support for %{srcname}.

%package zsh-completion
Summary:        Zsh completion for %{srcname}
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
Supplements:    (%{name} and zsh)

%description zsh-completion
Zsh command line completion support for %{srcname}.

%pyproject_extras_subpkg -n %{name} decompress

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}
%patch -P0 -p0 -b .documentation
%if 0%{?fedora} <= 43
%patch -P1 -p0 -b .pytest_8.3
%endif

# Replace pycryptodome dependency with pycryptodomex
tomcli set pyproject.toml arrays replace "project.dependencies" "(pycryptodome)(\s*[><=]+.*)" "\1x\2"

# Drop useless dependencies (only needed for building the HTML documentation)
tomcli set pyproject.toml arrays delitem "dependency-groups.docs" "furo\s*[><=]+.*"

%if 0%{?fedora} < 43
# Drop version constraint on setuptools
tomcli set pyproject.toml arrays replace "build-system.requires" "(setuptools)\s*[><=]+.*" "\1"
tomcli set pyproject.toml arrays replace "dependency-groups.dev" "(setuptools)\s*[><=]+.*" "\1"

# setuptools < 77.0.3 doesn't support PEP 639
tomcli set pyproject.toml del "project.license" "project.license-files"
%endif

%generate_buildrequires
%pyproject_buildrequires -g test -g build -g docs

%build
%pyproject_wheel

# Generate man pages
PYTHONPATH=$PWD/src %make_build -C docs/ man SPHINXOPTS=-j%{?_smp_build_ncpus}

# Generate shell completion files
PYTHONPATH=$PWD/src ./script/build-shell-completions.sh

%install
%pyproject_install
%pyproject_save_files %{srcname} %{srcname}_cli

# Install man page
install -Dpm 0644 docs/_build/man/%{srcname}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{srcname}.1

# Install shell completion files
install -Dpm 0644 -t $RPM_BUILD_ROOT%{bash_completions_dir} completions/bash/%{srcname}
install -Dpm 0644 -t $RPM_BUILD_ROOT%{zsh_completions_dir} completions/zsh/_%{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/%{srcname}
%{_mandir}/man1/%{srcname}.1.*

%files bash-completion
%{_datadir}/bash-completion/completions/%{srcname}

%files zsh-completion
%{_datadir}/zsh/site-functions/_%{srcname}

%changelog
%autochangelog
