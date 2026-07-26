%global source0_hash 79bbfa745d1901d685973584bd2d16a350686ddd176f6a2244490fb01996441f

%global srcname borgbackup

Name:           %{srcname}
Version:        1.4.3
Release:        3%{?dist}
Summary:        A deduplicating backup program with compression and authenticated encryption
# zlib:         src/borg/algorithms/{crc32_clmul.c, crc32_slice_by_8.c}
# Apache-2.0:   src/borg/cache_sync/{sysdep.h, unpack.h, unpack_template.h, unpack_define.h}
# PSF-2.0:      src/borg/shellpattern.py
License:        BSD-3-clause AND zlib AND Apache-2.0 AND PSF-2.0

URL:            https://borgbackup.readthedocs.org
Source0:        https://github.com/borgbackup/borg/releases/download/%{version}/borgbackup-%{version}.tar.gz
Source1:        https://github.com/borgbackup/borg/releases/download/%{version}/borgbackup-%{version}.tar.gz.asc
# upstream publishes only key ids:
#    https://borgbackup.readthedocs.io/en/stable/support.html#verifying-signed-releases
# gpg2 --export --export-options export-minimal "6D5B EF9A DD20 7580 5747 B70F 9F88 FB52 FAF7 B393" > gpgkey-6D5B_EF9A_DD20_7580_5747_B70F_9F88_FB52_FAF7_B393.gpg
Source2:        gpgkey-6D5B_EF9A_DD20_7580_5747_B70F_9F88_FB52_FAF7_B393.gpg

# we don't need the guzzley_sphinx theme for only man page generation
Patch1:         borgbackup-disable-guzzle-theme.patch

BuildRequires:  gnupg2
# build
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-pkgconfig

# test
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)

# doc
BuildRequires:  python3-sphinx
BuildRequires:  python3dist(sphinxcontrib-jquery)

# no python deps
BuildRequires:  gcc
BuildRequires:  openssl-devel >= 1.0.2
BuildRequires:  fuse-devel
BuildRequires:  make
BuildRequires:  libacl-devel
# versions required in "setup_checksums.py"
BuildRequires:  lz4-devel >= 1.7.0
BuildRequires:  libzstd-devel >= 1.3.0
BuildRequires:  xxhash-devel >= 0.7.3

# msgpack dependency is detected automatically
Requires:       python3-llfuse >= 1.3.8
Requires:       fuse

%description
BorgBackup (short: Borg) is a deduplicating backup program. Optionally, it
supports compression and authenticated encryption.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
rm -rf %{srcname}.egg-info

# remove copies of bundled libraries to ensure these don't end up in our
# binaries
rm -rf src/borg/algorithms/{lz4,xxh64,zstd}
# remove precompiled Cython code to ensure we always built "from source"
find src/ -name '*.pyx' | sed -e 's/.pyx/.c/g' | xargs rm -f

# https://bugzilla.redhat.com/show_bug.cgi?id=1630992
sed -i 's/msgpack-python/msgpack/' setup.py

%generate_buildrequires
%pyproject_buildrequires -x fuse

%build
%pyproject_wheel

# MANPAGE GENERATION
# workaround to dump sphinx_rtd_theme dependency - not needed for manpages
export READTHEDOCS=True

# workaround to include borg module for usage generation
export PYTHONPATH=$(pwd)/build/$(ls build/ | grep 'lib.')

make -C docs SPHINXBUILD=sphinx-build-%python3_version man

%install
find . -name *.so -type f -exec chmod 0755 {} \;

%pyproject_install
install -D -m 0644 docs/_build/man/borg*.1* %{buildroot}%{_mandir}/man1/borg.1

# add shell completions
#%define bash_compdir %(pkg-config --variable=completionsdir bash-completion)
%define bash_compdir %{_prefix}/share/bash-completion/completions
%define zsh_compdir %{_prefix}/share/zsh/site-functions
%define fish_compdir %{_prefix}/share/fish/completions

install -d  %{buildroot}%{bash_compdir}
install -d  %{buildroot}%{zsh_compdir}
install -d  %{buildroot}%{fish_compdir}

install -D -m 0644 scripts/shell_completions/bash/* %{buildroot}%{bash_compdir}
install -D -m 0644 scripts/shell_completions/zsh/* %{buildroot}%{zsh_compdir}
install -D -m 0644 scripts/shell_completions/fish/* %{buildroot}%{fish_compdir}

%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}

cd $PYTHONPATH
# exclude test_fuse: there is no modprobe in mock for fuse
# test_readonly_mount: needs fuse mount
# exclude benchmark: not relevant for package build
TEST_SELECTOR="not test_fuse and not test_readonly_mount and not benchmark"
%pytest -n auto -x -vk "$TEST_SELECTOR" borg/testsuite/*.py

%files
%license LICENSE
%doc README.rst AUTHORS
%doc docs/changes.rst
%{_mandir}/man1/*

%{python3_sitearch}/borg
%{python3_sitearch}/borgbackup-%{version}.dist-info
# - files in %%{python3_sitearch}/borg/algorithms/msgpack are licensed under the ASL
# - %%{python3_sitearch}/borg/algorithms/checksums.*.so contains code licensed
#   under the zlib license
%{_bindir}/borg
%{_bindir}/borgfs
%{_prefix}/share/bash-completion/completions/*
%{_prefix}/share/zsh/site-functions/*
%{_prefix}/share/fish/completions/*
# left-overs from testing
%exclude %{python3_sitearch}/.pytest_cache

%changelog
%autochangelog
