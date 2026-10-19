%global source1_hash 75cf208271938054bdef8c6620656c35bee598e59c69a466d5b4c6a00d074f20
%global source0_hash 4f9a5fe584c504b15485841236750dea16aa7cd2ddbc4a594e9d2ce5c49c4508
%global srcname borgbackup
Name:           %{srcname}
Version:        1.4.5
Release:        1%{?dist}
Summary:        A deduplicating backup program with compression and authenticated encryption
License:        BSD-3-clause AND zlib AND Apache-2.0 AND PSF-2.0
URL:            https://borgbackup.readthedocs.org
Source0:        https://github.com/borgbackup/borg/releases/download/%{version}/borgbackup-%{version}.tar.gz
Source1:        https://github.com/borgbackup/borg/releases/download/%{version}/borgbackup-%{version}.tar.gz.asc
Source2:        gpgkey-6D5B_EF9A_DD20_7580_5747_B70F_9F88_FB52_FAF7_B393.gpg
Patch1:         borgbackup-disable-guzzle-theme.patch
Requires:       python3-llfuse >= 1.3.8
Requires:       fuse
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(Cython) >= 3.0.3
BuildRequires:  python3dist(setuptools) >= 78.1.1
BuildRequires:  python3dist(setuptools_scm) >= 8
Requires:       python3-borgbackup = %{version}-%{release}
# /oreon:deps
%package -n       python3-borgbackup+llfuse
Summary:        Metapackage for python3-borgbackup llfuse extras
Requires:       python3-borgbackup = %{version}-%{release}
Requires:       python3dist(llfuse) >= 1.3.8
Provides:       python3dist(borgbackup[llfuse]) = %{version}-%{release}

%description -n python3-borgbackup+llfuse
Metapackage for python3-borgbackup llfuse extras.

%package -n       python3-borgbackup+pyfuse3
Summary:        Metapackage for python3-borgbackup pyfuse3 extras
Requires:       python3-borgbackup = %{version}-%{release}
Requires:       python3dist(pyfuse3) >= 3.1.1
Provides:       python3dist(borgbackup[pyfuse3]) = %{version}-%{release}

%description -n python3-borgbackup+pyfuse3
Metapackage for python3-borgbackup pyfuse3 extras.

%package -n       python3-borgbackup+nofuse
Summary:        Metapackage for python3-borgbackup nofuse extras
Requires:       python3-borgbackup = %{version}-%{release}
Provides:       python3dist(borgbackup[nofuse]) = %{version}-%{release}

%description -n python3-borgbackup+nofuse
Metapackage for python3-borgbackup nofuse extras.

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

%build

%pyproject_wheel
export READTHEDOCS=True
export PYTHONPATH=$(pwd)/build/$(ls build/ | grep 'lib.')
make -C docs SPHINXBUILD=sphinx-build-%python3_version man
%install
find . -name *.so -type f -exec chmod 0755 {} \;
%pyproject_install
install -D -m 0644 docs/_build/man/borg*.1* %{buildroot}%{_mandir}/man1/borg.1
%define bash_compdir %{_prefix}/share/bash-completion/completions
%define zsh_compdir %{_prefix}/share/zsh/site-functions
%define fish_compdir %{_prefix}/share/fish/completions
install -d  %{buildroot}%{bash_compdir}
install -d  %{buildroot}%{zsh_compdir}
install -d  %{buildroot}%{fish_compdir}
install -D -m 0644 scripts/shell_completions/bash/* %{buildroot}%{bash_compdir}
install -D -m 0644 scripts/shell_completions/zsh/* %{buildroot}%{zsh_compdir}
install -D -m 0644 scripts/shell_completions/fish/* %{buildroot}%{fish_compdir}
%oreon_autofiles main

%check

export PYTHONPATH=%{buildroot}%{python3_sitearch}
cd $PYTHONPATH
TEST_SELECTOR="not test_fuse and not test_readonly_mount and not benchmark"
%pytest -n auto -x -vk "$TEST_SELECTOR" borg/testsuite/*.py
%files

%changelog

%autochangelog
