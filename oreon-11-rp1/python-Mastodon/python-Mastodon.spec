%global source0_hash 1e51802b09d4aa46568ca9618ed39e6977a0813cede3296783c9f8f21a93f2a6
Name:               python-Mastodon
Version:            2.1.4
Release:        1%{?dist}
Summary:        Python wrapper for the Mastodon API
License:            MIT
URL:                https://github.com/halcy/Mastodon.py
Source0:        https://github.com/halcy/Mastodon.py/archive/v%{version}/Mastodon.py-%{version}.tar.gz
BuildArch:          noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-Mastodon = %{version}-%{release}
# /oreon:deps
%package -n       python3-Mastodon+webpush
Summary:        Metapackage for python3-Mastodon webpush extras
Requires:       python3-Mastodon = %{version}-%{release}
Requires:       python3dist(http-ece) >= 1.0.5
Requires:       python3dist(cryptography) >= 1.6.0
Provides:       python3dist(Mastodon[webpush]) = %{version}-%{release}

%description -n python3-Mastodon+webpush
Metapackage for python3-Mastodon webpush extras.

%package -n       python3-Mastodon+blurhash
Summary:        Metapackage for python3-Mastodon blurhash extras
Requires:       python3-Mastodon = %{version}-%{release}
Requires:       python3dist(blurhash) >= 1.1.4
Provides:       python3dist(Mastodon[blurhash]) = %{version}-%{release}

%description -n python3-Mastodon+blurhash
Metapackage for python3-Mastodon blurhash extras.

%package -n       python3-Mastodon+grapheme
Summary:        Metapackage for python3-Mastodon grapheme extras
Requires:       python3-Mastodon = %{version}-%{release}
Requires:       python3dist(grapheme) >= 0.6.0
Provides:       python3dist(Mastodon[grapheme]) = %{version}-%{release}

%description -n python3-Mastodon+grapheme
Metapackage for python3-Mastodon grapheme extras.

%package -n       python3-Mastodon+test
Summary:        Metapackage for python3-Mastodon test extras
Requires:       python3-Mastodon = %{version}-%{release}
Provides:       python3dist(Mastodon[test]) = %{version}-%{release}

%description -n python3-Mastodon+test
Metapackage for python3-Mastodon test extras.

%package -n       python3-Mastodon+test_old
Summary:        Metapackage for python3-Mastodon test_old extras
Requires:       python3-Mastodon = %{version}-%{release}
Provides:       python3dist(Mastodon[test_old]) = %{version}-%{release}

%description -n python3-Mastodon+test_old
Metapackage for python3-Mastodon test_old extras.

%package -n       python3-Mastodon+docs
Summary:        Metapackage for python3-Mastodon docs extras
Requires:       python3-Mastodon = %{version}-%{release}
Provides:       python3dist(Mastodon[docs]) = %{version}-%{release}

%description -n python3-Mastodon+docs
Metapackage for python3-Mastodon docs extras.

%description
%{summary}.

%package -n python3-Mastodon
Summary:        Python wrapper for the Mastodon API
# oreon:reqs
Requires:       python3dist(blurhash) >= 1.1.4
Requires:       python3dist(decorator) >= 4.0.0
Requires:       python3dist(requests) >= 2.4.2
# /oreon:reqs
%description -n python3-Mastodon
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Mastodon.py-%{version}
# Not packaged, and not strictly required:
tomcli set pyproject.toml lists delitem project.optional-dependencies.test \
    pytest-retry
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem project.optional-dependencies.test \
    pytest-cov
tomcli set pyproject.toml del tool.pytest.ini_options.addopts
# Avoid conflict of python3-magic with python3-file-magic, and it's not needed.
tomcli set pyproject.toml lists delitem project.dependencies 'python-magic ; platform_system!="Windows"'

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-Mastodon usr/lib/python3*/site-packages/Mastodon* usr/lib64/python3*/site-packages/Mastodon* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/Mastodon* usr/lib64/python3*/site-packages/Mastodon* usr/bin/*

%check

%files
%files -n python3-Mastodon -f %{oreon_filedir}/python3-Mastodon.list

%changelog

%autochangelog
