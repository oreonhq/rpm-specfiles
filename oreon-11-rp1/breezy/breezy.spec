%global source0_hash 32d26d0af0716e3580d7d97dda56ae441ab173f192092bcf762f590162f6bdae
%global brzmajor 3.3
%global brzminor .20
%bcond fastimport 0
%bcond github 0
Name:           breezy
Version:        %{brzmajor}%{?brzminor}
Release:        1%{?dist}
Summary:        Friendly distributed version control system
License:        GPL-2.0-or-later AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND MIT AND (Unlicense OR MIT)
URL:            http://www.breezy-vcs.org/
Source0:        https://github.com/%{name}-team/%{name}/archive/brz-%{version}.tar.gz
Source1:        brz-icon-64.png
Patch:          dulwich1.patch
Provides:       brz = %{version}-%{release}
Provides:       bzr = %{version}-%{release}
Obsoletes:      bzr < 3
Provides:       git-remote-bzr = %{version}-%{release}
Obsoletes:      git-remote-bzr < 3
Recommends:     breezy+launchpad
Suggests:       %{name}-doc = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 0.29
BuildRequires:  python3dist(setuptools) >= 60
BuildRequires:  python3dist(setuptools-gettext) >= 0.1.4
Requires:       python3-breezy = %{version}-%{release}
# /oreon:deps
%package -n       python3-breezy+fastimport
Summary:        Metapackage for python3-breezy fastimport extras
Requires:       python3-breezy = %{version}-%{release}
Requires:       python3dist(fastimport) >= 0.9.8
Provides:       python3dist(breezy[fastimport]) = %{version}-%{release}

%description -n python3-breezy+fastimport
Metapackage for python3-breezy fastimport extras.

%package -n       python3-breezy+git
Summary:        Metapackage for python3-breezy git extras
Requires:       python3-breezy = %{version}-%{release}
Requires:       python3dist(dulwich) >= 0.24.3
Provides:       python3dist(breezy[git]) = %{version}-%{release}

%description -n python3-breezy+git
Metapackage for python3-breezy git extras.

%package -n       python3-breezy+launchpad
Summary:        Metapackage for python3-breezy launchpad extras
Requires:       python3-breezy = %{version}-%{release}
Requires:       python3dist(launchpadlib) >= 1.6.3
Provides:       python3dist(breezy[launchpad]) = %{version}-%{release}

%description -n python3-breezy+launchpad
Metapackage for python3-breezy launchpad extras.

%package -n       python3-breezy+workspace
Summary:        Metapackage for python3-breezy workspace extras
Requires:       python3-breezy = %{version}-%{release}
Provides:       python3dist(breezy[workspace]) = %{version}-%{release}

%description -n python3-breezy+workspace
Metapackage for python3-breezy workspace extras.

%package -n       python3-breezy+doc
Summary:        Metapackage for python3-breezy doc extras
Requires:       python3-breezy = %{version}-%{release}
Provides:       python3dist(breezy[doc]) = %{version}-%{release}

%description -n python3-breezy+doc
Metapackage for python3-breezy doc extras.

%package -n       python3-breezy+pgp
Summary:        Metapackage for python3-breezy pgp extras
Requires:       python3-breezy = %{version}-%{release}
Provides:       python3dist(breezy[pgp]) = %{version}-%{release}

%description -n python3-breezy+pgp
Metapackage for python3-breezy pgp extras.

%package -n       python3-breezy+github
Summary:        Metapackage for python3-breezy github extras
Requires:       python3-breezy = %{version}-%{release}
Provides:       python3dist(breezy[github]) = %{version}-%{release}

%description -n python3-breezy+github
Metapackage for python3-breezy github extras.

%package -n       python3-breezy+paramiko
Summary:        Metapackage for python3-breezy paramiko extras
Requires:       python3-breezy = %{version}-%{release}
Provides:       python3dist(breezy[paramiko]) = %{version}-%{release}

%description -n python3-breezy+paramiko
Metapackage for python3-breezy paramiko extras.

%package -n       python3-breezy+subunit
Summary:        Metapackage for python3-breezy subunit extras
Requires:       python3-breezy = %{version}-%{release}
Provides:       python3dist(breezy[subunit]) = %{version}-%{release}

%description -n python3-breezy+subunit
Metapackage for python3-breezy subunit extras.

%package -n       python3-breezy+dev
Summary:        Metapackage for python3-breezy dev extras
Requires:       python3-breezy = %{version}-%{release}
Requires:       python3dist(cython) >= 0.29
Provides:       python3dist(breezy[dev]) = %{version}-%{release}

%description -n python3-breezy+dev
Metapackage for python3-breezy dev extras.

%package -n       python3-breezy+testing
Summary:        Metapackage for python3-breezy testing extras
Requires:       python3-breezy = %{version}-%{release}
Requires:       python3dist(dulwich) >= 0.24.3
Provides:       python3dist(breezy[testing]) = %{version}-%{release}

%description -n python3-breezy+testing
Metapackage for python3-breezy testing extras.

%description
Breezy (brz) is a decentralized revision control system, designed to be easy
for developers and end users alike.

By default, Breezy provides support for both the Bazaar and Git file formats.

%package doc
Summary:        Documentation for Breezy
License:        GPL-2.0-or-later
BuildArch:      noarch
%description doc
This package contains the documentation for the Breezy version control system.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-brz-%{version}%{?brzrc}

# Remove unused shebangs
sed -i '1{/#![[:space:]]*\/usr\/bin\/\(python\|env\)/d}' \
    breezy/__main__.py \
    breezy/git/git_remote_helper.py \
    breezy/git/tests/test_git_remote_helper.py \
    breezy/plugins/bash_completion/bashcomp.py \
    breezy/plugins/zsh_completion/zshcomp.py \
    breezy/tests/ssl_certs/create_ssls.py \
    contrib/brz_access

# Remove Cython generated .c files
find . -name '*_pyx.c' -exec rm \{\} \;

# Don't strip debug symbols, we generate debuginfo packages
sed -i 's/Strip.All/Strip.No/' setup.py

%build

%pyproject_wheel
chmod a-x contrib/bash/brzbashprompt.sh
%{__python3} tools/generate_docs.py man
make docs-sphinx PYTHON=%{__python3}
rm doc/*/_build/html/.buildinfo
rm -f doc/*/_build/html/_static/*/Makefile
pushd doc
for dir in *; do
  test -d $dir/_build/html && mv $dir/_build/html ../$dir
done
popd
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%pyproject_install
chmod -R a+rX contrib
chmod 0644 contrib/debian/init.d
chmod 0644 contrib/bzr_ssh_path_limiter  # note the bzr here
chmod 0644 contrib/brz_access
chmod 0755 %{buildroot}%{python3_sitearch}/%{name}/*.so
install -Dpm 0644 contrib/bash/brz %{buildroot}%{bash_completions_dir}/brz
rm contrib/bash/brz
install -d %{buildroot}%{_datadir}/pixmaps
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/brz.png
install -d %{buildroot}%{_mandir}/man1
install -m 0644 brz.1 %{buildroot}%{_mandir}/man1/
install -m 0644 breezy/git/git-remote-bzr.1 %{buildroot}%{_mandir}/man1/
mv %{buildroot}%{_bindir}/git-remote-bzr %{buildroot}%{_bindir}/git-remote-brz
mv %{buildroot}%{_mandir}/man1/git-remote-bzr.1 %{buildroot}%{_mandir}/man1/git-remote-brz.1
ln -s brz %{buildroot}%{_bindir}/bzr
ln -s git-remote-brz %{buildroot}%{_bindir}/git-remote-bzr
echo ".so man1/brz.1" > %{buildroot}%{_mandir}/man1/bzr.1
echo ".so man1/git-remote-brz.1" > %{buildroot}%{_mandir}/man1/git-remote-bzr.1
if [ -d %{buildroot}%{buildroot}%{_datadir}/locale ]
then
  mv %{buildroot}%{buildroot}%{_datadir}/locale %{buildroot}%{_datadir}
fi
%find_lang %{name}
cat %{name}.lang >> %{pyproject_files}
%oreon_autofiles breezy-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export %{py3_test_envvars}
brz init-repo testrepo
%files
%files -n breezy-doc -f %{oreon_filedir}/breezy-doc.list

%changelog

%autochangelog
